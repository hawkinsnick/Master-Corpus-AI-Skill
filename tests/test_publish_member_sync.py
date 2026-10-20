"""Exact-source publication and concurrent source preservation with real Git repositories."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from publish_member_sync import publish,ALLOWED

def git(root,*args):return subprocess.check_output(['git',*args],cwd=root,text=True,stderr=subprocess.PIPE).strip()

class Publication(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();base=Path(self.tmp.name);self.remote=base/'remote.git';self.root=base/'master'
        subprocess.run(['git','init','--quiet','--bare',str(self.remote)],check=True)
        subprocess.run(['git','init','--quiet','-b','main',str(self.root)],check=True)
        git(self.root,'config','user.name','Test');git(self.root,'config','user.email','test@example.invalid')
        for name in ALLOWED:
            p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('before\n')
        git(self.root,'add','.');git(self.root,'commit','--quiet','-m','source');self.source=git(self.root,'rev-parse','HEAD')
        git(self.root,'remote','add','origin',str(self.remote));git(self.root,'push','--quiet','origin','main')
        (self.root/'MEMBER-STATUS.md').write_text('validated change\n')
    def tearDown(self):self.tmp.cleanup()
    def advance(self):
        other=Path(self.tmp.name)/'competitor'
        subprocess.run(['git','clone','--quiet','--branch','main',str(self.remote),str(other)],check=True)
        git(other,'config','user.name','Other');git(other,'config','user.email','other@example.invalid')
        (other/'source.md').write_text('new source\n');git(other,'add','.');git(other,'commit','--quiet','-m','advance')
        git(other,'push','--quiet','origin','main');return git(other,'rev-parse','HEAD')
    def test_publish_on_exact_parent(self):
        with patch.dict(os.environ,{'SOURCE_COMMIT':self.source}):self.assertTrue(publish(self.root))
        self.assertEqual(git(self.root,'rev-parse','HEAD^'),self.source)
        self.assertEqual(git(self.remote,'rev-parse','main'),git(self.root,'rev-parse','HEAD'))
    def test_advanced_source_is_skipped_without_rebase(self):
        advanced=self.advance()
        with patch.dict(os.environ,{'SOURCE_COMMIT':self.source}):self.assertFalse(publish(self.root))
        self.assertEqual(git(self.remote,'rev-parse','main'),advanced)
        self.assertEqual(git(self.root,'rev-parse','HEAD'),self.source)
    def test_unrelated_changes_are_rejected(self):
        (self.root/'unexpected.txt').write_text('not generated\n')
        with patch.dict(os.environ,{'SOURCE_COMMIT':self.source}),self.assertRaisesRegex(ValueError,'unrelated'):publish(self.root)
        self.assertEqual(git(self.remote,'rev-parse','main'),self.source)
    def test_race_after_guard_cannot_force_overwrite(self):
        original=subprocess.run;advanced=[];triggered=[]
        def run(args,*a,**kw):
            if args[:2]==['git','push'] and not triggered:
                triggered.append(True)
                advanced.append(self.advance())
            return original(args,*a,**kw)
        with patch.dict(os.environ,{'SOURCE_COMMIT':self.source}),patch('publish_member_sync.subprocess.run',side_effect=run):
            with self.assertRaises(subprocess.CalledProcessError):publish(self.root)
        self.assertEqual(git(self.remote,'rev-parse','main'),advanced[0])
if __name__=='__main__':unittest.main()
