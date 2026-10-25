#!/usr/bin/env python3
"""Check every parsed IG view against frozen XML; record bounded fresh retrieval separately."""
import argparse
import concurrent.futures
import json
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from review_integrity import digest,exact,safe,checkpoints
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'research/2026-10-25';NS={'t':'http://www.tei-c.org/ns/1.0'};LANG='{http://www.w3.org/XML/1998/namespace}lang'
NAMES=('Cypriot-syllabic-Greek','Eteocypriot')
def norm(s):return ' '.join((s or '').split())
def signature(node):
    return [node.tag,dict(sorted(node.attrib.items())),node.text,[ [signature(c),c.tail] for c in node]]
def display(node,policy):
    if node is None:return ''
    label=node.tag.rsplit('}',1)[-1]
    prefix='\n' if label=='lb' or (policy=='csg' and label=='div' and node.get('type')=='textpart') else '[gap]' if policy=='csg' and label=='gap' else ''
    s=prefix+(node.text or '')+''.join(display(c,policy)+(c.tail or '') for c in node)
    return s

def compare(raw,row,name):
    xml=ET.fromstring(raw);checks=[]
    def add(field,xpath,actual,expected):checks.append({'field':field,'source_xpath':xpath,'match':exact(actual)==exact(expected)})
    if xml.tag!='{'+NS['t']+'}TEI':raise ValueError('not TEI')
    for field,xp in {'source_id':'.//t:idno[@type="localId"]','title':'.//t:titleStmt/t:title','site':'.//t:origPlace','date_source':'.//t:origDate','support':'.//t:support','provenance_source':'.//t:provenance[@type="found"]','bibliography_source':'.//t:div[@type="bibliography"]'}.items():
        node=xml.find(xp,NS);value=norm(''.join(node.itertext())) if node is not None else None
        add('/'+field,xp,value,row[field])
    licence=xml.find('.//t:licence',NS)
    add('/source/license_url','.//t:licence/@target',licence.get('target') if licence is not None else None,row['source']['license_url'])
    policy='csg' if name=='Cypriot-syllabic-Greek' else 'etec'
    edition=xml.find('.//t:div[@type="edition"]',NS)
    if edition is None:raise ValueError('source edition missing')
    def compare_node(node,stored,path,xp):
        add(path+'/xml',xp,signature(node),signature(ET.fromstring(stored['xml'])))
        add(path+'/text',xp+' [declared display policy]',norm(display(node,policy)),norm(stored['text']))
        if 'line_labels' in stored:add(path+'/line_labels',xp+'//t:lb/@n',[e.get('n') for e in node.iter() if e.tag==f"{{{NS['t']}}}lb"],stored['line_labels'])
    if policy=='csg':
        compare_node(edition,row['edition'],'/edition','.//t:div[@type="edition"]')
        nodes=edition.findall('.//t:div[@type="textpart"]',NS)
        add('/edition/parts [count]','.//t:div[@type="edition"]//t:div[@type="textpart"]',len(nodes),len(row['edition']['parts']))
        for i,(node,part) in enumerate(zip(nodes,row['edition']['parts'])):
            add(f'/edition/parts/{i}/n','textpart/@n',node.get('n'),part['n']);add(f'/edition/parts/{i}/text','textpart [ordinal '+str(i)+']',norm(display(node,policy)),norm(part['text']))
    else:
        nodes=edition.findall('.//t:div[@type="textpart"]',NS) or [edition]
        add('/components [count]','edition/textparts or whole edition',len(nodes),len(row['components']))
        for i,(node,component) in enumerate(zip(nodes,row['components'])):
            add(f'/components/{i}/source_part','textpart/@n or body',node.get('n') if node is not edition else 'body',component['source_part'])
            compare_node(node,component,f'/components/{i}','edition component ordinal '+str(i))
    translations=xml.findall('.//t:div[@type="translation"]',NS)
    for lang_key,fields in [(False,('translations','modern_source_translations')),(True,('greek_interpretations','greek_source_interpretations'))]:
        key=fields[0 if policy=='csg' else 1];nodes=[x for x in translations if (x.get(LANG,'').lower()=='grc')==lang_key]
        add('/'+key+' [count]','translation language partition',len(nodes),len(row[key]))
        for i,(node,item) in enumerate(zip(nodes,row[key])):
            compare_node(node,item,f'/{key}/{i}','translation ordinal '+str(i)+' in declared language partition')
            add(f'/{key}/{i}/responsibility','translation/@resp',(node.get('resp') or '').strip() or None,item['responsibility'])
    return checks

