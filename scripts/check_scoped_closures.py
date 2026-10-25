#!/usr/bin/env python3
"""Replay closed controls and ensure scientific follow-ups remain explicit."""
import argparse,hashlib,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={'ACD-003','ACD-015','ACD-017','ACD-021','ACD-025'}
def read(path):return json.loads(path.read_text())
def validate(root,checkouts):
    status=read(checkouts/'Linear-A/corpus-factory/academic-remediation-status.json')
    closed=[x for x in status['items'] if x['original_status']=='OPEN' and x['current_status'].startswith('CLOSED')]
    assert len(closed)==7 and status['cumulative_scoped_control_closures']==7
    assert status['remaining_open_original_entries']==45-len(closed)==38
    selected={x['id']:x for x in status['items'] if x['id'] in EXPECTED}
    assert set(selected)==EXPECTED and len(status['scientific_followups'])==5
    assert {f['parent'] for f in status['scientific_followups']}==EXPECTED
    assert all(f['status']=='OPEN_SCIENTIFIC_FOLLOWUP' for f in status['scientific_followups'])
    for row in selected.values():
        assert row['current_status']=='CLOSED_SCOPED_CONTROL' and row['scientific_evidence_resolved'] is False
        e=row['control_evidence'];name=e['repository'].split('/')[-1]
        folder=root if name=='Master-Corpus-AI-Skill' else checkouts/name
        p=(folder/e['path']).resolve();assert p.is_relative_to(folder.resolve())
        assert hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256']
    counts={}
    for name in ['Linear-A','Cretan-hieroglyphs','Byblos-syllabary']:
        folder=checkouts/name
        spec=importlib.util.spec_from_file_location('controls_'+name.replace('-','_'),folder/'scripts/closure_controls.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        result=module.build(folder);assert result==read(folder/'research/closure-controls.json')
        assert result['scientific_approval_granted'] is False and result['source_literals_changed'] is False
        counts[name]=result['counts']
    assert counts['Linear-A']=={'gap_records':23,'absent':19,'literal_missing':4,'admitted_exact_targets':0}
    assert counts['Cretan-hieroglyphs']=={'paired_conflict_records':2,'single_material_values_admitted':0}
    assert counts['Byblos-syllabary']=={'source_numbered_positions':123,'unambiguous_source_table_lookups':114,'excluded_conflicts':1,'excluded_unassigned':8}
    for script,saved in [('prepare_source_union.py','cypriot-source-union.json'),('prepare_milyan_union.py','milyan-source-union.json')]:
        spec=importlib.util.spec_from_file_location(script.replace('.','_'),root/'scripts'/script)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        assert module.assemble(checkouts)==read(root/'research/remediation'/saved)
    return {'status':'PASS_SCOPED_CLOSURES_WITH_OPEN_SCIENTIFIC_FOLLOWUPS','new_scoped_controls':5,
            'remaining_open_original_entries':38,'open_scientific_followups':5,'scholarly_adjudications_added':0,'counts':counts}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--checkouts',required=True,type=Path);a=p.parse_args()
    print(json.dumps(validate(ROOT,a.checkouts),indent=2))
