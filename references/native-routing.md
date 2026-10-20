# Native source-routing reference

This is the preserved source-routing narrative from the prior master skill.
It includes historical checkpoint counts and dated reports. For current claims,
read the selected native member skill and authority files anew. Paths beginning
`Linear-A/` identify files in the external Linear-A checkout, not this repository.
Other native data/scripts paths resolve inside the member explicitly named by
the surrounding note. If ownership is unclear, resolve it from the registry or
report the ambiguity; do not guess a file or scientific conclusion.



## Validate every individual skill before operational claims

Use `Linear-A/corpus-factory/AI-SKILL-VALIDATION-2026-10-20.md` and run
`python Linear-A/corpus-factory/validate_ai_skills.py --checkouts PARENT_DIRECTORY`
against matching local checkouts. Load each member's canonical
`ai-skill/SKILL.md` and its `docs/AI-SKILL-VALIDATION.md` before retrieval.
The master covers 18 corpus repositories; Egyptian Hieroglyphic Corpus remains
an independently audited acquisition project outside that membership. Do not
claim that a GitHub URL installs a skill or supplies inaccessible evidence.
A scoped functional pass establishes native evidence retrieval and integrity,
not accepted translation, scholarly verification or cross-platform AI accuracy.
If current files or execution are unavailable, state that validation was not run.


# Combined Corpus Research AI — 1.3.0

This is an orchestrator over independent corpus projects. It is not a corpus, a decipherment system, or a license umbrella.

## Guide a researcher's first session

Use `WORKED-EXAMPLES.md` for step-by-step onboarding.
Offer the browser-only route before optional AI or Python execution. Retrieve
canonical evidence or the explicitly identified saved dossier before answering;
examples and expected results are teaching snapshots, not fresh executions.
For ARKH 1a retain source-reported metadata, upstream attribution and rights;
for U008 preserve the unresolved locus/attribution gap without choosing a reading.
For counts retain the native unit, blanks, denominator, input hash and method.
Identify accessible files and distinguish expected, saved and newly executed
outputs. Route other languages through their native evidence guides; do not
transfer Linear A fields or readiness claims to them.

## Linear A research-readiness controls

For public SigLA-view provenance, context coverage or export/replay questions,
read `docs/NORTHWESTERN-RESEARCH-READINESS.md` and
`analysis/research-readiness.json`. Run `python scripts/research_readiness.py --check`
before describing the report as current. Keep the result scoped to the committed
public derivative; never generalize it to all inscriptions or other corpus members.
Preserve missing publication routes, source-reported context, unresolved readings,
rights refusals and expert/calibration gates. Use export v2 manifests to cite exact
source/output bytes; deterministic package replay establishes byte identity only.
Treat TEI JSON-note round trips as preservation tests, not validated EpiDoc.

## Mandatory routing
1. Identify which registered corpus project(s) can answer the question.
2. Load each project's individual SKILL.md and generated research-bundle index before using its evidence.
3. Treat each corpus's native identifiers, evidence model, uncertainty, exclusions, rights, and scientific gates as authoritative.
4. For a single-corpus question, defer to that corpus skill unless cross-corpus context is necessary.
5. For cross-corpus questions, run each corpus analysis independently first, then compare only fields whose semantics are demonstrably compatible.

## Evidence firewall
Never infer common sign value, language relationship, borrowing, chronology, morphology, decipherment, or independent replication from interoperability, visual similarity, string similarity, positional statistics, shared tooling, or repository membership alone.

A shared upstream source, edition, transcription tradition, code path, derived dataset, or duplicated witness is not independent evidence. State dependencies.

## Comparison gate
Before comparing corpora, report:
- research question;
- corpora included and why;
- unit of comparison in each corpus;
- whether units are semantically comparable;
- representation layer being compared;
- source-independence status;
- uncertainty/exclusion rules;
- rights constraints;
- known blockers.

If comparability is not established, stop at a descriptive side-by-side account and label the inferential comparison BLOCKED.

## Claim discipline
Classify substantive statements as corpus fact, source/editorial assertion, reproducible computation, scholarly interpretation, AI-derived analysis, or unknown/blocked. Never upgrade one class into another silently.

## Citation and reproducibility
Use stable corpus/record/claim identifiers and source locators when available. Name the corpus project and repository artifact supporting material claims. For AI-derived calculations, state inputs, exclusions and method sufficiently to reproduce.

## Rights firewall
Rights remain source- and corpus-specific. Never treat inclusion in this combined skill as permission to redistribute content. Prefer references/locators over reproduction when rights are unclear or restrictive.

## Staleness
Check each participating project's generated source-state. A stale or absent bundle must be disclosed; canonical corpus files take precedence.

## Default answer shape
Answer the research question directly, then provide Evidence by corpus; Comparability; Result/status; Uncertainty and blockers; Reproducibility; Rights/attribution where relevant.

## Translation/decipherment
For undeciphered or poorly understood material, do not manufacture translations or phonetic readings. For deciphered scripts/languages, preserve editorial uncertainty and do not transfer established values to other scripts without explicit evidence.

## Scope
The active project set is defined by registry/corpus-projects.json. New corpus projects join only through explicit registry entries and must provide an individual skill plus the shared research contract.

## Evidence-growth routing
For members with an `evidence_growth_state` in the registry, read the member's current-status and authority-profile artifacts before reporting coverage or readiness. Treat growth targets as plans, not achieved evidence. Never infer increased scientific readiness from repository version, archive size, or source count alone; only canonical admission and verification gates can change claim status.

## Fleet benchmark
Use `references/fleet-benchmark.md` when discussing corpus maturity or evidence acceleration. Linear A is the governance/reproducibility benchmark, not a linguistic donor. Parity means comparable rigor and usability under the evidence actually surviving for each corpus, never equal record counts.

## Corpus Factory benchmark
Before making fleet-wide maturity, coverage, or readiness claims, consult `../Linear-A/corpus-factory/fleet-gap-register.json` and `../Linear-A/corpus-factory/schemas/benchmark-status.schema.json`. Treat each member's `top_gap` as an unresolved research dependency, not a deficit that may be filled by inference. A corpus can satisfy parity with few surviving objects if coverage/accounting, provenance, rights, uncertainty, validation, independence, and AI authority are complete.

## Pre-Expert Maximum routing
When a registered member exposes `pre_expert_maximum_path`, consult that artifact before proposing expert review or describing unfinished work. Complete or explicitly disposition machine/source work first. Treat `human_only_boundary` as decisions that must not be silently resolved by the AI. A PRE_EXPERT_MAXIMUM contract is a work-boundary contract, not a claim that the corpus is scientifically complete or expert validated.

## New comparative members
Anatolian Hieroglyphic is a comparative control, Archanes is an early-Cretan disagreement-aware corpus, and Aegean Anomalous is a neutral quarantine layer. Never use their co-registration to imply common language, sign identity, descent or decipherment.

## Lydian, Sidetic and Pisidian reference routing
Treat these new members as attributed eDiAna digital reference layers until their native gates admit primary-edition/object verification. Count source document IDs separately from response grouping titles and physical objects; labels may collide, and ID zero is valid. Preserve source headings, uncertainty, edition references and response row pointers. Source grammar and language assignments remain source assertions. The source snapshots and derived reference records retain CC BY-SA 4.0; project-original noncommercial terms do not override upstream permissions. Shared eDiAna/edition lineage does not provide independent replication across projects.

