#!/usr/bin/env python3
"""Refresh exact validated native revisions; never silently advance failed or racing inputs."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import copy
import json
from pathlib import Path
import re
import subprocess
import tempfile
from common import ROOT,members,execute,sha
from build_starter import build
STATE='registry/member-state.json'


def remote_head(repository):
    if not re.fullmatch(r'hawkinsnick/[A-Za-z0-9-]+',repository):raise ValueError('invalid registered repository')
    text=subprocess.check_output(['git','ls-remote','https://github.com/'+repository+'.git','refs/heads/main'],text=True,stderr=subprocess.PIPE,timeout=60).strip()
    parts=text.split()
    if len(parts)!=2 or parts[1]!='refs/heads/main' or not re.fullmatch('[a-f0-9]{40}',parts[0]):raise ValueError('cannot resolve exact native main')
    return parts[0]


def validate_revision(repository,commit):
    with tempfile.TemporaryDirectory(prefix='master-member-') as folder:
        root=Path(folder)
        for cmd in (['git','init','--quiet'],['git','remote','add','origin','https://github.com/'+repository+'.git'],
                    ['git','fetch','--quiet','--depth','1','origin',commit],['git','checkout','--quiet','--detach','FETCH_HEAD']):
            subprocess.run(cmd,cwd=root,check=True,capture_output=True,text=True,timeout=120)
        if subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()!=commit:raise ValueError('native checkout revision mismatch')
        result=execute(root,['scripts/validate_ai_skill.py'])
        if result.get('repository')!=repository or result.get('status')!='PASS_SCOPED_FUNCTIONAL_CHECKS':raise ValueError('native skill validation did not pass')
        # Retain only integrity/scope metadata, not native source payloads or copied readings.
        return {key:result[key] for key in ('skill_name','skill_version','scope','skill_sha256','bundle_sha256','bundle_source_commit','indexed_artifact_entries_checked')}


def observe(member,previous,validator_hash,probe=remote_head,verify=validate_revision):
    repository=member['repository'];old=copy.deepcopy(previous or {'repository':repository,'accepted_commit':None})
    try:
        candidate=probe(repository)
        if old.get('status')=='VALIDATED' and old.get('accepted_commit')==candidate and old.get('validator_sha256')==validator_hash:
            return old
        details=verify(repository,candidate)
        if details['skill_version']!=member['required_skill_version']:raise ValueError('native skill contract version changed; admission update required')
        newest=probe(repository)
        if newest!=candidate:
            old.update({'repository':repository,'observed_commit':newest,'status':'PENDING_NEWER_NATIVE_REVISION',
                        'candidate_commit':candidate,'last_error':'Native main advanced during validation; accepted snapshot is unchanged.'})
            return old
        return {'repository':repository,'observed_commit':candidate,'accepted_commit':candidate,
                'status':'VALIDATED','validator_sha256':validator_hash,**details}
    except (ValueError,OSError,KeyError,subprocess.SubprocessError) as error:
        old.update({'repository':repository,'status':'VALIDATION_FAILED','last_error':str(error)[:2000]})
        if 'candidate' in locals():old['observed_commit']=candidate
        return old


def refresh(root=ROOT,probe=remote_head,verify=validate_revision):
    root=Path(root);_,registry=members(root)
    previous=json.loads((root/STATE).read_bytes()) if (root/STATE).is_file() else {'members':[]}
    old={r['repository']:r for r in previous['members']}
    # Source changes in the synchronization/check code force a recheck of native snapshots.
    fingerprint=sha((root/'scripts/sync_members.py').read_bytes()+(root/'scripts/validate.py').read_bytes()+(root/'scripts/common.py').read_bytes())
    with ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(lambda m:observe(m,old.get(m['repository']),fingerprint,probe,verify),registry))
    return {'format':'master-native-member-state-v1','master_repository':'hawkinsnick/Master-Corpus-AI-Skill',
            'policy':'Refresh metadata and starter only after exact native skill validation; preserve the last accepted revision on failure/race.',
            'refresh_interval_minutes':5,'schedule_latency_guaranteed':False,
            'members':results,'scholarly_acceptance_granted':False,'cross_platform_model_accuracy_established':False}


def write(result,root=ROOT):
    root=Path(root);(root/STATE).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    lines=['# Native corpus synchronization status','',
           'This is a byte-bound engineering snapshot. Scheduled refreshes run every five minutes; GitHub may delay them. Native evidence and rights remain authoritative.','',
           '| Corpus | Observed main | Last validated revision | Status |','|---|---|---|---|']
    for item in result['members']:
        repo=item['repository'];observed=item.get('observed_commit');accepted=item.get('accepted_commit')
        def link(commit):return '['+commit[:12]+'](https://github.com/'+repo+'/tree/'+commit+')' if commit else 'Not yet verified'
        lines.append('| ['+repo.split('/')[-1]+'](https://github.com/'+repo+') | '+link(observed)+' | '+link(accepted)+' | '+item['status']+' |')
    lines+=['','An accepted revision indicates the native functional checks passed. It does not establish accepted readings, decipherment, source independence, permissions or expert acceptance.','']
    (root/'MEMBER-STATUS.md').write_text('\n'.join(lines))
    pins=json.loads((root/'migration/member-checkpoints.json').read_bytes())
    # Only replace an existing checkpoint when this exact source snapshot passed.
    accepted={r['repository']:r['accepted_commit'] for r in result['members'] if r.get('status')=='VALIDATED'}
    for item in pins['members']:
        if item['repository'] in accepted:item['commit']=accepted[item['repository']]
    (root/'migration/member-checkpoints.json').write_text(json.dumps(pins,indent=2)+'\n')
    for relative,raw in build(root).items():(root/relative).write_bytes(raw)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',action='store_true');a=p.parse_args()
    result=refresh()
    if a.write:write(result)
    print(json.dumps({'members':len(result['members']),'validated':sum(r['status']=='VALIDATED' for r in result['members']),
                      'pending_or_failed':[{'repository':r['repository'],'status':r['status']} for r in result['members'] if r['status']!='VALIDATED']}))
    if any(r['status']!='VALIDATED' for r in result['members']):raise SystemExit(1)
if __name__=='__main__':main()
