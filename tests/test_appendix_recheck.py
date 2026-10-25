import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from check_published_appendix_recheck import verify
class AppendixRecheckControls(unittest.TestCase):
    def setUp(self):
        self.r=json.loads((ROOT/'research/2026-10-25/linear-b-appendix-recheck.json').read_text())
        self.data={'document':{a['native_pointer'].split('/')[-1]:a['expected'] for a in self.r['assertions'] if a['native_pointer'].startswith('/document/')},'units':[a['expected'] for a in self.r['assertions'] if a['native_pointer'].startswith('/units/')]}
        self.raw=json.dumps(self.data).encode()
        import hashlib
        self.r['native_sha256']=hashlib.sha256(self.raw).hexdigest()
    def test_changed_identifier_or_scope_is_rejected(self):
        self.assertEqual(verify(self.r,self.raw),10)
        for change in ['identifier','duplicate','gold']:
            r=copy.deepcopy(self.r)
            if change=='identifier':r['assertions'][0]['expected']='invented'
            elif change=='duplicate':r['assertions'][-1]=r['assertions'][-2]
            else:r['linguistic_gold_acquired']=True
            with self.subTest(change=change),self.assertRaises(ValueError):verify(r,self.raw)
    def test_changed_native_bytes_are_rejected(self):
        with self.assertRaises(ValueError):verify(self.r,self.raw+b' ')
