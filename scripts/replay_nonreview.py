#!/usr/bin/env python3
"""Acquire or replay the exact frozen inputs for all six non-review workstreams."""
import argparse
import concurrent.futures
import json
from pathlib import Path
import re
import subprocess
import sys
from nonreview_common import ROOT,OUT
SCRIPTS=('nonreview_backlog.py','ediana_fidelity.py','dependence_v2.py','research_regression.py','package_audit.py','replay_walkthroughs.py','check_forward_results.py')
def acquire(parent):
    manifest=json.loads((OUT/'inputs.json').read_text());rows=manifest['members']
    commit=manifest['master_input_commit']
    if not re.fullmatch('[a-f0-9]{40}',commit):raise ValueError('invalid frozen master input')
    subprocess.run(['git','fetch','--quiet','--depth','1','origin',commit],cwd=ROOT,check=True,timeout=180)
    def one(row):
        if not re.fullmatch(r'hawkinsnick/[A-Za-z0-9-]+',row['repository']) or not re.fullmatch('[a-f0-9]{40}',row['commit']):raise ValueError('invalid input identity')
        target=parent/row['repository'].split('/')[-1]
        if target.exists():raise ValueError('acquisition target already exists: '+str(target))
        target.mkdir(parents=True)
        for cmd in (['git','init','--quiet'],['git','remote','add','origin','https://github.com/'+row['repository']+'.git'],['git','fetch','--quiet','--depth','1','origin',row['commit']],['git','checkout','--quiet','--detach','FETCH_HEAD']):subprocess.run(cmd,cwd=target,check=True,timeout=180)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:list(ex.map(one,rows))
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--acquire',action='store_true');a=p.parse_args();parent=a.checkouts.resolve()
    if a.acquire:acquire(parent)
    for script in SCRIPTS:subprocess.run([sys.executable,str(ROOT/'scripts'/script),'--checkouts',str(parent)],cwd=ROOT,check=True)
    print('PASS: six frozen non-review workstreams replayed; no academic acceptance claimed')
