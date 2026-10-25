# Executed research studies and evaluation

[Open-item fixes and remaining external decisions](OPEN-ITEMS.md) include a printed-source recheck, the full member-pair artifact scan and corrected evaluation provenance.

This page tracks the evidence behind four improvements: reproducible demonstrations, record-level source checks, cross-corpus dependence and measured AI behavior. The study uses [18 frozen native revisions](research/2026-10-21/native-revisions.json), not an unversioned collection. Read the [protocol](research/2026-10-21/protocol.json) before interpreting its results.

## Three executed demonstrations

| Study | Executed finding | What it establishes |
|---|---|---|
| [Source-view overlap](research/2026-10-21/dependence-register.json) | Two Milyan cache copies are byte-identical, each with 114 nonempty source text rows; 25 Eteocypriot source IDs also occur in the broader Cypriot view | Documented source dependence, not additional physical inscriptions or independent witnesses |
| [Linear A U008](research/2026-10-21/demo-u008.json) | The inspected KH 8 slots are zero-based 11 and 14, with catalogue numbers 567 and 510; the legacy alternatives are not an attributed same-locus pair | A reproducible reason to withhold reading adjudication and the exact source work needed next |
| [Cretan Hieroglyphic/Cypro-Minoan units](research/2026-10-21/demo-comparability.json) | 13 CH reading versions contain 21 stored token fields, 12 with hyphens; the selected CM layer contains 28 occurrence rows on 13 record labels | These fields do not share an authenticated sign unit; descriptive source accounting is possible, the proposed pooled analysis is not |

These are selected replication/feasibility studies of known issues. They are not discoveries, independent collation or proof of research superiority. Each output identifies repository revisions, source paths, pointers, hashes, methods, findings and remaining gaps. The overlap output includes individual source-row and edition-ID links so that another researcher can inspect the grouping decisions. Unchecked relationships remain unknown; different file hashes do not prove independence.

## Source checks across all 18 projects

The [source-trace sample](research/2026-10-21/source-trace.json) takes three hash-ranked retrievable view rows per project: **54 rows in total**. Each dossier was independently resolved back to the committed source pointer and compared with the exact payload. The sample includes catalogue entries, project registers and documentary views as well as reading-related records; it is not a representative sample of ancient inscriptions.

The [per-project source-check summary](SOURCE-CHECKS.md) links every sampled row and makes missing metadata visible. The output preserves candidate citation, attribution and locator fields with their field pointers. Missing fields stay missing. A field labelled `source-checked`, a plausible bibliographic string or a matching hash does not show that this study inspected the primary edition. **The initial 54-row trace pass performed no fresh printed-edition collation or external specialist review.** The results identify where those checks need to start; they do not close that scholarly requirement. A separate targeted follow-up freshly acquired three first-party IG XML records, confirmed their source hashes and compared 21 metadata/component-text fields with zero mismatches after correcting XML line-break handling. [The source-check summary](SOURCE-CHECKS.md) distinguishes this digital-edition fidelity check from independent epigraphic verification.

## Source-grounded AI evaluation

The [12 task questions](research/2026-10-21/ai-tasks.json) and [compact evidence packet](research/2026-10-21/ai-evidence-packet.json) cover factual retrieval, source dependence, uncertain readings, incompatible units, component rights, missing evidence and unsupported translation. The [freeze commitments](research/2026-10-21/ai-freeze.json) bind the tasks, packet, protocol and separately held expected answers before responses are collected.

**Evaluation status: completed development pilot.** The [frozen expected outputs](research/2026-10-21/ai-oracle.json), [two response runs](research/2026-10-21/ai-runs.json), [replayable scores](research/2026-10-21/ai-scores.json) and [non-blinded semantic review](research/2026-10-21/ai-semantic-review.json) are public. The expected outputs were withheld from responding agents; their hash was published in [the freeze commit](https://github.com/hawkinsnick/Master-Corpus-AI-Skill/commit/a9da1f83b4678b9d558400c68cdf809f16176ffd) before either response was collected.

| Measure | Run A | Run B | Interpretation |
|---|---:|---:|---|
| Exact requested-value matches | 12/12 | 12/12 | Structured values match the frozen packet-grounded expected output |
| Intended evidence-ID selections | 12/12 | 12/12 | Correct packet references; not independently verified bibliography |
| Exact decision-label matches | 9/12 | 9/12 | Three ANSWER/QUALIFY/ABSTAIN rubric disagreements per run |
| All structured checks on a task | 9/12 | 9/12 | Preserve the frozen rubric rather than redefining a pass afterward |

Both sessions preserved the substantive license, missing-page and non-execution qualifications on the three label disagreements. The authoring assistant's non-blinded review identified no unsupported substantive assertion in these 24 responses; this is **not a measured general hallucination rate or independent expert grade**. One evidence item also has a provenance limitation: its non-execution flag is task-construction context, not a native profile field. Retain this disclosed packet limitation when interpreting its evidence-ID match.

A direct field-extraction baseline matched 3/3 factual tasks. It does not address interpretive/safety questions, and no human/manual timing experiment was performed. Both response sessions inherited the same model family; an exact build identifier was unavailable through the interface. This pilot establishes neither superiority to direct lookup nor cross-platform accuracy. Raw responses, errors, rubric limitations and scope are preserved.

## Reproduce the studies

Use Git clones at the exact revisions in the study manifest. Keep these separate from active working checkouts; an update to main is not a reason to change a frozen study input. Place the native clones in a common parent directory, retaining repository names, and run from the master repository:

```sh
python scripts/research_milestone.py --checkouts /path/to/frozen-corpora
python scripts/score_research_pilot.py
python scripts/provider_source_check.py --checkouts /path/to/frozen-corpora
```

The command rejects wrong revisions and modified tracked inputs, then compares recomputed JSON with the committed outputs. It does not fetch new sources or change native evidence. Use `--write` only when deliberately producing a new set of outputs; a mismatch requires investigation rather than automatic acceptance.

## What remains open

- Verify exact primary-edition loci and source assertions for a defined stratum, recording corrections and uncertainty.
- Obtain separately attributable specialist judgments where a reading or interpretation requires them.
- Extend dependence mapping beyond the two tested families without forcing unknown object identities into joins.
- Compare actual research outcomes against direct source use with the same permitted evidence; no human timing experiment was performed here.
- Evaluate AI responses with independent source-qualified graders and a genuinely held-out task set.

Read [the academic audit](references/academic-audit-2026-10-20.md) for the broader claim limits. For proposed workflows rather than executed findings, use [the cross-corpus examples](CROSS-CORPUS-EXAMPLES.md).

## Adversarial academic review preparation

The [25 October review and repairs](references/hostile-review-2026-10-25.md) cover all eighteen declared retrieval profiles, expanded digital-source checks and partial-text dependence screening. A fresh Linear B paper download and appendix check succeeded; earlier access failures remain historical. The development exercise is compact-evidence conformance, not independently validated academic accuracy. All43 inherited scholarly closure packages remain open or mitigated under their original criteria.
