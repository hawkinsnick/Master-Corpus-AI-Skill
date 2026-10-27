#!/usr/bin/env python3
"""Independently compare frozen eDiAna text and six annotation strata with derived rows."""
import json
from html.parser import HTMLParser
from collections import Counter
from nonreview_common import roots,receipt,cli,digest,exact,safe,pointer
KEYS=('surface','segmentation','lemma','translation','part_of_speech','morphology')
class Table(HTMLParser):
    """Build a tiny DOM; do not call the native table parser or importer."""
    def __init__(self):
        super().__init__(convert_charrefs=True);self.tree={'tag':'root','children':[]};self.stack=[self.tree]
    def handle_starttag(self,tag,attrs):
        n={'tag':tag,'children':[]};self.stack[-1]['children'].append(n)
        if tag not in ('br','hr','img','input','meta','link'):self.stack.append(n)
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i]['tag']==tag:self.stack=self.stack[:i];return
    def handle_data(self,data):self.stack[-1]['children'].append(data)
    def matrices(self):
        def text(n):
            if isinstance(n,str):return n
            return '\n' if n['tag']=='br' else ''.join(text(c) for c in n['children'])
        def walk(n,tag):
            if isinstance(n,str):return
            if n['tag']==tag:yield n
            for c in n['children']:yield from walk(c,tag)
        return [[text(c) for c in row['children'] if isinstance(c,dict) and c['tag'] in ('td','th')] for row in walk(self.tree,'tr')]

def build(parent):
    rs=roots(parent);root=rs['Lycian-and-Carian'];p='data/records.json';raw=safe(root,p).read_bytes();records=json.loads(raw);cache={};rows=[];mismatches=[];langs=Counter();seen=set();fieldchecks=0
    for ri,record in enumerate(records):
        s=record['source'];path=s['raw_path']
        if path not in cache:
            b=safe(root,path).read_bytes();cache[path]=(digest(b),json.loads(b))
        h,doc=cache[path]
        if h!=s['sha256']:raise ValueError('source checksum mismatch')
        group=pointer(doc,s['group_locator']);source_rows={i for i,v in enumerate(group) if v.get('sentence') not in ('',None)}
        if source_rows!={line['source_row'] for line in record['lines']}:raise ValueError('source row omitted or extra')
        for li,line in enumerate(record['lines']):
            source=pointer(doc,line['source_locator']);table=Table();table.feed(source['sentence_total']);matrix=table.matrices()
            if len(matrix)!=6:raise ValueError('unexpected source annotation strata')
            checks={'text':line['text']==source['sentence'],'label':line['label']==source['word'],'source_id':source['docid']==record['source_id'],'row_locator':line['source_locator']==s['group_locator']+'/'+str(line['source_row']),'principal_editions':s['principal_editions']==group[0]['ref'],'license':s['license']=='CC-BY-SA-4.0'}
            checks.update({'annotations/'+k:line['annotations'][k]==matrix[n] for n,k in enumerate(KEYS)})
            failed=[k for k,v in checks.items() if not v];fieldchecks+=len(checks);langs[record['language']]+=1;key=(path,line['source_locator'])
            if key in seen:raise ValueError('duplicate source row within derived view')
            seen.add(key)
            item={'id':record['record_id'],'derived_pointer':f'/{ri}/lines/{li}','source_path':path,'source_sha256':h,'source_pointer':line['source_locator'],'checks':len(checks),'mismatched_fields':failed,'source_annotation_sha256':digest(exact(matrix).encode()),'annotation_columns':[len(x) for x in matrix],'question_mark_present_in_source_annotations':any('?' in c for row in matrix for c in row)}
            rows.append(item)
            if failed:mismatches.append(item)
    # Check the other access path at its own native row representation.
    mr=rs['Milyan-Lycian-B'];mp='data/reference/lines.json';mb=safe(mr,mp).read_bytes();derived=json.loads(mb);mrows=[]
    for i,line in enumerate(derived):
        b=safe(mr,line['raw_path']).read_bytes();src=pointer(json.loads(b),line['source_locator'])
        if digest(b)!=line['source_sha256']:raise ValueError('Milyan raw hash mismatch')
        checks={'text':line['text']==src['sentence'],'label':line['line_label']==src['word'],'source_id':line['source_record_id']=='EDIANA-MILYAN-'+src['docid'],'license':line['license']=='CC-BY-SA-4.0','no_promotion':line['canonical_reading_admitted'] is False and line['independent_review'] is False}
        failed=[k for k,v in checks.items() if not v];fieldchecks+=len(checks)
        mrows.append({'id':line['id'],'derived_pointer':'/'+str(i),'source_path':line['raw_path'],'source_sha256':digest(b),'source_pointer':line['source_locator'],'checks':len(checks),'mismatched_fields':failed})
        if failed:mismatches.append(mrows[-1])
    expected=sum(bool(row['sentence']) for group in json.loads(safe(mr,derived[0]['raw_path']).read_bytes()).values() for row in group)
    if len(derived)!=expected:raise ValueError('Milyan derived coverage mismatch')
    return {'format':'independent-ediana-digital-fidelity-v1','date':'2026-10-27','inputs':'inputs.json','method':'Independent HTML DOM traversal; exact source strings, six annotation arrays including empty/repeated columns, row coverage, IDs, labels, bibliography and terms. No normalization of diacritics, editorial notation or annotation uncertainty. Milyan second access path checked separately; not an independent witness.','derived_inputs':[{'repository':'hawkinsnick/Lycian-and-Carian','path':p,'sha256':digest(raw)},{'repository':'hawkinsnick/Milyan-Lycian-B','path':mp,'sha256':digest(mb)}],'source_caches':[{'path':p,'sha256':h} for p,(h,_) in sorted(cache.items())],'totals':{'catalogue_records':len(records),'source_text_rows':len(rows),'second_access_path_rows':len(mrows),'field_checks':fieldchecks,'mismatches':len(mismatches),'rows_by_language':dict(sorted(langs.items())),'rows_with_question_mark_in_annotations':sum(r['question_mark_present_in_source_annotations'] for r in rows)},'rows':rows,'milyan_second_view':mrows,'printed_editions_inspected':False,'live_provider_freshness_checked':False,'linguistic_annotations_validated':False,'new_readings_adopted':0,'source_text_redistributed':False,'boundary':'Digital encoding fidelity across Lycian, Carian and Milyan; not print collation, authenticated annotation gold, linguistic acceptance or additional independent evidence.'}
if __name__=='__main__':
    a=cli(__doc__);r=receipt('ediana-fidelity.json',build(a.checkouts),a.write);print(r['totals'])
    if r['totals']['mismatches']:raise SystemExit(2)
