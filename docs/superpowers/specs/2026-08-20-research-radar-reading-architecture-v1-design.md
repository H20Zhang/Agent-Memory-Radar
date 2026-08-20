# Research Radar Reading Architecture v1

Date: 2026-08-20

## Problem statement

Agent Memory Radar has strong research content but currently mixes four different reader jobs on the same surface: discovering what is new, learning the field, comparing research lines, and auditing evidence. The result is avoidable repetition. README repeats paper-note material, time-based digests carry too much navigational burden, and recurring maintenance can gradually re-expand the public surface even after manual cleanup.

This design turns the repository into a layered research reading system. The same canonical research judgment should project into different reading depths without being rewritten as the same paragraph in multiple places.

Scope: root README, paper-note editorial contract, research-library navigation, category pages, compactions, validation, and the recurring maintenance workflow that derives them.

Non-goals: building GitHub Pages or a standalone frontend; maximizing paper count; replacing full-paper reading; forcing every paper into identical prose; hiding weak evidence behind concise summaries.

## Design principles

1. **Scan first, deepen in place.** A new reader should understand the current field signal in tens of seconds. Important work should still expose a useful 60–90 second explanation directly from README through progressive disclosure.
2. **One claim, multiple projections.** Canonical data and evidence notes are the source of truth. README, categories, libraries, and compactions each add a different kind of compression rather than restating the same prose.
3. **Structure is fixed; language is not.** Research notes follow a stable reasoning sequence, but the editor must not force recurring sentence templates such as “the important delta is not …” across papers.
4. **Time is a view, not the archive key.** Weekly/monthly/yearly compactions explain change over time. Historical discovery should primarily use research problem, research line, and orthogonal tags.
5. **Claims must be auditable.** Any strong interpretation names the closest meaningful comparison, the decisive evidence, and what the evidence does not establish.

## External writing basis

This design adopts three durable ideas from external technical-writing and research norms:

- Google Technical Writing: summarize key points at the start, fit the document to the audience, organize large documents with progressive disclosure, and prefer specific verbs/nouns with one idea per sentence.
- Microsoft Style Guide: optimize for scanning before close reading; use crisp, direct language and fewer words.
- NeurIPS paper/reviewer checklists: claims should match experimental support and scope; limitations and assumptions should be explicit; reviewers should evaluate significance compared with prior work, not prose polish alone.

The repository should not depend on a third-party writing skill at runtime. Public skills such as `writing-clearly-and-concisely`, `ste-plain-writing`, and evidence-backed research-writing skills are treated as design references. The enforceable contract lives in this repository.

## Reading architecture

The repository exposes five projections of the same research record:

```text
canonical record
  ├─ 30 sec: README scan row
  ├─ 60–90 sec: README fold for high-value work
  ├─ 5–10 min: paper note / evidence audit
  ├─ topic view: Research Library + category argument
  └─ time view: weekly → monthly → yearly compaction
```

A reader should never need to understand repository maintenance mechanics to use any public surface.

## README contract

The root README becomes a research router with this top-level order:

```text
Latest Papers
What’s Changing
Field Map
Reading Paths
Research Library / Browse All
How to Use This Radar
Scope / About / Contributing
```

The first screen must answer four questions quickly: what this radar covers; the current field thesis; what changed recently; where to go deeper.

Expose compact depth navigation near the top:

`30 sec: Latest · 5 min: Field Map · 15 min: Reading Paths · Browse All`

### Latest Papers

Keep roughly 6–8 high-signal recent entries rather than a fixed quota of 8–10. Recency does not guarantee placement. Importance and field-map impact decide visibility.

Each visible entry contains:

- title, category/tags, date, importance;
- one-sentence **Research delta** answering `previous design → changed variable → consequence`;
- primary links;
- an inline `<details>` explainer only for importance >= 4/5 or a paper that materially changes the field map.

The fold is a 60–90 second causal explanation. It covers these information points, but the editor may merge them into 3–5 natural paragraphs instead of six mechanical mini-headings:

- problem that survives the strongest existing approach;
- what actually changed;
- execution/data/control flow;
- closest meaningful comparison;
- decisive evidence;
- strongest unresolved caveat.

The fold must not duplicate the paper note sentence-for-sentence. It is a compression written for comprehension, not a truncated mini-review.

### What’s Changing

Lead with 2–4 cross-paper shifts. Use the form `older assumption → new evidence → research implication`. Chronological compaction links come after the shifts and should stay terse.

### Field Map

Field Map precedes Reading Paths because a newcomer needs a mental model before a route through it. For Agent Memory, the canonical map is:

`experience/archive → write → organize → access/admission → consumer state → update/evolve/forget → governance/cost/provenance`

Map labels should explain concepts before naming papers. Each node links to the relevant category/library view.

### Reading Paths

Keep three or four paths maximum. Each path answers a research question and specifies what the reader should learn, not merely a sequence of titles.

## Research Explainer Standard

High-visibility paper notes follow a reasoning contract rather than an abstract-summary template.

1. **Research delta** — the smallest claim that makes the paper worth opening.
2. **Problem** — what still fails under the closest reasonable existing design.
3. **Mechanism** — the actual execution/data/control flow; name modules only when they affect the causal story.
4. **Closest comparison** — closest baseline, what is held fixed, and what still changes together.
5. **Decisive evidence** — the minimum 1–3 results or ablations that should update a researcher’s belief.
6. **What remains unproven** — strongest alternative explanation, unsupported attribution, or condition that would weaken the claim.
7. **Field-map consequence** — which design boundary or research question this paper changes.
8. **Related reading** — 2–4 adjacent works selected for contrast or continuation.

