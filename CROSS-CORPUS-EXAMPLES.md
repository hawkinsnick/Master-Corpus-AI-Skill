# Cross-corpus research walkthroughs

A comparison starts with a question that needs evidence from more than one project. The master helps you select the projects, retrieve their records separately and decide which parts of the question the available evidence can answer.

These five walkthroughs are research designs with copyable prompts, not completed analyses or reported findings. They do not assume that every requested field or sample is already available. Each gives you a useful first task and a concrete output to take into further research.

## Choose a question

| Research question | Projects | First useful output |
|---|---|---|
| [Can these administrative samples be compared?](#1-comparing-administrative-evidence-linear-a-and-linear-b) | Linear A and Linear B | An evidence and sampling table |
| [What can a bilingual context establish?](#2-comparing-bilingual-contexts-eteocypriot-and-cypriot-syllabic-greek) | Eteocypriot and Cypriot syllabic Greek | An alignment and interpretation table |
| [Are two records really separate evidence?](#3-checking-overlap-lycian-and-carian-and-milyan) | Lycian-and-Carian and Milyan | An overlap register |
| [Does sign position vary with support?](#4-comparing-sign-position-cretan-hieroglyphic-and-cypro-minoan) | Cretan Hieroglyphic and Cypro-Minoan | A comparable-sample definition |
| [Is formula variation ancient or editorial?](#5-comparing-formula-variation-lydian-and-phrygian) | Lydian and Phrygian | Two attributed concordances and a comparison |

## Before you begin

Follow [the user guide](USER-GUIDE.md#set-up-your-first-session) to supply the master starter. For **each** selected project, supply its individual skill, authority profile, bundle index, source/rights guidance and the exact evidence files required. The [corpus directory](CORPUS-DOWNLOADS.md) links to each repository. If you do not know which evidence files to select, supply the instructions and index first and ask the assistant to identify the files needed. Supply those files before asking for findings.

You can upload a small packet for each project; you do not need to upload the entire collection. Keep a list of original paths, full repository revisions and files actually inspected. The assistant should use each project's own record IDs, notation and source rules. “Compare these” does not authorize it to silently join datasets or translate an undeciphered script.

Start each session with:

```text
Use the master instructions and both individual corpus skills. List the files
you can actually read, their project and revision, and any missing evidence.
Retrieve and cite a record from each project before comparing. Preserve each
project's native units and notation. Tell me which parts of my question can
be answered now, then proceed with those parts. Do not invent missing inputs,
executed calculations or scholarly conclusions.
```

If only one project's evidence is available, complete its inventory and request the second packet. A cross-corpus conclusion must wait for both.

## 1. Comparing administrative evidence: Linear A and Linear B

**Your question:** “Are these two selected administrative samples organized in similar ways, and how much of the apparent similarity comes from editorial presentation?”

**Use:** [Linear A](https://github.com/hawkinsnick/Linear-A) and [Linear B](https://github.com/hawkinsnick/Linear-B).

**Bring:** a bounded sample from each project, source representations, recorded entry boundaries, numerical notation, restorations and source attribution. Include archive, support or context metadata where available. Select and document the samples before looking for a preferred pattern. The saved [Linear A walkthrough](WORKED-EXAMPLES.md) teaches source tracing; its one-record exercise is not a comparative administrative sample.

**Work through it:**

1. Ask the assistant to inventory what is recorded in each sample: document, entry, sign slot, numerical component or another native unit. Have it quote the field definitions from the supplied guides.
2. Build two evidence tables. Keep Linear A source labels separate from Linear B readings and interpretations. List ambiguous boundaries, missing amounts and restored components.
3. Define one shared descriptive feature only if the evidence supports it—for example, placement of recorded numerical components relative to explicitly documented entry boundaries. Require a written mapping from each native representation to that feature.
4. Inspect the feature by project and repeat the comparison excluding restored or boundary-ambiguous cases. If the units cannot be reconciled, retain the two descriptions and explain the mismatch.

**Copy this prompt:**

```text
Compare the organization of my selected Linear A and Linear B administrative
samples. First show how each corpus represents a document, entry, numerical
component and uncertainty; mark unavailable definitions. Build separate,
source-linked tables. Propose one descriptive feature that can be measured
in both without interpreting Linear A sign labels as phonetic readings.

Before calculating, show the mapping rules, denominator, exclusions and
possible archive/support effects. Execute only if the inputs and execution
environment are available; otherwise provide the method without numerical
results. Repeat with restored and boundary-ambiguous cases excluded if possible.
Do not infer shared vocabulary, institutions or accounting practice merely
from a positional resemblance.
```

**What to save:** the two tables, the feature mapping, actual sample sizes, exclusions and either reproducible outputs or a clear statement of why calculation could not proceed. A supported conclusion would describe the selected records and the effect of editorial choices. A historical explanation requires additional evidence.

## 2. Comparing bilingual contexts: Eteocypriot and Cypriot syllabic Greek

**Your question:** “Does a proposed correspondence have independent alignment evidence, or does it rely on the fact that two texts occur together?”

**Use:** [Eteocypriot](https://github.com/hawkinsnick/Eteocypriot) and [Cypriot syllabic Greek](https://github.com/hawkinsnick/Cypriot-syllabic-Greek).

**Bring:** the exact Eteocypriot record, its associated Greek text if supplied, the source of the proposed correspondence, and a selected Cypriot syllabic Greek comparison passage with its attributed reading. Establish the proposal's exact forms and source locus. Do not assume that an associated Greek component is written in the Cypriot syllabary or is hosted in the Greek repository; use that repository for separately justified comparison material, not as a substitute for a missing component.

If you have not selected a proposal, begin by finding an attributable proposal in the accessible source material; the master starter cannot supply one by itself. Choose the Greek control using criteria stated before examining the proposed match: the specific formula or function being tested, supported context/genre, relevant dating where available and reading quality. Record why the passage is eligible and what differences remain. If no suitable control is accessible, complete the Eteocypriot source audit and record the missing comparison.

**Work through it:**

1. Retrieve each passage in its own project. Separate the evidence for physical association from scholarly claims about equivalence.
2. Ask the assistant to distinguish script identification, transliteration, reading, normalization and translation. Mark any step that lacks a source.
3. Build a table of proposed alignments: entire text, passage, name or word. For each, ask what evidence supports that level of alignment and whether the reasoning assumes the interpretation it is meant to test.
4. Use the Greek comparison only for a defined question that its reading and context can support, such as whether an attributed formula is a relevant control. Shared script conventions alone do not align words or establish meaning.

**Copy this prompt:**

```text
Evaluate [attributed proposed correspondence and exact loci] using my
Eteocypriot packet and the separately selected Cypriot syllabic Greek passage.
Document what each record actually contains. Do not assume that the associated
Greek component is in the second repository or uses its writing system.

Show physical/textual association, passage alignment, word alignment and
interpretation as separate claims. Cite the evidence and source for each.
State what makes the Greek comparison relevant, and what differences limit
it. Identify circular reasoning and competing interpretations. Give a table
of supported constraints and missing evidence, without manufacturing an
Eteocypriot translation.
```

**What to save:** an alignment table with a source and evidentiary status for every proposed link, followed by the next observation needed to distinguish interpretations. “The texts are associated” and “these words mean the same thing” are separate claims; the first does not establish the second.

## 3. Checking overlap: Lycian-and-Carian and Milyan

**Your question:** “If both repositories mention this material, do I have two independent attestations or two routes to the same source?”

**Use:** [Lycian-and-Carian](https://github.com/hawkinsnick/Lycian-and-Carian) and [Milyan (Lycian B)](https://github.com/hawkinsnick/Milyan-Lycian-B).

**Bring:** records suspected of overlap, their source chains, catalogue identifiers and language assignments. A shared catalogue label is a candidate for investigation, not an established join. If no overlapping record can be found in one selected view, record that limited search outcome.

**Work through it:**

1. Search both projects separately for the selected identifier and retrieve the relevant records. Preserve language labels; do not pool Lycian, Carian and Milyan automatically.
2. Ask for an overlap register with both native IDs, underlying source, quoted locus, proposed object/text identity and the evidence supporting the link.
3. Distinguish duplicate hosting, different editions of one text, repeated assertions from one edition and genuinely separate witnesses. Leave uncertain matches unresolved.
4. Rebuild your proposed evidence count using only documented joins. Report unresolved cases separately instead of assigning them fractional or invented identities.

**Copy this prompt:**

```text
Audit possible overlap between these Lycian-and-Carian and Milyan records:
[exact IDs and packet filenames]. Build a register preserving both namespaces,
language labels, source authors/editions and native loci. For each candidate,
classify the relationship only as far as the evidence permits: duplicate
hosting, same text in different editions, shared upstream assertion,
independent witness, or unresolved. Explain the basis for each classification.

If supported joins allow a revised count, show the counting rule and input
rows. Otherwise give bounds only if justified, or say that a unique count is
not established. Do not treat repeated repository records as replication.
```

**What to save:** a citable overlap register and an explicit evidence-counting rule. This can materially improve a research argument even when no new reading is proposed: the number of records, editions and independent witnesses may differ.

## 4. Comparing sign position: Cretan Hieroglyphic and Cypro-Minoan

**Your question:** “Does a proposed positional regularity survive differences in support, layout and modern segmentation?”

**Use:** [Cretan Hieroglyphic](https://github.com/hawkinsnick/Cretan-hieroglyphs) and [Cypro-Minoan](https://github.com/hawkinsnick/Cypro-Minoan).

**Bring:** bounded samples with recorded sign order, support, layout/orientation, segmentation conventions and source uncertainty. Any visual comparison additionally requires permitted, suitable images or attributed observations; catalogue identifiers alone are insufficient.

**Work through it:**

1. Make a table of available supports and layouts in each sample. Confirm whether “first,” “last” and “sequence” have compatible definitions.
2. Define eligible subsets with comparable recorded order. Keep sign identities within their own catalogues. Audit repeated impressions and shared source records before choosing independent units.
3. Choose one within-project positional measure and explain why comparing its distribution across projects is meaningful. Do not match signs merely because they share a catalogue number or look alike.
4. Examine the measure within support/layout categories before any aggregate comparison. Ask for a sensitivity analysis over documented boundary alternatives. Use descriptive results when sample size or dependence prevents justified inference.

**Copy this prompt:**

```text
Use my Cretan Hieroglyphic and Cypro-Minoan samples to investigate [explicit
positional question]. First define the native order, boundaries and unit in
each, then propose eligible comparable subsets. Show excluded cases and why.
Keep sign catalogues separate. Audit repeated impressions and source dependence.

Propose a positional measure with a declared denominator and explain its
comparability. Control for support/layout where the data permit. Show code
and sensitivity checks for any calculation; label unexecuted work as proposed.
Do not infer corresponding sound values, borrowing or shared language.
```

**What to save:** the eligibility table, separate positional concordances and an executed analysis with limitations—or a precise account of the missing layout evidence. Similar positional behavior is a descriptive observation requiring further explanation, not decipherment evidence by itself.

## 5. Comparing formula variation: Lydian and Phrygian

**Your question:** “Can I distinguish ancient formula variation from modern restoration practices in two separate language corpora?”

**Use:** [Lydian](https://github.com/hawkinsnick/Lydian) and [Phrygian](https://github.com/hawkinsnick/Phrygian).

**Bring:** source-attributed candidate formula passages in each language, with preserved/restored text distinguished and genre, date and provenance where supplied. If your question concerns funerary formulae, verify that the selected passages are actually classified as funerary and that the classification has a source. Do not assume either repository contains an exhaustive sample.

**Work through it:**

1. Build a concordance within each language using attributed readings. Keep diplomatic text, restoration, normalization and scholarly interpretation in separate columns.
2. Compare analytical problems first: how much of each proposed formula is preserved, how many assertions share an edition, and whether genre or date is known.
3. Reassess the distribution after excluding restored components. Compare the stability of the two analyses, using explicit denominators, rather than treating superficially similar strings as equivalent words.
4. Only investigate a lexical or historical connection if independent readings, contextual evidence and an appropriate linguistic method justify that further question.

**Copy this prompt:**

```text
Compare how restoration affects the formulae identified in my Lydian and
Phrygian packets. Verify each formula's attributed source and the basis for
its genre assignment. Build separate concordances showing preserved text,
supplied text, normalization, interpretation and source dependence.

Define what counts as an occurrence in each. Show what remains when restored
components are excluded, calculating only with declared inputs and execution.
Compare the robustness of the two analyses, not assumed lexical equivalence.
List alternative explanations and what further source work would distinguish
them. Do not infer cognacy, borrowing or a common formula from string similarity.
```

**What to save:** two attributed concordances, restoration-sensitivity results and a short methods comparison. The strongest supported outcome may concern which arguments are robust to editorial intervention, rather than a proposed relationship between the languages.

## Save a comparison another researcher can inspect

For any of these examples, finish with:

```text
Prepare a research packet containing the question, project revisions, files
actually inspected, source-linked tables, unit definitions, documented joins,
exclusions, code and execution status, results and unresolved issues. Draft
one short finding limited to this evidence, with its strongest alternative
explanation. Identify the exact source consultation or expert question needed
next. Preserve attribution and rights; do not include restricted source material
in a public packet without permission.
```

Use [the research log](USER-GUIDE.md#check-and-cite-the-result) to preserve the packet's provenance. The [comparability matrix](references/comparability-matrix.md) explains which additional evidence is required for stronger inferences. For examples within one project, see [the research example collection](RESEARCH-EXAMPLES.md).
