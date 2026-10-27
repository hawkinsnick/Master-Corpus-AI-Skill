#!/usr/bin/env python3
"""Run eighteen exact-ID walkthroughs through the actual master query CLI."""
import json
import subprocess
import sys
from nonreview_common import ROOT,OUT,roots,receipt,cli,digest,exact

def build(parent):
    roots(parent);cases=json.loads((OUT/'research-regression.json').read_text())['walkthroughs'];rows=[]
    for case in cases:
        args=[str(parent.resolve()) if x=='CHECKOUT_PARENT' else x for x in case['command'][1:]]
        p=subprocess.run([sys.executable]+args,cwd=ROOT,capture_output=True,text=True,timeout=90)
        if p.returncode:raise ValueError(case['repository']+': '+p.stderr)
        value=json.loads(p.stdout)
        if len(value['results_by_repository'])!=1 or value['unique_object_count'] is not None or value['independent_witness_count'] is not None:raise ValueError('namespace/denominator changed')
        result=value['results_by_repository'][0];payload=result['native_payload']
        # Native CLI dossier is the payload, not an invented master reserialization.
        if payload['provenance']!=case['source_ref'] or digest(exact(payload['native_record']).encode())!=case['full_record_sha256'] or len(payload['explicitly_linked_records'])!=case['expected_linked_records']:raise ValueError('walkthrough source/linked output changed')
        rows.append({'repository':case['repository'],'collection':case['collection'],'id':case['id'],'native_checkout_commit':result['native_checkout_commit'],'source_ref':payload['provenance'],'record_sha256':case['full_record_sha256'],'linked_records_checked':len(payload['explicitly_linked_records']),'status':'PASS_ACTUAL_MASTER_CLI','native_unit':payload['native_unit']})
    return {'format':'executed-eighteen-member-walkthroughs-v1','date':'2026-10-27','inputs':'inputs.json','rows':rows,'totals':{'walkthroughs_executed':len(rows),'passed':len(rows)},'master_checkpoint_relation_note':'Native input commits are pinned; later master acceptance may change checkpoint_relation without changing source assertions. That display field is checked by master query but not frozen into this study receipt.','claims':'Exact source output and linked assertions only. No model accuracy, scholarly correctness or user productivity measurement.'}
if __name__=='__main__':
    a=cli(__doc__);r=receipt('walkthrough-replay.json',build(a.checkouts),a.write);print(r['totals'])
