#!/usr/bin/env python3
"""Verify recorded documentary assertions and scope; a passing receipt is not expert adjudication."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];RECEIPT=ROOT/'research/2026-10-21-followup/printed-source-recheck.json'
def verify(receipt,native_rows):
    native={x['occurrence_id']:x for x in native_rows}
    if receipt['external_specialist_review'] or receipt['primary_object_inspected'] or receipt['new_independent_witnesses']!=0:raise ValueError('unsupported scientific upgrade')
    if receipt['corrections_to_native_readings']!=0:raise ValueError('this receipt does not authorize reading changes')
    for a in receipt['assertions']:
        x=native[a['occurrence_id']]
        if x['record_id']!=receipt['record_id'] or x['source_id']!=receipt['source_id'] or x['position']!=a['position'] or x['published_sign_label']!=a['recorded_source_label']:raise ValueError('documentary assertion mismatch')
    return len(receipt['assertions'])
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--pdf',type=Path);a=p.parse_args();r=json.loads(RECEIPT.read_text());folder=a.checkouts/'Cypro-Minoan';raw=(folder/r['native_path']).read_bytes()
    if subprocess.check_output(['git','rev-parse','HEAD'],cwd=folder,text=True).strip()!=r['native_input_commit']:raise ValueError('wrong frozen source state')
    if hashlib.sha256(raw).hexdigest()!=r['native_path_sha256']:raise ValueError('native input changed')
    count=verify(r,json.loads(raw)['occurrences'])
    if a.pdf:
        pdf=a.pdf.read_bytes()
        if not pdf.startswith(b'%PDF') or hashlib.sha256(pdf).hexdigest()!=r['publication']['pdf_sha256']:raise ValueError('PDF is not the inspected copy')
    print(json.dumps({'status':'PASS_RECORDED_DOCUMENTARY_ASSERTIONS','assertions':count,'pdf_copy_hash_checked':bool(a.pdf),'independent_scholarly_review':False,'visual_consultation_automatically_proven':False}))
if __name__=='__main__':main()
