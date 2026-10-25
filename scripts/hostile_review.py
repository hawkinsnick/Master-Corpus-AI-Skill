#!/usr/bin/env python3
"""Exhaust all declared retrieval views and screen partial textual overlaps; no scholarly certification."""
import argparse
import collections
import importlib.util
import json
import unicodedata
from pathlib import Path
from review_integrity import digest,exact,safe,pointer,parse,checkpoints
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/2026-10-25'
TEXT_KEYS={'text','reading','sentence','transliteration'}

def module(root):
    spec=importlib.util.spec_from_file_location('review_'+root.name.replace('-','_'),root/'scripts/evidence_query.py')
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value

def text_fields(value,path=''):
    if isinstance(value,dict):
        for k,v in value.items():
            p=path+'/'+k.replace('~','~0').replace('/','~1')
            if k in TEXT_KEYS and isinstance(v,str):
                normalized=' '.join(unicodedata.normalize('NFC',v).split())
                if len(normalized)>=24 and len(normalized.split())>=4:yield p,normalized
            yield from text_fields(v,p)
    elif isinstance(value,list):
        for i,v in enumerate(value):yield from text_fields(v,path+'/'+str(i))

def check_dossier(d,expected,artifacts):
    ref=d['provenance'];source=artifacts[ref['path']]
    if ref['sha256']!=source['sha256'] or ref['encoding']!=source['encoding']:raise ValueError('unbound dossier provenance')
    if exact(d['native_record'])!=exact(pointer(source['value'],ref['pointer'])) or exact(d['native_record'])!=exact(expected):raise ValueError('dossier changed exact source data')
    if not d.get('scholarly_limits') or not d.get('boundary'):raise ValueError('dossier lost scope limits')
    return ref

def upstream(ref,roots):
    root=roots[ref['repository'].split('/')[-1]]
    doc=json.loads(safe(root,ref['path']).read_bytes())
    if ref['path']=='data/records.json':
        index=int(ref['pointer'].split('/')[1]);row=doc[index]
        if root.name in {'Cypriot-syllabic-Greek','Eteocypriot'}:
            source=row['source'];raw=safe(root,source['raw_path']).read_bytes()
            if digest(raw)!=source['sha256']:raise ValueError('upstream XML pin changed')
            return {'family':'IG_XV_1_DIGITAL_EDITION','raw_sha256':digest(raw),'source_locus':row['source_id']}
        if root.name=='Lycian-and-Carian':
            bits=ref['pointer'].split('/');line=row['lines'][int(bits[3])];source=row['source'];raw=safe(root,source['raw_path']).read_bytes()
            if digest(raw)!=source['sha256']:raise ValueError('upstream cache pin changed')
            return {'family':'EDIANA_MILYAN_SOURCE_CACHE','raw_sha256':digest(raw),'source_locus':line['source_locator']}
    if root.name=='Milyan-Lycian-B':
        if ref['path']=='data/reference/lines.json':row=doc[int(ref['pointer'].split('/')[1])]
        elif ref['path']=='research/tl55-qualified-collation.json':row=doc['rows'][int(ref['pointer'].split('/')[2])]['source_reference_row']
        else:return None
        raw=safe(root,row['raw_path']).read_bytes()
        if digest(raw)!=row['source_sha256']:raise ValueError('upstream reference pin changed')
        return {'family':'EDIANA_MILYAN_SOURCE_CACHE','raw_sha256':digest(raw),'source_locus':row['source_locator']}
    return None

