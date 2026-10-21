import importlib.util,unittest,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('provider_check',ROOT/'scripts/provider_source_check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class ProviderChecks(unittest.TestCase):
    def test_line_breaks_cannot_merge_adjacent_tokens(self):
        xml=ET.fromstring('<div xmlns="http://www.tei-c.org/ns/1.0">alpha<lb n="2"/>beta</div>')
        self.assertEqual(m.norm(m.rendered_text(xml)),'alpha beta')
        self.assertNotEqual(m.norm(''.join(xml.itertext())),'alpha beta')
    def test_inline_markup_does_not_invent_spaces(self):
        xml=ET.fromstring('<div xmlns="http://www.tei-c.org/ns/1.0">a<hi>b</hi>c<lb/>d</div>')
        self.assertEqual(m.norm(m.rendered_text(xml)),'abc d')
if __name__=='__main__':unittest.main()
