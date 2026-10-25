#!/usr/bin/env python3
"""Resolve corrected field provenance and reject scope/citation forgery; do not score academic truth."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];STUDY=ROOT/'research/2026-10-21-followup'
from review_integrity import pointer

def resolve(ref,parent,root=ROOT):
    scope=ref['scope']
    if scope=='native':
        pins={m['repository']:m['commit'] for m in json.loads((root/'research/2026-10-21/native-revisions.json').read_text())['members']}
        if ref.get('repository') not in pins or ref.get('commit')!=pins[ref['repository']]:raise ValueError('unbound native identity/revision')
        folder=parent/ref['repository'].split('/')[-1]
        if subprocess.check_output(['git','rev-parse','HEAD'],cwd=folder,text=True).strip()!=ref['commit']:raise ValueError('wrong native checkout')
    elif scope in {'master','task_context'}:
        folder=root
        is_context=ref['path']=='research/2026-10-21-followup/evaluation-task-context.json'
        if (scope=='task_context')!=is_context:raise ValueError('task context/native or computation scope conflation')
    else:raise ValueError('unknown evidence scope')
    path=Path(ref['path']);target=(folder/path).resolve()
    if path.is_absolute() or '..' in path.parts or not target.is_relative_to(folder.resolve()):raise ValueError('unsafe evidence path')
    raw=target.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=ref['sha256']:raise ValueError('citation hash mismatch')
    if ref['encoding']=='json':value=json.loads(raw)
    elif ref['encoding']=='jsonl':value=[json.loads(x) for x in raw.decode().splitlines() if x.strip()]
    else:raise ValueError('unsupported encoding')
    value=pointer(value,ref['pointer']);transform=ref.get('transform')
    if transform=='length':value=len(value)
    elif transform=='pluck_slot_zero_based':value=[x['slot_zero_based'] for x in value]
    elif transform is not None:raise ValueError('undeclared transform')
    return value

def validate(parent):
    v=json.loads((STUDY/'evaluation-v2.json').read_text());seen=set();fields=0
    for task in v['items']:
        if task['id'] in seen:raise ValueError('duplicate task')
        seen.add(task['id'])
        if set(task['field_bindings'])!=set(task['expected_source_values']):raise ValueError('unbound response field')
        for key,ref in task['field_bindings'].items():
            actual=resolve(ref,parent)
            if json.dumps(actual,sort_keys=True)!=json.dumps(task['expected_source_values'][key],sort_keys=True):raise ValueError('field provenance mismatch: '+task['id']+' '+key)
            fields+=1
        if task['conformance_decision']!={'field_report':'ANSWER','premise_audit':'QUALIFY','unavailable_output_request':'ABSTAIN'}[task['primary_operation']]:raise ValueError('decision rubric drift')
    return {'status':'PASS_V2_FIELD_PROVENANCE_AND_RUBRIC','tasks':len(seen),'field_bindings':fields,'new_model_accuracy_measurement':False,'independent_scholarly_grade':False}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path);a=p.parse_args();print(json.dumps(validate(a.checkouts)))
