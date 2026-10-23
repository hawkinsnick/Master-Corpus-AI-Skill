import importlib.util
from pathlib import Path
import unittest
p=Path(__file__).resolve().parents[1]/'scripts/prepare_source_union.py'
s=importlib.util.spec_from_file_location('union',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class SourceUnionTests(unittest.TestCase):
    def test_only_registered_pair_and_unit_are_admissible(self):
        m.validate_study(list(m.REPOS),'digital_edition_entry')
        m.validate_study(list(reversed(m.REPOS)),'digital_edition_entry')
    def test_other_pairs_and_self_replication_rejected(self):
        for pair in [('Linear-A','Cypro-Minoan'),('Eteocypriot','Eteocypriot'),('Cypriot-syllabic-Greek','Eteocypriot','Linear-B')]:
            with self.assertRaisesRegex(ValueError,'Unregistered'):m.validate_study(pair,'digital_edition_entry')
    def test_illegal_unit_promotion_rejected(self):
        for unit in ('sign','physical_object','independent_witness','word','language'):
            with self.assertRaisesRegex(ValueError,'cannot supply'):m.validate_study(m.REPOS,unit)

class SourceUnionAssemblyTests(unittest.TestCase):
    def fixture(self, base, left, right):
        import hashlib,json
        from unittest.mock import patch
        base=Path(base);manifest=[];payloads={}
        for repo,records in zip(m.REPOS,(left,right)):
            raw=json.dumps({'records':records}).encode();root=base/'checkouts'/repo
            (root/'exports').mkdir(parents=True);(root/m.PATH).write_bytes(raw);payloads[repo]=raw
            manifest.append({'repository':'hawkinsnick/'+repo,'commit':'a'*40,'path':m.PATH,'sha256':hashlib.sha256(raw).hexdigest(),'records':len(records)})
        (base/'research/remediation').mkdir(parents=True)
        (base/'research/remediation/source-union-inputs.json').write_text(json.dumps({'source_family':m.FAMILY,'unit':'digital_edition_entry','inputs':manifest}))
        return payloads

    def row(self,n,**extra):return {'source_id':'IG XV 1, '+str(n),'id':'view-'+str(n),'record_unit':'digital_edition_entry',**extra}

    def test_overlap_is_one_group_with_both_distinct_assertion_pointers(self):
        import tempfile
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as d:
            payload=self.fixture(d,[self.row(1,title='left assertion'),self.row(2)],[self.row(1,title='different right assertion')])
            with patch.object(m,'ROOT',Path(d)),patch.object(m.subprocess,'check_output',side_effect=lambda cmd,cwd:payload[Path(cwd).name]):
                r=m.assemble(Path(d)/'checkouts')
            self.assertEqual((r['incoming_view_rows'],r['source_entry_groups'],r['repeated_view_rows_not_additive']),(3,2,1))
            self.assertEqual(len(r['groups'][0]['view_assertions']),2)
            self.assertEqual({x['repository'] for x in r['groups'][0]['view_assertions']},{'hawkinsnick/'+x for x in m.REPOS})
            self.assertIsNone(r['physical_object_count'])

    def test_changed_checkout_is_rejected_even_when_ids_match(self):
        import tempfile
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as d:
            payload=self.fixture(d,[self.row(1)],[self.row(1)])
            (Path(d)/'checkouts'/m.REPOS[0]/m.PATH).write_text('{}')
            with patch.object(m,'ROOT',Path(d)),patch.object(m.subprocess,'check_output',side_effect=lambda cmd,cwd:payload[Path(cwd).name]):
                with self.assertRaisesRegex(ValueError,'differs'):m.assemble(Path(d)/'checkouts')

    def test_duplicate_ids_and_changed_overlap_are_rejected(self):
        import tempfile
        from unittest.mock import patch
        for left,right,reason in [([self.row(1),self.row(1)],[self.row(1)],'duplicate'),([self.row(1)],[self.row(2)],'overlap')]:
            with tempfile.TemporaryDirectory() as d:
                payload=self.fixture(d,left,right)
                with patch.object(m,'ROOT',Path(d)),patch.object(m.subprocess,'check_output',side_effect=lambda cmd,cwd:payload[Path(cwd).name]):
                    with self.assertRaisesRegex(ValueError,reason):m.assemble(Path(d)/'checkouts')

if __name__=='__main__':unittest.main()
