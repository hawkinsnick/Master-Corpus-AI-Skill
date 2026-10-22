#!/usr/bin/env python3
"""Scan a declared file inventory across all frozen members; byte equality is not physical identity."""
import argparse,collections,hashlib,itertools,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];STUDY=ROOT/'research/2026-10-21';OUT=ROOT/'research/2026-10-21-followup'
DIRECTORIES={'data','exports','corpus','corpora','occurrences','catalogues','provenance'}
EXTENSIONS={'.json','.jsonl','.csv','.xml'}
MAX_BYTES=10_000_000

def digest(raw):return hashlib.sha256(raw).hexdigest()
def canonical(raw,suffix):
    if suffix=='.json':return json.dumps(json.loads(raw),sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
    return raw

def build(parent):
    members=json.loads((STUDY/'native-revisions.json').read_text())['members'];files=[];excluded=[]
    for member in members:
        name=member['repository'].split('/')[-1];root=parent/name
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
        if head!=member['commit']:raise ValueError('wrong frozen head: '+name)
        if subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=root).returncode:raise ValueError('modified frozen input')
        paths=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')
        profile=json.loads((root/'research/evidence-query-profile.json').read_text());view_paths={c['path'] for c in profile['collections']}
        for p in sorted(x for x in paths if x):
            path=Path(p)
            if path.suffix not in EXTENSIONS or not (path.parts[0] in DIRECTORIES or p in view_paths):continue
            if set(path.parts)&{'schemas','generated','tests'}:continue
            size=(root/p).stat().st_size
            if size>MAX_BYTES or size<32:
                excluded.append({'repository':member['repository'],'path':p,'bytes':size,'reason':'outside declared 32-byte to 10MB size bounds'});continue
            raw=(root/p).read_bytes();entry={'repository':member['repository'],'commit':head,'path':p,'bytes':len(raw),'sha256':digest(raw),'comparison_role':'native serialized source/view artifact, which may include metadata or legacy data'}
            try:entry['canonical_json_sha256']=digest(canonical(raw,path.suffix)) if path.suffix=='.json' else None
            except (ValueError,UnicodeError):entry['canonical_json_sha256']=None;entry['parse_status']='JSON_PARSE_FAILED_BYTES_STILL_HASHED'
            files.append(entry)
    groups=[]
    for key,kind in [('sha256','BYTE_IDENTICAL_ARTIFACT'),('canonical_json_sha256','EQUAL_PARSED_JSON_WITH_DIFFERENT_SERIALIZATION')]:
        indexed=collections.defaultdict(list)
        for f in files:
            if f.get(key):indexed[f[key]].append(f)
        for h,rows in sorted(indexed.items()):
            if len({x['repository'] for x in rows})<2:continue
            if key=='canonical_json_sha256' and len({x['sha256'] for x in rows})==1:continue
            role=('QUARANTINED_NON_SUPPORTING' if any('/quarantine/' in x['path'] for x in rows) else 'SHARED_METADATA_ONLY' if all(Path(x['path']).name in {'source-defects.json','unicode-evidence.json','signs.json'} for x in rows) else 'SHARED_DIGITAL_EDITION_DOCUMENT' if all(Path(x['path']).suffix=='.xml' for x in rows) else 'SHARED_SOURCE_CACHE' if all('milyan' in x['path'] for x in rows) else 'SOURCE_ROLE_REVIEW_REQUIRED')
            groups.append({'id':'DEP-'+kind+'-'+h[:16],'kind':kind,'evidence_role':role,'comparison_sha256':h,'members':[{'repository':x['repository'],'commit':x['commit'],'path':x['path'],'sha256':x['sha256']} for x in rows],'physical_object_count':None,'independent_witness_count':None,'analysis_rule':'Treat these serialized payloads as overlapping source/view material until their source roles are assessed; retain edition and language distinctions. Equality does not authenticate readings or establish an object join.'})
    pair_counts=collections.Counter()
    for g in groups:
        for a,b in itertools.combinations(sorted({x['repository'] for x in g['members']}),2):pair_counts[(a,b)]+=1
    pairs=[{'repositories':[a['repository'],b['repository']],'shared_artifact_groups':pair_counts[tuple(sorted([a['repository'],b['repository']]))],'independence':'NOT_ESTABLISHED'} for a,b in itertools.combinations(members,2)]
    return {'format':'all-member-serialized-source-dependence-v1','selection':{'directories':sorted(DIRECTORIES),'plus':'all native evidence collection paths','extensions':sorted(EXTENSIONS),'size_bounds_bytes':[32,MAX_BYTES],'excluded_subdirectories':['schemas','generated','tests']},'member_count':len(members),'repository_pairs_tested':len(pairs),'artifact_count':len(files),'inventory':files,'excluded_size_cases':excluded,'shared_groups':groups,'pair_summary':pairs,'limits':['This is an exhaustive pair comparison within the declared file inventory, not an exhaustive source-history or witness-independence audit.','No matching payload does not establish independence. Partial textual overlap, images, differently structured editions and unrecorded citations require other methods.','Shared metadata, empty scaffolds larger than the threshold or legacy views must not automatically become independent-evidence deductions. Review source roles before analytical use.'],'source_family_register':'../2026-10-21/dependence-register.json','new_readings_or_physical_joins':0}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',type=Path,required=True);p.add_argument('--write',action='store_true');a=p.parse_args();j=build(a.checkouts);text=json.dumps(j,ensure_ascii=False,indent=2)+'\n';target=OUT/'dependence-scan.json'
    if a.write:target.write_text(text)
    elif not target.exists() or target.read_text()!=text:raise ValueError('dependence scan replay mismatch')
    print(json.dumps({k:j[k] for k in ['member_count','repository_pairs_tested','artifact_count']}|{'shared_groups':len(j['shared_groups'])}))
if __name__=='__main__':main()
