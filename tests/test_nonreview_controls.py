import io
import json
from pathlib import Path
import sys
import unittest
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from ediana_fidelity import Table
from dependence_v2 import fields
from package_audit import verify_export,TOOLS,TERMS,FORMAT,component
from nonreview_common import digest
class NonreviewControls(unittest.TestCase):
    def test_annotation_entities_and_empty_columns(self):
        p=Table();p.feed('<table><tr><th>a&amp;b</th><th></th><th>x<br>y</th></tr></table>')
        self.assertEqual(p.matrices(),[['a&b','','x\ny']])
    def test_nested_editorial_uncertainty_retained(self):
        p=Table();p.feed('<table><tbody><tr><td><span>[ạ?]</span></td><td><small>(?)</small></td></tr></tbody></table>')
        self.assertEqual(p.matrices(),[['[ạ?]','(?)']])
    def test_single_sign_is_screened(self):self.assertEqual(list(fields({'text':'a'})),[('/text','a')])
    def test_damage_and_case_not_stripped(self):self.assertEqual(list(fields({'reading':' A? [b] '})),[('/reading','A? [b]')])
    def test_blank_strings_excluded(self):self.assertEqual(list(fields({'text':' \n '})),[])
    def test_canonical_equivalence_only(self):self.assertEqual(list(fields({'text':'a\u0301'})),[('/text','á')])
    def archive(self,extra=None,tamper=False):
        files={p:b'component' for p in TOOLS+TERMS}
        m={'format':FORMAT,'source_data_included':False,'source_permissions_granted':False,'software_license':'PolyForm-Noncommercial-1.0.0','components':[{'path':p,'sha256':digest(b),'bytes':len(b),'terms':component(p)} for p,b in files.items()]}
        if tamper:files[TOOLS[0]]=b'altered'
        files['tools-export-manifest.json']=json.dumps(m).encode()
        if extra:files[extra]=b'unreviewed source'
        out=io.BytesIO()
        with zipfile.ZipFile(out,'w') as z:
            for p,b in files.items():z.writestr(p,b)
        return out.getvalue()
    def test_tools_manifest_verifies(self):self.assertEqual(verify_export(self.archive())['format'],FORMAT)
    def test_unknown_source_rejected(self):
        with self.assertRaises(ValueError):verify_export(self.archive(extra='data/source.json'))
    def test_traversal_rejected(self):
        with self.assertRaises(ValueError):verify_export(self.archive(extra='../source.json'))
    def test_changed_component_rejected(self):
        with self.assertRaises(ValueError):verify_export(self.archive(tamper=True))
if __name__=='__main__':unittest.main()

class CommittedCitationControls(unittest.TestCase):
    def setUp(self):
        import tempfile,subprocess
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.parent=Path(self.temp.name);self.root=self.parent/'Example';self.root.mkdir()
        for command in (['git','init','-q'],['git','config','user.name','Test'],['git','config','user.email','test@example.invalid'],['git','remote','add','origin','https://github.com/hawkinsnick/Example.git']):subprocess.run(command,cwd=self.root,check=True)
        (self.root/'data.json').write_text('{"values":[false,null]}\n');(self.root/'guide.md').write_text('Exact source heading\n')
        subprocess.run(['git','add','.'],cwd=self.root,check=True);subprocess.run(['git','commit','-qm','fixture'],cwd=self.root,check=True)
        self.commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=self.root,text=True).strip()
        self.ref={'repository':'hawkinsnick/Example','commit':self.commit,'path':'data.json','sha256':digest((self.root/'data.json').read_bytes()),'pointer':'/values/0'}
    def test_atomic_pointer_to_false_valid(self):
        from verify_response_refs import verify
        self.assertEqual(verify(self.ref,self.parent,self.parent)['status'],'PASS_EXACT_COMMITTED_LOCUS')
    def test_combined_pointer_invalid(self):
        from verify_response_refs import verify
        with self.assertRaises((ValueError,KeyError)):verify({**self.ref,'pointer':'/values/0 and /values/1'},self.parent,self.parent)
    def test_uncommitted_file_cannot_claim_head(self):
        from verify_response_refs import verify
        p=self.root/'new.json';p.write_text('{}')
        with self.assertRaises(ValueError):verify({**self.ref,'path':'new.json','sha256':digest(p.read_bytes()),'pointer':''},self.parent,self.parent)
    def test_typed_text_locus(self):
        from verify_response_refs import verify
        ref={**self.ref,'path':'guide.md','sha256':digest((self.root/'guide.md').read_bytes()),'locator_type':'text_contains','locator':'Exact source heading'};ref.pop('pointer')
        self.assertEqual(verify(ref,self.parent,self.parent)['locator_type'],'text_contains')
