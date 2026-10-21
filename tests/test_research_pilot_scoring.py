import importlib.util,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('pilot_score',ROOT/'scripts/score_research_pilot.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class ScoringControls(unittest.TestCase):
    def setUp(self):self.oracle={'tasks':[{'id':'X','decision':'ABSTAIN','values':{'count':None},'required_evidence_ids':['E1'],'direct_extraction_baseline_applicable':False}]}
    def answer(self):return {'id':'X','decision':'ABSTAIN','values':{'count':None},'evidence_ids':['E1']}
    def test_unsupported_numeric_answer_fails(self):
        x=self.answer();x['values']['count']=99
        self.assertEqual(m.score([x],self.oracle,{'E1'})['requested_value_matches'],0)
    def test_forged_citation_fails(self):
        x=self.answer();x['evidence_ids']=['E1','INVENTED']
        self.assertEqual(m.score([x],self.oracle,{'E1'})['evidence_id_matches'],0)
    def test_missing_and_duplicate_responses_fail(self):
        with self.assertRaises(ValueError):m.score([],self.oracle,{'E1'})
        with self.assertRaises(ValueError):m.score([self.answer(),self.answer()],self.oracle,{'E1'})
    def test_booleans_are_not_counts(self):self.assertFalse(m.same(True,1))
if __name__=='__main__':unittest.main()