For Lydian, Sidetic and Pisidian, consult `analysis/record-admission.json`, `research/admission-policy.json`, `research/edition-dependencies.json` and `research/source-issues.json` before analytical claims. Use `analysis/benchmark-status.json` for scoped coverage and `research/source-frontier.json` for later publications. Bibliography searches are candidates; missing row citations must remain visible. Syntactic uncertainty flags do not adjudicate damaged signs. Snapshot hash binding and regression tests establish engineering integrity, not independent epigraphic verification.

## Collection expert validation handoff
Read `EXPERT-REVIEW.md` when preparing specialist validation. For members exposing `review_manifest_path`, read the current manifest and selected record packets before drafting a request. Bind requests to the evidence fingerprint and record hashes. Cite source inspections separately from independent reviews; disclose missing edition locators and access barriers. Preserve reviewer decisions by dimension. Do not fabricate reviewer identity, treat structural validation as authenticated expertise, or auto-admit evidence. Other members retain their native review protocols; do not assume the new three-member packet format exists fleet-wide.
## Linear A / Linear B pre-expert handoff
Read each member's `analysis/pre-expert-source-audit.json`, `docs/PRE-EXPERT-HANDOFF.md`, and `research/linear-a-b-control-interface.json`. Local materialization is distinct from public record admission. Source-record counts are not physical-object counts; source-defined groups are not adjudicated linguistic words. Open source-collation or aligned-gold gates prevent claims of a completed pre-expert ceiling. Continue machine/source work until the native contract records a supported terminal disposition.

For corpus-development work, apply `references/pre-expert-standing-order.md`.

## Lydian, Sidetic and Pisidian source work

Read each member’s `research/source-worklist.json` before preparing an exhaustive handoff. It accounts for every frozen record and citation while preserving unresolved edition joins. Consult linked source checks for precise locators and attributed competing readings. Inscription numbers may differ between editions; matching numbers alone do not establish identity. Museum inventory references in a publication are dated source assertions until independently reconciled. Acquired PDFs and targeted checks do not establish complete collation, redistribution permission or expert review.

## Linear A GORILA rights firewall

For Linear A, EFA has expressly refused this project's proposed reproduction of GORILA visual material and creation/publication/redistribution/exploitation of structured or machine-readable GORILA-derived datasets, including AI-assisted and non-commercial research outputs. The orchestrator must not route GORILA into ingestion, reconstruction, extraction, or redistribution workflows. It may be cited as bibliographic/edition-location context where lawful. Historical bounded inspection artifacts are audit history only. This member-specific restriction overrides any generic fleet preference for source acquisition.


For Linear A evidence-growth work, also read `../research/rights-compatible-evidence-frontier.json`; it is the member-specific source-admission routing table after the EFA GORILA decision.


## 3.0.17 researcher capability routing
For Linear A capability-development questions, read `research/eight-step-execution-3.0.17.json` and its eight referenced contracts. Treat COMPLETE_CONTRACT as a frozen design/admission contract, not proof that the corresponding UI, API, exporter, contextual population, map, metrology engine or analytical interface is implemented. Preserve GORILA rights restrictions, sealed prospective outcomes, source lineage, uncertainty and expert-only boundaries.


## 3.0.19 working researcher interfaces
Linear A now has working scripts for the read-only public-source API, compact browser index, source-context extraction, JSON/CSV/JSON-LD/EpiDoc-compatible loss-aware export, model-explicit accounting checks, and source-defined sequence analysis (KWIC, collocations, patterns, form-family distance). Prefer these committed interfaces over inventing ad hoc transformations. Their outputs remain source-reported evidence and do not establish decipherment, independent confirmation or expert validation.


## 3.0.20 browser and coverage discipline
For Linear A researcher-facing work, prefer the generated offline browser (`workbench/linear-a-browser.html`) and committed API/export scripts. Consult `analysis/evidence-population-coverage.json` when available, or regenerate it with `scripts/report_evidence_coverage.py`, before making completeness claims. A working validator/exporter does not mean scholarship, geography or context is populated. Missing evidence must remain missing rather than being inferred. See `docs/RESEARCHER-CAPABILITY-STATUS-3.0.20.md`.


## 3.0.21 pre-expert maximum / rights-dominant gate
Linear A has a machine-resolvable tooling baseline under admitted evidence; source acquisition, factual reconciliation, primary collation, calibration and expert judgment remain separately gated. Whole-corpus human-only readiness is not established. Read `research/residual-blocker-ledger-3.0.21.json` and `docs/RIGHTS-ONLY-READINESS-3.0.21.md`. Do not describe independent epigraphic confirmation or the sealed prospective experiment as unfinished software: they require admissible independent evidence and/or human object review. Current evidence-growth gates are dominated by source rights/access (GORILA/EFA refusal, Raison–Pope rights/access, and permission for richer object-level datasets). Optional UI/statistical/export depth may continue but is not prerequisite to ingesting lawful independent evidence.


## Corpus-family browser standard
Corpus-family repositories should expose an offline browser generated from an explicit rights-reviewed allowlist. Standard sister-project paths are `research/browser-sources.json`, `scripts/build_corpus_browser.py`, and generated `workbench/corpus-browser.html`; Linear A may use its richer native `workbench/linear-a-browser.html`. Never recursively sweep data directories into a browser. Treat browser admission as redistribution: verify source/record rights and provenance first. A browser is an access surface, not decipherment or expert validation.


## Collection >9 evidence gate
For collection-strength assessments, treat 9.0 as the current minimum target, but never manufacture a score from repository polish. A member earns >9 only when its lawful evidence depth, coverage accounting, source-lineage independence/reconciliation, object/text identity controls, uncertainty/disagreement handling, rights provenance, reproducible validation and researcher interfaces are all strong relative to the surviving evidence. If evidence growth is constrained by protected critical editions, unpublished fascicles, inaccessible object evidence or expert-only adjudication, report the member as externally gated rather than inflating its score. Current remediation members include Cypriot Syllabic Greek, Sidetic, Lycian/Carian/Milyan and Anatolian Hieroglyphic; consult each native pre-expert/GT9 artifact before rating.


## Collection-wide >9 floor
The corpus fleet uses a >9 scholarly-readiness graduation gate. A member does not graduate by version number, file count, or tooling alone. Assess lawful primary/critical evidence depth, declared coverage versus the scholarly universe, source independence and lineage, object/text identity reconciliation, uncertainty/disagreement controls, reproducibility, rights provenance, and expert-review boundaries. Corpora below the gate remain in remediation until evidence depth supports graduation or a concrete rights/access/expert dependency prevents further lawful machine-resolvable progress. Never inflate a score to hide an external blocker.

## Milyan software admission checkpoint (2026-10-10)
`hawkinsnick/Milyan-Lycian-B` is structurally admitted through the native-schema research-contract adapter. Route Milyan/Lycian B questions to its `ai-skill/SKILL.md`; current evidence is three bibliographic segment records for two monuments, with zero verified transcriptions. Text-level cross-corpus inference remains blocked pending critical edition collation and source-specific rights review. Replay native and master validation before claiming synchronized software admission. Milyan is not synonymous with Lycian A.

Milyan update: member research API now provides bibliographic inventory search, empty line-layer KWIC, coverage and JSON/CSV exports. Its source-reconciliation matrix explicitly blocks all unverified readings; zero KWIC hits cannot establish lexical absence. Follow the individual Milyan skill and bundle index for current evidence state.

## Byblos rights-dominant routing

For Byblos Syllabary evidence-growth or readiness questions, consult the member repository's `analysis/preexpert-residual-ledger.json` and `docs/RIGHTS-DOMINANT-READINESS.md`. Under its currently lawfully admitted evidence, the identified non-rights pre-expert machine/source work has been exhausted. The dominant acquisition dependencies are lawful access to Dunand 1945/1978, authoritative object/accession witnesses, and applicable upstream terms for provider sequence/encoding reuse. Keep the fourteen A-N publication labels distinct from physical-object counts and keep OCBI rendered rows distinct from inscription counts. Independent epigraphic review remains downstream and must not be simulated.


