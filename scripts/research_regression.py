#!/usr/bin/env python3
"""Exercise full-record retrieval, literal search and unsupported-inference rejection in every view."""
import json
from collections import Counter
from hostile_review import module
from package_audit import delivery
from nonreview_common import roots,receipt,cli,digest,exact,safe,pointer

def atoms(v):
    if isinstance(v,dict):
        for x in v.values():yield from atoms(x)
    elif isinstance(v,list):
        for x in v:yield from atoms(x)
    else:yield v

def complexity(row):
    a=list(atoms(row['value']));return (sum(x is None or x is False for x in a),sum(isinstance(x,str) and any(c in x for c in '?[]\u0323') for x in a),len(exact(row['value'])))

def build(parent):
    rs=roots(parent);cases=[];walkthroughs=[]
    for name,root in rs.items():
        e=module(root).Evidence(root);m=delivery(root);member_cases=[]
        for collection,c in e.collections.items():
            if not c['records']:
                cases.append({'repository':'hawkinsnick/'+name,'collection':collection,'status':'EMPTY_DECLARED_VIEW','cases_executed':0});continue
            row=max(c['records'],key=complexity);d=e.dossier(row['id'],collection);ref=d['provenance'];source=json.loads(safe(root,ref['path']).read_bytes()) if ref['encoding']=='json' else __import__('review_integrity').parse(safe(root,ref['path']).read_bytes(),ref['encoding'])
            if exact(pointer(source,ref['pointer']))!=exact(row['value']) or exact(d['native_record'])!=exact(row['value']):raise ValueError('full source record changed')
            links=[]
            for link in d['explicitly_linked_records']:
                p=link['provenance'];b=safe(root,p['path']).read_bytes();v=__import__('review_integrity').parse(b,p['encoding'])
                if digest(b)!=p['sha256'] or exact(pointer(v,p['pointer']))!=exact(link['native_record']):raise ValueError('linked assertion changed')
                links.append(p)
            refusal=m.answer(collection,row['id'],root,request='supply_new_translation')
            if refusal['status']!='REFUSED_UNSUPPORTED_INFERENCE' or refusal['scientific_approval_granted'] is not False:raise ValueError('unsupported inference admitted')
            scalars=list(atoms(row['value']));strings=[v for v in scalars if isinstance(v,str) and v.strip()]
            # Literal damaged/uncertain strings preferred. This is declared development selection.
            term='?' if any('?' in x for x in strings) else next((x[:24] for x in strings if any(ord(c)>127 for c in x)),strings[0][:24] if strings else row['id'])
            found=m.search(term,root,collection,1)
            expected=[x for x in c['records'] if term.casefold() in json.dumps(x['value'],ensure_ascii=False).casefold()]
            if found['matched_view_rows']!=len(expected) or len(found['records'])!=min(1,len(expected)):raise ValueError('literal search count/limit wrong')
            if expected and found['records'][0]['id']!=expected[0]['id']:raise ValueError('search order wrong')
            if found['unique_object_count'] is not None or found['independent_witness_count'] is not None:raise ValueError('unsupported denominator')
            missing='__NO_SUCH_NATIVE_RECORD_NONREVIEW_20261027__'
            try:e.dossier(missing,collection)
            except (ValueError,KeyError):pass
            else:raise ValueError('missing ID silently substituted')
            item={'repository':'hawkinsnick/'+name,'collection':collection,'id':row['id'],'unit':c['spec']['unit'],'provenance':ref,'full_record_sha256':digest(exact(d['native_record']).encode()),'linked_records_checked':len(links),'linked_trace_sha256':digest(exact(links).encode()),'source_null_atoms_preserved':sum(v is None for v in scalars),'source_false_atoms_preserved':sum(v is False for v in scalars),'literal_search':{'term':term,'matched_view_rows':len(expected),'returned_limit':1,'truncated':len(expected)>1},'unsupported_inference':'REFUSED_UNSUPPORTED_INFERENCE','missing_id':'REJECTED','checks':['EXACT_FULL_RECORD_AND_LOCUS','EXACT_LINKED_RECORDS','LITERAL_SEARCH_AND_LIMIT','NULL_AND_FALSE_PRESERVED','UNSUPPORTED_INFERENCE_REJECTED','MISSING_ID_REJECTED'],'status':'PASS_DECLARED_DEVELOPMENT_CONTRACT','cases_executed':6}
            cases.append(item);member_cases.append(item)
        chosen=max(member_cases,key=lambda x:(x['linked_records_checked'],x['source_null_atoms_preserved']+x['source_false_atoms_preserved']))
        walkthroughs.append({'repository':chosen['repository'],'collection':chosen['collection'],'id':chosen['id'],'unit':chosen['unit'],'source_ref':chosen['provenance'],'full_record_sha256':chosen['full_record_sha256'],'expected_linked_records':chosen['linked_records_checked'],'command':['python','scripts/query.py','--checkouts','CHECKOUT_PARENT','--repository',chosen['repository'],'--collection',chosen['collection'],'--id',chosen['id']],'learning_goal':'Retrieve the full attributed record, retain uncertainty and linked assertions, and state why its native unit cannot be promoted to independent physical evidence.'})
    return {'format':'full-record-retrieval-development-regression-v1','date':'2026-10-27','inputs':'inputs.json','selection':'All declared collections. Select one row lexicographically maximizing null/false atoms, then editorial-marker-bearing strings, then serialized length. These are exposed, purposive development cases, not an unexposed representative academic sample.','cases':cases,'totals':{'members':len(rs),'collections':len(cases),'nonempty_collections':sum(c['cases_executed']>0 for c in cases),'contract_checks':sum(c['cases_executed'] for c in cases),'linked_records_checked':sum(c.get('linked_records_checked',0) for c in cases),'null_atoms_preserved':sum(c.get('source_null_atoms_preserved',0) for c in cases),'false_atoms_preserved':sum(c.get('source_false_atoms_preserved',0) for c in cases)},'walkthroughs':walkthroughs,'model_responses_scored':0,'academic_accuracy_established':False,'boundary':'Tests execute deterministic native retrieval interfaces, not an LLM. Fresh agent walkthrough responses are a separately identified development exercise. No linguistic gold or specialist acceptance is implied.'}
if __name__=='__main__':
    a=cli(__doc__);r=receipt('research-regression.json',build(a.checkouts),a.write);print(r['totals'])
