"""Frozen inputs and deterministic receipts for the six non-review workstreams."""
import argparse
import json
from pathlib import Path
from review_integrity import checkpoints, digest, exact, safe, pointer
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/2026-10-27'
def roots(parent):
    return checkpoints(parent,json.loads((OUT/'inputs.json').read_text()))
def receipt(name,result,write=False):
    raw=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode();path=OUT/name
    if write:path.write_bytes(raw)
    elif path.read_bytes()!=raw:raise ValueError('receipt drift: '+name)
    return result

def cli(description):
    p=argparse.ArgumentParser(description=description);p.add_argument('--checkouts',required=True,type=Path);p.add_argument('--write',action='store_true');return p.parse_args()
