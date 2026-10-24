# Academic remediation and controlled source unions

The Linear A [current status](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/academic-remediation-status.json) records two narrowly closed audit items: ACD-004 rejects the wrong HT53a/b targets in researcher retrieval, retaining the historical URL without inventing a replacement; ACD-002 exposes existing component/snapshot-gap/interpretation dispositions for five legacy cases. The original audit omitted the existing membership ledger. No new source join, accepted reading or competing scholarly pair was established. Forty-three items remain open, including partially mitigated risks.

Read the native [researcher guide](https://github.com/hawkinsnick/Linear-A/blob/main/docs/ACADEMIC-REMEDIATION.md). Retrieve exact `edition-route-decisions` and `case-dispositions` alongside native assertions. The five legacy cases are no longer silently treated as one missing-inscription category. All fifteen legacy alternative pairs remain unadmitted.

## Assemble the registered Cypriot source-entry union

```sh
python scripts/prepare_source_union.py --checkouts /path/to/corpora --output /tmp/cypriot-union.json
python scripts/prepare_source_union.py --checkouts /path/to/corpora --output research/remediation/cypriot-source-union.json --check
```

The [input manifest](../research/remediation/source-union-inputs.json) fixes commits, paths, hashes and counts from the two registered same-edition views. The tool refuses changed bytes, duplicate source IDs within a view, incompatible units and unregistered pairings. It groups 617 view rows into 592 digital-edition entries, with 25 repeated view rows retained as provenance rather than added as new evidence. The [saved union](../research/remediation/cypriot-source-union.json) preserves all 617 exact source pointers under their 592 source-ID groups. A group can contain differently structured or incomplete assertions; the tool does not choose or merge their readings.

This controls the known overlap in this assembled source-entry dataset. It does not close ACD-021 for every possible downstream analysis or certify collection-wide independence, Greek/Eteocypriot language classification, comparable sign units or unique ancient objects. Milyan shared-cache and other semantic/partial-overlap questions remain governed by their own frozen dependence evidence; this tool refuses those inputs.

No new independent model accuracy, external review, primary-edition access, phonetic equivalence or scholarly acceptance is claimed. Historical pilot scores and frozen audits remain unchanged.

## Published implementation and verification

| Repository | Published change | Verification |
|---|---|---|
| Linear-A | `c5adfae5e745db4b34083a7d535f50f5d5bd9f1a`; draft packet bindings refreshed at `db46818b1491830091e63d9fa566b86400dc0afc` | All 21 hosted workflows passed at the packet-refresh revision, including actual route/case retrieval and AI skill checks |
| Cypriot-syllabic-Greek | `a0a88f192c2024cb67401736fa643c1794051705` | All 7 hosted workflows passed; individual guide, skill and source bundle updated |
| Eteocypriot | `8b3b8b518e16406f8cc56d93ee9b756ada7f6ebc` | All 8 hosted workflows passed; individual guide, skill and source bundle updated |
| Master-Corpus-AI-Skill | `bbb7d14cb551334e81547149548c471374020472` | Hosted standalone/native/frozen-study validation passed; 50 local tests passed, including unit/overlap rejection and source-union assembly tests |

A source-profile update invalidated two unreviewed packet fingerprints. Their draft forms were checked to be unsubmitted before regeneration. Both packet replay workflows now pass; no real specialist response was replaced. Individual source-bundle publication is separate from master acceptance; inspect `registry/member-state.json` for actual accepted revisions, especially while updates are in flight. An old failed refresh must not be reported as a failed ancient reading or a reason to promote an unvalidated revision.

The [24 October execution review](academic-remediation-2026-10-24.md) checks all 43 remaining items and adds the Milyan source-row union. The open scholarly count remains 43; improvements are not silently treated as closure.
