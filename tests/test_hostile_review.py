import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from review_integrity import pointer,exact,digest
from hostile_review import check_dossier,text_fields
from score_hostile_development import score
from query import native_revision
class PointerReview(unittest.TestCase):
    def test_invalid_array_aliases_and_escapes_fail(self):
        value={'a':['first','last']}
        for path in ['/a/-1','/a/01','/a/+1','/a/ 1','/a/-','/a~2','/a~']:
            with self.subTest(path=path),self.assertRaises(ValueError):pointer(value,path)
    def test_valid_object_keys_and_typed_values(self):
        self.assertIs(pointer({'a/b':{'~key':False}},'/a~1b/~0key'),False)
        self.assertIsNone(pointer({'01':None},'/01'))
        self.assertNotEqual(exact(False),exact(0))
        self.assertEqual(pointer(['first','last'],'/1'),'last')
    def test_scalar_traversal_and_non_string_pointer_fail(self):
        for path in ['/a/x',None,3,'a']:
            with self.subTest(path=path),self.assertRaises(ValueError):pointer({'a':False},path)
    def test_v2_resolver_uses_strict_pointer(self):
        from validate_evaluation_v2 import pointer as corrected
        with self.assertRaises(ValueError):corrected([1,2],'/-1')
class RetrievalReview(unittest.TestCase):
    def test_record_hash_pointer_and_uncertainty_must_survive(self):
        source={'value':[{'reading':'a-?-[b]','accepted':False}]};raw=json.dumps(source).encode();h=digest(raw)
        artifacts={'source.json':{'sha256':h,'encoding':'json','value':source}}
        dossier={'provenance':{'path':'source.json','sha256':h,'encoding':'json','pointer':'/value/0'},'native_record':source['value'][0],'scholarly_limits':['unreviewed'],'boundary':'not adjudicated'}
        check_dossier(dossier,source['value'][0],artifacts)
        for key,value in [('native_record',{'reading':'a-b','accepted':True}),('boundary',''),('provenance',dossier['provenance']|{'pointer':'/value/-1'}),('provenance',dossier['provenance']|{'sha256':'0'*64})]:
            bad=copy.deepcopy(dossier);bad[key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):check_dossier(bad,source['value'][0],artifacts)
    def test_text_screen_preserves_critical_characters_and_case(self):
        a=list(text_fields({'text':'alpha   beta gamma delta [x] ?'}))[0][1]
        self.assertEqual(a,'alpha beta gamma delta [x] ?')
        self.assertNotEqual(a,list(text_fields({'text':'Alpha beta gamma delta x'}))[0][1])
        self.assertEqual(list(text_fields({'text':'a-b ?'})),[])
    def test_dirty_native_checkout_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);subprocess.run(['git','init','-q'],cwd=root,check=True);(root/'evidence.json').write_text('{}')
            subprocess.run(['git','add','evidence.json'],cwd=root,check=True)
            subprocess.run(['git','-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm','fixture'],cwd=root,check=True)
            self.assertEqual(len(native_revision(root)),40)
            (root/'evidence.json').write_text('[]')
            with self.assertRaisesRegex(ValueError,'modified tracked'):native_revision(root)
class DevelopmentScoring(unittest.TestCase):
    def fixture(self):return [{'id':'X','answer':None,'decision':'QUALIFY','native_unit':'source row','citation':{'path':'a.json','pointer':'/0'}}]
    def test_missing_duplicate_and_unexpected_response_fail(self):
        expected=self.fixture()
        for rows in [[],expected*2,[expected[0]|{'id':'Y'}]]:
            with self.assertRaises(ValueError):score(expected,rows)
    def test_forged_citation_wrong_decision_and_typed_answer_fail(self):
        expected=self.fixture();actual=expected[0]|{'rationale':'Unknown is not zero.'}
        self.assertTrue(score(expected,[actual])[0]['all_checks_pass'])
        for key,value in [('answer',0),('decision','ANSWER'),('native_unit','object'),('citation',{'path':'other.json','pointer':'/0'}),('rationale','')]:
            bad=copy.deepcopy(actual);bad[key]=value
            self.assertFalse(score(expected,[bad])[0]['all_checks_pass'])
