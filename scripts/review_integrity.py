"""Strict evidence resolution shared by the hostile-review checks."""
import csv
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path

def digest(raw):return hashlib.sha256(raw).hexdigest()
def exact(value):return json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'))
def safe(root,relative):
    root=Path(root).resolve();p=Path(relative);target=(root/p).resolve()
    if p.is_absolute() or '..' in p.parts or not target.is_relative_to(root) or not target.is_file():raise ValueError('unsafe or missing evidence path: '+relative)
    return target

def pointer(value,path):
    if not isinstance(path,str) or (path and not path.startswith('/')):raise ValueError('invalid JSON pointer')
    for part in path.split('/')[1:] if path else []:
        if re.search(r'~(?![01])',part):raise ValueError('invalid JSON pointer escape')
        part=part.replace('~1','/').replace('~0','~')
        if isinstance(value,list):
            if not re.fullmatch(r'0|[1-9][0-9]*',part):raise ValueError('noncanonical array pointer')
            value=value[int(part)]
        elif isinstance(value,dict):value=value[part]
        else:raise ValueError('pointer traverses scalar')
    return value

def parse(raw,encoding):
    if encoding=='json':return json.loads(raw)
    if encoding=='jsonl':return [json.loads(x) for x in raw.decode().splitlines() if x.strip()]
    if encoding=='csv':return list(csv.DictReader(io.StringIO(raw.decode())) )
    if encoding=='text':return raw.decode()
    raise ValueError('unsupported encoding')

def checkpoints(parent,manifest):
    roots={}
    rows=manifest['members']
    if len(rows)!=18 or len({m['repository'] for m in rows})!=18:raise ValueError('eighteen-member scope mismatch')
    for m in rows:
        if not re.fullmatch(r'hawkinsnick/[A-Za-z0-9-]+',m['repository']) or not re.fullmatch('[a-f0-9]{40}',m['commit']):raise ValueError('invalid checkpoint')
        name=m['repository'].split('/')[-1];root=Path(parent)/name
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
        origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=root,text=True).strip().rstrip('/').removesuffix('.git')
        if head!=m['commit'] or origin!='https://github.com/'+m['repository']:raise ValueError('wrong input identity/revision: '+name)
        if subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=root).returncode:raise ValueError('modified tracked input: '+name)
        roots[name]=root
    return roots
