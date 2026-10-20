#!/usr/bin/env python3
"""Validate a standalone instruction bundle and optionally its separate native checkouts."""
import argparse
import json
from pathlib import Path
import re
import subprocess
from common import ROOT,EXCLUDED,local,members,checkout,execute,sha
from build_starter import build

def links(root=ROOT):
    for path in Path(root).rglob('*.md'):
        if any(part in ('.git','.checkouts','__pycache__') for part in path.relative_to(root).parts):continue
        for link in re.findall(r'\]\(([^\s)]+)\)',path.read_text()):
            if re.match(r'(?:https?://|mailto:|#)',link):continue
            target=link.split('#',1)[0]
            resolved=(path.parent/target).resolve()
            if not resolved.is_relative_to(Path(root).resolve()) or not resolved.exists():raise ValueError('unresolved standalone link: '+str(path.relative_to(root))+' -> '+link)

def validate(root=ROOT,checkouts=None,require_canonical=False):
    root=Path(root);manifest,registry=members(root)
    skill=local(root,'SKILL.md').read_text()
    front=re.match(r'\A---\n(.*?)\n---\n',skill,re.S)
    if not front or not re.search(r'^name: combined-corpus-research$',front[1],re.M) or not re.search(r'^description: .+',front[1],re.M):raise ValueError('invalid standalone skill frontmatter')
    if '# Master Corpus AI Skill — '+manifest['version'] not in skill:raise ValueError('master heading/version mismatch')
    origin=json.loads(local(root,'migration/origin.json').read_bytes())
    status=manifest['migration_status']
    if status!=origin['status'] or status not in ('PREPARED_NOT_CANONICAL','CANONICAL_PUBLISHED'):raise ValueError('migration status disagreement')
    if require_canonical and status!='CANONICAL_PUBLISHED':raise ValueError('dedicated publication not yet verified')
    if not re.fullmatch('[a-f0-9]{40}',origin['commit']):raise ValueError('origin commit missing')
    if manifest['scientific_approval_granted'] is not False or manifest['cross_platform_model_accuracy_established'] is not False:raise ValueError('unsupported scientific/model certification')
    for p in ['README.md','START-HERE.md','SKILL.md','LICENSING.md','NOTICE','LICENSE','LICENSE-CODE','LICENSE-CONTENT.md']:
        local(root,p)
    for relative,raw in build(root).items():
        if local(root,relative).read_bytes()!=raw:raise ValueError('stale master fingerprint/starter: '+relative)
    for item in origin['migrated_files']:
        if sha(local(root,item['destination_path']).read_bytes())!=item['destination_sha256']:raise ValueError('migrated source changed without provenance update: '+item['destination_path'])
    state=json.loads(local(root,'registry/member-state.json').read_bytes())
    states=state['members'];expected={m['repository'] for m in registry}
    if len(states)!=len(expected) or {r['repository'] for r in states}!=expected:raise ValueError('synchronization state membership drift')
    for row in states:
        if row['status'] not in ('VALIDATED','PENDING_INITIAL_VALIDATION','PENDING_NEWER_NATIVE_REVISION','VALIDATION_FAILED'):raise ValueError('unknown synchronization status')
        for key in ('observed_commit','accepted_commit'):
            if row.get(key) is not None and not re.fullmatch('[a-f0-9]{40}',row[key]):raise ValueError('invalid native state revision')
        if row['status']=='VALIDATED':
            if row.get('accepted_commit') is None or row['accepted_commit']!=row.get('observed_commit'):raise ValueError('validated state does not bind observed revision')
            for key in ('skill_sha256','bundle_sha256'):
                if not re.fullmatch('[a-f0-9]{64}',row.get(key,'')):raise ValueError('validated native hash missing')
    links(root)
    cases=json.loads(local(root,'tests/adversarial-cases.json').read_bytes())['cases']
    if len(cases)<12 or len({x['id'] for x in cases})!=len(cases):raise ValueError('invalid behavioral case inventory')
    result={'format':'standalone-master-validation-v1','status':'PASS_STANDALONE_INSTRUCTIONS',
            'migration_status':status,'migration_completed':status=='CANONICAL_PUBLISHED',
            'member_count':len(registry),'behavioral_prompt_inventory':len(cases),
            'behavioral_prompts_automatically_scored':False,'native_member_results':[],
            'native_corpus_payload_included':False,'scholarly_acceptance_granted':False}
    if checkouts is not None:
        for member in registry:
            native=checkout(checkouts,member)
            value=execute(native,['scripts/validate_ai_skill.py'])
            if value['repository']!=member['repository'] or value['skill_version']!=member['required_skill_version'] or value['status']!='PASS_SCOPED_FUNCTIONAL_CHECKS':raise ValueError('invalid native skill result')
            result['native_member_results'].append(value)
        result['status']='PASS_MASTER_AND_18_NATIVE_WORKFLOWS'
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',type=Path);p.add_argument('--output',type=Path)
    p.add_argument('--require-canonical',action='store_true');a=p.parse_args()
    try:r=validate(checkouts=a.checkouts,require_canonical=a.require_canonical)
    except (ValueError,OSError,KeyError,subprocess.SubprocessError) as e:p.exit(2,str(e)+'\n')
    text=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    else:print(text,end='')
if __name__=='__main__':main()
