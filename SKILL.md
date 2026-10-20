---
name: combined-corpus-research
description: Coordinate evidence-first research across the registered ancient-script corpora. Use for choosing a corpus, tracing source records, comparing native evidence, assessing coverage or preparing reproducible cross-corpus research while preserving uncertainty, source dependence and component rights.
---

# Master Corpus AI Skill — 1.4.0

## Establish the available evidence

Read `manifest.json` and `registry/corpus-projects.json`. This master coordinates
18 independent corpus projects. Egyptian Hieroglyphic Corpus remains a separate
acquisition project; exclude photography and endurance projects. Do not merge
native evidence models or treat repository membership as linguistic evidence.

Read `migration/origin.json` for the exact extraction source and provenance.
The canonical published home is `hawkinsnick/Master-Corpus-AI-Skill`, with
`SKILL.md` at the repository root. The Linear-A combined-ai-skill entry is a
compatibility route. Supplying a URL does not install a skill or grant file access.
Identify which instructions, native files and scripts are actually accessible.
State any unexecuted check or unavailable source explicitly.

Resolve master paths relative to this repository. Resolve paths declared in a
member's registry entry relative to THAT member repository. `Linear-A/...` paths
in the routing reference identify the external Linear-A checkout. Never search
this master repository for native inscription data or invent missing files.

## Refresh and inspect native corpus state

Read `registry/member-state.json`, `MEMBER-STATUS.md` and `AUTO-SYNC.md` before
current coverage/readiness claims. The master automatically checks registered
native main revisions on a five-minute schedule and on master pushes. Only
validated, stable revisions advance accepted checkpoints; failed/racing updates
retain the previous accepted snapshot and are visibly pending. Scheduled delivery
can be delayed by GitHub. This refresh changes integrity/status metadata and the
starter, not scholarly readings, permissions, source independence or expert gates.
If the observed head differs from the accepted head, disclose that difference
and validate current native evidence before using it. No data from excluded
projects is admitted by synchronization.

## Route the research question

1. Select the member repositories whose stated scope can answer the question.
2. Load each selected member's `individual_skill_path`, `authority_profile_path`
   and `bundle_index_path`. Read its current native evidence and rights guides.
3. Prefer the native current authorities over dated registry summaries or saved
   worked examples. Treat inherited admission fields as declarations requiring
   validation, not independent scientific acceptance or permission.
4. Retrieve exact IDs within a repository and collection namespace. Retain the
   source path, JSON pointer or other locus, SHA-256, original attribution,
   editorial notation, uncertainty, exclusions and component rights.
5. For one member, follow that member's research workflow. For multiple members,
   retrieve their evidence separately before considering a comparison.

Use `references/native-routing.md` for specialist source/review routes and
historical checkpoints. Read the current native files before adopting any count,
readiness status, reading, source-access claim or dated instruction from it.

## Execute the standalone workflows when available

Use Python 3.10+ and the standard library. No native corpus checkout is needed to
check the master instruction bundle:

```sh
python scripts/validate.py
```

With native checkouts in one parent directory, validate the selected/current
member workflows and produce scoped receipts:

```sh
python scripts/validate.py --checkouts /path/to/corpora --output member-checks.json
```

Discover native collections and then retrieve an exact ID:

```sh
python scripts/query.py --checkouts /path/to/corpora --repository hawkinsnick/Linear-A --coverage
python scripts/query.py --checkouts /path/to/corpora --repository hawkinsnick/Linear-A --id "ARKH 1a" --collection source-documents
```

Search literal text across registered native views without pooling their counts:

```sh
python scripts/query.py --checkouts /path/to/corpora --search "?" --limit 3
```

A literal question mark is a retrieval term; it is not a universal classification
of damage or uncertainty. Report truncation and missing collections explicitly.
Unknown IDs mean absent from the selected view; never infer global absence.

Optional deeper federation, frozen-source replay and private research packaging
remain maintained tools of Linear-A. Run those from its checkout using its own
current guides and exact source checkpoints. This master does not duplicate
native code or acquire restricted datasets to imitate those workflows.

## Apply the comparison gate

Read `references/comparability-matrix.md`. State the question, native unit in each
member, included/excluded population, representation layer, counting denominator,
source dependence, uncertainty and relevant rights. If comparability is unknown,
limit the answer to a descriptive side-by-side account and mark inference BLOCKED.

Never infer sign values, phonetic equivalence, language family, borrowing,
chronology, morphology, decipherment or independent replication from visual/string
similarity, interoperability, shared tooling or duplicated source witnesses.
Do not transfer Linear B values into undeciphered scripts as established readings.
Preserve quarantined/superseded analyses as non-supporting where the native rules
require. Distinguish observed/source text, editorial reconstruction, normalized
representation, computation, scholarly interpretation and AI inference.

## Preserve source rights and scientific gates

Keep component terms and attribution intact. A public URL, purchased copy,
uploaded PDF or downstream reproduction grants no new redistribution permission.
Preserve GORILA restrictions and route growth to admissible sources. Do not
reconstruct restricted datasets indirectly. Upstream CC0/CC-BY/CC-BY-SA rights
remain applicable rather than inheriting project-original noncommercial terms.

Software integrity and source replay establish neither accepted readings nor
expert acceptance. Prepared review forms are not completed reviews. Missing gold,
annotations, source alignment, access or permissions remain distinct prerequisites.
Do not treat Linear B calibration as executed when its native gates remain open.

## Answer with inspectable evidence

Lead with the supported finding. Include native repository/collection/record IDs,
source citation/locus and path/hash/pointer, evidentiary category, source dependence,
uncertainty and exact method for new calculations. Keep unknowns unknown; do not
manufacture restorations, translations, physical identity or independent witnesses.
Give the next admissible research step when a claim is blocked.

For first-use guidance and real examples, read `START-HERE.md` and
`WORKED-EXAMPLES.md`. Saved examples teach the workflow; do not represent them as
fresh executions. A bounded functional pass is not a cross-platform AI accuracy
measurement or independent scholarly validation.


## Assess academic claims critically

Read `references/academic-audit-2026-10-20.md` and its linked frozen review when assessing critical-edition, independence, linguistic-inference or AI-accuracy claims. Preserve its distinction between source fidelity and scholarly correctness. Treat its post hoc diagnostics as exploratory methodological probes, never canonical object joins, new linguistic results or independent expert acceptance. Prefer current native source/review gates over the audit when later evidence changes. If the reference is unavailable, disclose that limitation and retrieve the linked published report before relying on its findings.
