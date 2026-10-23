#!/usr/bin/env python3
"""Assemble only the registered Cypriot source-entry union, preserving both views.

This is a digital-edition source union, not physical-object deduplication or a
language-frequency dataset. Other cross-corpus relations remain inadmissible.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FAMILY='IG_XV_1_FROZEN_DIGITAL_EDITION'
REPOS=('Cypriot-syllabic-Greek','Eteocypriot')
PATH='exports/corpus.json'

def assemble(checkouts):
    manifest=json.loads((ROOT/'research/remediation/source-union-inputs.json').read_text())
    if manifest['source_family']!=FAMILY or manifest['unit']!='digital_edition_entry':
        raise ValueError('Source family/unit manifest drift')
    pins={x['repository'].split('/')[-1]:x for x in manifest['inputs']}
    if set(pins)!=set(REPOS) or len(manifest['inputs'])!=2:
        raise ValueError('Registered input membership drift')
    observations=[]; inputs=[]; grouped={}
    for repo in REPOS:
        root=checkouts/repo
        commit=pins[repo]['commit']
        if pins[repo]['path']!=PATH:
            raise ValueError('Registered input path drift')
        raw=subprocess.check_output(['git','show',f'{commit}:{PATH}'],cwd=root)
        if (root/PATH).read_bytes()!=raw:
            raise ValueError('Input differs from recorded commit: '+repo)
        pin=hashlib.sha256(raw).hexdigest()
        if pin!=pins[repo]['sha256']:
            raise ValueError('Frozen source hash mismatch')
        records=json.loads(raw)['records']
        if len(records)!=pins[repo]['records']:
            raise ValueError('Frozen source count mismatch')
        seen=set()
        for i,r in enumerate(records):
            if r['record_unit']!='digital_edition_entry':
                raise ValueError('Incompatible evidence unit; no implicit sign/record conversion')
            sid=r['source_id']
            if not sid.startswith('IG XV 1, ') or sid in seen:
                raise ValueError('Invalid or duplicate source ID within view')
            seen.add(sid)
            item={'repository':'hawkinsnick/'+repo,'commit':commit,'path':PATH,'sha256':pin,
                  'pointer':f'/records/{i}','view_record_id':r['id']}
            grouped.setdefault(sid,[]).append(item)
            observations.append(sid)
        inputs.append({'repository':'hawkinsnick/'+repo,'commit':commit,'path':PATH,'sha256':pin,'records':len(records)})
    left={k for k,v in grouped.items() if any(x['repository'].endswith('/'+REPOS[0]) for x in v)}
    right={k for k,v in grouped.items() if any(x['repository'].endswith('/'+REPOS[1]) for x in v)}
    if not right<=left:
        raise ValueError('Registered overlap changed; investigate before assembly')
    return {'format':'registered-source-entry-union-v1','source_family':FAMILY,
            'unit':'digital_edition_entry','inputs':inputs,
            'incoming_view_rows':len(observations),'source_entry_groups':len(grouped),
            'repeated_view_rows_not_additive':len(observations)-len(grouped),
            'groups':[{'source_id':k,'source_family':FAMILY,'view_assertions':v,
                       'views_are_independent_witnesses':False} for k,v in grouped.items()],
            'physical_object_count':None,'language_frequency_allowed':False,
            'source_readings_adjudicated':False,
            'boundary':'Group IDs from the registered same digital edition only. Retain distinct view assertions and exact pointers; no preference or sign/reading reconciliation is implied. Unknown corpus relations are not admitted by this tool.'}

def validate_study(repositories,unit):
    if set(repositories)!=set(REPOS) or len(repositories)!=2:
        raise ValueError('Unregistered comparison: source dependence and compatible units must be established first')
    if unit!='digital_edition_entry':
        raise ValueError('This union cannot supply sign, linguistic, physical-object or independent-witness units')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path)
    p.add_argument('--unit',default='digital_edition_entry');p.add_argument('--repositories',nargs='+',default=list(REPOS));p.add_argument('--output',type=Path);p.add_argument('--check',action='store_true')
    a=p.parse_args();validate_study(a.repositories,a.unit);r=assemble(a.checkouts)
    text=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.check:
        if a.output is None or a.output.read_text()!=text:
            raise ValueError('Source union replay drift')
    elif a.output:
        a.output.write_text(text)
    print(json.dumps({k:v for k,v in r.items() if k not in ('groups','inputs')},indent=2))
