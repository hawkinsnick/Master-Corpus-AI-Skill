import importlib.util
import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('source_batch',ROOT/'scripts/check_source_batch.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class BatchControls(unittest.TestCase):
    def setUp(self):
        self.r=json.loads(m.RECEIPT.read_text())
        self.native={'comparisons':[{k:c[k] for k in ['comparison_id','record_id','zone_id','position']}|{'assertions':[{k:v for k,v in a.items() if k not in ['outcome','direct_source_inspected']} for a in c['assertions']]} for c in self.r['cases']]}
        self.raw=json.dumps(self.native).encode();self.r['native_sha256']=m.hashlib.sha256(self.raw).hexdigest()
    def test_complete_scope(self):self.assertEqual(m.verify(self.r,self.raw)['assertions'],12)
    def test_missing_case_rejected(self):
        self.r['cases'].pop()
        with self.assertRaises(ValueError):m.verify(self.r,self.raw)
    def test_missing_outcome_rejected(self):
        self.r['cases'][0]['assertions'][0]['outcome']=None
        with self.assertRaises(ValueError):m.verify(self.r,self.raw)
    def test_direct_access_upgrade_rejected(self):
        self.r['cases'][0]['assertions'][0]['direct_source_inspected']=True
        with self.assertRaises(ValueError):m.verify(self.r,self.raw)
    def test_uncertainty_loss_rejected(self):
        self.r['cases'][4]['uncertainty_preserved']=False
        with self.assertRaises(ValueError):m.verify(self.r,self.raw)
    def test_changed_source_rejected(self):
        with self.assertRaises(ValueError):m.verify(self.r,self.raw+b' ')
    def test_silent_resolution_rejected(self):
        self.r['cases'][5]['case_outcome']='VERIFIED'
        with self.assertRaises(ValueError):m.verify(self.r,self.raw)
