# Record-level source checks

[Open-item fixes and remaining external decisions](OPEN-ITEMS.md) include a printed-source recheck, the full member-pair artifact scan and corrected evaluation provenance.

This bounded diagnostic independently replayed 54 source pointers, three retrievable view rows per registered project. All matched their committed native payload. The sample includes project registers and documentary views; it is not a sample of 54 authenticated inscriptions. Candidate metadata are field extracts, not verified citations.

Full methods, original field pointers, hashes and follow-up requirements: [source-trace.json](research/2026-10-21/source-trace.json). Exact [native revisions](research/2026-10-21/native-revisions.json) are frozen.

| Project | Sampled view IDs | Rows with no extracted candidate metadata | Fresh primary-edition checks |
|---|---|---:|---|
| Linear-A | `HT 116a`, `KH Wc 2101`, `HT Wa 1295` | 0 | Not performed |
| Cypro-Minoan | `CMOC-0026`, `194`, `40` | 0 | Not performed |
| Linear-B | `pwid21195`, `4215`, `4165` | 0 | Not performed |
| Cretan-hieroglyphs | `CHIC-260`, `CHIC-107`, `CHIC-307` | 2 | Not performed |
| Phaistos-Disc | `PD-A-E27-S03`, `PD-B-E30-S04`, `PD-B-E18-S01` | 0 | Not performed |
| Byblos-syllabary | `BYB-C`, `BYB-CAND-PALIMPSEST-KAI4`, `BYB-G` | 0 | Not performed |
| Cypriot-syllabic-Greek | `CSG-IGXV1-231`, `CSG-IGXV1-335`, `CSG-IGXV1-283-5` | 0 | Not performed |
| Eteocypriot | `ETEC-IGXV1-16`, `ETE-IG150-QUARANTINE`, `ETEC-IGXV1-46` | 0 | Not performed |
| Eteocretan | `ECR-PRAISOS-2-CONWAY-127-II`, `ECR-PRAISOS-1-WIKIPEDIA-174295509`, `ECR-DREROS-2-WIKIPEDIA-174295509` | 0 | Not performed |
| Lycian-and-Carian | `EDIANA-CARIAN-547`, `EDIANA-CARIAN-468`, `EDIANA-CARIAN-606` | 0 | Not performed |
| Phrygian | `Phryg._Old-Phryg._G_258`, `Phryg._Old-Phryg._P_101`, `PHR-DIS-004` | 0 | Not performed |
| Anatolian-Hieroglyphic | `EDIANA-HL-037`, `EDIANA-HL-079`, `HL-URBS-CITY-20261017` | 0 | Not performed |
| Archanes-Script | `AS#04`, `AS#13`, `ARC-DIS-002` | 1 | Not performed |
| Aegean-anomalous | `ANO-DIS-005`, `ANO-DIS-002`, `ANO-DIS-001` | 2 | Not performed |
| Lydian | `lydian:ediana:10`, `lydian:ediana:49`, `lydian:ediana:48` | 0 | Not performed |
| Sidetic | `FERRER2025-S10-ethnic`, `sidetic:ediana:306`, `FERRER2025-S6-2` | 0 | Not performed |
| Pisidian | `pisidian:ediana:9`, `pisidian:ediana:21`, `PIS-RAMSAY1895-9` | 0 | Not performed |
| Milyan-Lycian-B | `EDIANA-MILYAN-1-ROW-8`, `TL55-L1-A089`, `TL55-L7-A034` | 0 | Not performed |

## How to use this audit

Start with a sampled row, open the pinned native source and check the cited field. Resolve each source ID or bibliographic candidate to its actual edition and locus. Consult the edition lawfully; record what was inspected, where it agrees or disagrees and what cannot be judged. Distinguish that documentary check from a specialist assessment of the ancient reading. Where the selected row is only a project register, locate a suitable reading-bearing source before attempting epigraphic verification.

Zero candidate fields means this extractor found none of its declared field types; it does not prove that no relevant citation exists elsewhere. Nonzero fields may be only a source ID, rights label or project locator. Their presence is not a completeness score.

No author/locus has been invented, no native reading changed and no expert gate upgraded. Follow-up primary-edition inspection and independent review remain open for this sample. See [research results](RESEARCH-RESULTS.md) for the executed studies and the AI evaluation.

## Fresh source-access follow-up

A targeted attempt to acquire the Linear B publication appendix returned HTTP 403 on ordinary HTTP retrieval; the web retrieval route was also unavailable. [The access receipt](research/2026-10-21/source-access-attempt.json) records the failure. No new PDF inspection was claimed, no access restriction bypassed and no earlier native consultation promoted to a fresh source check. The unresolved next step is lawful access to that publication and an actual page-level comparison.

## Fresh provider-edition field checks

A separate targeted follow-up acquired three sampled records directly from the first-party Inscriptiones Graecae XML service: Eteocypriot entries 16 and 46 and the Cypriot Greek view of entry 231. [The receipt and per-field results](research/2026-10-21/fresh-provider-checks.json) identify the provider URLs, hashes, XPath selectors, exported field pointers and source terms. All three acquired XML hashes match the frozen raw sources. The corrected checker compares 21 metadata/component-text fields with zero mismatches. It preserves explicit XML line breaks rather than merging adjacent lines. The initial checker diagnostics are retained; no native reading was changed.

These are fresh digital-edition fidelity checks for three records in two projects. They are not printed-page collation, independent autopsy or an independent judgment that the source reading is correct. The other sampled projects have not received this fresh provider check.

Replay against the frozen source bytes without network access:

```sh
python scripts/provider_source_check.py --checkouts /path/to/frozen-corpora
```

A deliberately fresh acquisition uses `--live`; adding `--write` records new receipts. A changed provider source or disagreement must be investigated rather than silently replacing the frozen evidence. Raw source XML is not republished in this master.

## Fixed source batch and Tiryns review packet

The [22 October completion record](research/2026-10-22/README.md) assigns outcomes to all six existing comparison cases and twelve assertions. Five primary-edition sides remain inaccessible; the internal source discrepancy remains unresolved. The [Tiryns packet](research/2026-10-22/TIRYNS-REVIEW-PACKET.md) is ready for independent review; no review has been received.

## Adversarial academic review preparation

The [25 October review and repairs](references/hostile-review-2026-10-25.md) cover all eighteen declared retrieval profiles, expanded digital-source checks and partial-text dependence screening. A fresh Linear B paper download and appendix check succeeded; earlier access failures remain historical. The development exercise is compact-evidence conformance, not independently validated academic accuracy. All43 inherited scholarly closure packages remain open or mitigated under their original criteria.
