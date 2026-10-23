#!/usr/bin/env python3
"""Check fixed batch scope and native bindings; does not automate visual review."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RECEIPT=ROOT/'research/2026-10-22/source-batch.json'
def verify(receipt,raw):
    if hashlib.sha256(raw).hexdigest()!=receipt['native_sha256']:
        raise ValueError('native source checksum mismatch')
    native=json.loads(raw)['comparisons']; cases=receipt['cases']
    if len(native)!=6 or len(cases)!=6 or len({x['comparison_id'] for x in cases})!=6:
        raise ValueError('fixed six-case scope changed')
    verified=inaccessible=discrepant=0
    for i,(c,n) in enumerate(zip(cases,native)):
        for key in ['record_id','zone_id','position','comparison_id']:
            if c[key]!=n[key]: raise ValueError('native case binding mismatch')
        if c['native_pointer']!=f'/comparisons/{i}' or len(c['assertions'])!=2:
            raise ValueError('assertion scope mismatch')
        for a,b in zip(c['assertions'],n['assertions']):
            if any(a[k]!=v for k,v in b.items()): raise ValueError('native assertion changed')
            direct=a['source_id']!='olivier2007'
            if a['direct_source_inspected']!=direct or a['outcome']!=('VERIFIED_ATTRIBUTION' if direct else 'INACCESSIBLE_PRIMARY'):
                raise ValueError('unsupported inspection upgrade or missing outcome')
            verified+=direct; inaccessible+=not direct
        outcome='DISCREPANT_SOURCE' if i==5 else 'INACCESSIBLE_PRIMARY'
        if c['case_outcome']!=outcome or c['reading_adopted'] or not c['uncertainty_preserved']:
            raise ValueError('unsupported resolution or lost uncertainty')
        discrepant+=i==5
    expected={'cases':6,'assertions':12,'verified_attributions':verified,'inaccessible_primary_assertions':inaccessible,'discrepant_source_cases':discrepant,'native_attribution_errors_found':0}
    if receipt['totals']!=expected: raise ValueError('summary mismatch')
    if receipt['reading_changes'] or receipt['external_reviews_received'] or receipt['primary_object_inspected'] or receipt['source_files_redistributed']:
        raise ValueError('unsupported scholarly upgrade')
    return expected

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--pdf',type=Path);a=p.parse_args()
    r=json.loads(RECEIPT.read_text());folder=a.checkouts/'Cypro-Minoan'
    if subprocess.check_output(['git','rev-parse','HEAD'],cwd=folder,text=True).strip()!=r['native_commit']:raise ValueError('wrong native checkpoint')
    totals=verify(r,(folder/r['native_path']).read_bytes())
    if a.pdf:
        raw=a.pdf.read_bytes()
        if not raw.startswith(b'%PDF') or len(raw)!=r['publication']['bytes'] or hashlib.sha256(raw).hexdigest()!=r['publication']['sha256']:raise ValueError('wrong publication copy')
    print(json.dumps({'status':'PASS_FIXED_BATCH_BINDINGS','totals':totals,'pdf_hash_checked':bool(a.pdf),'visual_review_automatically_proven':False}))
if __name__=='__main__':main()