## Eteocretan rights-wall routing

For Eteocretan readiness and evidence-growth work, consult the member repository's `research/pre-expert-maximum.json`, `research/residual-blocker-ledger.json`, and `research/rights-wall-audit-2026-10-06.md`. Guarducci III has a confirmed public digital access route through University of Crete Anemi, but access does not itself authorize redistribution or systematic structured derivative use. Duhoux 1982, complete Dreros primary evidence, authoritative object/accession evidence, and source-specific reuse terms remain evidence-growth gates. Preserve Praisos classification conflicts, Dreros location uncertainty, and Azoria candidate/item denominators; never convert derivative witnesses into independent ancient observations or admit readings merely because a source is downloadable.



### Eteocretan four-front closure
The member repository now also controls Duhoux's 13-text universe as an attributed target denominator, a conservative Praisos/IC publication crosswalk, an Azoria discovery denominator of 17 inscribed sherds with only two individually represented handle candidates, and a Dreros witness genealogy. Do not synthesize the unresolved Azoria items, copy Duhoux's protected critical edition, or count dependent editions/transcriptions as independent witnesses. Further canonical growth requires new lawful source/institutional evidence before human epigraphic adjudication.


## Phrygian maximum pre-expert routing

The Phrygian member's former rights-only assessment has been narrowed. Protected systematic extraction from Brixhe-Lejeune, Obrador-Cursach and uncertain-rights digital editions remains rights-gated, but lawful public record-level identity/object metadata reconciliation remains open. Consult `research/catalogue-denominator-control.json`, `research/subcorpus-source-genealogy.json`, `research/public-object-metadata-lane.json`, and `research/residual-blocker-ledger.json`.

Keep CIPPh/modern catalogue/TITUS/UD/TM denominators distinct; TITUS headings are not unique-inscription counts; Mysian comparison material is not automatically Phrygian evidence; dependent digital corpora do not constitute independent epigraphic witnesses. Canonical readings remain sealed until source-level verification.



### Phrygian public-evidence expansion
The member repository now has a broader monumental Old Phrygian factual-metadata lane and a publisher-hosted Kerkenes K-01 inspection route. Keep catalogue namespaces explicit (notably the W-11 / MPhr-01 collision) and use OIP 135 for attributed factual excavation/catalogue/inventory controls only under its source-specific rights boundary. Downloadable access is not blanket permission to redistribute protected figures, prose or critical text.



### Phrygian Gordion/Kerkenes small-object controls
The member corpus now distinguishes Penn Museum's institutional Gordion discovery categories (11 stone inscriptions; 245 graffiti, primarily on vessels) from TM/TITUS/UD denominators and from the monumental-index layer. It also tracks OIP 148 as a publisher-hosted Kerkenes pot-mark/graffiti context route. Do not turn category counts into exact unique-object totals, classify all marks as Phrygian language, or count repeated publication of the same evidence as independent witnesses.


## Fleet EpiDoc and universal identity standards

Two collection-wide interoperability contracts are normative for new corpus engineering:
- `Linear-A/corpus-factory/schemas/epidoc-interoperability-contract.json`: native records remain authoritative; EpiDoc exports must be loss-aware, rights-aware, mapping-audited and round-trip tested for declared reversible fields.
- `Linear-A/corpus-factory/schemas/universal-identity-graph-contract.json`: external IDs and object/text/edition/place relationships are provenance-bearing assertions, not string joins.

Never infer physical identity from matching catalogue labels, adjacent numbers, inherited digital links, shared coordinates or visual resemblance. Preserve negative/disputed identity edges. EpiDoc encoding establishes interoperability only; it does not establish reading correctness, source independence, decipherment or expert review.



### Interoperability rollout status — 2026-10-06
Linear A: existing TEI exporter audited as PARTIAL_NOT_YET_EPIDOC_CONFORMANT; native JSON payload is preserved but structured EpiDoc mapping/validation/round-trip and rights allowlist gates remain. A rights-aware source identity graph is seeded; GORILA remains historical audit/bibliographic-only under the project-specific refusal.

Linear B: existing source-ID-preserving EpiDoc importer is an engineering strength, but fleet conformance remains open pending a real authenticated annotated source export, mapping/loss reports, export path and round-trip tests. A DĀMOS/source identity graph is seeded without equating source IDs with physical tablets.


Cypro-Minoan: fleet pilot separates physical object, text-bearing surface, inscription/potmark and sign-occurrence assertions. EpiDoc export remains unimplemented; partial occurrence coverage and authority-specific sign labels must remain explicit.

Cretan Hieroglyphic: fleet pilot separates CHIC catalogue identity, INSCRIBE-derived context, critical reading assertions and sign classes. EpiDoc export remains unimplemented; alternative script classification, writing/iconographic uncertainty and zero asserted native phonetic values must survive serialization.

## Eteocypriot, Eteocretan and Phaistos Disc denominator safeguards
For Eteocypriot distinguish digital edition entries, editorial components, archaeological objects and independent witnesses; shared Cypriot Greek source copies are not replication. For Eteocretan distinguish inscriptions, alternative reading versions, source rows and analytically admitted tokens (currently zero in the documented baseline). For Phaistos Disc preserve the historical 241 versus project 242 slot-count disagreement, and never count two faces as two independent objects. Consult each member's current README and `ai-skill/SKILL.md` before reporting these numbers. These documentation safeguards do not themselves update generated source-state fingerprints or establish independent review.

## Native-schema admission adapters
Anatolian Hieroglyphic, Archanes Script, Aegean Anomalous and Milyan use `ai-skill/generated/fleet-contract-index.json` alongside their native bundle. Replay the member validator and master admission validator before claiming synchronized admission. These adapters hash declared native authorities and preserve source-specific rights, exclusions and uncertainty. Admission does not certify readings, object identities, source independence or human expert review. For Phaistos Disc, read the machine-replayed `analysis/acceptance-2.0.json`; receipt or schema validity is not human acceptance.

## Six-workstream P1 reconciliation

Read `docs/P1-RECONCILIATION-2026-10-11.md` and `Linear-A/corpus-factory/p1-evidence-snapshot.json` before fleet-wide closure claims. All eighteen members declare source-bound collection ledgers and review packets in the registry. Replay each native collection builder before using its packet. Respect separate native record units, restricted local derivatives and unresolved primary-source work. Rights authority presence is not permission; an interoperability artifact is not full EpiDoc conformance; a valid decision template is not independent human acceptance. The six recovered workstreams are not six identified GitHub issues. Never invent their ticket numbers or report evidence-dependent gates closed from software checks.

## P1 closure assessment

The declared baseline and eighteen-member common handoff coverage are complete. Scholarly data coverage, full interoperability, documentary rights acceptance and independent review retain their documented open criteria. Cypro-Minoan now has executable expected-hash verification and upstream RNG plus all 57 embedded Schematron patterns for its partial 12-occurrence pilot; read its validation receipt and pins. Do not extrapolate that result to full corpus conformance or human acceptance. Phaistos Disc issue 4 remains the actual open GitHub issue. Report workstream status and live ticket state separately.

