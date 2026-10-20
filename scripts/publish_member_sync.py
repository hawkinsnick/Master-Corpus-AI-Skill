#!/usr/bin/env python3
"""Publish generated master synchronization state on the exact reviewed source parent."""
import os
from pathlib import Path
import subprocess
from common import ROOT
ALLOWED={'registry/member-state.json','MEMBER-STATUS.md','migration/member-checkpoints.json','generated/skill-bundle-index.json','downloads/Master-Corpus-AI-Skill-Starter.txt'}

def publish(root=ROOT):
    root=Path(root)
    source=os.environ.get('SOURCE_COMMIT') or subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
    subprocess.run(['git','fetch','--quiet','origin','main'],cwd=root,check=True)
    if subprocess.check_output(['git','rev-parse','FETCH_HEAD'],cwd=root,text=True).strip()!=source:
        print('SKIP: master source advanced; the next refresh will rebuild.');return False
    changed=set(subprocess.check_output(['git','diff','--name-only'],cwd=root,text=True).splitlines())
    untracked=set(subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines())
    if (changed|untracked)-ALLOWED:raise ValueError('refuse unrelated master changes: '+repr(sorted((changed|untracked)-ALLOWED)))
    subprocess.run(['git','add','--']+sorted(ALLOWED),cwd=root,check=True)
    if subprocess.run(['git','diff','--cached','--quiet'],cwd=root).returncode==0:
        print('No validated member-state changes.');return False
    subprocess.run(['git','commit','-m','chore(master): refresh validated native corpus state and starter'],cwd=root,check=True)
    # Never rebase or force a validated artifact commit onto different source code.
    subprocess.run(['git','push','origin','HEAD:main'],cwd=root,check=True)
    return True
if __name__=='__main__':publish()
