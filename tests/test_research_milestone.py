import importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('research_milestone',ROOT/'scripts/research_milestone.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class ResearchControls(unittest.TestCase):
    def test_pointer_and_hash_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'x.json').write_text('{"rows":[{"id":"a"}]}')
            # avoid Git in this focused payload test; verify source compares the actual resolved value.
            raw=(root/'x.json').read_bytes();v=m.ptr(m.parse(raw,'json'),'/rows/0')
            self.assertEqual(v,{'id':'a'})
            with self.assertRaises((IndexError,KeyError)):m.ptr(m.parse(raw,'json'),'/rows/1')
            self.assertNotEqual(m.digest(raw),m.digest(raw+b' '))
    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):m.safe(ROOT,'../outside.json')
    def test_citation_candidates_do_not_become_consultation(self):
        values=m.metadata({'source_locator':'p.9','primary_edition_verified':False,'text':'do not copy'})
        self.assertIn({'field_pointer':'/primary_edition_verified','value':False},values)
        self.assertNotIn('text',str(values))
    def test_frozen_manifest_matches_registry(self):
        a=json.loads((m.STUDY/'native-revisions.json').read_text());b=json.loads((ROOT/'registry/corpus-projects.json').read_text())
        self.assertEqual({x['repository'] for x in a['members']},{x['repository'] for x in b['members']})
        self.assertEqual(len(a['members']),18)
    def test_study_preserves_unknown_physical_counts(self):
        d=json.loads((m.STUDY/'dependence-register.json').read_text())
        self.assertTrue(all(g['physical_object_count'] is None and g['independent_witness_count'] is None for g in d['groups']))
if __name__=='__main__':unittest.main()