For Agent Memory, add a compact lifecycle projection when useful: `write / organize / read / update-forget / governance`. Do not force lifecycle fields when the paper does not meaningfully touch them.

The note should distinguish three epistemic levels explicitly in wording: paper-reported fact; curator interpretation; open hypothesis.

## Editorial standard

Create a repository-local Research Radar Editor contract and apply it to README, category prose, paper notes, and compactions.

Preferred prose:

- active voice and concrete verbs;
- specific system objects, operations, datasets, controls, and numbers;
- one main claim per paragraph;
- short topic sentence first;
- comparison before evaluation language;
- numbers only when they change the interpretation;
- direct uncertainty: `the paper does not isolate X`, `this supports the package more strongly than component Y`.

Avoid AI-house-style signals:

- repeated sentence skeletons across papers, especially `the important/interesting/meaningful delta is not X`;
- generic evaluative words without evidence or comparison (`important`, `significant`, `powerful`, `robust`, `novel`);
- synthetic three-part symmetry used only for rhythm;
- abstract nouns where a mechanism can be named (`framework`, `landscape`, `paradigm`, `capability`) unless technically necessary;
- promotional adjectives and decorative emoji/badges;
- conclusion-like restatement of the introduction.

A deterministic editorial linter should warn rather than blindly rewrite. It should check repeated lead-in phrases across recent notes, generic-judgment terms without nearby evidence/comparison cues, README section/order/depth contracts, and excessive duplication across public surfaces. The linter is a guardrail; human/research judgment remains authoritative.

## Research Library

Chronology remains available, but it is no longer the primary historical navigation model.

Generate or maintain a Research Library with three entry points:

- **Browse by Problem** — Representation & Organization; Retrieval & Access; Write/Update/Consolidation; Memory Learning & Evolution; Evaluation & Governance.
- **Browse by Research Line** — durable design/genealogy chains such as raw archive → structured memory → admission → consumer-state reconstruction, or static skill memory → evolving procedural memory → evolving retrieval policy.
- **Browse by Year** — compact chronological index for provenance and recency lookup.

Orthogonal tags provide secondary filtering: episodic, semantic, procedural, multimodal, raw, structured, graph, timeline, personalization, acting-agent, and other controlled taxonomy values.

A historical paper should remain discoverable even after it leaves Latest Papers. Weekly digests must never be the only route to old work.

## Layer responsibilities

- `data/papers/*.json`: canonical identity, structured metadata, evidence status, links, taxonomy, provenance.
- `papers/YYYY/*.md`: evidence layer; closest comparison, decisive evidence, caveats, full research interpretation.
- `categories/*.md`: argument layer; current tensions, design boundaries, what evidence would decide them.
- Research Library/index: retrieval layer over the historical corpus.
- `digests/*`: temporal synthesis layer; what changed and which prior beliefs weakened/strengthened.
- root README: judgment/router layer; what matters now and where to read next.

Do not copy the same paragraph across these surfaces.

## Maintenance workflow

The scheduler becomes thin. Repository-owned workflow defines behavior.

Each maintenance transaction follows:

`preflight → discover → independent judgment → canonical update → evidence note → relationship/category update → derive reader projections → editorial review → validate → log → notify only if material`

A new paper does not automatically modify every surface. Update a surface only when the paper creates reader value at that level.

README folds are derived editorial artifacts, not canonical text fields. Category or Reading Path changes require a field-level consequence, not mere recency.

## Validation

Extend deterministic validation with reader-facing contracts:

- README section order and latest-entry bounds;
- fold eligibility and required information coverage for high-visibility entries;
- paper-note section/semantic contract without requiring exact prose headings;
- every README item resolves to a note and canonical record;
- historical records remain reachable through at least one Research Library route;
- no maintenance/scheduler internals leak to public surfaces;
- repeated house-style phrase warnings over a rolling set of notes;
- duplicate-paragraph or high-similarity warnings across README/category/note/compaction;
- existing schema, taxonomy, link, visual, and compaction checks continue to pass.

Editorial warnings should not reject a correct research update solely because a specific word appears. Detect pattern density, not banned vocabulary.

## Migration

The first migration is structural, not a wholesale rewrite of every historical note.

1. Rebuild README to the new order and progressive-depth contract.
2. Preserve valuable existing 60-second content but rewrite it to remove duplication and recurring sentence templates.
3. Add the Research Library entry surface and connect existing category/year indexes.
4. Add the repository-local Research Radar Editor standard and editorial linter.
5. Update maintenance docs/workflow so future runs preserve the structure.
6. Backfill past high-importance notes opportunistically, prioritizing works that appear in Reading Paths, anchors, or current field arguments.

Do not churn old notes merely to make all files cosmetically identical.

## Success criteria

A successful v1 should let a reader:

- identify the current Agent Memory thesis and top recent changes within 30 seconds;
- understand an important new paper from README alone in roughly 60–90 seconds;
- reach causal evidence and caveats in one click;
- find older work by research problem or research line without knowing its publication week;
- distinguish paper claims from curator interpretation;
- read several consecutive notes without detecting a repetitive AI-generated house style.

The maintainer should be able to change the public reading contract in repository files without rewriting a giant scheduler prompt.