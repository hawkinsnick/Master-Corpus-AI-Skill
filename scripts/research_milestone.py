#!/usr/bin/env python3
"""Replay bounded source-trace, dependence and comparability studies on frozen public inputs."""
import argparse,csv,hashlib,importlib.util,io,json,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STUDY=ROOT/'research/2026-10-21'

def digest(raw):return hashlib.sha256(raw).hexdigest()
def ptr(value,pointer):
    for p in pointer.split('/')[1:] if pointer else []:
        p=p.replace('~1','/').replace('~0','~');value=value[int(p)] if isinstance(value,list) else value[p]
    return value
def parse(raw,encoding):
    text=raw.decode()
    if encoding=='json':return json.loads(text)
    if encoding=='jsonl':return [json.loads(x) for x in text.splitlines() if x.strip()]
    if encoding=='csv':return list(csv.DictReader(io.StringIO(text)))
    if encoding=='text':return text
    raise ValueError('unknown encoding')
def safe(root,path):
    p=Path(path);target=(root/p).resolve()
    if p.is_absolute() or '..' in p.parts or not target.is_relative_to(root.resolve()):raise ValueError('unsafe native path')
    return target

def source(root,path,pointer='',encoding='json'):
    raw=safe(root,path).read_bytes()
    return ptr(parse(raw,encoding),pointer),{'repository':'hawkinsnick/'+root.name,'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'path':path,'pointer':pointer,'encoding':encoding,'sha256':digest(raw)}
def verify_dossier(root,d):
    p=d['provenance'];v,ref=source(root,p['path'],p['pointer'],p['encoding'])
    if ref['sha256']!=p['sha256'] or v!=d['native_record']:raise ValueError('source trace mismatch')
    return ref

def metadata(value,prefix=''):
    """Return candidate metadata, never promote a field name into primary verification."""
    found=[]
    keys={'source_id','source_url','citation','citation_as_supplied','references','ref','bibliography_source','source_location','source_locator','locator','locator_as_supplied','attribution','source_license','license','rights','edition_locators','primary_edition_verified','direct_edition_checked','independent_epigraphic_review','independent_review_complete'}
    def walk(v,p):
        if isinstance(v,dict):
            for k,x in v.items():
                q=p+'/'+k.replace('~','~0').replace('/','~1')
                if k in keys and x not in (None,'',[]):
                    if not isinstance(x,(dict,list)):found.append({'field_pointer':q,'value':x})
                    elif isinstance(x,list) and all(isinstance(t,str) for t in x):
                        found.append({'field_pointer':q,'value':x})
                walk(x,q)
        elif isinstance(v,list):
            for i,x in enumerate(v):walk(x,p+'/'+str(i))
    walk(value,prefix)
    return found

def load_evidence(root):
    spec=importlib.util.spec_from_file_location('native_'+root.name.replace('-','_'),root/'scripts/evidence_query.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m.Evidence(root)

def acquire_roots(parent):
    manifest=json.loads((STUDY/'native-revisions.json').read_text());roots={}
    for m in manifest['members']:
        root=(parent/m['repository'].split('/')[-1]).resolve()
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
        if head!=m['commit']:raise ValueError('wrong frozen revision: '+root.name)
        origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=root,text=True).strip().removesuffix('.git')
        if origin!='https://github.com/'+m['repository']:raise ValueError('wrong origin')
        if subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=root).returncode:raise ValueError('dirty native input: '+root.name)
        roots[root.name]=root
    return roots

