import importlib.util,json,unittest
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'scripts/prepare_milyan_union.py'
s=importlib.util.spec_from_file_location('milyan_union',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class MilyanUnionTests(unittest.TestCase):
    def fixture(self):
        raw=json.dumps({'source/heading~1':[{'sentence':' '},{'sentence':'abc'},{'sentence':'def'}]}).encode()
        pins=[{'repository':repo,'commit':'a'*40,'path':'source.json','sha256':m.sha(raw)} for repo in sorted(m.REPOS)]
        return raw,pins
    def test_two_paths_are_preserved_without_duplicating_rows(self):
        raw,pins=self.fixture();r=m.group([raw,raw],pins,2)
        self.assertEqual((r['incoming_view_rows'],r['source_row_groups'],r['repeated_view_rows_not_additive']),(4,2,2))
        self.assertEqual(r['groups'][0]['source_row_pointer'],'/source~1heading~01/1')
        self.assertEqual(len(r['groups'][0]['view_assertions']),2)
        self.assertIsNone(r['physical_object_count']);self.assertIsNone(r['independent_witness_count'])
    def test_changed_cache_even_with_similar_text_is_rejected(self):
        raw,pins=self.fixture()
        with self.assertRaisesRegex(ValueError,'differ'):m.group([raw,raw+b' '],pins,2)
    def test_hash_and_coverage_tampering_rejected(self):
        raw,pins=self.fixture()
        with self.assertRaisesRegex(ValueError,'coverage'):m.group([raw,raw],pins,3)
        pins[0]['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'hash'):m.group([raw,raw],pins,2)
    def test_self_replication_and_unit_promotion_rejected(self):
        raw,pins=self.fixture()
        with self.assertRaisesRegex(ValueError,'registered'):m.group([raw,raw],[pins[0],pins[0]],2)
        with self.assertRaisesRegex(ValueError,'promote'):m.assemble(Path('.'),'physical_object')
if __name__=='__main__':unittest.main()
