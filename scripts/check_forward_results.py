#!/usr/bin/env python3
"""Replay citation scoring of unchanged fresh-agent responses, preserving recorded failures."""
import json
from verify_response_refs import score
from nonreview_common import ROOT,OUT,cli,digest,roots
if __name__=='__main__':
    a=cli(__doc__);roots(a.checkouts);saved=json.loads((OUT/'forward-results.json').read_text())
    for session in saved['sessions']:
        raw=(OUT/session['response_path']).read_bytes()
        if digest(raw)!=session['sha256'] or score(json.loads(raw),a.checkouts,ROOT)!=session['citation_scoring']:raise ValueError('raw response or citation score changed')
    print('PASS: preserved development results, including 8 rejected citations; no response repaired')
