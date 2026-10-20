"""Relocation, stale-input, source-boundary and query rejection controls."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_starter import build
from common import members,local
from validate import validate
from query import query

class Standalone(unittest.TestCase):
    def copy(self,parent):
        root=Path(parent)/'relocated-master'
        shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','.checkouts','__pycache__'))
        return root

    def test_master_works_without_linear_a_adjacent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.copy(tmp)
            run=subprocess.run([sys.executable,'scripts/validate.py'],cwd=root,capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            value=json.loads(run.stdout)
            self.assertEqual(value['member_count'],18)
            self.assertEqual(value['migration_completed'],json.loads((root/'manifest.json').read_text())['migration_status']=='CANONICAL_PUBLISHED')
            self.assertFalse(value['native_corpus_payload_included'])

    def test_draft_is_never_certified_as_published(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.copy(tmp)
            for name,key in [('manifest.json','migration_status'),('migration/origin.json','status')]:
                p=root/name;d=json.loads(p.read_text());d[key]='PREPARED_NOT_CANONICAL';p.write_text(json.dumps(d))
            for name,raw in build(root).items():(root/name).write_bytes(raw)
            with self.assertRaisesRegex(ValueError,'not yet verified'):
                validate(root,require_canonical=True)

    def test_changed_instruction_bytes_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.copy(tmp);p=root/'SKILL.md';p.write_text(p.read_text()+'\nTampered instructions.\n')
            with self.assertRaisesRegex(ValueError,'stale master'):validate(root)

    def test_missing_starter_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.copy(tmp);(root/'downloads/Master-Corpus-AI-Skill-Starter.txt').unlink()
            with self.assertRaisesRegex(ValueError,'missing master'):validate(root)

    def test_unregistered_duplicate_and_excluded_members_are_rejected(self):
        for change in ('duplicate','excluded','version','unsafe','admission'):
            with self.subTest(change=change),tempfile.TemporaryDirectory() as tmp:
                root=self.copy(tmp);p=root/'registry/corpus-projects.json';d=json.loads(p.read_bytes())
                if change=='duplicate':d['members'][1]['repository']=d['members'][0]['repository']
                elif change=='excluded':d['members'][0]['repository']='hawkinsnick/Egyptian-Hieroglyphic-Corpus'
                elif change=='version':d['members'][0]['required_skill_version']='0.0.0'
                elif change=='unsafe':d['members'][0]['individual_skill_path']='../outside'
                else:d['members'][0]['admission']['master_ai_member']=False
                p.write_text(json.dumps(d))
                with self.assertRaises(ValueError):members(root)

    def test_output_receipts_and_native_checkouts_are_never_packaged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.copy(tmp);expected=build(root)
            for rel in ('.checkouts/Linear-A/data/native.json','data/corpus.json','member-checks.json','generated/member-validation.json'):
                p=root/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('{"private":"not instruction context"}')
            self.assertEqual(expected,build(root))
            validate(root)

    def test_path_escape_and_missing_files_are_rejected(self):
        for path in ('../outside','/etc/passwd','missing'):
            with self.subTest(path=path),self.assertRaises(ValueError):local(ROOT,path)

    def test_unsupported_query_targets_and_ambiguous_requests_are_rejected(self):
        cases=[dict(repository='hawkinsnick/Egyptian-Hieroglyphic-Corpus',search='?'),
               dict(repository='hawkinsnick/LightroomIsSlow',search='?'),
               dict(repository='invented',search='?'),dict(identity='ARKH 1a',collection='source-documents'),
               dict(repository='hawkinsnick/Linear-A',identity='ARKH 1a'),dict(search='?',limit=0),
               dict(search='?',collection='source-documents')]
        for args in cases:
            with self.subTest(args=args),self.assertRaises(ValueError):query('/nonexistent',**args)

    def test_builds_are_repeatable(self):
        self.assertEqual(build(),build())

if __name__=='__main__':unittest.main()