### Verified Phrygian catalogue and reference interchange
Phrygian PR 11 (merge `6f0be30df492acdb6b07c05507d9e3f991156314`) closes the factual K-01 catalogue crosswalk and frozen-reference export validation gaps. Read `research/k01-catalogue-concordance.json`, `interchange/export-manifest.json`, `research/interoperability-identity-graph.json` and `analysis/upstream-epidoc-validation.json`. Eight catalogue entries carry fourteen identification labels. The introduction and entry descriptions use incompatible piece counts; unique physical count remains unknown. Catalogue/concordance XI is retained alongside the contents-page IX discrepancy. No certified physical joins or independent review are added.

All 203 frozen UD reference records (1,921 tokens; 162 distinct source TM labels) round-trip every native record field through EpiDoc. Pinned upstream RNG and all 57 embedded Schematron patterns pass with 613 fired rules and zero findings. This closes that finite reference-view validation gate, not full critical-edition coverage. UD-derived XML retains CC-BY-SA-4.0 attribution. OIP 135 factual metadata has a separate source-specific rights boundary; public access and the publisher license do not grant model-training permission. Protected prose, images and critical readings are not incorporated. Scientific data gaps, other component rights and independent acceptance remain open at their documented scopes.

### Milyan reference population and inspected edition controls
Merged Milyan PRs 4 and 5 populate two frozen eDiAna digital catalogue entries and 114 source text rows: TL 44c has 34, TL 44d 71, and TL 55 nine. The byte-pinned raw source and row locators preserve exact strings and original annotations. Explicit reference-layer API queries offer literal KWIC, JSON and CSV. Canonical/provisional queries remain separate and verified canonical readings remain zero. This is the same source lineage as the Lycian-and-Carian cached Milyan partition; never double-count its rows or call these independent witnesses.

Route through `docs/EDIANA-REFERENCE.md`, `research/reference-manifest.json`, `research/ediana-reference-crosswalk.json`, `research/primary-edition-locator-control.json` and `analysis/upstream-epidoc-validation.json`. Reference-derived components retain CC-BY-SA-4.0 with original eDiAna hyperlinks and primary-edition attribution; project-original NC terms do not override them. Exact source text and every derived row field round-trip through EpiDoc. Pinned upstream RNG and all 57 embedded Schematron patterns execute, with 348 fired rules and zero findings. This validates the full declared frozen reference view, not a complete independently collated corpus.

Visual Kalinka 1901 scan inspection establishes precise printed/PDF page locators. Preserve the historical TL55 eight-line description versus nine digital source rows without forcing physical-line joins. Exact historical reading comparison remains open. A broad source bibliography and an exact text-page locator are different claims. Public primary access does not create an independent witness or human acceptance. No claim that the fleet has reached its pre-expert maximum follows from this checkpoint.

## Current member summaries and calibration acquisition
For Linear A, Linear B and Milyan, use the generated marked current README summary together with its native status authorities; distinguish native release versions from later tooling checkpoints. Historical sections do not override current gates. Milyan is structurally admitted and has a populated reference layer, while canonical verified readings remain absent. For Linear B acquisition, require the separate linguistic annotation package linked to document/word-occurrence IDs: the described DĀMOS EpiDoc export omits those analyses. A graphical benchmark remains separately gated. Never infer calibration performance from source acquisition or importer checks.