def build(parent):
    roots=checkpoints(parent,json.loads((OUT/'inputs.json').read_text()));rows=[]
    for name in NAMES:
        root=roots[name];path='exports/corpus.json';export=safe(root,path).read_bytes()
        for i,row in enumerate(json.loads(export)['records']):
            raw=safe(root,row['source']['raw_path']).read_bytes();checks=compare(raw,row,name)
            if digest(raw)!=row['source']['sha256']:raise ValueError('raw XML changed')
            rows.append({'repository':'hawkinsnick/'+name,'id':row['id'],'source_id':row['source_id'],'export_path':path,'export_sha256':digest(export),'export_pointer':'/records/'+str(i),'raw_path':row['source']['raw_path'],'raw_sha256':digest(raw),'url':row['source']['xml_url'],'field_checks':len(checks),'mismatches':[c for c in checks if not c['match']],'checks_sha256':digest(exact(checks).encode()),'printed_edition_inspected':False,'independent_epigraphic_review':False})
    return {'format':'complete-frozen-ig-view-fidelity-review-v1','date':'2026-10-25','inputs':'inputs.json','selection':'All 592 parsed Cypriot view entries and all 25 Eteocypriot view entries, with 25 shared source identities; malformed quarantined IG XV 1,150 is excluded from parsed comparison, not repaired or admitted.','method':'Independently implemented XPath/expanded-namespace XML structure checks; exact metadata, component and translation cardinality; readable fields checked under each native declared whitespace/lb/textpart/gap display policy. This is an encoding fidelity check, not a linguistic or epigraphic assessment.','rows':rows,'totals':{'view_rows':len(rows),'distinct_source_ids':len({r['source_id'] for r in rows}),'field_checks':sum(x['field_checks'] for x in rows),'mismatches':sum(len(x['mismatches']) for x in rows)},'raw_xml_redistributed':False,'independent_witnesses_added':0}

def live_selection(report):
    unique={r['source_id']:r for r in report['rows'] if r['repository'].endswith('/Cypriot-syllabic-Greek')}
    etec={r['source_id'] for r in report['rows'] if r['repository'].endswith('/Eteocypriot')}
    rank=lambda sid:digest(('hostile-review-2026-10-25|'+sid).encode())
    ids=sorted(etec,key=rank)[:6]+sorted(set(unique)-etec,key=rank)[:12]
    return [unique[s] for s in ids]

def acquire(row):
    result={k:row[k] for k in ['source_id','url','raw_sha256']}
    try:
        request=urllib.request.Request(row['url'],headers={'User-Agent':'Master-Corpus-AI-Skill source-fidelity-check/2026-10-25'})
        with urllib.request.urlopen(request,timeout=20) as response:raw=response.read();status=response.status
        xml=ET.fromstring(raw);sid=xml.find('.//t:idno[@type="localId"]',NS);licence=xml.find('.//t:licence',NS)
        result.update(http_status=status,bytes=len(raw),sha256=digest(raw),same_frozen_bytes=digest(raw)==row['raw_sha256'],source_identity_matches=sid is not None and norm(sid.text)==row['source_id'],licence_target=licence.get('target') if licence is not None else None,outcome='ACQUIRED')
    except (OSError,ValueError,ET.ParseError) as e:result.update(outcome='INACCESSIBLE_OR_INVALID',error=type(e).__name__+': '+str(e),same_frozen_bytes=None)
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',type=Path,required=True);p.add_argument('--write',action='store_true');p.add_argument('--live',action='store_true');a=p.parse_args();j=build(a.checkouts);s=json.dumps(j,ensure_ascii=False,indent=2)+'\n';target=OUT/'provider-stratum.json'
    if a.write:target.write_text(s)
    elif target.read_text()!=s:raise ValueError('provider stratum replay drift')
    if a.live:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(acquire,live_selection(j)))
        live={'format':'bounded-fresh-provider-retrieval-v1','date':'2026-10-25','selection':'SHA-256-ranked six Eteocypriot subset IDs plus twelve remaining parsed IG IDs; eighteen distinct first-party routes; purposive strata, not a language-wide random sample or held-out model task set.','selection_seed':'hostile-review-2026-10-25|SOURCE_ID','rows':rows,'ordinary_http_only':True,'new_readings_adopted':0,'source_files_redistributed':False}
        (OUT/'fresh-provider-retrieval.json').write_text(json.dumps(live,indent=2)+'\n')
        print(json.dumps({'fresh_requested':len(rows),'fresh_acquired':sum(x['outcome']=='ACQUIRED' for x in rows),'changed':sum(x['same_frozen_bytes'] is False for x in rows)}))
    print(json.dumps(j['totals']))
    if j['totals']['mismatches']:raise SystemExit(2)
if __name__=='__main__':main()
