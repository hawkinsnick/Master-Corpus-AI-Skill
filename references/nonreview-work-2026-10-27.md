# Six workstreams without academic review — 27 October 2026

This is an executed engineering and documentary work package, with bounded results in all six requested areas. It does not close the broader scholarly backlog. **38 original entries and five scientific follow-ups remain open.** No original closure criterion was relaxed and no new specialist decision was received.

| Workstream | Executed result | Limit |
|---|---|---|
| Backlog | Individually classified all 38 original entries and five follow-ups; each preserves its criterion, executable next action and external evidence requirement | Classification does not complete every listed subtask |
| Source fidelity | 453 eDiAna catalogue entries; 1,974 derived text rows across Carian, Lycian and Milyan; 114-row second Milyan view; 24,258 checks, no mismatches | Frozen digital edition only; no new printed-page consultation or linguistic gold |
| Dependence | 11,744 eligible fields individually disposed; 174 cross-repository text groups, including 44 below the old length threshold; 139 shared digital-source locus groups | 1,103 field lineages remain unknown; no semantic or physical identity inferred |
| Development evaluation | 624 deterministic contract checks across all 104 declared collections; 146 linked records checked; 185 null and 862 false atoms retained | Exposed purposive development selection; deterministic interfaces, not representative model accuracy |
| Package terms | Opened 18 native local research packages and checked 464 components; built and verified 18 separate tools-only exports | 338 components lack public-export clearance in this audit; full corpus redistribution remains blocked pending component decisions |
| Researcher walkthroughs | Eighteen exact-ID examples, source refs, hashes, native units and expected links; executed through the actual master CLI | Retrieval reproducibility, not measured researcher benefit |

The source-row and view totals are different units. Do not add the 114 second-view rows to 1,974 as independent evidence. Text groups, source loci and field occurrences are not ancient objects or witnesses. The source-fidelity test preserves the annotation uncertainty in 667 source rows; it does not adjudicate those annotations.

## Inspect the evidence

[Frozen inputs](../research/2026-10-27/inputs.json) · [Backlog](../research/2026-10-27/backlog.json) · [eDiAna fidelity](../research/2026-10-27/ediana-fidelity.json) · [Dependence dispositions](../research/2026-10-27/dependence-v2.json) · [Development cases](../research/2026-10-27/research-regression.json) · [Package audit](../research/2026-10-27/package-audit.json) · [Executed walkthroughs](../research/2026-10-27/walkthrough-replay.json)

All source pointers bind frozen bytes. The receipts contain IDs, hashes, locators and method metadata rather than a new redistribution of edition text. Source text in the underlying member repositories retains its own terms. Annotation-matrix inspection uses a separate DOM traversal, not the native importer. The short-text screen preserves case, punctuation, damage and diacritics after NFC/whitespace normalization; unknown source histories stay unknown. It does not find semantic equivalence or all upstream edition relationships.

## Replay all six workstreams

Use Python 3.10+ and Git. From this master checkout, acquire the frozen native inputs into a new directory and replay the saved receipts:

```sh
python scripts/replay_nonreview.py --checkouts /path/to/new-frozen-corpora --acquire
```

For existing exact, clean checkouts:

```sh
python scripts/replay_nonreview.py --checkouts /path/to/frozen-corpora
```

Acquisition refuses an existing target rather than replacing user work. Replay checks every native origin, exact commit and tracked-input cleanliness. All scripts compare deterministic outputs against saved receipts and exit nonzero on drift. Later native or master checkpoints must not silently replace the dated inputs. The current master may expose a different accepted-checkpoint relationship; actual native source commits remain explicit.

## Export software without source data

The existing member research-package command continues to produce a **local research package**, not a corpus redistribution clearance. The component audit opens the generated archive and checks every listed component/hash. Unresolved public reuse is conservatively blocked. Do not infer permission from a file extension, hash, reference wrapper, public URL or project-wide license.

For the narrower noncommercial tools export:

```sh
python scripts/package_audit.py --checkouts /path/to/frozen-corpora --export-tools Linear-A --output /path/to/tools.zip
```

