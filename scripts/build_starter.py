#!/usr/bin/env python3
"""Build instruction-only downloads and source fingerprints; never crawl native corpora."""
import argparse
import json
from pathlib import Path
from common import ROOT,sha
DIRECTORIES=('scripts','references','registry','tests','migration','.github')
ROOT_FILES=('AUTO-SYNC.md','MEMBER-STATUS.md','SKILL.md','README.md','START-HERE.md','QUICKSTART.md','PROMPTS.md','WORKED-EXAMPLES.md','EXPERT-REVIEW.md','CORPUS-DOWNLOADS.md','manifest.json','LICENSE','LICENSE-CODE','LICENSE-CONTENT.md','LICENSING.md','NOTICE','.gitignore')

def source_files(root=ROOT):
    root=Path(root);files=[]
    for name in ROOT_FILES:
        path=root/name
        if not path.is_file():raise ValueError('missing master source '+name)
        files.append(path)
    for directory in DIRECTORIES:
        for path in (root/directory).rglob('*'):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix in ('.py','.md','.json','.yml','.yaml'):files.append(path)
    return {str(p.relative_to(root)):p.read_bytes() for p in sorted(files)}

def build(root=ROOT):
    root=Path(root);files=source_files(root)
    origin=json.loads(files['migration/origin.json']);manifest=json.loads(files['manifest.json'])
    index={'format':'standalone-master-source-index-v1','version':manifest['version'],
           'migration_status':manifest['migration_status'],'origin_repository':origin['repository'],
           'origin_commit':origin['commit'],'native_corpus_payload_included':False,
           'files':[{'path':p,'sha256':sha(raw),'bytes':len(raw)} for p,raw in sorted(files.items())]}
    pieces=['Master Corpus AI Skill — instruction-only starter\nMigration status: '+manifest['migration_status']+'\nNative evidence must be supplied separately.\n']
    for path in ['SKILL.md','registry/corpus-projects.json','registry/member-state.json','MEMBER-STATUS.md','references/comparability-matrix.md','START-HERE.md']:
        pieces.append('\n===== '+path+' =====\n'+files[path].decode())
    starter=('\n'.join(pieces).rstrip()+'\n').encode()
    index['starter']={'path':'downloads/Master-Corpus-AI-Skill-Starter.txt','sha256':sha(starter),'bytes':len(starter)}
    return {'generated/skill-bundle-index.json':(json.dumps(index,indent=2)+'\n').encode(),index['starter']['path']:starter}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--write',action='store_true');a=parser.parse_args()
    data=build()
    if a.write:
        for relative,raw in data.items():
            p=ROOT/relative;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
    else:
        for relative,raw in data.items():
            if not (ROOT/relative).is_file() or (ROOT/relative).read_bytes()!=raw:parser.exit(2,'stale generated master file: '+relative+'\n')
    print(json.dumps({'status':'PASS_INSTRUCTION_ONLY_BUILD','files':len(data),'native_payload_included':False}))
if __name__=='__main__':main()
