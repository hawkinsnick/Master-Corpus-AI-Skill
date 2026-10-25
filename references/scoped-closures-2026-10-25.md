# Scoped control closures — 25 October 2026

Five controls now satisfy the representation, exclusion or workflow alternatives in the original criteria. They are not five new scholarly adjudications.

| Item | Closed scope | Open scientific follow-up |
|---|---|---|
| ACD-003 | Explicit exclusion/accounting for all 23 missing-reference entries | Recover actual edition locators |
| ACD-015 | Preserve both material assertions and return no resolved value | Adjudicate material and physical identity |
| ACD-017 | Exclude ordinal 32 and eight unassigned positions from unambiguous lookup | Resolve source discrepancy and missing memberships |
| ACD-021 | Count registered Cypriot source entries once | Claims beyond the frozen source-entry union |
| ACD-025 | Count identical Milyan source rows once | Reading, object and witness claims beyond that union |

The ledger now has **38 unclosed original entries**, plus **five explicit open scientific follow-ups** attached to these controls. Seven original entries have scoped control closure in total, including the two earlier dispositions/rejected mappings. Do not describe this as five recovered sources, adjudicated readings or independent witnesses. The earlier 43-item reports retain their historical scope.

Read the [native ledger](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/academic-remediation-status.json) and [closure evidence](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/SCOPED-CLOSURES-2026-10-25.md). Individual source literals and scholarly gates remain unchanged. The two union units remain distinct; never sum them as ancient attestations.

```sh
python scripts/check_scoped_closures.py --checkouts /path/to/corpora
```

This replays the three native control datasets and both frozen unions, checks the ledger's counts and source hashes, and verifies that all five scientific follow-ups are still open. Native regression tests exercise actual researcher queries and reject inconsistent source evidence. Passing these checks is evidence of the control's behavior, not an expert judgment about an ancient mark or object.
