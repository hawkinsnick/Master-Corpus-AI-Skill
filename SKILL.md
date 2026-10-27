---
name: combined-corpus-research
description: Coordinate evidence-first research across the registered ancient-script corpora. Use for choosing a corpus, tracing source records, comparing native evidence, assessing coverage or preparing reproducible cross-corpus research while preserving uncertainty, source dependence and component rights.
---

# Master Corpus AI Skill — 1.4.1

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

For setup and research workflows, read `USER-GUIDE.md` and
`RESEARCH-EXAMPLES.md`; use `CROSS-CORPUS-EXAMPLES.md` for multi-project
research sessions. Retrieve each member separately and establish the specific
comparison prerequisites before analyzing a combined sample. Treat proposed studies as research designs,
not executed results or evidence of native coverage. For saved executed examples,
read `WORKED-EXAMPLES.md`. Saved examples teach the workflow; do not represent them as
fresh executions. A bounded functional pass is not a cross-platform AI accuracy
measurement or independent scholarly validation.


## Assess academic claims critically

Read `references/academic-audit-2026-10-20.md` and its linked frozen review when assessing critical-edition, independence, linguistic-inference or AI-accuracy claims. Preserve its distinction between source fidelity and scholarly correctness. Treat its post hoc diagnostics as exploratory methodological probes, never canonical object joins, new linguistic results or independent expert acceptance. Prefer current native source/review gates over the audit when later evidence changes. If the reference is unavailable, disclose that limitation and retrieve the linked published report before relying on its findings.

## Use executed research results within their scope

Read `RESEARCH-RESULTS.md` for completed study outputs and evaluation status.
Use `research/2026-10-21/native-revisions.json` for their frozen source state;
never substitute a current member head silently. Read the dependence register
before counting the tested Milyan or Cypriot views as independent evidence.
Treat untested relationships as unknown, not independent. Source-trace passes
verify returned bytes and pointers, not primary-edition correctness. Distinguish
candidate citation fields, actual source consultation, expert review and model
evaluation. Check the evaluation's status and rubric before reporting a score.
Do not promote a development pilot to independently validated academic accuracy.

## Apply research follow-up controls

Read `OPEN-ITEMS.md` for the later printed-source check, expanded artifact
dependence scan and evaluation fixes. Distinguish shared metadata and quarantined
bytes from admitted inscription evidence. No matching artifact does not establish
independence. For evaluation, preserve field-level origin: native assertion,
master calculation or declared task condition. A task's execution flag must not
be attributed to a native source profile. Apply an explicit operation-based
decision rubric and keep historical pilot scores unchanged. New conformance
fixtures and external review protocols grant no new model accuracy or scholarly
acceptance. Report actual sources inspected and actual external decisions only.

## Use the itemized academic register

Read `references/academic-defect-register-2026-10-23.md` for the current itemized backlog and linked pinned evidence. Distinguish confirmed mapping defects, unresolved source conflicts, missing scholarly evidence, methodological risks and rights constraints. Report open and bounded-resolved counts separately. Do not turn closure-package counts into false-reading counts or software P0 counts. Check later native evidence before changing an item status; preserve original pilot scores and historical audits.

## Apply implemented academic remediation

Read `references/academic-remediation.md` and later native status before repeating a frozen audit's open count. In Linear A source-document dossiers, follow `edition-route-decisions`; rejected target URLs cannot be used as confirmed entry locators. Follow `case-dispositions` for legacy cases and never admit queue strings as source-qualified alternative pairs. The native closure of two rejection/disposition tasks does not establish corrected replacement locators or scholarly readings.

For the registered Cypriot same-edition source-entry union use `scripts/prepare_source_union.py` with its frozen manifest. Preserve all view-specific assertions while counting source-entry groups once. The tool refuses unsupported corpus pairings and unit promotion. Do not generalize its 592 digital-edition groups to physical objects, language frequencies, independent witnesses or collection completeness.

