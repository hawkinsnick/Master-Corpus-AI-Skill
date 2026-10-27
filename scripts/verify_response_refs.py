#!/usr/bin/env python3
"""Verify atomic machine-readable response citations against actual committed source bytes."""
import argparse
import json
from pathlib import Path
import re
import subprocess
from review_integrity import safe,digest,pointer

def verify(ref,parent,master):
    repo=ref['repository']
    if not re.fullmatch(r'hawkinsnick/[A-Za-z0-9-]+',repo):raise ValueError('invalid repository')
    root=master if repo=='hawkinsnick/Master-Corpus-AI-Skill' else parent/repo.split('/')[-1]
    path=ref['path'];current=safe(root,path).read_bytes();commit=ref.get('commit')
    if not isinstance(commit,str) or not re.fullmatch('[a-f0-9]{40}',commit):raise ValueError('committed citation requires exact commit')
    origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=root,text=True).strip().removesuffix('.git')
    if origin!='https://github.com/'+repo:raise ValueError('repository origin differs')
    if subprocess.run(['git','cat-file','-e',commit+'^{commit}'],cwd=root,capture_output=True).returncode:raise ValueError('cited commit is unavailable; acquire it before verification')
    r=subprocess.run(['git','show',commit+':'+path],cwd=root,capture_output=True)
    if r.returncode:raise ValueError('path does not exist at cited commit')
    if digest(r.stdout)!=ref['sha256']:raise ValueError('hash does not bind cited commit bytes')
    if digest(current)!=ref['sha256']:raise ValueError('working bytes differ from cited source')
    kind=ref.get('locator_type','json_pointer')
    if kind=='json_pointer':
        if not path.endswith(('.json','.jsonl')):raise ValueError('text citation requires typed text locator')
        if path.endswith('.jsonl'):value=[json.loads(x) for x in r.stdout.decode().splitlines() if x.strip()]
        else:value=json.loads(r.stdout)
        pointer(value,ref['pointer'])
    elif kind=='text_contains':
        needle=ref.get('locator')
        if not isinstance(needle,str) or not needle or needle not in r.stdout.decode():raise ValueError('text locator not present')
        if 'pointer' in ref:raise ValueError('text locator must not masquerade as JSON pointer')
    else:raise ValueError('unsupported locator type')
    return {'status':'PASS_EXACT_COMMITTED_LOCUS','repository':repo,'commit':commit,'path':path,'sha256':ref['sha256'],'locator_type':kind}

def score(value,parent,master):
    rows=[]
    for ai,answer in enumerate(value['answers']):
        for ri,ref in enumerate(answer['source_refs']):
            try:result=verify(ref,parent,master)
            except (ValueError,KeyError,IndexError,OSError,subprocess.SubprocessError) as e:result={'status':'FAIL_CITATION','error':str(e)}
            rows.append({'answer':ai,'reference':ri,**result})
    return {'references_checked':len(rows),'passed':sum(x['status']=='PASS_EXACT_COMMITTED_LOCUS' for x in rows),'failed':sum(x['status']=='FAIL_CITATION' for x in rows),'results':rows,'bibliographic_truth_or_expert_approval_established':False}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--responses',required=True,type=Path);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--master',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();r=score(json.loads(a.responses.read_text()),a.checkouts,a.master);print(json.dumps(r,indent=2));raise SystemExit(bool(r['failed']))
