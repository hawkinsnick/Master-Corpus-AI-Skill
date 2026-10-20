"""Shared path, identity and registry controls for the standalone master."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'hawkinsnick/Egyptian-Hieroglyphic-Corpus','hawkinsnick/LightroomIsSlow','hawkinsnick/Open-Endurance-Coaching'}

def sha(raw):return hashlib.sha256(raw).hexdigest()

def local(root,relative):
    root=Path(root).resolve();part=Path(relative)
    if part.is_absolute() or '..' in part.parts:raise ValueError('unsafe master path: '+relative)
    path=(root/part).resolve()
    if not path.is_relative_to(root) or not path.is_file():raise ValueError('missing master input: '+relative)
    return path

def members(root=ROOT):
    manifest=json.loads(local(root,'manifest.json').read_bytes())
    registry=json.loads(local(root,manifest['registry']).read_bytes())
    values=registry['members'];names=[m['repository'] for m in values]
    if len(values)!=manifest['member_count'] or len(names)!=len(set(names)):raise ValueError('registry cardinality/uniqueness mismatch')
    if set(names)&EXCLUDED:raise ValueError('excluded project in factory master registry')
    for member in values:
        if not re.fullmatch(r'hawkinsnick/[A-Za-z0-9-]+',member['repository']):raise ValueError('invalid repository identity')
        for key in ['individual_skill_path','authority_profile_path','bundle_index_path','validation_path']:
            path=member[key]
            if Path(path).is_absolute() or '..' in Path(path).parts:raise ValueError('unsafe native registry path')
        admission=member['admission']
        if admission.get('status')!='PASS' or admission.get('individual_ai_skill') is not True or admission.get('master_ai_member') is not True:raise ValueError('member not declared admitted')
        if set(admission.get('licensing_paths',[]))!={'LICENSE','LICENSE-CODE','LICENSE-CONTENT.md','LICENSING.md','NOTICE'}:raise ValueError('component licensing architecture missing')
        if member['required_skill_version']!=manifest['required_member_skill_version']:raise ValueError('member skill contract mismatch')
    return manifest,values

def checkout(parent,member):
    parent=Path(parent).resolve();root=(parent/member['repository'].split('/')[-1]).resolve()
    if not root.is_relative_to(parent) or not root.is_dir():raise ValueError('missing/unsafe native checkout: '+member['repository'])
    origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=root,text=True,stderr=subprocess.PIPE).strip()
    expected=member['repository']
    if origin.rstrip('/').removesuffix('.git') not in ('https://github.com/'+expected,'git@github.com:'+expected):raise ValueError('native Git origin identity mismatch: '+expected)
    return root

def execute(root,args):
    result=subprocess.run([sys.executable]+args,cwd=root,capture_output=True,text=True,timeout=180)
    if result.returncode:raise ValueError(result.stderr.strip() or result.stdout.strip() or 'native command failed')
    return json.loads(result.stdout)
