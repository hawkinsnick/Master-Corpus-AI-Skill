# A researcher's first session: three worked examples

Start here if you want to see what the corpus can do before installing anything.
These examples use Linear A to teach source tracing, assessment of an unresolved
comparison, and reproducible counting. Other languages use their own evidence
models: choose their guide in the [18-corpus directory](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/EVIDENCE-AND-ALTERNATIVES.md).
This is a teaching sample, not a representative assessment of the collection.

## Choose your route

- **Browser only:** follow the numbered steps in each example and inspect the saved outputs. No account, AI subscription, Git or Python is needed to read these public pages.
- **With an AI assistant:** complete the [starter setup](START-HERE.md), then upload the indicated example JSON file and use the prompt provided. The starter supplies instructions; the example dossier supplies selected evidence.
- **With Python:** follow the optional reproduction section below. The displayed results were actually generated, not simulated AI responses.

## Example 1 — What evidence do we have for ARKH 1a?

**Question:** What does the source record say about this document, and where did those statements come from?

1. Open the [ARKH 1a dossier](https://github.com/hawkinsnick/Linear-A/blob/main/docs/examples/researcher-walkthrough/ARKH-1a.json). This JSON is structured text: names to the left of a colon identify fields; square brackets contain lists.
2. Find `native_record`, then `source_fields`. Read `id`, `typology`, `site`, `dimensions_cm` and `period`.
3. Compare what you see with this source-reported summary:

   | Field | Value in the record |
   |---|---|
   | Identifier | ARKH 1a |
   | Type | Tablet |
   | Site | Arkhanes |
   | Dimensions | `[6.0, 8.0, 0.95]` cm, retaining source order |
   | Period | LM I |
   | Status | SOURCE_REPORTED_NOT_INDEPENDENTLY_VERIFIED |

4. Find the outer `provenance`: it identifies `research/sigla-source-documents.jsonl`, pointer `/0`, and the file's SHA-256. `/0` means the first nonempty JSONL record, using zero-based indexing. Inside `native_record.provenance`, the upstream input hash and `/documents/0` describe a different stage of the source chain. Preserve both.
5. Read `native_record.provenance.attribution` and `license`. Attribution is **Ester Salgarella and Simon Castellan, SigLA; derivative by Ryan Pavlicek/pyaegean**. These source-derived fields retain **CC BY-NC-SA 4.0**. Read the [license matrix](https://github.com/hawkinsnick/Linear-A/blob/main/DATA-LICENSE-MATRIX.md) before reuse.
6. Read `public_reference_url` as a bibliographic route supplied by the record. Its presence does not establish that you or this tutorial inspected the edition, that the route currently works, or that edition content may be imported. The recorded GORILA refusal remains binding.

**A defensible result:** “The admitted SigLA-derived entry ARKH 1a reports a tablet from Arkhanes, dated LM I. These are source assertions; the project does not certify the physical-object identity.”

Sign labels such as TA and PI are source conventions, not established Linear A pronunciation or translation. The dimension axes are not named here; do not silently relabel the three values as length, width and thickness.

**Try it with AI.** Use the dossier page's download/raw control to save `ARKH-1a.json`, then attach it after the starter and send:

> Read the uploaded ARKH-1a.json. Identify the files you can actually read. Summarize the source-reported metadata in a table. Give the repository path, JSON pointer, source hash, attribution and rights. Distinguish recorded labels from independently established facts. Do not translate the signs or infer dimension axes.

**Check the response:** it should reproduce the table and provenance above, preserve the unverified status and identify the actual uploaded file. Its wording may vary. This paragraph is an acceptance criterion, not a captured model response.

## Example 2 — Can two recorded alternatives really be compared?

**Question:** Does case U008 establish competing readings at the same place on KH 8?

1. Open the [U008 dossier](https://github.com/hawkinsnick/Linear-A/blob/main/docs/examples/researcher-walkthrough/U008.json).
2. Find `native_record.legacy_alternatives`: it preserves `QA2PU vs *510` as a historical queue label. A queue label does not identify two scholarly editions.
3. Read `finding` and `source_evidence`. The audit reports A567 at source-array slot 11 and A510 at slot 14. Those are different slots. They are zero-based array indices, not inscription line numbers.
4. Read the two `alternatives` entries side by side:

   | Historical literal | Recorded attribution status |
   |---|---|
   | QA2PU | UNTRACED_LEGACY_LITERAL_AND_LOCUS |
   | *510 | SOURCE_IDENTIFIER_PRESENT_LOCUS_CONFLICT_WITH_RC2 |

5. Check `same_locus_competing_pair_established` and `independent_witnesses_established`. Both are `false`. This audit has not established either property; it does not prove that no relevant scholarly comparison exists elsewhere.
6. Read `remaining_evidence_gap`: resolve which slot the case concerns and recover the source and notation of QA2PU before comparing it with either identifier.

**A defensible result:** “U008 does not yet support a same-locus editorial comparison. The project audit identifies a locus conflict and incomplete attribution. No preferred reading follows.”

This is a useful research outcome: it prevents an apparent disagreement from becoming a false claim and identifies the next source work needed. It is not a completed critical apparatus or new epigraphic adjudication.

**Try it with AI.** Download and attach `U008.json`, then send:

> Assess U008 using only the uploaded dossier. Show the historical literals and attribution statuses side by side. Can the same locus and source independence be established? Cite the exact fields and list the missing evidence. Separate the project's audit from primary-edition consultation. Do not choose a reading.

**Check the response:** it should identify the slot conflict, missing attribution, both false flags and the specific next steps. An answer claiming that two scholars disagree at a verified locus overstates this packet.

## Example 3 — Reproduce a count without changing its meaning

**Question:** How many entries and attestation slots are in this public source view, and how many slots in ARKH 1a have nonempty sign labels?

1. Open the [saved calculation](https://github.com/hawkinsnick/Linear-A/blob/main/docs/examples/researcher-walkthrough/counts.json).
2. Read its input path and SHA-256. The input is the committed public source-document JSONL, not a catalogue of certified unique physical objects.
3. Read the inclusion rule in `scope`: every nonempty JSONL row and every attestation slot is included, including blank slots.
4. Compare the result:

   | Measure | Executed result |
   |---|---:|
   | Source-document entries | 802 |
   | Attestation slots across those entries | 5,144 |
   | ARKH 1a attestation slots | 18 |
   | ARKH 1a slots with `kind` equal to `blank` | 1 |
   | ARKH 1a nonempty sign labels | 17 |

5. Open the [calculation script](https://github.com/hawkinsnick/Linear-A/blob/main/scripts/walkthrough_count.py). It counts rows and list elements, then tests the literal `kind` and `sign` fields. It makes no linguistic inference.
6. Retain the denominator and exclusions in your notes. “17 nonempty sign labels in this source entry” does not mean 17 distinct signs, 17 words or 17 independently confirmed readings. An encoded blank is not automatically a damaged or missing ancient sign.

**Try it with AI.** Attach `ARKH-1a.json` and ask:

> Calculate the number of entries in native_record.source_fields.attestations, the number whose kind is blank, and the number with a nonempty sign label. Show your inclusion rules. Do not count context resources as attestations. Report this as a calculation over the uploaded source entry; do not infer whole-corpus totals from this one file.

Expected record-level results are **18, 1 and 17**. To reproduce the whole-view totals, supply the canonical JSONL too, or run the script below. The saved totals alone are a report, not the full calculation input.

## Optional: reproduce the examples on your computer

Use Python 3.12; these commands need only its standard library. If Python is unavailable, use the browser route or ask a research computing colleague to run this section.

1. Open the [Linear A repository](https://github.com/hawkinsnick/Linear-A). Select **Code → Download ZIP**, then extract the archive. The extracted folder is normally `Linear-A-main`. A ZIP downloaded from main may contain later changes.
2. Open a terminal in that folder (Windows: open the folder in File Explorer and use **Open in Terminal**; macOS: open Terminal, type `cd `, drag the folder into the window, and press Return).
3. Check Python with `python --version`. If your installation uses `python3` or `py`, substitute that command throughout. Copy one command at a time:

```sh
python scripts/evidence_query.py --check
python scripts/evidence_query.py --record "ARKH 1a" --collection source-documents > arkh-result.json
python scripts/evidence_query.py --record U008 --collection attribution-audit > u008-result.json
python scripts/walkthrough_count.py > count-result.json
```

4. Open the three result files in a text editor. Compare their parsed JSON content with the saved examples. Whitespace differences are immaterial; changed values or hashes require inspecting the source version.
5. To reproduce the exact teaching snapshot, use [this pinned source revision](https://github.com/hawkinsnick/Linear-A/tree/7eab440986e696d65bc8be026a68cbd78e9b3ad8). The query scripts and canonical input files existed there; the new `walkthrough_count.py` is supplied with this tutorial. Preserve that script separately if using the older source checkout. Saved dossiers preserve complete query outputs, including their qualifications.

If the check reports a stale source pin, stop and inspect the mismatch. Do not edit hashes merely to obtain a pass. If an identifier is not found, keep spaces and collection names exactly as shown. A blocked scholarly comparison can coexist with successful software checks.

## Save and cite your research session

Record the repository commit you actually used: on GitHub open the file's **History**, select the relevant commit and copy its full SHA; in a Git checkout use `git rev-parse HEAD`. A source-file SHA-256 identifies bytes, not a repository commit or scholarly authenticity.

Copy and fill this research log:

```text
Question:
Corpus repository and full commit:
Files actually inspected, including any tutorial output:
Record ID and native unit:
Canonical source path, JSON pointer and SHA-256:
Underlying source/publication and locator, where available:
Method and inclusion/exclusion rules:
Result and evidentiary status:
Uncertainty, source dependence and missing evidence:
Attribution and applicable rights:
Date of access:
```

For Example 1, the locator is `research/sigla-source-documents.jsonl`, `/0`, record
`ARKH 1a`, SHA-256 `9643a3b7f794fe13b94526dadbe9421faa0eb5488233ba2618054944eba3a10b`.
Cite the source authors and underlying publication for scholarly assertions;
identify this repository revision and any computation as part of your method.
Do not invent a publication page from an array index. The saved JSON includes
upstream attribution and a bibliographic route; consult the underlying source
before claiming direct consultation. The AI assistant is a tool, not an ancient witness.

## Continue with your own language or inscription

1. Choose its [corpus-specific guide](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/EVIDENCE-AND-ALTERNATIVES.md).
2. Use that guide's native collection and exact identifier. Do not copy Linear A field meanings into another corpus.
3. Ask for evidence and provenance first, interpretation second, and a reproducible method for calculations.
4. For expert feedback, use the [review guide](EXPERT-REVIEW.md) and include your research log, exact records, source locators and one focused question.

These walkthroughs were executed against source revision
`7eab440986e696d65bc8be026a68cbd78e9b3ad8` on 17 October 2026 UTC
(16 October in Chicago). They add documentation and derived example outputs,
not new readings, primary-source collation or expert acceptance.

## Specialist research questions

Continue with the [Linear A, Linear B and Luwian task pilots](https://github.com/hawkinsnick/Linear-A/blob/61f1cd73ae66fd6a5f98d03f2f5694b05bf11d18/corpus-factory/SPECIALIST-RESEARCH-PILOTS.md). Each guide distinguishes its executed exercise from the evidence required for deeper interpretation.
