# Combined Corpus Research AI — Researcher Quickstart

**New: [Follow three worked examples](WORKED-EXAMPLES.md)** — trace a real record, assess an unresolved comparison, and reproduce a calculation. Browser-only and optional AI/Python routes include verified results.

This guide explains the research workflow after setup. For downloads and upload instructions, begin with [Start here](START-HERE.md). You can start with one text file, without Git or Python.

## Five-minute start

1. [Download the starter](downloads/Master-Corpus-AI-Skill-Starter.txt) and attach its text file to your AI conversation or project.
2. Use the first-message prompt in [Start here](START-HERE.md) to confirm that the assistant can read it and identify relevant corpora.
3. Choose a corpus from the [download directory](CORPUS-DOWNLOADS.md). Make its individual instructions, index, source-state and selected canonical evidence accessible. The starter and an index alone do not supply inscription evidence.
4. Ask your research question normally. [Prompts](PROMPTS.md) cover source tracing, edition comparisons and reproducibility.
5. For cross-corpus questions, require the AI to show the comparability check before interpreting similarities.

A good first prompt is: **“Which registered corpus projects are relevant to my question, what evidence can each currently provide, and which comparisons are allowed, gated or blocked?”**

## Good research questions

- “Find the evidence relevant to this sign or sequence and distinguish source observations from later interpretation.”
- “Compare positional patterns across these two corpora, but stop if their units or segmentation are not comparable.”
- “Trace this statement to corpus records and source locators.”
- “Reproduce this statistic and list its inputs and exclusions.”
- “Which apparent replications share an upstream source or witness?”
- “What specific evidence is missing before this blocked comparison could proceed?”
- “Show disagreements among editions without selecting a preferred reading unless the corpus records a justified preference.”

## What a trustworthy answer should show

For substantive work, expect the answer to identify the corpus project(s), evidence layer, relevant IDs/locators where available, evidentiary status, uncertainty/exclusions, source-independence limitations, reproducibility method for new calculations, and rights/attribution constraints when reproduction is involved.

For cross-corpus work, expect a **Comparability** section stating each corpus's unit of analysis, representation layer, source dependence and whether the requested inference is permitted.

## Undeciphered and poorly understood material

The system must not manufacture translations, phonetic values, morphemes or language relationships. Recurrence, position, visual resemblance or correspondence with a deciphered script may be reported as evidence only at the level actually established by the corpus.

A deciphered writing system also does not imply that every language written in it is understood. This is especially important for Eteocypriot.

## Deciphered corpora and controls

For Linear B, Cypriot syllabic Greek and other readable material, the system still separates transcription, normalization, restoration, linguistic interpretation and translation. Established readings from one script cannot be transferred automatically to another.

## When the AI says BLOCKED

Do not ask it to “take its best guess.” Instead ask:

**“What evidence, source acquisition, review, calibration or methodological change would be necessary to unblock this question?”**

That converts a negative result into a research agenda.

## Staleness and validation

Before relying on a generated bundle, inspect its source-state and research-bundle index. The source commit should identify the corpus state represented by the bundle. If generated material conflicts with canonical corpus files, canonical evidence wins and the discrepancy should be reported.

Individual corpus validators protect corpus-specific authorities. The Combined validator protects the registry and orchestration contract. Neither proves that an ancient reading is epigraphically correct or peer reviewed.

## Rights and citation

The Combined skill is not a licence umbrella. Every corpus and upstream source keeps its own terms. Ask the AI to identify the source and applicable rights before reproducing substantial source-derived material.

For scholarly citation, cite the underlying corpus record/source or publication rather than citing the Combined AI as though it were the evidence.

## Suggested reproducible workflow

**Question → route to corpus project(s) → validate bundle state → retrieve native evidence → classify evidence → check source independence → check comparability → compute only if permitted → report result and blockers → record corpus versions/commits and methods.**

This workflow is intentionally conservative. A scientifically meaningful BLOCKED result is preferable to a fluent unsupported conclusion.
