import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from provider_stratum_review import display,signature,norm,ET
class ProviderStratumControls(unittest.TestCase):
    def test_editorial_structure_cannot_disappear_in_display_check(self):
        a=ET.fromstring('<ab>a<unclear>b</unclear><lb/>c</ab>');b=ET.fromstring('<ab>ab<lb/>c</ab>')
        self.assertEqual(norm(display(a,'csg')),norm(display(b,'csg')))
        self.assertNotEqual(signature(a),signature(b))
    def test_lbs_and_part_boundaries_cannot_merge_words(self):
        a=ET.fromstring('<ab><div type="textpart">alpha<lb/>beta</div><div type="textpart">gamma</div></ab>')
        self.assertEqual(norm(display(a,'csg')),'alpha beta gamma')
    def test_gap_is_explicit_in_csg_display_policy(self):
        a=ET.fromstring('<ab>a<gap/>b</ab>')
        self.assertEqual(display(a,'csg'),'a[gap]b')
        self.assertEqual(display(a,'etec'),'ab')
        self.assertIn('gap',str(signature(a)))
