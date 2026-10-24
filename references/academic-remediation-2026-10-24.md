# Remaining academic work and Milyan source-row union — 24 October 2026

All 43 remaining work items were checked against 57 current repository observations. The recorded observations remain unchanged; no new scholarly closure is claimed. The [execution review](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/REMEDIATION-EXECUTION-REVIEW-2026-10-24.md) gives every item's next evidence requirement and preserves its original closure rule. Categories are work types, not a claim that every task is permanently blocked.

| Next requirement | Items |
|---|---:|
| Source collation |12|
| Source access |5|
| Specialist adjudication |8|
| Study design or validation |15|
| Known dependence control |2|
| Component rights |1|

## Count the shared Milyan source rows once

```sh
python scripts/prepare_milyan_union.py --checkouts /path/to/corpora --output /tmp/milyan-union.json
python scripts/prepare_milyan_union.py --checkouts /path/to/corpora --output research/remediation/milyan-source-union.json --check
```

The [input manifest](../research/remediation/milyan-union-inputs.json) fixes the two repositories, source paths, commits, byte hashes and expected 114 nonempty digital source-text rows. The [saved union](../research/remediation/milyan-source-union.json) groups 228 view rows into 114 source-row groups, retaining both exact provenance paths. It rejects changed caches rather than treating similar text as the same source. Empty header strings are excluded explicitly. It supplies no sign, word, physical-object, physical-line or independent-witness count and adds no reading adjudication.

The individual Milyan and Lycian/Carian skills now document this workflow. Preserve native eDiAna attribution, edition references and CC BY-SA 4.0/change notices. This bounded control improves ACD-025; source dependence, object identities and critical apparatus claims outside this assembled dataset remain unresolved. ACD-021 retains its separately registered Cypriot source-entry union. Do not interchange their units or combine their group totals.

## Preserve new source caution without manufacturing a correction

The native Linear A retrieval profile now links MY Zf 2 to an attributed manuscript caution by Anna P. Judson about the isolated vessel sign's function and script relationship. Only extracted PDF text was available; direct byte download and page rendering returned HTTP 503. No checksum, page-image inspection or final publication pagination is invented. The underlying mark, source record, sign identity and physical join are unchanged. Read the [native consultation record](https://github.com/hawkinsnick/Linear-A/blob/main/research/myzf2-source-context-2026-10-24.json) and retrieve the linked `source-context-cautions` collection before making a classification claim.

This adds one qualified source-context pointer, not 23 repaired original edition references. Eight CM occurrence gaps remain unencoded; count-only museum descriptions do not supply sign positions. Five Olivier comparison sides remain indirect. Phrygian TM sentence identifiers do not supply 159 missing edition/locus joins. Independent specialist decisions, human workflow outcomes, unexposed historical data and unavailable exact model builds cannot be created by software replay.
