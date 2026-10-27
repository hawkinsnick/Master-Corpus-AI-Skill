#!/usr/bin/env python3
"""Screen short text and explicit source lineage; never infer identity from matching strings."""
import collections
import itertools
import json
import unicodedata
from hostile_review import module
from nonreview_common import roots,receipt,cli,digest,exact,safe
KEYS={'text','reading','sentence','transliteration'}
def fields(value,path=''):
    if isinstance(value,dict):
        for key,v in value.items():
            p=path+'/'+key.replace('~','~0').replace('/','~1')
            if key in KEYS and isinstance(v,str):
                norm=' '.join(unicodedata.normalize('NFC',v).split())
                if norm:yield p,norm
            yield from fields(v,p)
    elif isinstance(value,list):
        for i,v in enumerate(value):yield from fields(v,path+'/'+str(i))
def binding(root,ref,document):
    bits=ref['pointer'].split('/')[1:]
    if ref['path']=='data/records.json' and bits and bits[0].isdigit():
        row=document[int(bits[0])]
        if root.name in ('Cypriot-syllabic-Greek','Eteocypriot'):
            source=row['source'];b=safe(root,source['raw_path']).read_bytes()
            if digest(b)!=source['sha256']:raise ValueError('upstream source hash drift')
            return {'family':'IG_XV_1','raw_sha256':digest(b),'locus':row['source_id']}
        if root.name=='Lycian-and-Carian' and len(bits)>=3 and bits[1]=='lines':
            line=row['lines'][int(bits[2])];source=row['source'];b=safe(root,source['raw_path']).read_bytes()
            if digest(b)!=source['sha256']:raise ValueError('upstream source hash drift')
            return {'family':'EDIANA','raw_sha256':digest(b),'locus':line['source_locator']}
    if root.name=='Milyan-Lycian-B':
        if ref['path']=='data/reference/lines.json':row=document[int(bits[0])]
        elif ref['path']=='research/tl55-qualified-collation.json' and len(bits)>=2 and bits[0]=='rows':row=document['rows'][int(bits[1])]['source_reference_row']
        else:return None
        b=safe(root,row['raw_path']).read_bytes()
        if digest(b)!=row['source_sha256']:raise ValueError('Milyan source hash drift')
        return {'family':'EDIANA','raw_sha256':digest(b),'locus':row['source_locator']}
    return None

