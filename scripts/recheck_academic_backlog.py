#!/usr/bin/env python3
"""Re-resolve all 43 inherited open closure packages without relaxing their scholarly criteria."""
import argparse
import collections
import json
import subprocess
from pathlib import Path
from review_integrity import safe,digest,exact,pointer,checkpoints
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/2026-10-25'
def build(parent):
    manifest=json.loads((OUT/'inputs.json').read_text());roots=checkpoints(parent,manifest);roots['Master-Corpus-AI-Skill']=ROOT
    native=roots['Linear-A'];path='corpus-factory/academic-defect-register-2026-10-23.json';register=json.loads(safe(native,path).read_bytes());prior_path='corpus-factory/remediation-execution-review-2026-10-24.json';prior=json.loads(safe(native,prior_path).read_bytes())
    included={x['id']:x for x in prior['items']};items=[]
    if len(included)!=43:raise ValueError('inherited open scope changed')
    for item in register['items']:
        if item['id'] not in included:continue
        observations=[]
        for e in item['evidence']:
            root=roots[e['repository'].split('/')[-1]]
            if e['repository']=='hawkinsnick/Master-Corpus-AI-Skill':
                safe(ROOT,e['path'])
                raw=subprocess.check_output(['git','show',manifest['master_input_commit']+':'+e['path']],cwd=ROOT)
            else:raw=safe(root,e['path']).read_bytes()
            if e['locator_type']=='json_pointer':value=pointer(json.loads(raw),e['locator'])
            elif e['locator_type']=='text_contains':value=[[i+1,line] for i,line in enumerate(raw.decode().splitlines()) if e['locator'] in line]
            else:raise ValueError('unknown observation locator')
            observed=digest(exact(value).encode());matches=observed==e['observed_sha256'] if 'observed_sha256' in e else exact(value)==exact(e['observed'])
            observations.append({'repository':e['repository'],'path':e['path'],'current_sha256':digest(raw),'locator_type':e['locator_type'],'locator':e['locator'],'observed_sha256':observed,'frozen_observation_unchanged':matches})
        items.append({'id':item['id'],'title':item['title'],'scope':item['affected_scope'],'work_class':included[item['id']]['work_class'],'claim_limited':item['claim_blocked_or_limited'],'closure_criteria_unchanged':item['closure_criteria'],'evidence_recheck':observations,'status':'HISTORICAL_QUEUE_REQUIREMENT_NOT_CURRENT_LEDGER_COUNTER','next_evidence_requirement':included[item['id']]['remaining_action']})
    return {'format':'all-open-academic-closure-recheck-v1','date':'2026-10-25','inputs':'inputs.json','register':{'repository':'hawkinsnick/Linear-A','path':path,'sha256':digest(safe(native,path).read_bytes())},'prior_execution_review':{'path':prior_path,'sha256':digest(safe(native,prior_path).read_bytes())},'totals':{'items':len(items),'observations':sum(len(i['evidence_recheck']) for i in items),'changed_observations':sum(not e['frozen_observation_unchanged'] for i in items for e in i['evidence_recheck']),'new_scholarly_closures':0},'by_work_class':dict(collections.Counter(i['work_class'] for i in items)),'items':items,'boundary':'Re-resolved observations at eighteen pinned native checkpoints and the pinned pre-change master git blobs. Equal observations do not exhaust source literature or prove no improvement is possible. New engineering/source-fidelity controls do not satisfy missing specialist, primary-edition or human-outcome criteria. This replays the inherited 43-package state; later scoped-control closures are tracked separately in references/scoped-closures-2026-10-25.md, not reversed by this receipt.'}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--write',action='store_true');a=p.parse_args();r=build(a.checkouts);s=json.dumps(r,ensure_ascii=False,indent=2)+'\n';t=OUT/'academic-backlog-recheck.json'
    if a.write:t.write_text(s)
    elif t.read_text()!=s:raise ValueError('academic backlog replay drift')
    print(json.dumps(r['totals']))
if __name__=='__main__':main()