def build(parent,manifest_name="inputs.json"):
    if manifest_name not in {"inputs.json","publication-inputs.json"}:raise ValueError("unregistered review manifest")
    manifest=json.loads((OUT/manifest_name).read_text());roots=checkpoints(parent,manifest);members=[];texts=collections.defaultdict(dict)
    for name,root in roots.items():
        e=module(root).Evidence(root);artifacts={};collections_out=[];links=0
        for path,item in e.artifacts.items():
            raw=safe(root,path).read_bytes();spec=item['spec']
            if digest(raw)!=spec['sha256']:raise ValueError('artifact pin mismatch')
            artifacts[path]={'sha256':digest(raw),'encoding':spec['encoding'],'value':parse(raw,spec['encoding'])}
        for collection,c in e.collections.items():
            digests=[]
            for row in c['records']:
                d=e.dossier(row['id'],collection);ref=check_dossier(d,row['value'],artifacts)
                if d['repository']!='hawkinsnick/'+name or d['collection']!=collection or d['native_unit']!=c['spec']['unit']:raise ValueError('namespace/unit drift')
                if ref['pointer']!=row['pointer'] or ref['path']!=c['spec']['path']:raise ValueError('wrong row locator')
                for link in d['explicitly_linked_records']:
                    linkref=link['provenance'];src=artifacts[linkref['path']]
                    if linkref['sha256']!=src['sha256'] or exact(link['native_record'])!=exact(pointer(src['value'],linkref['pointer'])):raise ValueError('linked source changed')
                    links+=1
                digests.append(digest(exact({'id':row['id'],'provenance':ref,'native_record':d['native_record']}).encode()))
                for field,text in text_fields(row['value']):
                    h=digest(text.encode());key=(name,ref['path'],ref['pointer']+field)
                    texts[h][key]={'repository':'hawkinsnick/'+name,'path':ref['path'],'sha256':ref['sha256'],'pointer':ref['pointer']+field,'native_id':row['id'],'collection':collection,'native_unit':c['spec']['unit']}
            collections_out.append({'name':collection,'unit':c['spec']['unit'],'rows_checked':len(c['records']),'source_path':c['spec']['path'],'source_sha256':artifacts[c['spec']['path']]['sha256'],'ordered_row_trace_sha256':digest(exact(digests).encode())})
        members.append({'repository':'hawkinsnick/'+name,'commit':next(m['commit'] for m in manifest['members'] if m['repository'].endswith('/'+name)),'profile_sha256':e.profile_hash,'artifact_pins_checked':len(artifacts),'collections':collections_out,'all_declared_rows_checked':sum(c['rows_checked'] for c in collections_out),'linked_records_checked':links})
    groups=[]
    for h,occurrences in sorted(texts.items()):
        if len({x[0] for x in occurrences})<2:continue
        members_in_group=list(occurrences.values());bindings=[upstream(ref,roots) for ref in members_in_group]
        shared=bindings[0] if all(b is not None and b==bindings[0] for b in bindings) else None
        groups.append({'normalized_text_sha256':h,'disposition':'REPEATED_UPSTREAM_SOURCE_FIELD' if shared else 'OVERLAP_CANDIDATE_NOT_ADMITTED_IDENTITY','upstream_binding':shared,'members':members_in_group,'independent_witness_count':None,'physical_object_count':None})
    pairs=collections.Counter()
    import itertools
    for g in groups:
        for pair in itertools.combinations(sorted({v['repository'] for v in g['members']}),2):pairs[pair]+=1
    return {'format':'hostile-review-retrieval-and-partial-overlap-v1','date':'2026-10-25','inputs':manifest_name,'members':members,'totals':{'members':len(members),'collections':sum(len(m['collections']) for m in members),'retrieved_view_rows':sum(m['all_declared_rows_checked'] for m in members),'linked_records_checked':sum(m['linked_records_checked'] for m in members),'partial_text_match_groups':len(groups),'source_bound_repeat_groups':sum(g['upstream_binding'] is not None for g in groups)},'partial_overlap_method':{'fields':sorted(TEXT_KEYS),'transform':'Unicode NFC then whitespace collapse only; retain case, punctuation, damaged signs, diacritics, and editorial characters. Equal text need not have equal meaning, edition, or object.','minimum_normalized_characters':24,'minimum_whitespace_tokens':4,'eligible_text_fields':sum(len(v) for v in texts.values()),'unit':'source field occurrence; duplicate view loci within a repository collapsed by path/pointer','limits':'Not semantic equivalence, fuzzy matching, cross-language translation matching, or exhaustive upstream source-history research. Short strings are deliberately omitted. Candidates may be translations, commentary or reused infrastructure; inspect each source role before deductions. No text payload redistributed.'},'partial_overlap_candidates':groups,'repository_pairs_with_text_matches':[{'repositories':list(k),'candidate_groups':v,'independence':'SAME_SOURCE_ONLY_WHERE_GROUP_BINDING_ESTABLISHED_OTHERWISE_UNKNOWN'} for k,v in sorted(pairs.items())],'scientific_approval_granted':False,'model_accuracy_measured':False,'boundary':'All declared rows means all retrieval views at these eighteen checkpoints, including registers, hypotheses and repeated views. It is not all inscriptions, independent witnesses, verified readings or all source literature.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',type=Path,required=True);p.add_argument('--write',action='store_true');p.add_argument('--publication-checkpoints',action='store_true');a=p.parse_args();j=build(a.checkouts,'publication-inputs.json' if a.publication_checkpoints else 'inputs.json');s=json.dumps(j,ensure_ascii=False,indent=2)+'\n';target=OUT/('publication-retrieval-and-overlap.json' if a.publication_checkpoints else 'retrieval-and-overlap.json')
    if a.write:target.write_text(s)
    elif target.read_text()!=s:raise ValueError('hostile review replay drift')
    print(json.dumps(j['totals']))
if __name__=='__main__':main()