def build(parent):
    rs=roots(parent);occurrences={};bytext=collections.defaultdict(list);bylineage=collections.defaultdict(list)
    for name,root in rs.items():
        e=module(root).Evidence(root);docs={p:json.loads(safe(root,p).read_bytes()) for p,a in e.artifacts.items() if a['spec']['encoding']=='json'}
        for collection,c in e.collections.items():
            for row in c['records']:
                ref=e.provenance(c['spec']['path'],row['pointer'])
                for suffix,text in fields(row['value']):
                    p=ref['pointer']+suffix;key=(name,ref['path'],p)
                    if key in occurrences:continue
                    source=binding(root,{**ref,'pointer':p},docs.get(ref['path']))
                    value={'repository':'hawkinsnick/'+name,'path':ref['path'],'sha256':ref['sha256'],'pointer':p,'collection':collection,'id':row['id'],'native_unit':c['spec']['unit'],'normalized_text_sha256':digest(text.encode()),'normalized_characters':len(text),'whitespace_tokens':len(text.split()),'source_binding':source,'dependence_disposition':'KNOWN_SOURCE_ORIGIN_NOT_INDEPENDENCE_CERTIFICATION' if source else 'UNKNOWN_SOURCE_LINEAGE','physical_identity_established':False}
                    occurrences[key]=value;bytext[value['normalized_text_sha256']].append(value)
                    if source:bylineage[exact(source)].append(value)
    groups=[]
    for h,rows in sorted(bytext.items()):
        if len({x['repository'] for x in rows})<2:continue
        known=collections.defaultdict(list)
        for row in rows:
            if row['source_binding']:known[exact(row['source_binding'])].append(row)
        repeats=[{'source_binding':json.loads(k),'occurrences':[[x['repository'],x['path'],x['pointer']] for x in v]} for k,v in sorted(known.items()) if len({x['repository'] for x in v})>1]
        groups.append({'normalized_text_sha256':h,'normalized_characters':rows[0]['normalized_characters'],'below_prior_long_text_threshold':rows[0]['normalized_characters']<24 or rows[0]['whitespace_tokens']<4,'occurrences':[[x['repository'],x['path'],x['pointer']] for x in rows],'verified_same_source_subgroups':repeats,'other_relationships':'UNKNOWN_EVEN_WHEN_TEXT_MATCHES','unit':'normalized source-field string; no physical or semantic merge'})
    lineage=[]
    for source,rows in sorted(bylineage.items()):
        if len({x['repository'] for x in rows})<2:continue
        lineage.append({'source_binding':json.loads(source),'occurrences':[[x['repository'],x['path'],x['pointer']] for x in rows],'different_text_hashes':len({x['normalized_text_sha256'] for x in rows}),'disposition':'SHARED_DIGITAL_SOURCE_LOCUS_PRESERVE_DIFFERENT_FIELDS_AND_VIEWS'})
    # Intern repeated provenance so every field remains inspectable without duplicating long hashes.
    artifacts=[];artifact_ids={};bindings=[];binding_ids={};table=[];field_ids={}
    for index,v in enumerate(occurrences.values()):
        a=(v['repository'],v['path'],v['sha256'])
        if a not in artifact_ids:artifact_ids[a]=len(artifacts);artifacts.append(dict(zip(('repository','path','sha256'),a)))
        b=v['source_binding'];bi=None
        if b is not None:
            key=exact(b)
            if key not in binding_ids:binding_ids[key]=len(bindings);bindings.append(b)
            bi=binding_ids[key]
        field_ids[(v['repository'],v['path'],v['pointer'])]=index
        table.append([artifact_ids[a],v['pointer'],v['normalized_text_sha256'],v['normalized_characters'],v['whitespace_tokens'],bi])
    for g in groups:
        g['occurrences']=[field_ids[tuple(x)] for x in g['occurrences']]
        for sub in g['verified_same_source_subgroups']:
            sub['source_binding_id']=binding_ids[exact(sub.pop('source_binding'))]
            sub['occurrences']=[field_ids[tuple(x)] for x in sub['occurrences']]
    for g in lineage:
        g['source_binding_id']=binding_ids[exact(g.pop('source_binding'))]
        g['occurrences']=[field_ids[tuple(x)] for x in g['occurrences']]
    return {'format':'short-text-and-source-lineage-screen-v2','date':'2026-10-27','inputs':'inputs.json','method':{'keys':sorted(KEYS),'minimum_characters':1,'minimum_tokens':1,'normalization':'NFC and whitespace collapse; case, punctuation, diacritics and damage symbols retained','field_unit':'Unique repository/path/pointer, collapsing repeated retrieval views only','identity_rule':'Only explicit raw-source hash and source locus justify a shared-source relation. Equal short strings never justify an object, edition, language or witness merge.'},'totals':{'eligible_source_fields':len(occurrences),'cross_repository_text_groups':len(groups),'short_groups_newly_screened':sum(g['below_prior_long_text_threshold'] for g in groups),'known_shared_source_locus_groups':len(lineage),'fields_with_unknown_source_lineage':sum(v['source_binding'] is None for v in occurrences.values()),'physical_joins_added':0},'artifact_table':artifacts,'source_binding_table':bindings,'field_dispositions':{'columns':['artifact_id','pointer','normalized_text_sha256','normalized_characters','whitespace_tokens','source_binding_id'],'disposition_rule':'Non-null source_binding_id: known digital source origin only; null: UNKNOWN_SOURCE_LINEAGE. No physical identity established. Group occurrence integers index these rows.','rows':table},'text_match_groups':groups,'source_lineage_groups':lineage,'sensitivity_policy':{'unknown_as_independent':'DISALLOWED_AS_CANONICAL_ASSUMPTION','descriptive_scenarios':'Report source-family-stratified results and exclusions; any hypothetical dependence scenario must remain separately labelled.','combined_physical_count':None,'independent_witness_count':None},'limits':'No fuzzy/semantic equivalence, translations across languages or exhaustive edition genealogy. Every eligible field receives a disposition; UNKNOWN is an unresolved requirement, not a resolved semantic-dependence decision. Short nonmatches do not imply independence. No source text redistributed.'}
if __name__=='__main__':
    a=cli(__doc__);r=receipt('dependence-v2.json',build(a.checkouts),a.write);print(r['totals'])