## Execute scoped Milyan unions and preserve remaining evidence gaps

Read `references/academic-remediation-2026-10-24.md` for the current 43-item execution review and the exact-byte Milyan source-row union. Use `scripts/prepare_milyan_union.py` only at its declared nonempty digital source-text-row unit, retaining both input provenance paths. Its 114 groups are neither independent witnesses nor physical lines/objects. New source-qualified studies require their own units and dependence decisions.

For Linear A MY Zf 2 retrieve the linked `source-context-cautions` record and preserve its text-only consultation limits and attributed uncertainty. Do not upgrade a caution, missing checksum, uninspected bibliographic lead or controlled source union to a reading correction, expert acceptance or completed academic validation. The 43 original scholarly closure criteria remain in force.

## Report scoped controls separately from open scientific requirements

Read `references/scoped-closures-2026-10-25.md` and the current native ledger before quoting an open count. Five additional controls have closed scope: reference exclusions, paired material representation, Byblos lookup exclusions and the two registered source unions. Report 38 unclosed original entries and five attached open scientific follow-ups separately. Preserve null material/locators, excluded memberships and exact unit boundaries. Do not report these controls as recovered source evidence, adjudicated scholarship or expert acceptance. Historical 43-item reviews are not a current original-entry counter.

## Prepare claims for adversarial academic review

Use `references/hostile-review-2026-10-25.md` and its pinned study inputs for the
expanded retrieval, source-fidelity and partial-overlap checks. Resolve exact
canonical JSON pointers; reject negative indices, leading-zero array aliases and
invalid escapes. Cite the actual native checkout revision returned by the master
query and disclose when it differs from the accepted master checkpoint. A dirty
tracked checkout or a revision changing during retrieval invalidates that run.

Distinguish complete traversal of declared retrieval views from complete corpus
coverage. A text match after NFC/whitespace normalization is a dependence lead,
not an object join, linguistic equivalence or new witness. Source XML/display
fidelity is not primary-print collation, adjudication or translation validation.
Keep the development stress test's known-task exposure and grading limitations
visible. Use expert acceptance and human benefit claims only when actual,
attributable evidence supports them. Do not relabel unmet scholarly closure
criteria as completed because software checks passed.

## Execute the six workstreams without academic review

Read `references/nonreview-work-2026-10-27.md` and the frozen inputs in `research/2026-10-27/inputs.json`. Use `scripts/replay_nonreview.py` to replay the itemized backlog, expanded eDiAna digital fidelity, short-text/source-lineage dispositions, full-record development regression, concrete package audit and eighteen CLI walkthroughs. Preserve the 38 original open entries and five follow-ups; executable subtasks do not satisfy missing external closure evidence. Distinguish digital annotation fidelity from linguistic gold and printed-source consultation. A short text match is not a physical join or independent witness. Treat unknown lineages as unknown, and keep field, source-row, entry and object units separate. Publicly exporting a native research package requires component-specific clearance; the separate noncommercial tools-only export includes no source payload. Report deterministic retrieval tests and fresh model development responses separately from independently validated academic accuracy or participant outcomes.

For machine-readable source citations, emit one exact JSON pointer per reference. Do not put ranges, semicolon lists, prose headings or several pointers into a `pointer` field. For text use `locator_type: text_contains` and a literal `locator` instead. Bind each reference to bytes actually present at the stated commit; verify with `git show COMMIT:PATH` and SHA-256. A working-tree file absent from that commit cannot be cited as committed evidence. Disclose uncommitted execution context separately from source evidence. Use the master `scripts/verify_response_refs.py` when available; a passing citation check establishes byte/locus binding, not bibliographic truth.

For the later live SigLA source drift, follow the linked native inspection in `references/nonreview-work-2026-10-27.md`. Preserve its unchanged source hash gate, distinguish source-map keys from ancient objects, and require a separately versioned field comparison before ingesting the changed serialization. Historical study replay must execute its pinned adapter, not current packaging code.
