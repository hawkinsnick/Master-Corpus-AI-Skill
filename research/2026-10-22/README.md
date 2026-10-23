# Completed fixed batch and review handoff

The source batch is complete as a six-case documentary task: **12 assertions assigned outcomes, seven verified against their attributed source and five awaiting primary pages**. All six existing comparison cases were included. This repeats the earlier native collation with a fresh acquisition and visual inspection; it discovers no new correction and does not certify readings.

| Cases | Outcome | Remaining evidence |
|---|---|---|
| CMOC-0026 positions2 and5; CMOC-0027 position3; CMOC-0209 top position3 and A.I.2.01 position2 | INACCESSIBLE_PRIMARY: Valério side checked, Olivier side still indirect | Olivier printed pp.76,77,496 |
| CMOC-0209 A.II.5.01 position2 | DISCREPANT_SOURCE: 09 versus10 within Valério | Authorial correction or qualified sign-level assessment |

[Machine-readable receipt](source-batch.json) retains each assertion, outcome, exact locus, source hash and scope. Seven verified attributions include both sides of the internal inconsistency; they do not imply agreement between those two labels. A.I.2.01 doubt and lacuna remain preserved. No readings changed and no external reviews were received.

The [Tiryns review packet](TIRYNS-REVIEW-PACKET.md) is complete and ready to hand to a source-qualified reviewer, with three defined claims, pinned evidence, review procedure and blank response form. Actual independent review remains pending.

Replay the batch bindings with `python scripts/check_source_batch.py --checkouts /path/to/frozen-corpora`; add `--pdf /path/to/lawfully-obtained-thesis.pdf` to verify the inspected copy. Replay validates records, not human inspection. Source PDFs/images are not distributed.
