#!/usr/bin/env python3
"""Score exact development conformance only; not academic accuracy or specialist review."""
import argparse
import json
from pathlib import Path
from review_integrity import digest,exact,safe,pointer,parse,checkpoints
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/2026-10-25'
def score(expected,actual):
    ids=[x['id'] for x in actual]
    if len(ids)!=len(set(ids)) or set(ids)!={x['id'] for x in expected}:raise ValueError('missing, duplicate or unexpected response')
    by_id={x['id']:x for x in actual};rows=[]
    for wanted in expected:
        answer=by_id[wanted['id']]
        result={k:exact(answer.get(k))==exact(wanted[k]) for k in ['decision','answer','native_unit']}
        cite=answer.get('citation')
        if not isinstance(cite,dict):cite={}
        result['citation']=set(cite)==set(wanted['citation']) and all(exact(cite[k])==exact(v) for k,v in wanted['citation'].items())
        result['rationale_present']=isinstance(answer.get('rationale'),str) and bool(answer['rationale'].strip())
        rows.append({'id':wanted['id'],'checks':result,'all_checks_pass':all(result.values())})
    return rows

def build(parent):
    commitment=json.loads((OUT/'development-commitment.json').read_text())
    for key,path in [('packet_sha256','development-packet.json'),('oracle_sha256','development-oracle.json'),('protocol_sha256','development-protocol.json')]:
        if digest((OUT/path).read_bytes())!=commitment[key]:raise ValueError('frozen development inputs changed')
    packet=json.loads((OUT/'development-packet.json').read_text());expected=json.loads((OUT/'development-oracle.json').read_text())['items']
    roots=checkpoints(parent,json.loads((OUT/'inputs.json').read_text()));oracle_by_id={x['id']:x for x in expected}
    if len(packet['cases'])!=18 or len(expected)!=54:raise ValueError('development scope changed')
    for case in packet['cases']:
        e=case['evidence'];root=roots[e['repository'].split('/')[-1]];ref=e['source'];raw=safe(root,ref['path']).read_bytes()
        if digest(raw)!=ref['sha256']:raise ValueError('development source changed')
        value=pointer(parse(raw,ref['encoding']),ref['pointer']+e['field_pointer_within_record'])
        if exact(value)!=exact(e['field_value']):raise ValueError('packet field differs from native source')
        for t in case['tasks']:
            o=oracle_by_id[t['id']];op=t['primary_operation'];cite={'repository':e['repository'],'commit':e['commit'],'path':ref['path'],'sha256':ref['sha256'],'pointer':ref['pointer']+(e['field_pointer_within_record'] if op=='field_report' else '')}
            if o['citation']!=cite or exact(o['answer'])!=exact(value if op=='field_report' else None) or o['decision']!={'field_report':'ANSWER','premise_audit':'QUALIFY','unavailable_output_request':'ABSTAIN'}[op] or o['native_unit']!=e['native_unit']:raise ValueError('unbound development oracle')
    actual=[];response_sources=[]
    for label in ['a','b']:
        path=f'development-responses-{label}.json';raw=(OUT/path).read_bytes();j=json.loads(raw)
        wanted_ids={t['id'] for c in packet['cases'][0:9] if label=='a' for t in c['tasks']} if label=='a' else {t['id'] for c in packet['cases'][9:] for t in c['tasks']}
        if {r['id'] for r in j['responses']}!=wanted_ids:raise ValueError('session partition mismatch')
        actual+=j['responses'];response_sources.append({'path':path,'sha256':digest(raw),'responses':len(j['responses'])})
    rows=score(expected,actual)
    return {'format':'all-member-development-conformance-results-v1','date':'2026-10-25','sessions':2,'tasks':len(rows),'member_cases':18,'inputs_commitment':commitment,'response_files':response_sources,'totals':{key:sum(r['checks'][key] for r in rows) for key in ['decision','answer','native_unit','citation','rationale_present']}|{'all_checks_pass':sum(r['all_checks_pass'] for r in rows)},'per_task':rows,'narrative_review':{'reviewer':'authoring assistant','independent_source_qualified_specialist':False,'scope':'Read all 54 raw rationales against the compact packet and execution conditions. No unsupported substantive assertion identified in this bounded review; not a validated hallucination-rate measurement.','limitations':'Narrative grading is nonblind and development-authored. Exact-match scores do not independently authenticate source attributions or ancient readings.'},'model_metadata':{'sessions':'Fresh isolated assistant threads, each restricted to its supplied skill and nine-case packet. Expected answers and prior reasoning were not supplied.','family':'Same session-provided assistant family; no second provider tested','exact_backend_build':None,'external_human_participants':0},'academic_accuracy_established':False,'independent_scholarly_review':False,'researcher_benefit_measured':False,'interpretation':'Known-source, compact-evidence development conformance only. Related tasks share eighteen dossiers; many field reports are identifiers. No held-out, population-general or cross-platform accuracy estimate.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--write',action='store_true');a=p.parse_args();r=build(a.checkouts);s=json.dumps(r,ensure_ascii=False,indent=2)+'\n';p=OUT/'development-results.json'
    if a.write:p.write_text(s)
    elif p.read_text()!=s:raise ValueError('development score replay drift')
    print(json.dumps({'tasks':r['tasks'],'totals':r['totals'],'academic_accuracy_established':False}))
if __name__=='__main__':main()