def source_trace(roots):
    rows=[]
    for name,root in roots.items():
        e=load_evidence(root);candidates=[]
        for collection,c in e.collections.items():
            for row in c['records']:
                key='source-trace-v1|hawkinsnick/'+name+'|'+collection+'|'+row['id']
                candidates.append((digest(key.encode()),collection,row['id']))
        for rank,collection,identity in sorted(candidates)[:3]:
            d=e.dossier(identity,collection);ref=verify_dossier(root,d)
            fields=metadata(d['native_record'])+metadata(d.get('collection_context',{}),'/collection_context')
            rows.append({'repository':'hawkinsnick/'+name,'collection':collection,'id':identity,'native_unit':d['native_unit'],'selection_hash':rank,'source':ref,'byte_trace':'PASS','metadata_fields':fields,'citation_assessment':'CANDIDATE_FIELDS_ONLY_NOT_AUTHENTICATED','fresh_primary_edition_check':'NOT_PERFORMED','external_review':'NOT_PERFORMED','next_step':'Resolve the candidate bibliography to an exact edition/locus and inspect that source; obtain an attributable specialist check where interpretation requires it.'})
    return {'format':'bounded-source-trace-v1','members':len(roots),'sampled_view_rows':len(rows),'selection':json.loads((STUDY/'protocol.json').read_text())['selection']['source_trace'],'primary_checks_newly_performed':0,'external_reviews_added':0,'rows':rows,'scope':'Re-executed source fidelity checks and candidate citation extraction. Not independent scholarly verification or a physical-object sample.'}

def dependence(roots):
    a=roots['Lycian-and-Carian'];b=roots['Milyan-Lycian-B']
    p='data/raw/ediana/milyan-1-0.json';q='data/reference/ediana-milyan-source.json'
    x,rx=source(a,p);y,ry=source(b,q)
    count=sum(1 for rows in x.values() for row in rows if row.get('sentence','').strip())
    identical=safe(a,p).read_bytes()==safe(b,q).read_bytes()
    # Enumerate source-row loci rather than claim physical or linguistic line joins.
    row_links=[{'left_pointer':'/'+key.replace('~','~0').replace('/','~1')+'/'+str(i),'right_pointer':'/'+key.replace('~','~0').replace('/','~1')+'/'+str(i),'source_group':key} for key,rs in x.items() for i,row in enumerate(rs) if row.get('sentence','').strip()] if identical else []
    c,rc=source(roots['Cypriot-syllabic-Greek'],'exports/corpus.json');d,rd=source(roots['Eteocypriot'],'exports/corpus.json')
    cids={}
    for i,row in enumerate(c['records']):cids.setdefault(row['source_id'],[]).append((i,row['id']))
    links=[]
    for i,row in enumerate(d['records']):
        for n,identity in cids.get(row['source_id'],[]):links.append({'source_id':row['source_id'],'left_id':identity,'left_pointer':'/records/'+str(n),'right_id':row['id'],'right_pointer':'/records/'+str(i)})
    return {'format':'observed-source-dependence-v1','scope':'Two predeclared source-family checks; not exhaustive all-pairs independence certification.','groups':[{'id':'DEP-MIL-CACHE','kind':'IDENTICAL_SOURCE_CACHE' if identical else 'CHANGED_CACHE_REQUIRES_REVIEW','sources':[rx,ry],'identical_bytes':identical,'nonempty_source_text_rows_per_copy':count,'naive_two_copy_row_count':2*count,'distinct_serialized_rows_after_exact_copy_exclusion':count if identical else None,'row_links':row_links,'physical_object_count':None,'independent_witness_count':None,'analysis_rule':'Count one cache view; preserve both routes. No physical identity, ancient-line count or reading correctness certified.'},{'id':'DEP-CY-EDITION','kind':'SHARED_DIGITAL_EDITION_ID','sources':[rc,rd],'left_view_entries':len(c['records']),'right_view_entries':len(d['records']),'shared_source_ids':len({x['source_id'] for x in links}),'links':links,'physical_object_count':None,'independent_witness_count':None,'analysis_rule':'Group by documented digital source ID for source-level dependence; retain language/component boundaries. No physical-object merge.'}],'untested_relationships':'UNKNOWN_NOT_INDEPENDENT','scientific_approval_granted':False}