It includes three exact project software files, five controlling terms/notice documents and a generated per-file manifest. No transcription, source cache, annotation dataset, image, PDF or GORILA-derived dataset is included. Preserve the PolyForm Noncommercial terms and required notice. The tools require separately supplied native evidence to run corpus queries. This does not clear a full-data package or grant new source rights.

## Walk through every member

Run each command from the master checkout with `CHECKOUT_PARENT` replaced by the frozen checkout parent. For every answer retain the returned native unit, source hash/pointer and linked assertions. A missing ID in a view says nothing about global absence.

| Member | Collection / exact ID | Native unit | Expected linked records |
|---|---|---|---|
| Linear-A | `critical-pilot` / `HT 34` | `selected critical pilot entry` | 2 |
| Cypro-Minoan | `rich-dossiers` / `CMOC-0032` | `rich-record dossier` | 4 |
| Linear-B | `source-study` / `LB-ANNOTATION-ACQUISITION-20261017` | `bounded source-acquisition or scholarly-argument study` | 0 |
| Cretan-hieroglyphs | `catalogue-dossiers` / `CHIC-252` | `CHIC catalogue dossier` | 7 |
| Phaistos-Disc | `graphical-groups` / `PD-A-E15` | `source graphical group` | 7 |
| Byblos-syllabary | `survey-count-assertions` / `BYB-G` | `survey count assertion` | 0 |
| Cypriot-syllabic-Greek | `digital-entries` / `CSG-IGXV1-408` | `digital edition entry` | 0 |
| Eteocypriot | `digital-entries` / `ETEC-IGXV1-16` | `digital edition entry` | 0 |
| Eteocretan | `reading-versions` / `ECR-PRAISOS-2-CONWAY-127` | `attributed digital reading version` | 2 |
| Lycian-and-Carian | `digital-entries` / `EDIANA-LYCIAN-182` | `digital catalogue entry` | 0 |
| Phrygian | `p1-source-followup` / `PHR-TM1002268-ROLE` | `bounded source/identity follow-up disposition` | 0 |
| Anatolian-Hieroglyphic | `visual-source-routes` / `HL-VISUAL-SOURCE-ROUTES-20261019` | `bounded source-route inspection` | 0 |
| Archanes-Script | `attribution-review` / `ARC-DIS-001` | `bounded documentary attribution review task` | 0 |
| Aegean-anomalous | `attribution-review` / `ANO-DIS-003` | `bounded documentary attribution review task` | 0 |
| Lydian | `attribution-review` / `LYD-GUSMANI1975-LW59` | `bounded documentary attribution review task` | 1 |
| Sidetic | `attribution-review` / `SID-S9-2025-PIGBE` | `bounded documentary attribution review task` | 1 |
| Pisidian | `attribution-review` / `PIS-ADIEGO2012-N37` | `bounded documentary attribution review task` | 1 |
| Milyan-Lycian-B | `digital-entries` / `EDIANA-MILYAN-1` | `digital catalogue entry` | 105 |

Commands, expected full-record hashes and exact source references are in the `walkthroughs` array of the [development receipt](../research/2026-10-27/research-regression.json). Each member also has `docs/NONREVIEW-WORK.md` with its command. These examples deliberately retain ambiguity, null/false values or source links where available.

## Item-by-item remaining work

The following classification is a desk assessment of the unchanged criteria. Source access and participants are external dependencies distinct from academic review; many items include executable subtasks even where final closure needs external evidence.

