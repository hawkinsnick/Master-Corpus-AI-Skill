"""Reject failed/racing native revisions and retain inspectable accepted snapshots."""
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from common import members
from sync_members import observe,write

class Synchronization(unittest.TestCase):
    def setUp(self):
        self.member=members()[1][0];self.old={'repository':self.member['repository'],'accepted_commit':'a'*40,
            'observed_commit':'a'*40,'status':'VALIDATED','validator_sha256':'h'}
        self.details={'skill_name':'example','skill_version':'0.3.1','scope':'NATIVE_EVIDENCE_RETRIEVAL',
            'skill_sha256':'b'*64,'bundle_sha256':'c'*64,'bundle_source_commit':'d'*40,'indexed_artifact_entries_checked':4}
    def test_unchanged_native_head_does_not_reclone(self):
        def never(*args):raise AssertionError('unchanged source was revalidated')
        self.assertEqual(observe(self.member,self.old,'h',lambda _: 'a'*40,never),self.old)
    def test_changed_source_advances_only_after_validation_and_stability(self):
        result=observe(self.member,self.old,'h',lambda _: 'b'*40,lambda *_:self.details)
        self.assertEqual(result['status'],'VALIDATED');self.assertEqual(result['accepted_commit'],'b'*40)
        self.assertEqual(result['skill_sha256'],self.details['skill_sha256'])
    def test_failure_preserves_last_accepted_commit(self):
        def fail(*args):raise ValueError('native authority hash mismatch')
        result=observe(self.member,self.old,'h',lambda _: 'b'*40,fail)
        self.assertEqual(result['accepted_commit'],'a'*40);self.assertEqual(result['observed_commit'],'b'*40)
        self.assertEqual(result['status'],'VALIDATION_FAILED')
    def test_race_preserves_last_accepted_commit(self):
        replies=iter(['b'*40,'c'*40])
        result=observe(self.member,self.old,'h',lambda _:next(replies),lambda *_:self.details)
        self.assertEqual(result['accepted_commit'],'a'*40);self.assertEqual(result['observed_commit'],'c'*40)
        self.assertEqual(result['status'],'PENDING_NEWER_NATIVE_REVISION')
    def test_changed_contract_is_not_silently_admitted(self):
        bad={**self.details,'skill_version':'99.0.0'}
        result=observe(self.member,self.old,'h',lambda _: 'b'*40,lambda *_:bad)
        self.assertEqual(result['status'],'VALIDATION_FAILED');self.assertEqual(result['accepted_commit'],'a'*40)
    def test_validator_changes_force_a_native_recheck(self):
        called=[]
        def verify(*args):called.append(args);return self.details
        result=observe(self.member,self.old,'new-validator',lambda _: 'a'*40,verify)
        self.assertEqual(len(called),1);self.assertEqual(result['validator_sha256'],'new-validator')
    def test_pending_state_does_not_replace_accepted_ci_checkpoints(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)/'master';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','.checkouts','__pycache__'))
            state=json.loads((root/'registry/member-state.json').read_bytes())
            pins=(root/'migration/member-checkpoints.json').read_bytes()
            # Initial/pending rows have no newly accepted snapshot to publish.
            for item in state['members']:item['status']='PENDING_INITIAL_VALIDATION';item['accepted_commit']=None
            write(state,root)
            self.assertEqual(json.loads((root/'migration/member-checkpoints.json').read_bytes()),json.loads(pins))
            self.assertNotIn('native_record',(root/'registry/member-state.json').read_text())
if __name__=='__main__':unittest.main()
