# Executed research studies and evaluation

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

The output preserves candidate citation, attribution and locator fields with their field pointers. Missing fields stay missing. A field labelled `source-checked`, a plausible bibliographic string or a matching hash does not show that this study inspected the primary edition. **No fresh primary-edition checks or external specialist reviews were performed in this pass.** The results identify where those checks need to start; they do not close that scholarly requirement.

## Source-grounded AI evaluation

The [12 task questions](research/2026-10-21/ai-tasks.json) and [compact evidence packet](research/2026-10-21/ai-evidence-packet.json) cover factual retrieval, source dependence, uncertain readings, incompatible units, component rights, missing evidence and unsupported translation. The [freeze commitments](research/2026-10-21/ai-freeze.json) bind the tasks, packet, protocol and separately held expected answers before responses are collected.

**Evaluation status: frozen; response collection and scoring pending.** Results will distinguish structured source fidelity from human interpretation review. This is a development pilot; independent source-qualified academic grading, cross-platform accuracy and researcher time savings are not established.

## Reproduce the studies

Use Git clones at the exact revisions in the study manifest. Keep these separate from active working checkouts; an update to main is not a reason to change a frozen study input. Place the native clones in a common parent directory, retaining repository names, and run from the master repository:

```sh
python scripts/research_milestone.py --checkouts /path/to/frozen-corpora
```

The command rejects wrong revisions and modified tracked inputs, then compares recomputed JSON with the committed outputs. It does not fetch new sources or change native evidence. Use `--write` only when deliberately producing a new set of outputs; a mismatch requires investigation rather than automatic acceptance.

## What remains open

- Verify exact primary-edition loci and source assertions for a defined stratum, recording corrections and uncertainty.
- Obtain separately attributable specialist judgments where a reading or interpretation requires them.
- Extend dependence mapping beyond the two tested families without forcing unknown object identities into joins.
- Compare actual research outcomes against direct source use with the same permitted evidence; no human timing experiment was performed here.
- Evaluate AI responses with independent source-qualified graders and a genuinely held-out task set.

Read [the academic audit](references/academic-audit-2026-10-20.md) for the broader claim limits. For proposed workflows rather than executed findings, use [the cross-corpus examples](CROSS-CORPUS-EXAMPLES.md).