| Item | Scope | Dependency | Executable next action |
|---|---|---|---|
| ACD-001 | Linear-A | SOURCE_AND_SPECIALIST | Trace each queued alternative to two page-level assertions; preserve dependence and shared-locus uncertainty. |
| ACD-005 | Linear-A | EVALUATION | Freeze new task/source commitments and preserve untouched outputs, failures and exposure logs. |
| ACD-006 | Linear-A | EVALUATION | Serialize exposure histories for all 24 labels and replay eligibility decisions. |
| ACD-007 | Linear-A | METHOD | Execute declared competing/control models and explicitly retain structural-only claims in the absence of discrimination. |
| ACD-008 | Linear-A | SOURCE_AND_SPECIALIST | Run separately labelled cluster sensitivity scenarios; never overwrite identity with heuristic joins. |
| ACD-009 | Linear-A | METHOD | Enumerate inclusion strata, missingness and sensitivity analyses within evidenced populations. |
| ACD-010 | Linear-B | SOURCE_AND_EVALUATION | Freeze aligned prediction/gold schema and leakage checks; test rejection of absent gold. |
| ACD-011 | Linear-B | SOURCE_ACCESS | Build reproducible degradation code using explicitly labelled synthetic controls. |
| ACD-012 | Cypro-Minoan | SOURCE_ACCESS | Give each of the eight records a source/locus and occurrence-coverage disposition. |
| ACD-013 | Cypro-Minoan | DEPENDENCE | Enumerate source-specific assertions, units and known dependence; retain unknowns. |
| ACD-014 | Cretan-hieroglyphs | SOURCE_ACCESS | Publish per-entry reading coverage and exact unavailable-source exclusions. |
| ACD-016 | Byblos-syllabary | SOURCE_AND_SPECIALIST | Bind sequence, layout and uncertainty to precise inspected source loci. |
| ACD-018 | Byblos-syllabary | SOURCE_AND_SPECIALIST | Expose parallel source-specific directions, layouts and counts without pooling incompatible conventions. |
| ACD-019 | Cypriot-syllabic-Greek | SOURCE_AND_SPECIALIST | Implement explicit included/excluded/unknown source-class filters and bounded denominators. |
| ACD-020 | Eteocypriot | SPECIALIST | Package Greek parallels and uncertain component assignments without promoting them to gold. |
| ACD-022 | Eteocretan | SOURCE_AND_SPECIALIST | Trace historical reading versions to exact loci and list nonadmitted rows. |
| ACD-023 | Lycian-and-Carian | SOURCE_AND_SPECIALIST | Preserve digital entries and candidate object relations as different units. |
| ACD-024 | Milyan-Lycian-B | SOURCE_AND_SPECIALIST | Trace apparatus alternatives to both real loci and document shared upstream editions. |
| ACD-026 | Phrygian | SOURCE_AND_SPECIALIST | Resolve or explicitly exclude each of the 159 missing edition-lineage groups. |
| ACD-027 | Phrygian | SOURCE_ACCESS | Expand bounded edition comparisons, recording restorations and line-fold transformations. |
| ACD-028 | Anatolian-Hieroglyphic | SOURCE_ACCESS | Build text/object/bibliography crosswalks only where exact source evidence exists. |
| ACD-029 | Archanes-Script | SOURCE_ACCESS | Represent each face as covered, unavailable or excluded, preserving source geometry. |
| ACD-030 | Archanes-Script | SPECIALIST | Prepare attributable sign/membership dossiers with conflicts and uncertainty. |
| ACD-031 | Aegean-anomalous | SOURCE_ACCESS | Keep historical segmentations and counts separate; record source-access outcomes. |
| ACD-032 | Lydian | SOURCE_AND_SPECIALIST | Apply Lydian row-level source-admission checks and preserve reference-only exclusions. |
| ACD-033 | Sidetic | SOURCE_AND_SPECIALIST | Apply Sidetic row-level source-admission checks and preserve reference-only exclusions. |
| ACD-034 | Pisidian | SOURCE_AND_SPECIALIST | Apply Pisidian row-level source-admission checks and preserve reference-only exclusions. |
| ACD-035 | Phaistos-Disc | SPECIALIST | Validate packet completeness, exact slot/group targets and absence of fabricated assessments. |
| ACD-036 | Phaistos-Disc | SPECIALIST | Exercise release rejection when external acceptance is absent. |
| ACD-037 | Master-Corpus-AI-Skill | EVALUATION | Run harder full-record retrieval development tasks, preserving source hashes and exposure limits. |
| ACD-038 | Master-Corpus-AI-Skill | SPECIALIST | Publish transparent field-level scoring and preserve raw model outputs. |
| ACD-039 | Master-Corpus-AI-Skill | EVALUATION | Record all observable build/platform metadata and explicitly mark unknown builds. |
| ACD-040 | Master-Corpus-AI-Skill | PARTICIPANTS | Implement timing/error collection and equal-evidence baseline tooling. |
| ACD-041 | All 18 members | DEPENDENCE | Screen short fields and source lineage; assign source-specific or unknown dependence without automatic object merges. |
| ACD-042 | All 18 members | RIGHTS | Audit every concrete package member; exclude unresolved components from public redistribution. |
| ACD-043 | All 18 members | SOURCE_AND_SPECIALIST | Retain null combined counts and require explicit unit/dependence crosswalks. |
| ACD-049 | Cypro-Minoan | SOURCE_ACCESS | Attempt lawful access for the five missing primary sides; preserve individual failure receipts. |
| ACD-050 | Cypro-Minoan | SOURCE_AND_SPECIALIST | Preserve both 09/10 assertions and exclude them from single-label gold. |
| FUP-003 | Parent ACD-003 | SOURCE_ACCESS | Search the 23 exact entry identifiers against inspectable edition routes; retain exclusions. |
| FUP-015 | Parent ACD-015 | SPECIALIST | Preserve both material assertions and their independent provenance. |
| FUP-017 | Parent ACD-017 | SOURCE_AND_SPECIALIST | Keep ordinal 32 and eight unassigned positions excluded from unambiguous lookup. |
| FUP-021 | Parent ACD-021 | DEPENDENCE | Keep the source-entry union bounded and preserve per-view components. |
| FUP-025 | Parent ACD-025 | DEPENDENCE | Keep the exact-cache source-row union bounded and preserve access paths. |

