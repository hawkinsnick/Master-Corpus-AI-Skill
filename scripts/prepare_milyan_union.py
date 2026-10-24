#!/usr/bin/env python3
"""Union two byte-identical Milyan caches at the digital source-text-row unit."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST='research/remediation/milyan-union-inputs.json'
REPOS={'hawkinsnick/Lycian-and-Carian','hawkinsnick/Milyan-Lycian-B'}
UNIT='nonempty_digital_source_text_row'

def sha(raw):return hashlib.sha256(raw).hexdigest()
def escape(s):return s.replace('~','~0').replace('/','~1')

def group(raws,inputs,expected_rows):
    if len(raws)!=2 or len(inputs)!=2 or {x['repository'] for x in inputs}!=REPOS:
        raise ValueError('Only the registered two source views are admitted')
    if raws[0]!=raws[1]:
        raise ValueError('Caches differ; no implicit re-edition or semantic equivalence is allowed')
    for raw,pin in zip(raws,inputs):
        if sha(raw)!=pin['sha256']:
            raise ValueError('Frozen source hash mismatch')
    source=json.loads(raws[0]);rows=[]
    if not isinstance(source,dict):raise ValueError('Unsupported source layout')
    for heading,values in source.items():
        if not isinstance(values,list):raise ValueError('Unsupported source rows')
        for i,row in enumerate(values):
            text=row.get('sentence')
            if not isinstance(text,str):raise ValueError('Missing source string')
            if not text.strip():continue
            pointer='/'+escape(heading)+'/'+str(i)
            rows.append({'source_row_pointer':pointer,'source_text_sha256':sha(text.encode()),
                         'view_assertions':[{**pin,'pointer':pointer} for pin in inputs],
                         'views_are_independent_witnesses':False})
    if len(rows)!=expected_rows:raise ValueError('Frozen row coverage drift')
    return {'format':'registered-identical-source-row-union-v1','source_family':'EDiAna_Milyan_2021_frozen_cache',
            'unit':UNIT,'inputs':inputs,'incoming_view_rows':2*len(rows),'source_row_groups':len(rows),
            'repeated_view_rows_not_additive':len(rows),'groups':rows,
            'physical_object_count':None,'independent_witness_count':None,
            'reading_adjudications_added':0,'linguistic_comparability_established':False,
            'rights':'Retain CC BY-SA 4.0 and native eDiAna attribution/change notices. This output contains identifiers, hashes and source pointers, not a new license for any printed edition.',
            'boundary':'Exact byte identity only. Exclude empty header rows by a declared source-string rule. Two cache access paths remain visible for each row; neither adds an ancient attestation or validates the underlying reading.'}

def assemble(checkouts,unit=UNIT):
    if unit!=UNIT:raise ValueError('Cannot promote digital rows to signs, words, objects or witnesses')
    manifest=json.loads((ROOT/MANIFEST).read_text())
    if manifest['unit']!=UNIT or manifest['source_family']!='EDiAna_Milyan_2021_frozen_cache':
        raise ValueError('Source family/unit drift')
    raws=[]
    for pin in manifest['inputs']:
        if pin['repository'] not in REPOS:raise ValueError('Unregistered source repository')
        root=checkouts/pin['repository'].split('/')[-1]
        raw=subprocess.check_output(['git','show',pin['commit']+':'+pin['path']],cwd=root)
        if (root/pin['path']).read_bytes()!=raw:raise ValueError('Active checkout differs from frozen source')
        raws.append(raw)
    return group(raws,manifest['inputs'],manifest['expected_source_rows'])

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path)
    p.add_argument('--unit',default=UNIT);p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true')
    a=p.parse_args();r=assemble(a.checkouts,a.unit);text=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.check:
        if not a.output or a.output.read_text()!=text:raise ValueError('Union replay drift')
    elif a.output:a.output.write_text(text)
    print(json.dumps({k:v for k,v in r.items() if k not in ('groups','inputs')},indent=2))
