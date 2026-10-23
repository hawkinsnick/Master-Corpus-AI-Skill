# Tiryns 244: documentary review packet

Prepared 22 October 2026. **Ready for review; no external review received.** This public case is already exposed and is unsuitable as an untouched model evaluation case.

## Question and decision boundary

Do the three attributed catalogue labels for CMOC-TIRY-ADD244 accurately represent the named publication at the cited locus? Review each claim independently. A documentary agreement does not certify the ancient signs, assign sounds, decipher a text or establish a second witness. The authoring assistant already checked the source; an independent reviewer should examine it directly and record disagreement.

## Evidence to inspect

Melissa Vetters, *A Clay Ball with a Cypro-Minoan Inscription from Tiryns*, Archäologischer Anzeiger 2011/2, pp.1–49. [Publisher route](https://publications.dainst.org/journals/aa/article/download/99/4770); [German National Library copy](https://d-nb.info/1266074589/34). The inspected offprint has 50 PDF pages including a cover. Printed pp.16–17 are one-based PDF pages17–18. SHA-256: `d303242bba1e547c4da5688c033758d55747d162042b2bf82f974effd3c99132`; 587,527 bytes. A different legitimate copy needs its own checksum and page mapping.

Native evidence: [occurrences.json at the frozen revision](https://github.com/hawkinsnick/Cypro-Minoan/blob/185ef0a44222281fbde53589185f8b647ad85313/occurrences/occurrences.json), `/occurrences` entries located by the unique occurrence IDs below. File SHA-256: `d020ba8a3630e234b9ee33c59eb8c8631f1dfd78e8284907532f2cd5a8041dcb`. [Full authoring-assistant receipt](../2026-10-21-followup/printed-source-recheck.json).

| Claim / occurrence ID | Record position | Attributed label | Source locus |
|---|---:|---|---|
| CMOCC-TIRY244-1 | 1 | 41 | Printed p.16, concluding paragraph under Interpretation of the Signs; p.17 discussion and notes129/139 |
| CMOCC-TIRY244-2 | 2 | 41 | Same passage, second occurrence |
| CMOCC-TIRY244-3 | 3 | 97 | Same passage, final occurrence |

These are catalogue identifiers, not phonetic values. Preserve reading direction and the distinction between a source's attribution and a fresh sign identification.

## Reviewer procedure

1. Record your name, relevant expertise, affiliation or public profile, prior involvement and conflicts. Record which source copy and exact pages you actually inspected, including any access limitations.
2. Locate the three native entries by occurrence ID and compare their record, source, position and label with the publication. Check whether our page mapping or sequence interpretation is wrong.
3. For each claim choose SUPPORTED, CORRECTION_REQUIRED or INCONCLUSIVE. Supply the exact locus and a reason. A missing source is INCONCLUSIVE. If a correction is needed, specify the field and evidence; retain uncertainty.
4. Separately identify any question that requires images, object inspection or specialist judgment beyond this documentary task. Do not turn a documentary decision into graphical or phonetic certification.
5. Complete a copy of [the response form](tiryns-review-response.json). All decisions begin null; nothing is pre-endorsed. Return through an agreed review channel. No recipient has been contacted by this project task.

A submission is complete only when identity/expertise, conflicts, sources inspected, all three decisions and their rationales are supplied. Verify reviewer identity and source access before describing it as independent specialist review. Keep inconclusive outcomes and conflicting submissions visible. No automatic promotion or reading change follows from form completion.

## Reproduction and rights

Run `python scripts/check_printed_source_recheck.py --checkouts /path/to/frozen-corpora --pdf /path/to/lawfully-obtained.pdf`. This checks source identity and stored claim bindings; it cannot perform the visual review. The master bundles no source PDF, figures or page images. Consult the publication under its own access and reuse terms. A reviewer may report concise catalogue facts and original reasoning without reproducing protected pages.