Cypro-Minoan’s 2026-10-11 source-located concordance repair (PR #19, merge `43def2a2d2728735ccbd0464f88d07d8fc8fba34`) resolves the 186 former number-only mappings. The bounded register now has 254/254 source-attributed sigla. Consult `catalogues/source-located-concordance.json`, `analysis/catalogue-mapping-audit.json` and `docs/CATALOGUE-CONCORDANCE.md` in that repository. Preserve source asterisks, their NOT_ADJUDICATED meaning and `ENKO?`; these factual joins add no independent witness, physical certification or sign readings. At that earlier checkpoint there were 21 rich records, 12 occurrences and 15 uncovered rich records, distinct from catalogue slots. The later source checkpoint below supersedes those occurrence/coverage counts with 16 occurrences on nine records and 12 currently uncovered records. The scholarly-data, full interoperability, component-rights and independent-review workstreams remain open.

Cypro-Minoan’s uncovered-record source controls (`research/uncovered-record-review-controls.json`, `research/met-open-image-controls.json`, `docs/UNCOVERED-RECORD-REVIEW.md`) now locate evidence and expert questions for all fifteen uncovered rich records. Eight have visually inspected dependent-edition locators; four Met candidates have fourteen inspected/hash-pinned CC0 image views and pinned accession data. Two records retain museum-metadata-only acquisition routes; one official source returns HTTP403. Preserve blank UNREVIEWED decisions, possible/alternative-script labels, uncertainty and source dependence. The Met CC0 component exception overrides project-original noncommercial terms for the imported basic data and explicitly public-domain images; it does not apply to other sources. No new sign readings or completed expert review are asserted.

Lydian, Sidetic and Pisidian now expose complete frozen native-reference EpiDoc views (respectively 118/471, 11/32 and 54/99 directory records/nonempty rows). Consult each member’s `docs/EPIDOC-REFERENCE.md`, `interchange/export-manifest.json` and `analysis/upstream-epidoc-validation.json`. Every native reference field and exact source row roundtrips; raw upstream fields omitted by native derivation, physical geometry and accepted critical apparatus remain outside the view. Distinct source document IDs survive catalogue-label collisions. EDiAna-derived XML remains CC-BY-SA-4.0 with attribution; project-original NC terms do not supersede it. All 57 embedded upstream Schematron patterns execute with zero findings (358 Lydian / 37 Sidetic / 166 Pisidian fired rules). Each native repository passes 53 tests including actual upstream and adversarial controls. This closes the frozen-view export gap for these three members, not the fleet’s full scholarly interoperability or expert acceptance.
## Source-specific evidence frontier

For Linear A, Linear B, Phrygian, Eteocretan, Lydian and Sidetic, read each repository’s `research/source-action-plan.json` and `docs/SOURCE-ACTION-PLAN.md` before claiming rights-only readiness. Separate endpoint access, permission for the intended operation, source delivery, factual reconciliation and human adjudication. Dated searches do not prove global exhaustion. Respect existing completed crosswalks and their unresolved edges. Linear B’s `docs/CALIBRATION-INTAKE.md` describes private metadata/digest intake only; it does not establish acquired gold, certification or authority to reveal answers. Other members retain their own native stopping authorities; this checkpoint does not certify the entire fleet.

## Source checkpoint and reevaluation — 2026-10-11

Read `Linear-A/corpus-factory/REEVALUATION-2026-10-11.md`, `Linear-A/corpus-factory/source-checkpoints-2026-10-11.json` and `Linear-A/corpus-factory/coverage-denominators.json` before current coverage claims. CH/CM source-qualified coverage has expanded; primary reconciliation and independent acceptance remain open. Other member views are explicitly historical snapshots. Retain native units and source dependency; never sum overlapping views as physical inscriptions.

## Reconciliation-only checkpoint

Read `Linear-A/corpus-factory/RECONCILIATION-ONLY-2026-10-11.md`, `Linear-A/corpus-factory/fleet-enumeration-audit-v2.json` and the member `research/reference-reconciliation-v2.json`/`research/identity-reconciliation-v2.json` before certainty, apparatus or identity claims. Reading coverage is fixed. All 18 declared public native views have immutable enumeration snapshots; restricted A/B inventories remain unacquired. Treat missing primary uncertainty marks, damage notes and conditional alternatives as apparatus limitations of the digital reference. Unknown physical duplication and unresolved source disputes remain explicit. This supersedes earlier descriptions of the other 16 views as merely historical audit imports.

The supplementary Donnelly 2020 pp. 104–105 / Fig. 3 inspection confirms the already encoded Louvre AM 1639 attribution. The legacy probable status and Masson figure lineage are retained. A comparison with ADD##219 does not establish shared object identity; the numbered catalogue join remains absent and no occurrence is added. The native receipt/control is `research/donnelly-existing-assertion-check.json`.

## Integrity priorities before expansion

Read `Linear-A/corpus-factory/PRIORITY-REVIEW-2026-10-11.md` when planning subsequent corpus work. It distinguishes a confirmed apparatus-delivery gap, synchronization ordering risk, required shared-evidence safeguards and unresolved scholarly decisions. These are proposed fixes, not completed remediation or new scientific acceptance. Do not interpret absent CI on a generated sync head as a passed or failed source build.

Use `Linear-A/corpus-factory/PRE-EXPERT-EXIT-CRITERIA.md` to assess scoped pre-expert handoff readiness. Finish source acquisition/reconciliation and independent nonexpert repairs before final expert acceptance; do not relabel missing access, licensing or calibration data as an expert-only blocker.

## Published dependency and synchronization controls

Read `Linear-A/corpus-factory/DEFECT-REMEDIATION-2026-10-12.md` for the repair checkpoint superseding the proposed software fixes in the October 11 priority review. Use `Linear-A/corpus-factory/cross-corpus-dependencies.json` for the 15 known source-supported relationships restored from 17 published native projections. Screen record selections with `python Linear-A/corpus-factory/check_cross_corpus_dependencies.py --records repository::record-id ...`. Unknown relationships remain unknown; pooled physical-object counts, independent-witness counts and phonetic transfer are prohibited by this register. These are bounded source assertions, not physical certification or exhaustive discovery.

Generated native bundles and master starter downloads must be built and validated on their exact source parent. A changed main branch must skip or reject publication and trigger a rebuild; never rebase or force-push validated artifacts. Lydian, Sidetic and Pisidian use one guarded automatic publisher each. Read the native corpus authorities before any scientific claim. Source-access/permission, unresolved readings, independent review and Linear B calibration prerequisites remain explicit dependencies.

Consult `Linear-A/corpus-factory/defect-validation-2026-10-12.json` for the exact local validation scope and fingerprints. These receipts describe validation stages on named base commits; final published revisions require their own CI evidence.

## Mega corpus before final independent acceptance

Use `Linear-A/Linear-A/corpus-factory/MEGA-CORPUS.md`, `build_mega_corpus.py` and `query_mega_corpus.py` to materialize and inspect native corpus views across all 18 members. The initial package has 9,116 view rows, including private authenticated A/B source records; it is not 9,116 unique inscriptions or a globally complete corpus. Original source fields, uncertainty, apparatus context and component terms travel with the rows. Native corpora remain authoritative. Preserve restricted payloads locally; do not infer a combined redistribution license, physical identity or independent witnesses. Continue lawful native coverage growth before final expert acceptance.

Linear B's `analysis/calibration-prepared-inputs-2026-10-12.json` reports real prepared observations: 5,932 documents, 5,890 nonempty transliteration surfaces and 42 missing/empty ones. Source word-ID crosswalks, linked linguistic annotations and source-certified graphical occurrences remain missing. `docs/CALIBRATION-PREPARED-INPUTS.md` and `research/calibration-acquisition-2026-10-12.json` distinguish preparation from gold delivery. Corpus expansion can continue while calibration is blocked. Do not replace occurrence gold with generated lexical analyses or expose the mixed mega-corpus interpretation layers to a blinded run.

## Full dossier and geographic discovery views

Read `Linear-A/corpus-factory/COVERAGE-EXPANSION-2026-10-12.md` for Anatolian and Cypriot expansion questions. Query the 287 Anatolian dossier entries with their source bibliography and uncertainty. Keep the 210 Cypriot legacy squeeze identifiers separate from the 592 parsed digital-edition entries and Greek admission/frequency populations. Preserve cast/fragment labels and unknown language/object joins. Do not turn the package's 9,562 mixed rows into a unique-inscription or independent-witness total.

## Source delivery before expert review

Use `Linear-A/corpus-factory/SOURCE-DELIVERY-2026-10-12.md` and its worklist for Raison–Pope, Dunand and Linear B input acquisition. Keep lawful access, source delivery, component permissions, exact alignment and scholarly acceptance separate. Respect native restrictions; preserve routing uncertainty and drafted-versus-sent status. No missing-source payload or permission was acquired by this checkpoint. Follow native intake checks before inspecting calibration answers.


## lineara.xyz: secondary reference and GORILA rights boundary

Checked 2026-10-12. [Linear A Explorer](https://lineara.xyz/) and its [maintainer README](https://github.com/mwenge/lineara.xyz#readme) are attributed secondary discovery resources. The README identifies GORILA-derived images, George Douros's transcription spreadsheet, and John Younger's commentary as inputs. This is the maintainer's provenance description, not our independent verification of each displayed reading.

**This project does not have permission to redistribute GORILA images, transcriptions, or structured derivatives.** The project-specific EFA/GORILA refusal remains in force. Public access through lineara.xyz or GitHub does not grant this project reuse rights. This reference grants no third-party rights and does not assert that the external site's use is unauthorized.

Use links, inscription identifiers, bibliographic leads, and attributed research questions. Do not harvest or bundle the site's GORILA-derived images, text, or machine-readable corpus, or reconstruct restricted material indirectly. Do not treat a downstream copy as an independent edition, witness, calibration gold, or expert validation. Missing provenance means unresolved source attribution; proposed translations remain hypotheses, not established decipherment.

SigLA's separately documented component licence remains component-specific; this notice neither expands nor revokes that licence. No external inscription payload or image is included with this reference.

Read `docs/LINEARA-XYZ-REFERENCE.md` for the source and rights boundary.


## Available source layers — 2026-10-12

Read `Linear-A/corpus-factory/AVAILABLE-EVIDENCE-GROWTH-2026-10-12.md`. The earlier verified package contains 10,527 mixed view rows across 18 members; earlier 9,562/9,116 totals describe historical packages. Added views: 802 dependent SigLA layout documents (5,144 source rectangles), two KN Fp 13 museum assertions, and Byblos 123 ordinal reviews plus 38 type-table rows. Preserve source coordinate units, the unresolved HT 6a exporter difference, modern cast status, source chronology, unassigned/competing types, false admission flags and component rights. These additions grant no new reading, independent witness, calibration result or expert acceptance.


## CH/CM source growth — 2026-10-12

Read `Linear-A/corpus-factory/CH-CM-SOURCE-GROWTH-2026-10-12.md` and each member’s source-growth guide and audit. The current package contains 10,759 mixed view rows; earlier totals are historical. CH has 193 dependent DBAS catalogue leads, a 204/331 named-route union, 26 existing context rows, and three unmapped INSCRIBE pages. Script dashes, motif comparisons and CHIC sign numbers are not catalogue/object identifications. CM has nine exact Louvre inventory/edition assertions and primary Tiryns context; TN 241 is a Tracing Networks database ID and footnote 3 is separate. Preserve damage versus identification certainty, source units/qualifiers, publication dates and rights. No new readings, physical witnesses, glyph adjudication or expert acceptance.

For the Tiryns primary context, preserve appendix `3 (?) signs`, its 8–9 mm sign-height range, and the unresolved main-description VB / appendix VC coordinate difference with printed/PDF locators. No certainty or coordinate correction is admitted.

## Cretan Hieroglyphic H/Y primary frontier — 2026-10-13
Read `Linear-A/corpus-factory/CH-HY-FRONTIER-2026-10-13.md` and the member’s `docs/HY-FRONTIER-2026-10-13.md` plus native registers/receipt. Report the former 127-route gap (114 H, 13 Y) as closed for historical primary catalogue contexts: the three-route union is 331/331 identities, while the earlier two-route union remains 204. Canonical coverage stays 13 versions on six entries, 325 without encoded readings, and zero independent reviews. Preserve CHIC-331 unknown holding/angle brackets, historical-versus-current museum status, Vrysinas proposed identifications/alternatives and primary visual-collation limits, and the two CMS script dashes. Keep post-1996 candidates outside the CHIC spine and do not infer independent witnesses, whole-corpus completeness or expert-only readiness. The 127-row supplement is not yet included in a rebuilt mega-corpus; do not revise its historical row total by addition.

## Current CM coverage and LB freeze controls — 2026-10-14
Read `Linear-A/corpus-factory/CM-LB-PROGRESS-2026-10-14.md` and both native guides/registers. CM now has 26 source assertions on 12/21 rich records: six primary, twenty dependent; nine remain unencoded. Ten source-qualified positions on existing CMOC-0028/0032/0033 preserve the old sixteen and add no independent witness, physical certification or expert acceptance. Prefer this dated checkpoint over historical 16-on-nine summaries. Keep the 254 catalogue slots separate and all apparatus/primary-colllation limits explicit.

For LB, use `scripts/freeze_calibration_run.py` only for private exactly aligned inputs outside the repository. A hash-bound pre-reveal receipt does not verify prediction/scoring semantics, chronology, source authority or rights, and does not authorize answer reveal or calibration. Nine synthetic controls are software tests, not linguistic gold. DĀMOS/LiBER/CaLiBRA About availability is distinct from linked annotations or certified graphics. Calibration remains unexecuted; source-delivery requests remain unsent.

## CMOC-0209 bounded source check — 2026-10-14

Read `Linear-A/corpus-factory/CM209-SOURCE-CHECK-2026-10-14.md` and the member’s native register, guide and reconciliation. Current CM coverage is 28 assertions on 13/21 rich records, eight without encoded positions. Two isolated positions only; retain the uncertain 10 proposal, reported originals and unresolved internal 09/10 discrepancy. Do not admit either conflicting label, infer complete-tablet coverage, independent witnesses, primary collation or expert acceptance. Earlier dated counts remain historical; corpus-wide inference remains blocked.

## Inputs and primary reconciliation — 14 October 2026

Read `Linear-A/corpus-factory/INPUTS-AND-RECONCILIATION-2026-10-14.md` and the three native checkpoint registers/guides. Linear B has a published appendix ID example only (one item, seven units: five lexical words, one logogram, one numeral); same-snapshot crosswalk, annotations and graphical certification remain undelivered. Milyan TL55 eight is Texier quoted by Kalinka, whose printed transliteration has nine entry groups; preserve boundary differences and unchanged114 source rows without physical-line/full-reading acceptance. Byblos drawing categories partition123 as119+3+1; retain literal 32 collision, eight gaps and unadopted32/92 hypothesis. No ancient-loss certification, expert acceptance or calibration. Current CM209 checkpoint is unchanged.

## Queryable Linear A critical evidence

For Linear A pilot evidence or competing-reading questions, read `docs/CRITICAL-EVIDENCE-QUERIES.md` and `analysis/critical-evidence-coverage-v1.json`. Use `python scripts/query_critical_evidence.py --record 'HT 17'` (exact native ID) or `--coverage`. Keep source witness fields, attributed assertions and legacy queue labels separate. Cite assertion/case IDs, source locators and the input hash. Do not describe legacy alternatives as two attributed scholarly readings: no such pair is collated in this pilot. Report the five unjoined cases separately from the ten joined cases; an interpretation-only case is not an inscription. Absence from this bounded pilot does not mean absence from the corpus. Preserve all uncertainty, source dependence, mixed rights and unreviewed states. These capabilities and counts apply only to Linear A; route other corpora through their own evidence models.

## Native evidence queries across all members

Read `Linear-A/corpus-factory/EVIDENCE-AND-ALTERNATIVES.md` and `Linear-A/corpus-factory/evidence-query-rollout.json` when tracing evidence or alternative readings. Route each member through its registered `evidence_query_profile_path`, `evidence_query_coverage_path` and `evidence_query_guide_path`. Use exact native IDs and collection names; preserve whole source records, source locators, uncertainty, inspection state, component rights and language partitions. Explicit ID links establish declared editorial associations only. Do not apply all corpus-level registers to every record, equate untraced labels with attributed readings, or count catalogue entries as collated inscriptions. Keep all native view counts separate. Alternative-pair and independent-witness metrics remain unknown in these query reports; consult qualified native comparison records for their actual scope. The 18-member rollout is an engineering capability over existing evidence, not new collation or expert acceptance. Egyptian Hieroglyphic Corpus and LightroomIsSlow remain outside this language-corpus membership.

## Milyan Schürr2005 bounded collation

Read `Linear-A/corpus-factory/MILYAN-SCHUERR2005-COLLATION.md` and the native register/qualified view. The PDF is now acquired; nine source labels and six selected issues are located, not completely collated or accepted. Preserve alternative/doubtful readings, emendation versus graphic evidence, source row-boundary allocations, and the distinction between revised transcription and poetic reconstruction. `research_api.py collation` exposes nine qualified reference rows; rows without selected issues have not passed full collation. All114 source strings and zero verified canonical readings remain unchanged. Qualified reference data and comparison annotations retain CC-BY-SA-4.0; source article/images are excluded and not relicensed. PDF extraction and unattributed overlays are not authorities. No new independent witness, expert review or bulk reuse permission.


## TL55 first-pass coverage and expert handoff

Milyan’s `research/tl55-first-pass-review.json` records the completed first documentary comparison pass for all9 revised lines and74 apparatus entries, numbered7,10,11,10,13,10,5,6,2 within source lines. Four literal digital break markers occur in rows2,4,7,8. The qualified query exposes exhaustive literal span accounting and attributed apparatus review notes. Six selected issue dossiers are not the total discrepancy count. Preserve all114 source rows and every uncertainty/alternative; no canonical reading is promoted.

Read `review/tl55-independent-review.json`: PREPARED_NOT_REVIEWED, null reviewer/assessment, zero accepted readings. Complete first-pass coverage does not establish complete sign-by-sign epigraphic collation, expert adjudication, full-article interpretation, physical-line certification or independent evidence. Never close expert review with an AI-generated assessment, automated validation or the source publication itself. Native checks protect input hashes, all74 entry identities, all4 markers and the unperformed review state. Source PDF/images and full modern edition remain excluded; original notes and qualified reference context retain component licensing. Full critical collation and external adjudication remain open.

## Linear A legacy-case attribution audit

For U001–U009 and U011, load `research/legacy-case-attribution.json`, its pinned search log and `docs/LEGACY-CASE-ATTRIBUTION.md`. Treat this audit as the current qualification of unsupported claims in the unchanged RC2, visual-evidence and branch registers. Report the bounded pass as complete, with all ten scholarly cases still open: three published contexts are not three recovered alternative pairs. Do not call the HT17 37/38 case a verified SigLA numerical conflict; sign-number37 is not an account quantity. Keep KH8 A567 and A510 at their distinct source slots until the disputed locus is established. The identified Consani passage does not establish the full MA10b pair; Flouda’s punctuation report does not establish the queued before-IZU lexical split or independent physical adjudication. Preserve every legacy literal, source dependence, consultation limit and remaining gap; never infer a source because another project register repeats the claim. Use `legacy_case_attribution.py --case U008` or the native `attribution-audit` collection for the case assessment. No new GORILA data, canonical reading, expert review or source-collated competing pair is admitted by this pass.

## Corpus-wide bounded attribution review

All18 registered members expose `research/attribution-review.json`, `analysis/attribution-review-audit.json`, `docs/ATTRIBUTION-REVIEW.md` and `scripts/attribution_review.py`. Consult the member’s case query and exact pinned evidence before claiming an alternative reading. The238 review tasks include classification, counts, identity, source role, representation, interpretations and apparatus notes; they are not238 scholarly pairs or objects. This pass reviews existing repository packets, not sources afresh. Inherit their author/publication, locus, consultation limits, source dependence and current gaps; keep missing evidence unknown. Read `Linear-A/corpus-factory/ATTRIBUTION-REVIEW.md` and the member-specific scope. Do not claim new readings, autopsy, independent review, source independence or literature completeness.

## Four-corpus selected publication checks (2026-10-15)

Consult `Linear-A/corpus-factory/FOUR-CORPUS-SOURCE-COLLATION-2026-10-15.md` for the17 selected Cypro-Minoan, Lydian, Sidetic and Pisidian follow-ups. Route to the member’s `research/source-collation-2026-10-15.json` and `scripts/source_collation.py --case ID` before using those comparisons. Separate printed forms from project-added notation and author-prose uncertainty; distinguish rendered PDFs, web text, indirect reports and bibliographic routes. In Sidetic, use printed ewpel with its prose qualifications; preserve the earlier project underdots only as correction history. Do not turn integrity success into reading acceptance, author autopsy into project autopsy, or the17 follow-ups into17 new objects. Preserve the stated acquisition and adjudication gaps.


## Milyan TL55 exhaustive encoded-sign comparison

Read native `research/tl55-sign-alignment.json`, `docs/TL55-SIGN-COMPARISON.md` and `review/tl55-sign-adjudication.json`. All1348 literal reference grapheme/notation units and1233 printed source-unit positions are accounted for across nine source labels in1441 candidate alignment records. The36 ambiguous records overlap relation categories; the152 pending triage items are not152 proven errors, alternative scholarly reading pairs or witnesses. Mixed print/notation units must not become counts of ancient signs.

Use native `python scripts/research_api.py signs --text TL55-L2-A087` for exact reference offsets, source page/PDF bounding boxes, uncertainty and comparison method. Public validation checks exact frozen inputs and exhaustive accounting; optional `tl55_sign_alignment.py --pdf PATH` replays the exact lawfully held PDF with the declared font mapping and optimal-path alignment. These are same-method checks, not independent scholarly review. No stored reference normalization; comparison-only NFC and chi/x conventions do not establish literal equality. Preserve the explicit alternative, every underdot/underlined colon, opaque editorial entities, wrap hyphens, vacat and ambiguous partner status.

The encoded-sign comparison layer is complete in coverage; full epigraphic certification, expert adjudication and broader modern-edition reuse remain open. Original first-pass and six-issue packets stay historical checkpoints; the current supplement has null reviewer/assessment and zero accepted readings. Do not turn automated agreement into a canonical correction, lexical claim, independent witness or expert acceptance. The PDF, source images and full modern transcription remain outside GitHub; all114 frozen reference rows and canonical zero are unchanged.


## TL55 documentary comparison completed

The Milyan bounded documentary sign-comparison task is COMPLETE: all1441 encoded records remain accounted for and all152 flagged records have58 source-located documentary assessments in native `research/tl55-documentary-sign-review.json`. Read `docs/TL55-DOCUMENTARY-COMPLETION.md`. The36 original ambiguity flags remain immutable:19 have positional/notation explanations,2 have repeated-run correspondence and15 remain range-only. These are candidate-record counts, not resolved ancient signs, readings, objects or independent witnesses. No flagged record lacks a documentary disposition.

Use native `research_api.py sign-review --text TL55-REVIEW-55` for notes, exact reference literals, source-position coordinates, input hashes and rights. `signs` retains original candidate flags with the documentary overlay attached. `tl55_documentary_review.py` checks exact coverage and no acceptance; optional `--pdf PATH` verifies the exact source and preferred placeholder/delimiter/run correspondences. Mapping a proposed letter to an unknown slot does not validate the restoration. Do not pick a unique letter from a repeated run or damaged range when the evidence supplies only a range comparison.

This closes documentary work for the revised TL55 transcription/apparatus under the stated provisional source-label allocation. It does not close independent expert adjudication, epigraphic/physical-line certification, monument autopsy, full-article lexical/poetic interpretation, TL44 source work or source rights. The original152-item expert packet stays PREPARED_NOT_REVIEWED; all114 frozen reference rows and canonical zero remain unchanged.


## Milyan TL44 source checkpoint

Read `Linear-A/corpus-factory/MILYAN-TL44-SOURCE-CHECKPOINT.md` and native `research/tl44-source-checkpoint.json`. Two DOI identities are confirmed; both modern PDFs remain unacquired. Keep North2016 and West2018 print years distinct from platform dates, and retain West55–105/55–106 pagination conflict pending actual PDF inspection. All105 existing TL44 digital rows have proposed Kalinka label/page routes, not105 sign collations or certified physical lines. Preserve the c64/65 carryover, West page boundary and separately unplaced fragments. The three observations are bounded, not an exhaustive disagreement count. Native `tl44_source_checkpoint.py` and evidence collections expose exact IDs/hashes/limits. All114 frozen rows, canonical zero and completed bounded TL55 documentary work remain unchanged; no independent review, source independence or bulk modern reuse grant follows.


## Lydian/Sidetic supplied-PDF follow-up — 2026-10-15

The current four-corpus source-collation guide and native packets supersede their earlier web-only acquisition gaps for Payne–Sasseville2016, Phillips–Rutherford2025 and Rizza–Zinko2025. All three now have supplied-PDF byte and visual page receipts. Attribute LW40’s ẹšν̣ tasẽν̣ acνil / partaras maλiλ to its edition; preserve initial-e and final-ν underdots and distinguish the plain ẽ tilde. For Sidetic, retain the qualified Abydos w(?), source-specific N22 a/a2/V labels, bracketed pigbe[s], and the distinction between provisional N02 u2 and N22 V. These close selected publication checks, not physical-sign adjudication, independent review or whole-corpus completion. The17 selected tasks remain17, with44 page inspections including one blank leaf; no new object count follows. Supplied PDFs/images are not included in public bundles.

## Software P0 audit evidence

Read `Linear-A/corpus-factory/P0-REAUDIT-2026-10-16.md` and its revision-bound `p0-validation-2026-10-16.json` before citing the 2026-10-16 software audit. Preserve its scoped exclusions. Revalidate changed authorities; never infer scientific acceptance, resolved permissions, or independent review from passing software checks or an empty issue search.

## Current P1 execution and evidence limits

Consult `Linear-A/corpus-factory/P1-EXECUTION-2026-10-16.md`, `Linear-A/corpus-factory/p1-current-work.json` and each member's revision-bound `current_evidence` in the fleet gap register for current work. Treat the18-member status refresh as completed, while preserving the explicitly open source/identity/edition and independent-review requirements. Retrieve the new Phrygian, Eteocypriot and Sidetic native `p1-source-followup` dispositions before using their affected records. Do not repeat completed TL55 documentary accounting or supplied-PDF typography checks as missing work. Do not turn new documentary task/page counts into objects, independent witnesses or accepted readings.

## Route residual P1s to human validation

Use `Linear-A/corpus-factory/HUMAN-VALIDATION-ROUTE.md` and the revision-bound `Linear-A/corpus-factory/p1-human-readiness.json` to distinguish acquisition/permission prerequisites, source-editor or catalogue clarification, enforced policy controls and independent epigraphic judgment. Follow each native acceptance gate. Prepared requests and documentary/software checks are not human validation. TL44 now has105-row/199-code-point-span accounting and47 qualified historical boundary contexts; c40 exceptional routing, damage/editorial distinctions and page/column transitions remain explicit. Do not infer accepted readings, unique sign alignment, independent witnesses, completed modern-edition collation or whole-corpus human-only readiness.


## Competing Abydos editions — 2026-10-16

Read `Linear-A/corpus-factory/SIDETIC-ABYDOS-EDITION-COMPARISON-2026-10-16.md` and the current Sidetic source-collation packet. The supplied Ferrer–Soler–Adiego2025 PDF closes the selected two-edition documentary comparison; Pojau / final u, qualified w(?) and possible overwriting remain attributed alternatives, not an adopted reading. Preserve j/y source conventions, N02/new-u versus N22, separate S9 identity, initial submissions versus final-article dependence, and first-graffito-only revised scope. Same17 selected tasks, now49 logged page inspections, one historical blank-leaf inspection included; no objects, independent reviews or accepted readings added. Fuller new-vowel source comparison and physical adjudication remain separate work.

## Full-collection research delivery and review

Read `Linear-A/corpus-factory/NORTHWESTERN-RESEARCH-PROGRAM.md` for the seven P0/P1
controls and their limits. Run `Linear-A/corpus-factory/federated_research.py` against
all registered local checkouts for exact-ID or literal-text retrieval, a live
byte-bound audit, or the five exercises. Load each member's native dossier and
individual skill before analysis; preserve repository/collection/ID namespaces,
source categories, uncertainty, source dependence and rights. Never count mixed
views as unique inscriptions or independent witnesses. Use native
`scripts/research_delivery.py` to produce evidence-only responses, local replay
packages and source-bound review drafts. Do not treat deterministic response
checks as empirical LLM evaluation, a complete form as authenticated expert
review, or delivery controls as closure of scholarly P0/P1 source/permission gaps.

## Specialist research-task pilots

Read `Linear-A/corpus-factory/SPECIALIST-RESEARCH-PILOTS.md` and each native `docs/RESEARCH-TASK-PILOT.md` / `analysis/task-pilot-example.json`. Route Linear B to its 25-record literal retrieval with a character-marker sensitivity screen, Linear A to its 25-entry exact source-label/group concordance, and Luwian to seven documentary edition routes. Do not call the Luwian sign-reading study executed or Linear B literal matches identified people/secure readings. Preserve all local-only payload defaults, component rights, unknowns, raw flags and source/physical/edition distinctions. Do not pool pilot counts or imply named scholar participation, endorsement, model evaluation or human acceptance. Require admitted source/linguistic evidence before interpretation.


For the 2026-10-17 Linear B, Linear A and Anatolian Hieroglyphic source studies, first read `Linear-A/corpus-factory/SOURCE-STUDIES-2026-10-17.md`, then the member-native source-study register and review packet. Keep documentary identity, script classification and attributed reading-level assertions distinct. Prepared specialist packets do not establish expert acceptance.


## Three-source acquisition status — 2026-10-18

Read `Linear-A/corpus-factory/THREE-SOURCE-FOLLOWUP-2026-10-18.md` and `Linear-A/corpus-factory/source-intake-2026-10-18.json`. The Ferrer PDF is acquired:22 rendered pages and all33 appendix lines/groups have a bounded direct comparison; Brixhe–Neumann and Olivier original checks remain open. Route to the native intake packets for partial consultation, corrected identity and remaining delivery requirements; do not count acquisition tasks as objects or pool them with the17 earlier comparisons. The joint Brixhe–Neumann1988 article is DOI10.1515/kadmos-1988-0105;0108 is a different Neumann article. Preserve deposited metadata versus original-page inspection and prepared versus sent requests. No global sign/numbering normalization, accepted reading or expert review follows.


For the2026-10-18 source follow-up, read `Linear-A/corpus-factory/SOURCE-FOLLOWUP-AND-REVIEW-2026-10-18.md`. Route to the member’s `research/review-exercise-2026-10-18.json` and exact native target. Distinguish a PKZb21 text-rendition contrast from full-word/page collation and Luwian reference candidates from exact reading joins. Never present a teaching example as human review.

## Current page and supplied-file checks

Read `Linear-A/corpus-factory/SOURCE-PAGE-CHECKPOINT-2026-10-18.md` and each member’s `source_page_check_path` before current source-access claims. One selected Peker section is located; Hawkins2000 is not directly inspected. PK Zb21 original pages and the linked DĀMOS annotation package remain undelivered. Do not turn a catalogue heading, HTTP200 HTML, supplied flat document file or unsent request into completed source review.

## Public visual and document source routes

Read `Linear-A/corpus-factory/PUBLIC-SOURCE-ROUTES-2026-10-19.md` and the native `public_source_route_path` registers. Treat Gelb page/plate records as presentations, not objects; preserve his limited Gürün collation. Physical line3 is not clause§3b. Hosted editorial drawings do not establish full-edition consultation. Two DĀMOS public responses for4307 supply no linked annotation package; do not generalize that negative result to every possible route or the internal database. Preserve source-specific rights and all unresolved original-page/word-crosswalk gates.

## Direct Ferrer PDF follow-up

Read the current three-source guide and native `research/ferrer2025-pdf-comparison-2026-10-18.json` before answering source-access or appendix questions. Preserve discussion/final sign conventions, directory S11 versus Ferrer S13 and questioned letters. The33 notes do not constitute exact diplomatic encoding, independent witnesses or expert acceptance. The master refresh block has cleared; two original-source acquisition tasks remain open.

## Selected Ferrer assertions (2026-10-19)

Route to Sidetic collection `ferrer2025-reading-assertions` and `docs/FERRER2025-READING-ASSERTIONS.md` for six attributed names on four source lines and three directory targets. Retrieve both the source display and literal earlier reading, retain uncertainty and one shared edition dependence group. No new object, source acquisition, accepted reading or expert review is implied. The current three-source guide records the publication-bound follow-up.


## Validity and sanity audit routing — 20 October 2026

Read `Linear-A/corpus-factory/VALIDITY-AUDIT-2026-10-20.md` and its revision-bound receipt before citing this audit. Treat its 163-command replay and 1,095 matching artifact entries as bounded engineering evidence. Do not infer comprehensive source verification, empirical AI accuracy, executed calibration or independent expert acceptance. Resolve current readiness per native task and evidence layer; source acquisition/collation remains separate from expert judgment.


## Current coverage and readiness entry point

Read `Linear-A/corpus-factory/CURRENT-READINESS.md` and its pinned `readiness-snapshot.json` before collection-wide coverage or handoff claims. Run `python Linear-A/corpus-factory/readiness_overview.py --check` to check the committed projection; this is offline integrity validation, not a live freshness check. Keep native catalogue, reading, comparison and accepted-review units distinct. A missing status field means unknown or differently scoped, never zero or automatic completion. Current native authorities supersede the pinned overview when newer evidence is available.


## Keep frozen native replay checkpoints coherent

When a native adapter or skill-bound delivery input changes, refresh the exact
source revisions and saved federation/exercise receipts together. Run
`Linear-A/corpus-factory/verify_federated_snapshot.py --checkouts DIRECTORY` on those exact
checkouts before citing the frozen replay. Use `Linear-A/corpus-factory/AI-SKILL-VALIDATION-2026-10-20.md`
for the 19-skill audit and the synchronization repair. Do not describe a local
pass as a hosted workflow result; use its exact published revision and job status.
