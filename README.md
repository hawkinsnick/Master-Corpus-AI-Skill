# Master Corpus AI Skill

[Open-item fixes and remaining external decisions](OPEN-ITEMS.md) include a printed-source recheck, the full member-pair artifact scan and corrected evaluation provenance.

**Researcher guides:** [Step-by-step user guide](USER-GUIDE.md) · [Research examples for all 18 corpora](RESEARCH-EXAMPLES.md) · [Cross-corpus walkthroughs](CROSS-CORPUS-EXAMPLES.md).

A dedicated home for the master research skill coordinating 18 ancient-script
corpus projects. Begin with [SKILL.md](SKILL.md), the
[researcher walkthrough](START-HERE.md), or the
[corpus directory](CORPUS-DOWNLOADS.md).

**Canonical repository:** [hawkinsnick/Master-Corpus-AI-Skill](https://github.com/hawkinsnick/Master-Corpus-AI-Skill). The master instructions live at the root in [SKILL.md](SKILL.md). The legacy Linear-A entry is retained for compatibility; native evidence stays in its own corpus repository.

The master holds instructions, routing metadata and software. Native corpus data,
individual skills and source/review authorities remain in their own repositories.
Egyptian Hieroglyphic Corpus remains separate from the 18-member factory.

[Automatic corpus updates](AUTO-SYNC.md) · [Current member status](MEMBER-STATUS.md)

[Executed research studies and evaluation](RESEARCH-RESULTS.md) provide frozen source-trace, dependence and comparability results with explicit scholarly limits.

## Check the standalone package

Use Python 3.10+; no third-party packages or native corpus checkout are required:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

With the native corpus checkouts available:

```sh
python scripts/validate.py --checkouts /path/to/corpora --output member-checks.json
```

The [starter text](downloads/Master-Corpus-AI-Skill-Starter.txt) supplies context
for an AI that can read uploaded text. It does not install a plugin, connect to
GitHub, supply member evidence or grant source permissions.

Source provenance and exact extraction hashes: [migration/origin.json](migration/origin.json).
The [cutover plan](migration/CUTOVER.md) preserves old entry points until the
new destination is published and validated. Original project licensing and
all applicable upstream conditions remain intact.

## Fixed source batch and Tiryns review packet

The [22 October completion record](research/2026-10-22/README.md) assigns outcomes to all six existing comparison cases and twelve assertions. Five primary-edition sides remain inaccessible; the internal source discrepancy remains unresolved. The [Tiryns packet](research/2026-10-22/TIRYNS-REVIEW-PACKET.md) is ready for independent review; no review has been received.
