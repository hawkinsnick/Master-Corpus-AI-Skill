# Researcher's user guide: from question to inspectable evidence

Use the Corpus AI to assemble, question and document evidence for a research argument. Start with a narrow question, supply the relevant corpus files, and ask for an auditable result. You remain responsible for source consultation, philological judgment and the argument you submit.

**Start without programming:** download the starter, select one corpus, upload a small evidence packet, and use the first-session prompt below. A GitHub URL alone does not give every AI assistant access to the repository.

## Contents

- [What you receive](#what-you-receive)
- [Set up your first session](#set-up-your-first-session)
- [Work through a research question](#work-through-a-research-question)
- [Examples for your corpus](#examples-for-your-corpus)
- [Optional reproducible retrieval](#optional-reproducible-retrieval)
- [Check and cite the result](#check-and-cite-the-result)
- [Updates and troubleshooting](#updates-and-troubleshooting)

## What you receive

The master coordinates 18 registered corpus projects. It directs the assistant to the individual skill, source authorities and evidence model for your material. It can help identify records, trace assertions, separate editions from witnesses, design comparisons and prepare reproducible research packets. It does not contain all native inscription data.

| Material | Purpose | What it does not supply |
|---|---|---|
| [Master starter](downloads/Master-Corpus-AI-Skill-Starter.txt) | Instructions, member routing and a saved status snapshot | Native inscription evidence or a live connection |
| [Individual corpus skill](CORPUS-DOWNLOADS.md) | Rules and workflows specific to your material | Proof of a reading or access to every source |
| Native evidence files | Inspectable records, recorded assertions and provenance | Automatic authentication of physical objects |
| [Executed walkthroughs](WORKED-EXAMPLES.md) | Saved, reproducible demonstrations with reported results | Current results for a later repository revision |
| [Research examples](RESEARCH-EXAMPLES.md) | Research designs and prompts for every member | Completed studies, new readings or tested model accuracy |

Egyptian Hieroglyphic Corpus remains an independent project outside these 18 members. The Phaistos Disc and Aegean Anomalous repositories describe research objects or groupings; registry membership does not establish a language identity.

## Set up your first session

### 1. Obtain the instructions

Open the [starter text](downloads/Master-Corpus-AI-Skill-Starter.txt). Use GitHub's raw/download control to save the text file, then attach it to an AI assistant that accepts text files. Alternatively, copy its text into the conversation. Interface names and upload limits depend on your AI service. This workflow provides context; it does not install a plugin or promise identical behavior across models.

For a repository-aware assistant, provide this repository and ask it to read `SKILL.md`, `manifest.json`, the member registry and the current member status. Have it confirm the files it actually opened.

### 2. Choose one research question and one corpus

Open the [corpus directory](CORPUS-DOWNLOADS.md), select the relevant repository and download its ZIP or the selected files. Extract a ZIP before selecting uploads. Start with one inscription, one alleged editorial disagreement or one tightly defined sample. You can expand after the first retrieval is correct.

### 3. Supply a small evidence packet

Use the selected member's registry entry to locate its `individual_skill_path`, `authority_profile_path` and `bundle_index_path`. Paths are relative to that member's repository, not the master. Normally these are:

```text
ai-skill/SKILL.md
ai-skill/references/authority-profile.json
ai-skill/generated/research-bundle-index.json
```

Add its current source/rights guidance and the exact evidence files required by the question. The index helps identify those files; it is not their contents. When the packet references additional files, supply them before asking the assistant to use their evidence. Preserve original filenames and repository paths in a short attachment list if the upload interface renames files.

If you cannot identify the evidence files, upload the individual skill, authority profile and index first. Ask the assistant to name the specific indexed files needed and explain why; then supply those files before analysis. For a bilingual monument, begin with the native record for that monument. A Greek component does not automatically require a second corpus repository.

If your assistant has permitted repository access, it can read the selected files there instead. Ask it to record a full commit SHA and keep the session at that revision. For a private or restricted source, establish permitted use before uploading it to a third-party AI service; possession of a PDF is not a new license.

### 4. Copy this first-session prompt

```text
Use the attached Master Corpus AI instructions and the individual corpus skill.
My research question is: [one precise question].
My selected corpus is: [repository].
My evidence packet contains: [filenames and original repository paths].

First list what you can actually read and what is missing. Identify the native
collection, record IDs, source revision and unit of analysis. Check whether
this packet can address my question. If you cannot run a validator, say so;
do not report a software pass from reading a receipt.

Retrieve one relevant record before proposing an interpretation. Preserve
source text, editorial notation, attribution, rights, source locator, path,
pointer and hash where supplied. Separate observation, recorded scholarly
interpretation, computation and your own inference. Do not fill missing fields.
End with the next evidence-based step I should take.
```

A useful first response may say that an edition, image or sample definition is missing. Request that item or narrow the question before proceeding.

## Work through a research question

### Stage 1: make the claim testable

Ask: “Restate my question as a falsifiable claim. Specify the observational unit, candidate population, exclusions, rival explanations and evidence needed to distinguish them. Mark which inputs are currently available.”

For example, “Are these sequences word endings?” is too broad when segmentation is uncertain. A tractable first task is to ask whether recorded terminal positions differ from internal positions under explicitly stated segmentation rules. A distributional result still does not identify a morpheme.

### Stage 2: build an evidence table

Ask for one row per source assertion or observation, using the native units rather than a generic inscription count:

| Required column | Why it matters |
|---|---|
| Repository, collection and native ID | Prevents collisions between corpora |
| Full commit, path, pointer/locus and hash | Makes the retrieved bytes traceable |
| Source author, edition and supplied locator | Connects the assertion to scholarship |
| Diplomatic/source representation | Preserves what was actually recorded |
| Normalized/restored representation, separately | Exposes editorial intervention |
| Evidence category and uncertainty | Keeps interpretation distinct from observation |
| Witness/source dependence | Prevents duplicate editions becoming extra evidence |
| Rights and attribution | Supports lawful citation and reuse |

Treat columns as a requested reporting schema. Native corpora may not expose every field. Use `not supplied` or `not inspected` rather than inventing a page, hash, line number or source relationship.

### Stage 3: agree on a method before calculating

Ask the assistant to write a short analysis plan before seeing or optimizing a result: inclusion rules; treatment of damage, restoration and blanks; deduplication policy; denominator; contrasts; and sensitivity analyses. If statistical inference is appropriate, specify the null model and the independent sampling unit. Sign slots within one text are not automatically independent observations. Small, selected or dependent samples may support only descriptive analysis.

The master retrieves evidence; custom statistical analysis requires separately supplied data and an executable method. Request code and input manifests, execute them in an appropriate environment, and inspect the output. If execution is unavailable, the response must remain a proposed analysis, without invented numerical results.

### Stage 4: challenge the result

Copy this follow-up:

```text
Audit the strongest claim in this result. Which source dependence, selection,
restoration, transcription, dating or segmentation choices could produce it?
Show the result with disputed/restored items excluded, if the data and execution
are available. Distinguish 'not retrieved' from 'not attested'. List the evidence
that would falsify the claim. Reduce the claim if the current packet cannot
support it. Do not treat software validation as expert acceptance.
```

### Stage 5: prepare something a colleague can inspect

Request a packet containing the research question, input manifest, evidence table, analysis plan/code, executed results or explicit non-execution statement, sensitivity analysis, unresolved source issues and a short interpretation. Ask for a draft methods paragraph grounded only in that packet. Check every citation and relevant primary source before using it in a publication.

## Examples for your corpus

The [research example collection](RESEARCH-EXAMPLES.md) supplies a focused problem and copyable research prompt for all 18 repositories. Each specifies required evidence, a practical sequence of tasks, a deliverable and a boundary on interpretation. These are proposed research exercises, not claims that the required samples are complete or that their analyses have been executed.

For questions spanning projects, follow [the cross-corpus walkthroughs](CROSS-CORPUS-EXAMPLES.md). They show which files to supply, what to ask first, how to compare the evidence and what to save for each of five concrete research questions.

For frozen cross-project study outputs, source-trace checks and a scored AI development pilot, read [Research results](RESEARCH-RESULTS.md).

For a first exercise with saved results, use [ARKH 1a, U008 and reproducible source-view counting](WORKED-EXAMPLES.md). Those examples identify the teaching snapshot, expected results and source limitations.

## Optional reproducible retrieval

Python is optional for reading and discussing a small uploaded packet. Use this route when you want machine-readable retrieval and software checks.

Download and extract this master repository and the selected native repository. Place native repositories in a common parent directory, retaining each repository's name. The query tools verify Git remote identity, so **use Git clones for native checkouts**, not extracted ZIP folders. A colleague or research computing service can prepare these. For example:

```sh
git clone https://github.com/hawkinsnick/Master-Corpus-AI-Skill.git
git clone https://github.com/hawkinsnick/Linear-A.git corpora/Linear-A
cd Master-Corpus-AI-Skill
python scripts/validate.py --require-canonical
python scripts/query.py --checkouts ../corpora --repository hawkinsnick/Linear-A --coverage --output coverage.json
python scripts/query.py --checkouts ../corpora --repository hawkinsnick/Linear-A --id "ARKH 1a" --collection source-documents --output arkh-evidence.json
```

Use Python 3.10 or later and Git. If your Python command is `python3` or `py`, substitute it. Run from the master repository directory. The coverage output discovers native views; exact lookups require both repository and collection. Open the JSON output in a text editor or attach it to your AI conversation. These commands retrieve a source entry; they do not translate Linear A.

For another corpus, clone its repository under its own name and run coverage first. For example, after cloning `https://github.com/hawkinsnick/Eteocypriot.git` into `corpora/Eteocypriot` alongside the master:

```sh
python scripts/query.py --checkouts ../corpora --repository hawkinsnick/Eteocypriot --coverage --output eteocypriot-coverage.json
```

Use the returned collection names and identifiers from actual native records for your next exact lookup; do not substitute a guessed collection or inscription ID.

To search the selected native research view:

```sh
python scripts/query.py --checkouts ../corpora --repository hawkinsnick/Linear-A --search "ARKH" --limit 10 --output search.json
```

Search is literal retrieval over the supported view, not a linguistic search engine or exhaustive bibliography. Check `truncated`; inspect full relevant inputs before deriving a denominator. A full cross-member search or `validate.py --checkouts ../corpora` requires all 18 native clones. Selected-repository queries require only that member. Query-time validation checks the local checkout, not that it is the latest remote revision or the master's accepted checkpoint. The accepted member revision, a bundle's source revision and a historical teaching checkpoint can differ. They describe different stages, so retain each label rather than treating their SHAs as interchangeable. Record the local checkout's actual SHA with `git -C ../corpora/Linear-A rev-parse HEAD` and compare with [member status](MEMBER-STATUS.md).

## Check and cite the result

Before using an answer, open its cited records yourself. Confirm that a quoted reading occurs at the cited locus, that a computed denominator matches the defined sample, and that several rows have not silently become several independent objects. Unavailable originals must remain unavailable in the report.

Use the following research log with the [expert review guide](EXPERT-REVIEW.md):

```text
Research question and hypothesis:
Corpus repository/collection and full commit SHA:
Native record IDs and unit of analysis:
Files inspected, paths, supplied hashes and pointers/loci:
Source authors, publication/edition and verified locators:
Files or sources not accessible:
Inclusion, exclusion, restoration and deduplication rules:
Analysis code/version and execution status:
Results, denominators, uncertainty and sensitivity checks:
Source/witness dependence and unresolved issues:
Rights, required attribution and material reproduced:
AI service/model identifier as displayed, date, prompts and human corrections:
Human source checks and outstanding expert questions:
```

Cite the underlying scholarly sources for scholarly assertions, and the exact repository revision and files for your dataset/method. A JSON array index is not a publication page or ancient line number. If you have consulted only a derivative record, disclose that rather than implying primary-edition consultation. Follow your institution's AI disclosure policy. Neither a fluent answer nor a green validator is peer review.

## Updates and troubleshooting

The master [automatically checks member updates](AUTO-SYNC.md) on a five-minute schedule. Successful native validation updates accepted revision records and the downloadable starter; failures retain the last accepted revision and are shown in [member status](MEMBER-STATUS.md). GitHub can delay scheduled runs. Downloaded files and existing AI conversations do not refresh themselves. For a new session, check current status, download a fresh starter and deliberately choose the evidence revision. Keep an existing analysis pinned for reproducibility; assess later changes in a separate run.

| Problem | What to do |
|---|---|
| AI cannot read GitHub | Upload the selected instruction and evidence files; ask it to list accessible attachments |
| Context/upload limit reached | Narrow to one question and one packet; retain the manifest and source paths |
| Exact ID not found | Check repository, collection, spacing and native coverage; report absence from this view only |
| Bundle/source mismatch | Stop calculations, preserve the discrepancy and use the native maintenance guidance |
| Two editions appear to disagree | Verify same locus and editorial notation before comparing; audit source dependence |
| Comparison is blocked | Ask for the missing evidence and the smallest defensible descriptive task |
| AI supplies an unsupported translation | Reject it, return to the source representation and request the source for every proposed value |
| Need help or want to report a defect | Open an issue in the affected corpus for native evidence, or the master for routing/docs; include minimal reproducible public inputs and expected versus observed behavior |

Do not post restricted source files or private research material in a public issue. A useful report identifies the exact revision, affected records and the point at which the evidence chain breaks.

## Adversarial academic review preparation

The [25 October review and repairs](references/hostile-review-2026-10-25.md) cover all eighteen declared retrieval profiles, expanded digital-source checks and partial-text dependence screening. A fresh Linear B paper download and appendix check succeeded; earlier access failures remain historical. The development exercise is compact-evidence conformance, not independently validated academic accuracy. All43 inherited scholarly closure packages remain open or mitigated under their original criteria.