The JSON backlog preserves the external evidence requirement and original closure criterion alongside each action. Remaining primary-page access, edition locators, graphical controls, object identity, annotation decisions, unexposed evaluation, independent grading, platform diversity, researcher outcomes and component permissions have not been supplied by these software checks.

## Fresh model development walkthroughs and observed failures

Two fresh minimal-context agent sessions answered three multi-source questions each using the actual frozen checkouts. The six substantive conclusions agree with the native evidence in an internal, nonblind desk assessment. The unchanged [raw responses and citation results](../research/2026-10-27/forward-results.json) preserve an important failure: session A supplied 11 valid committed atomic references; session B supplied 10 references, of which **8 fail** strict commit/locus verification. Several combine pointers or use prose in the JSON-pointer field; one attributes an unpublished working file to a commit where it does not exist. Do not call this six fully passing research answers.

The instructions now require atomic typed locators and committed-byte verification. `scripts/verify_response_refs.py` rejects the observed errors. `scripts/check_forward_results.py` replays their original failed scores; no response was repaired. This small exposed exercise is not independent grading, a representative academic sample, cross-platform testing or a validated hallucination rate. No post-fix fresh-model success is claimed. The [response component terms](../research/2026-10-27/RIGHTS.md) preserve eDiAna attribution and applicable share-alike terms.

## Verify the published revisions

The [publication receipt](../research/2026-10-27/publication-verification.json) binds all eighteen published source and generated-artifact commits, exact skill/bundle hashes and successful native validation. The master accepts those exact artifact revisions; frozen study inputs above remain unchanged. The revised local research packages now carry `docs/NONREVIEW-WORK.md`, the guide referenced by each skill.

A [second package audit](../research/2026-10-27/publication-package-audit.json) checks the actual published revisions: 18 archives, 482 components and 18 tools-only exports; 356 components remain uncleared for public redistribution. The increase from 464/338 is the eighteen added guides, not new source data or newly discovered permission violations. Replay this second check with `python scripts/package_audit.py --checkouts /path/to/published-corpora --publication-checkpoints`; it requires the exact artifact commits in the publication receipt. Do not replace the earlier frozen package receipt or add the two snapshots together.
