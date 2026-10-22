import copy,hashlib,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module(name,path):
 s=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
v=module('eval_v2','scripts/validate_evaluation_v2.py');d=module('dependence_scan','scripts/scan_source_dependence.py');p=module('printed_recheck','scripts/check_printed_source_recheck.py')
class FollowupControls(unittest.TestCase):
 def test_task_condition_cannot_be_master_computation(self):
  path='research/2026-10-21-followup/evaluation-task-context.json'
  ref={'scope':'master','path':path,'pointer':'/execution_conditions/lookup_executed','encoding':'json','sha256':hashlib.sha256((ROOT/path).read_bytes()).hexdigest()}
  with self.assertRaises(ValueError):v.resolve(ref,Path('/not-used'))
 def test_citation_hash_forgery_rejected(self):
  ref={'scope':'task_context','path':'research/2026-10-21-followup/evaluation-task-context.json','pointer':'/execution_conditions/lookup_executed','encoding':'json','sha256':'0'*64}
  with self.assertRaises(ValueError):v.resolve(ref,Path('/not-used'))
 def test_json_formatting_does_not_hide_equal_payload(self):
  self.assertEqual(d.canonical(b'{"a":1,"b":2}', '.json'),d.canonical(b'{ "b": 2, "a": 1 }','.json'))
 def test_type_and_list_order_are_not_discarded(self):
  self.assertNotEqual(d.canonical(b'{"a":true}', '.json'),d.canonical(b'{"a":1}', '.json'))
  self.assertNotEqual(d.canonical(b'[1,2]', '.json'),d.canonical(b'[2,1]', '.json'))
 def fixture(self):
  r=json.loads(p.RECEIPT.read_text());rows=[{'occurrence_id':a['occurrence_id'],'record_id':r['record_id'],'source_id':r['source_id'],'position':a['position'],'published_sign_label':a['recorded_source_label']} for a in r['assertions']];return r,rows
 def test_printed_receipt_cannot_upgrade_expert_gate(self):
  r,rows=self.fixture();r['external_specialist_review']=True
  with self.assertRaises(ValueError):p.verify(r,rows)
 def test_changed_source_label_is_not_silently_accepted(self):
  r,rows=self.fixture();rows[0]['published_sign_label']='999'
  with self.assertRaises(ValueError):p.verify(r,rows)
if __name__=='__main__':unittest.main()
