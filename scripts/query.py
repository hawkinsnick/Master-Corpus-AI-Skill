#!/usr/bin/env python3
"""Route public native evidence queries without copying adapters or merging populations."""
import argparse
import json
from pathlib import Path
import subprocess
from common import ROOT,members,checkout,execute
from validate import validate

def native_revision(root):
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
    if subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=root).returncode:
        raise ValueError('native checkout has modified tracked evidence; commit and validate before research retrieval')
    return revision

def query(checkouts,repository=None,identity=None,collection=None,coverage=False,search=None,limit=20):
    validate()
    if not 1<=limit<=1000:raise ValueError('limit must be 1..1000')
    _,registry=members();names={m['repository'] for m in registry}
    if repository and repository not in names:raise ValueError('repository is not a registered member')
    if (identity is not None or coverage) and not repository:raise ValueError('exact-ID/coverage queries require an explicit repository')
    if collection and not repository:raise ValueError('collection filtering requires an explicit repository')
    if identity is not None and not collection:raise ValueError('exact-ID lookup requires an explicit collection')
    if search is None and identity is None and not coverage:raise ValueError('no query mode')
    outputs=[]
    accepted={r['repository']:r.get('accepted_commit') for r in json.loads((ROOT/'registry/member-state.json').read_text())['members']}
    for member in registry:
        if repository and member['repository']!=repository:continue
        root=checkout(checkouts,member)
        revision=native_revision(root)
        integrity=execute(root,['scripts/validate_ai_skill.py'])
        if integrity['repository']!=member['repository']:raise ValueError('native identity mismatch')
        if coverage:args=['scripts/evidence_query.py','--coverage']
        elif identity is not None:args=['scripts/evidence_query.py','--record',identity,'--collection',collection]
        else:
            args=['scripts/research_delivery.py','--search',search,'--limit',str(limit)]
            if collection:args+=['--collection',collection]
        payload=execute(root,args)
        if native_revision(root)!=revision:raise ValueError('native revision changed during retrieval')
        outputs.append({'repository':member['repository'],'native_payload':payload,
                        'native_checkout_commit':revision,'master_accepted_commit':accepted[member['repository']],
                        'checkpoint_relation':'MATCHES_MASTER_ACCEPTED' if revision==accepted[member['repository']] else 'DIFFERS_FROM_MASTER_ACCEPTED',
                        'truncated':(payload.get('matched_view_rows',0)>len(payload.get('records',[]))) if search is not None else False,
                        'skill_sha256':integrity['skill_sha256'],'bundle_source_commit':integrity['bundle_source_commit']})
    return {'format':'namespaced-master-retrieval-v1','results_by_repository':outputs,
            'comparison_status':'NOT_ESTABLISHED_BY_RETRIEVAL','unique_object_count':None,
            'independent_witness_count':None,'physical_identity_join_performed':False,
            'scientific_approval_granted':False}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path)
    mode=p.add_mutually_exclusive_group(required=True);mode.add_argument('--id');mode.add_argument('--coverage',action='store_true');mode.add_argument('--search')
    p.add_argument('--repository');p.add_argument('--collection');p.add_argument('--limit',type=int,default=20);p.add_argument('--output',type=Path);a=p.parse_args()
    try:r=query(a.checkouts,a.repository,a.id,a.collection,a.coverage,a.search,a.limit)
    except (ValueError,OSError,KeyError,subprocess.SubprocessError) as e:p.exit(2,str(e)+'\n')
    text=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    else:print(text,end='')
if __name__=='__main__':main()
