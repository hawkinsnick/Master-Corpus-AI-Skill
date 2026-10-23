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
