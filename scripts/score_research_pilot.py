#!/usr/bin/env python3
"""Score disclosed structured development responses; no automatic scholarly truth grading."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];STUDY=ROOT/'research/2026-10-21'
def digest(raw):return hashlib.sha256(raw).hexdigest()
def same(a,b):return json.dumps(a,sort_keys=True,ensure_ascii=False)==json.dumps(b,sort_keys=True,ensure_ascii=False)
def verify_freeze(study=STUDY):
    freeze=json.loads((study/'ai-freeze.json').read_text())
    for path,wanted in freeze['commitments'].items():
        if digest((study/path).read_bytes())!=wanted:raise ValueError('freeze commitment mismatch: '+path)
    return freeze

def score(responses,oracle,evidence_ids):
    answers={}
    for r in responses:
        if r['id'] in answers:raise ValueError('duplicate response ID')
        answers[r['id']]=r
    expected={r['id'] for r in oracle['tasks']}
    if set(answers)!=expected:raise ValueError('missing or extra response task IDs')
    rows=[]
    for target in oracle['tasks']:
        r=answers[target['id']];refs=r.get('evidence_ids',[])
        if not isinstance(refs,list) or not all(isinstance(x,str) for x in refs):raise ValueError('invalid evidence citation list')
        checks={'decision':r.get('decision')==target['decision'],'requested_values':same(r.get('values'),target['values']),'evidence_id_selection':set(target['required_evidence_ids'])==set(refs) and set(refs)<=set(evidence_ids)}
        rows.append({'id':target['id'],'checks':checks,'all_structured_checks_pass':all(checks.values()),'direct_extraction_baseline_applicable':target['direct_extraction_baseline_applicable']})
    return {'tasks':len(rows),'decision_matches':sum(r['checks']['decision'] for r in rows),'requested_value_matches':sum(r['checks']['requested_values'] for r in rows),'evidence_id_matches':sum(r['checks']['evidence_id_selection'] for r in rows),'all_structured_checks_pass':sum(r['all_structured_checks_pass'] for r in rows),'results':rows,'semantic_truth_automatically_scored':False}

def baseline(packet):
    evidence={r['evidence_id']:r['supplied_fields'] for r in packet['evidence']}
    return [
        {'id':'T01','values':{k:evidence['E01'][k] for k in ['site','period']},'evidence_ids':['E01']},
        {'id':'T06','values':{k:evidence['E06'][k] for k in ['source_catalog_label','primary_edition_verified']},'evidence_ids':['E06']},
        {'id':'T08','values':{k:evidence['E07'][k] for k in ['locator','stored_token_fields']},'evidence_ids':['E07']}]

def build(study=STUDY):
    verify_freeze(study);oracle=json.loads((study/'ai-oracle.json').read_text());packet=json.loads((study/'ai-evidence-packet.json').read_text());runs=json.loads((study/'ai-runs.json').read_text())
    known={r['evidence_id'] for r in packet['evidence']};results=[]
    for r in runs['runs']:
        path=study/r['response_file'];raw=path.read_bytes()
        if digest(raw)!=r['response_sha256']:raise ValueError('response hash mismatch')
        results.append({'run_id':r['id'],'response_file':r['response_file'],'score':score(json.loads(raw),oracle,known)})
    base=baseline(packet);targets={x['id']:x for x in oracle['tasks']};b=[{'id':x['id'],'requested_values_match':same(x['values'],targets[x['id']]['values'])} for x in base]
    return {'format':'source-grounded-ai-pilot-scores-v1','runs':results,'direct_extraction_baseline':{'tasks':len(b),'requested_value_matches':sum(x['requested_values_match'] for x in b),'results':b,'scope':'Source field extraction only; no safety-task or researcher-time baseline.'},'accuracy_population':'These selected tasks only; no population accuracy estimate, independent scholarly grade or cross-platform comparison.','citation_measure':'Evidence-ID selection against frozen packet, not bibliographic correctness or independent source consultation.','expert_validation_granted':False}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',action='store_true');a=p.parse_args();value=build();text=json.dumps(value,ensure_ascii=False,indent=2)+'\n';dest=STUDY/'ai-scores.json'
    if a.write:dest.write_text(text)
    elif not dest.exists() or dest.read_text()!=text:raise ValueError('pilot score replay mismatch')
    print(json.dumps({'status':'PASS_STRUCTURED_PILOT_SCORE_REPLAY','runs':len(value['runs']),'expert_validation':False}))
if __name__=='__main__':main()
