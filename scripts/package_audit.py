#!/usr/bin/env python3
"""Audit concrete native research packages and build a narrow noncommercial tools-only export."""
import argparse
import importlib.util
import io
import json
import sys
import zipfile
from nonreview_common import roots,receipt,digest,exact,safe
TOOLS=('scripts/evidence_query.py','scripts/research_delivery.py','scripts/validate_ai_skill.py')
TERMS=('LICENSE','LICENSE-CODE','LICENSE-CONTENT.md','LICENSING.md','NOTICE')
FORMAT='noncommercial-native-tools-export-v1'

def delivery(root):
    # Resolve the native dependency in a fresh module name; Evidence accepts an explicit root.
    spec=importlib.util.spec_from_file_location('package_evidence',root/'scripts/evidence_query.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
    prior=sys.modules.get('evidence_query');sys.modules['evidence_query']=e
    try:
        spec=importlib.util.spec_from_file_location('package_delivery',root/'scripts/research_delivery.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    finally:
        if prior is None:sys.modules.pop('evidence_query',None)
        else:sys.modules['evidence_query']=prior
    return m

def component(path):
    if path in TOOLS:return 'PROJECT_SOFTWARE_POLYFORM_NONCOMMERCIAL_1.0.0'
    if path in TERMS:return 'CONTROLLING_TERMS_OR_NOTICE_DOCUMENT'
    return 'UNRESOLVED_FOR_PUBLIC_REDISTRIBUTION'

def tools_export(root,commit):
    # Deliberately exclude every source, data, annotation and research-result payload.
    files={p:safe(root,p).read_bytes() for p in TOOLS+TERMS}
    if b'PolyForm Noncommercial License 1.0.0' not in files['LICENSE-CODE']:raise ValueError('unrecognized software terms')
    manifest={'format':FORMAT,'repository':'hawkinsnick/'+root.name,'input_commit':commit,'scope':'Noncommercial project software only; native evidence must be obtained separately under its own terms.','software_license':'PolyForm-Noncommercial-1.0.0','required_notice':'Copyright (c) 2026 hawkinsnick corpus project contributors','changes':'Exact source bytes copied without modification; export manifest added.','source_data_included':False,'source_permissions_granted':False,'components':[{'path':p,'sha256':digest(b),'bytes':len(b),'terms':component(p),'terms_path':'LICENSE-CODE' if p in TOOLS else p} for p,b in sorted(files.items())]}
    files['tools-export-manifest.json']=(json.dumps(manifest,indent=2)+'\n').encode()
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_STORED) as z:
        for p,b in sorted(files.items()):
            i=zipfile.ZipInfo(p,(1980,1,1,0,0,0));i.create_system=3;i.external_attr=0o100644<<16;z.writestr(i,b)
    raw=out.getvalue();verify_export(raw);return raw

def verify_export(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        names=z.namelist()
        if len(names)!=len(set(names)) or set(names)!=set(TOOLS+TERMS+('tools-export-manifest.json',)):raise ValueError('unexpected export component')
        m=json.loads(z.read('tools-export-manifest.json'))
        if m.get('format')!=FORMAT or m.get('source_data_included') is not False or m.get('source_permissions_granted') is not False or m.get('software_license')!='PolyForm-Noncommercial-1.0.0':raise ValueError('export scope/license changed')
        if len(m['components'])!=len(TOOLS+TERMS) or {c['path'] for c in m['components']}!=set(TOOLS+TERMS):raise ValueError('component manifest mismatch')
        for c in m['components']:
            b=z.read(c['path'])
            if digest(b)!=c['sha256'] or len(b)!=c['bytes'] or c['terms']!=component(c['path']):raise ValueError('component hash/terms mismatch')
    return m

def build(parent,publication=False):
    if publication:
        from nonreview_common import OUT
        from review_integrity import checkpoints
        pins=json.loads((OUT/'publication-verification.json').read_text())['native_members']
        rs=checkpoints(parent,{'members':[{'repository':x['repository'],'commit':x['artifact_commit']} for x in pins]})
    else:rs=roots(parent)
    rows=[]
    import subprocess
    for name,root in rs.items():
        m=delivery(root);raw=m.package(root)
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            manifest=json.loads(z.read('research-package-manifest.json'));listed={i['path']:i for i in manifest['files']}
            if set(z.namelist())!=set(listed)|{'research-package-manifest.json'}:raise ValueError('package file inventory mismatch')
            components=[]
            for p,spec in sorted(listed.items()):
                b=z.read(p)
                if digest(b)!=spec['sha256'] or len(b)!=spec['bytes']:raise ValueError('package component hash mismatch')
                if not p or p.startswith('/') or '..' in p.split('/'):raise ValueError('unsafe package path')
                components.append({'path':p,'sha256':digest(b),'bytes':len(b),'redistribution_disposition':component(p)})
        commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip();tools=tools_export(root,commit)
        unresolved=sum(c['redistribution_disposition']=='UNRESOLVED_FOR_PUBLIC_REDISTRIBUTION' for c in components)
        profile=json.loads(safe(root,'ai-skill/references/authority-profile.json').read_bytes())
        rights=[{'path':a['path'],'sha256':digest(safe(root,a['path']).read_bytes())} for a in profile['required_authorities'] if any(k in (a.get('role','')+' '+a['path']).lower() for k in ('rights','licens','third_party','third-party'))]
        rows.append({'repository':'hawkinsnick/'+name,'commit':commit,'local_research_package_sha256':digest(raw),'components':components,'rights_authorities':rights,'public_release_decision':'BLOCK_LOCAL_RESEARCH_PACKAGE_PENDING_COMPONENT_REVIEW' if unresolved else 'CHECK_DECLARED_TERMS','unresolved_public_components':unresolved,'tools_export':{'sha256':digest(tools),'bytes':len(tools),'components':len(TOOLS+TERMS),'scope':'Eight exact code/terms files plus generated manifest; noncommercial only, no native source payload.'},'local_research_permission_or_legality_adjudicated':False})
    return {'format':'concrete-package-component-audit-v1','date':'2026-10-27','inputs':'publication-verification.json' if publication else 'inputs.json','members':rows,'totals':{'packages_opened':len(rows),'components_checked':sum(len(r['components']) for r in rows),'unresolved_public_components':sum(r['unresolved_public_components'] for r in rows),'tools_exports_built_and_verified':len(rows)},'policy':'No blanket corpus license inferred. Existing native packages remain local-research packages; unresolved means no public-export clearance in this audit, not a finding of unlawful acquisition or use. Exact-source code is offered only under native software terms. GORILA and all native source content excluded from tools exports. Full-data public packages still require source-specific attribution/terms and permission where necessary.','archives_published':False}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=__import__('pathlib').Path);p.add_argument('--write',action='store_true');p.add_argument('--publication-checkpoints',action='store_true');p.add_argument('--export-tools');p.add_argument('--output',type=__import__('pathlib').Path);a=p.parse_args()
    if a.export_tools:
        if not a.output:p.error('--export-tools requires --output')
        rs=roots(a.checkouts)
        if a.export_tools not in rs:p.error('unregistered repository basename')
        import subprocess
        root=rs[a.export_tools];commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip();raw=tools_export(root,commit);a.output.write_bytes(raw);print(json.dumps({'sha256':digest(raw),'bytes':len(raw),'source_data_included':False}))
    else:r=receipt('publication-package-audit.json' if a.publication_checkpoints else 'package-audit.json',build(a.checkouts,a.publication_checkpoints),a.write);print(r['totals'])
