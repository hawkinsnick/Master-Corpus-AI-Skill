#!/usr/bin/env python3
"""Check three provider-XML source routes; keep digital fidelity distinct from epigraphic review."""
import argparse,hashlib,json,subprocess,sys,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];STUDY=ROOT/'research/2026-10-21'
NS={'t':'http://www.tei-c.org/ns/1.0'}
TARGETS=[('Eteocypriot','ETEC-IGXV1-16'),('Eteocypriot','ETEC-IGXV1-46'),('Cypriot-syllabic-Greek','CSG-IGXV1-231')]
def norm(t):return ' '.join(t.split())
def rendered_text(node):
    parts=[node.text or '']
    for child in node:
        if child.tag.rsplit('}',1)[-1]=='lb':parts.append('\n')
        parts.append(rendered_text(child));parts.append(child.tail or '')
    return ''.join(parts)
def field_checks(xml,row):
    checks=[]
    paths={'source_id':'.//t:idno[@type="localId"]','title':'.//t:titleStmt/t:title','site':'.//t:origPlace','date_source':'.//t:origDate','support':'.//t:support','provenance_source':'.//t:provenance[@type="found"]'}
    for key,xpath in paths.items():
        node=xml.find(xpath,NS)
        if node is None or key not in row:raise ValueError('required comparison field missing: '+key)
        if node is not None and key in row:checks.append({'native_field':'/'+key,'source_xpath':xpath,'match_after_declared_whitespace_normalization':norm(rendered_text(node))==norm(str(row[key]))})
    for j,c in enumerate(row.get('components',[])):
        xp=('.//t:div[@type="edition"]/t:ab' if c['source_part']=='body' else './/t:div[@type="edition"]//t:div[@type="textpart"][@n="'+c['source_part']+'"]');node=xml.find(xp,NS)
        if node is None:raise ValueError('source component missing')
        checks.append({'native_field':'/components/'+str(j)+'/text','source_xpath':xp,'match_after_declared_whitespace_normalization':norm(rendered_text(node))==norm(c['text'])})
    return checks

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--live',action='store_true');p.add_argument('--write',action='store_true');a=p.parse_args()
    if a.write and not a.live:p.error('writing a new live receipt requires --live')
    pins={x['repository']:x['commit'] for x in json.loads((STUDY/'native-revisions.json').read_text())['members']};results=[]
    for name,id in TARGETS:
        root=a.checkouts/name;head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
        if head!=pins['hawkinsnick/'+name]:raise ValueError('wrong source checkpoint')
        if subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=root).returncode:raise ValueError('modified native source input')
        records=json.loads((root/'exports/corpus.json').read_text())['records'];i=next(i for i,x in enumerate(records) if x['id']==id);row=records[i];source=row['source']
        if a.live:
            with urllib.request.urlopen(source['xml_url'],timeout=30) as response:raw=response.read();status=response.status
        else:raw=(root/source['raw_path']).read_bytes();status=None
        h=hashlib.sha256(raw).hexdigest();xml=ET.fromstring(raw);checks=field_checks(xml,row)
        record={'repository':'hawkinsnick/'+name,'id':id,'export_path':'exports/corpus.json','export_pointer':'/records/'+str(i),'native_commit':head,'url':source['xml_url'],'access':'ACQUIRED_AND_XML_PARSED' if a.live else 'FROZEN_SOURCE_REPLAY','http_status':status,'bytes':len(raw),'sha256':h,'matches_frozen_raw_source_sha256':h==source['sha256'],'license_target':xml.find('.//t:licence',NS).get('target'),'field_checks':checks,'mismatches':sum(not x['match_after_declared_whitespace_normalization'] for x in checks),'printed_primary_edition_inspected':False,'independent_epigraphic_check':False,'source_language_assertion_adopted_as_independent':False}
        if not a.live:
            committed=next(x for x in json.loads((STUDY/'fresh-provider-checks.json').read_text())['rows'] if x['id']==id)
            for key in ['sha256','field_checks','matches_frozen_raw_source_sha256','license_target']:
                if record[key]!=committed[key]:raise ValueError('provider-source replay mismatch: '+id+' '+key)
        results.append(record)
    report={'format':'fresh-provider-edition-comparison-v2','selection':'Targeted follow-up of three sampled rows with accessible first-party XML routes; not representative or independently blinded.','method':'Ordinary unauthenticated provider XML acquisition. Compare hashes and explicit native fields/XPaths; render XML lb elements as line separators before whitespace normalization.','rows':results,'source_independence':'Same upstream digital edition; source fidelity checks do not add independent witnesses or authenticate readings.','raw_xml_redistributed':False,'initial_checker_diagnostic':{'method':'Plain itertext concatenation, then whitespace normalization','false_mismatches':2,'record':'ETEC-IGXV1-16','cause':'XML lb elements do not insert whitespace into itertext. Concatenation merged adjacent lines.','correction':'Treat lb as a line separator before whitespace normalization. No native source or reading changed.','unpartitioned_body_handling':'The first strict checker expected named textparts; body-only editions now use explicit edition/ab selection rather than silently skipping the component.'},'interpretation':'A matching export is faithful to the checked provider encoding. It is not printed-edition collation, independent autopsy, translation validation or independent scholarly review.'}
    if a.write:(STUDY/'fresh-provider-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS_PROVIDER_SOURCE_FIELDS' if all(x['mismatches']==0 and x['matches_frozen_raw_source_sha256'] for x in results) else 'PROVIDER_SOURCE_DISCREPANCIES','records':len(results),'field_checks':sum(len(x['field_checks']) for x in results),'mismatches':sum(x['mismatches'] for x in results),'mode':'live' if a.live else 'frozen_replay'}))
    if any(x['mismatches'] or not x['matches_frozen_raw_source_sha256'] for x in results):sys.exit(2)
if __name__=='__main__':main()