def attribution(roots):
    root=roots['Linear-A'];j,ref=source(root,'research/legacy-case-attribution.json');i=next(i for i,c in enumerate(j['cases']) if c['case_id']=='U008');c=j['cases'][i];ref['pointer']='/cases/'+str(i)
    observations=[]
    for item in c['source_evidence']:
        v,r=source(root,item['path'],item['pointer']);observations.append({'source':r,'series':v['series'],'number':v['number'],'raw_flags':v['raw_flags'],'slot_zero_based':int(item['pointer'].split('/')[-1])})
    loci={x['slot_zero_based'] for x in observations}
    return {'format':'executed-u008-source-audit-v1','case_source':ref,'record_id':c['source_record_id'],'observations':observations,'distinct_loci':len(loci),'same_locus_pair_established':False,'legacy_alternative_attribution':[{'literal':x['literal'],'complete_author_source_locus_attribution':x['complete_author_source_locus_attribution'],'status':x['attribution_status']} for x in c['alternatives']],'decision':'NOT_ELIGIBLE_FOR_READING_ADJUDICATION','finding':'The checked slots are distinct; their presence in KH 8 does not align the legacy alternatives. No preferred reading follows.','remaining_evidence_gap':c['remaining_evidence_gap'],'fresh_primary_edition_check':'NOT_PERFORMED','canonical_readings_changed':0}

def comparability(roots):
    ch,cr=source(roots['Cretan-hieroglyphs'],'corpus/critical-readings.json');cm,mr=source(roots['Cypro-Minoan'],'occurrences/occurrences.json','/occurrences')
    forms=[t['form'] for r in ch for t in r.get('tokens',[])];hyphen=sum('-' in x for x in forms)
    return {'format':'executed-ch-cm-comparability-v1','sources':[cr,mr],'ch_reading_versions':len(ch),'ch_distinct_recorded_object_labels':len({r['object_id'] for r in ch}),'ch_stored_token_fields':len(forms),'ch_token_fields_containing_hyphens':hyphen,'cm_occurrence_rows':len(cm),'cm_distinct_rich_record_labels':len({r['record_id'] for r in cm}),'units':[{'repository':'hawkinsnick/Cretan-hieroglyphs','stored_unit':'reading version with token fields; some fields encode hyphenated source groups, numerical notation or markers','supporting_paths':['/tokens','/source_id','/locator']},{'repository':'hawkinsnick/Cypro-Minoan','stored_unit':'selected source-attributed occurrence with zone and position','supporting_paths':['/position','/zone_id','/published_sign_label','/source_role']}],'decision':'DESCRIPTIVE_COMPARISON_ONLY','pooled_sign_frequency':None,'finding':'Do not equate CH token fields with CM occurrence rows or split hyphenated groups as authenticated signs. Selected source strata, repeated reading versions and incompatible units preclude the proposed pooled positional test at this checkpoint.','next_steps':['Define a source-authorized common unit and preserve markers/numerals separately.','Establish support/layout and orientation eligibility for each selected record.','Resolve edition dependence and define independent sampling units before inference.'],'phonetic_equivalence_established':False}

def build(parent):
    roots=acquire_roots(parent)
    return {'source-trace.json':source_trace(roots),'dependence-register.json':dependence(roots),'demo-u008.json':attribution(roots),'demo-comparability.json':comparability(roots)}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',type=Path,required=True);p.add_argument('--write',action='store_true');a=p.parse_args()
    for path,value in build(a.checkouts).items():
        raw=json.dumps(value,ensure_ascii=False,indent=2)+'\n';dest=STUDY/path
        if a.write:dest.write_text(raw)
        elif not dest.is_file() or dest.read_text()!=raw:raise ValueError('research replay mismatch: '+path)
    print(json.dumps({'status':'PASS_BOUNDED_RESEARCH_REPLAY','primary_edition_checks_added':0,'external_reviews_added':0}))
if __name__=='__main__':main()
