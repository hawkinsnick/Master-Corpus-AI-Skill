# Research follow-up: fixes and remaining decisions

This follow-up addresses the open items in [Research Results](RESEARCH-RESULTS.md). The original pilot, expected answers and scores remain unchanged. The new work uses the same [frozen native revisions](research/2026-10-21/native-revisions.json); current main branches may have advanced.

| Item | Work completed | Current limit |
|---|---|---|
| Printed-source comparison | Visually inspected Vetters' printed pp.16–17 and compared three existing Tiryns source assertions; [receipt](research/2026-10-21-followup/printed-source-recheck.json) and [native documentation](https://github.com/hawkinsnick/Cypro-Minoan/blob/main/docs/SOURCE-RECHECK-2026-10-21.md) published | Bounded documentary agreement on one record; no independent glyph adjudication or collection-wide collation |
| Dependence beyond the original two tests | Compared 1,531 declared artifacts across all 153 repository pairs; [full inventory and groups](research/2026-10-21-followup/dependence-scan.json) | Equality checks extend the inspected inventory, not independence certification for unmatched material |
| AI evidence provenance | Replaced the misleading native citation for task execution context with a separately typed context source; every requested field now has an exact pointer, hash and declared transform where needed | This fixes the evaluation fixture; it does not retroactively improve the historical score |
| AI decision rubric | Defined the primary operation for each task and an explicit ANSWER/QUALIFY/ABSTAIN rule; [12 corrected fixtures](research/2026-10-21-followup/evaluation-v2.json) bind 21 fields | The fixture reuses known topics; it is not a held-out model accuracy experiment |
| Independent review and workflow comparison | Prepared a source-qualified [external evaluation protocol](research/2026-10-21-followup/external-evaluation-protocol.json), including equal evidence access, exposure control, counterbalancing and grading requirements | No external participant or specialist submission has been received; actual human outcomes and timing remain unmeasured |

## What the wider dependence scan found

The 30 shared-artifact groups comprise **25 shared digital-edition documents, three shared metadata groups, one quarantined non-supporting artifact group and one shared Milyan cache**. They remain concentrated in the already identified Cypriot and Milyan source families. This broader scan does not justify inventing additional source families or calling other projects independent.

The quarantine group must not become admitted evidence merely because two repositories preserve the same bad source. Shared sign registries, Unicode metadata and defect registers are infrastructure, not repeated ancient attestations. The scanner records all 153 tested repository pairs, inventory paths, byte hashes, optional canonical-JSON comparisons, scope exclusions and unknown independence states. It does not find every partial textual overlap, differently structured re-edition or shared upstream citation.

## What the source recheck establishes

The publisher PDF route returned a download error in ordinary retrieval. An accessible German National Library copy supplied the same named publication as a 50-page digital offprint, including a cover. Printed pp.16–17 are PDF pages 17–18. The authoring assistant rendered those pages and inspected the author's numerical catalogue-label statement. The existing labels agree. The receipt retains the copy URL, checksum and inspection scope; no PDF, figure, source image or extended prose is redistributed.

The **Cypro-Minoan individual skill, source-check documentation and generated bundle were updated together**. Its native validator passed. The master's automatic member monitor will record the validated new native revision; the frozen studies retain their earlier inputs for reproducibility.

A page-level documentary check does not authenticate an ancient sign reading or supply a second independent witness. The Linear B publication access attempt recorded in the earlier pass remains unresolved; this Tiryns check does not pretend to close that separate route.

## How the evaluation fixture was repaired

The original evidence-ID score could not verify whether a particular field came from a native source, a master computation or a condition declared by the task author. Version 2 gives each requested field a typed origin, exact file pointer and hash. The resolver checks the native revision, the field's actual value and any declared length/list transformation. It rejects conflation of task conditions with native-source provenance.

The decision rubric now ties the label to the primary task operation: a field report uses ANSWER; a premise audit uses QUALIFY; an unsupported output request uses ABSTAIN. Null and false values retain their meaning. The historical two runs still have 9/12 exact decision matches each; no post hoc regrading is presented as a new successful experiment.

```sh
python scripts/scan_source_dependence.py --checkouts /path/to/frozen-corpora
python scripts/validate_evaluation_v2.py --checkouts /path/to/frozen-corpora
```

## Remaining work that needs external evidence or people

- Broaden printed-edition collation to additional defined source strata, using lawful access and reporting errors and uncertainty.
- Obtain attributable source-qualified specialist decisions on the actual readings or interpretations under review.
- Have an external coordinator select unexposed evaluation cases and qualified graders; the public development fixtures are unsuitable as an untouched holdout.
- Collect real researcher outcomes in the two workflow conditions and report failures, corrections and measured effort with uncertainty.

The external protocol is ready for use. It is not a completed review, measured human benefit or authority to upgrade a scholarly gate. No outreach messages have been sent as part of this follow-up.
