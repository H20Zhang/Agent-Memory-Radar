# Maintainer Guide

This page collects repository-maintenance details that are intentionally kept out of the audience-facing README.

## Source of truth

- `data/papers/*.json` — canonical structured paper records.
- `papers/YYYY/*.md` — researcher-facing notes grounded in the full paper.
- `categories/*.md` — living arguments by research problem.
- `papers/anchors.md` — bounded durable design points.
- `digests/weekly/`, `digests/monthly/`, `digests/yearly/` — research compactions at decreasing temporal resolution.
- `assets/visuals/` — published researcher-facing WebP explainers and synthesis maps.
- `runs/daily/` — compact archival provenance for each maintenance run.

## Maintenance contracts

- [`../CURATION.md`](../CURATION.md) — inclusion, role separation, evidence, publication, and QC rules.
- [`../COMPACTION.md`](../COMPACTION.md) — weekly/monthly/yearly synthesis and correction rules.
- [`../VISUAL_POLICY.md`](../VISUAL_POLICY.md) — GPT Image grounding and visual-QA protocol.
- [`../assets/README.md`](../assets/README.md) — binary visual publication contract.
- [`../taxonomy.yaml`](../taxonomy.yaml) — controlled primary research problems and orthogonal tags.
- [`../data/paper.schema.json`](../data/paper.schema.json) — canonical record schema.
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — public paper/correction contribution path.

## Editorial separation

The root `README.md` is a public research landing page. It should let a researcher answer, in order:

1. What are the newest papers worth inspecting?
2. What changed in the field recently?
3. What is the shortest reading path for the design question I care about?
4. How is the current design space organized?
5. What evidence standard and scope does this radar use?

Operational details — scheduling, prompt text, file-generation mechanics, upload paths, schema internals, and backfill queues — belong here or in the contracts above, not in README.

## Researcher-first presentation

The public surface should feel like a **living survey**, not a GitHub dashboard or product landing page.

- Prefer restrained headings, whitespace, tables, and short argument paragraphs over cards, badges, emoji-heavy headings, or decorative status UI.
- Research content dominates the first screen. Star/cross-radar calls to action are secondary and should not interrupt the main reading flow.
- Use **Research take** for curator interpretation on public pages; avoid “AI take” as a visual label.
- Use compact numeric importance (`4/5`) where researchers compare rows quickly; star glyphs are optional in prose but should not dominate tables.
- README is the **judgment layer**; category pages are the **argument layer**; paper notes are the **evidence layer**; compactions are the **temporal synthesis layer**. Avoid repeating the same paragraph across all four.
- Deep pages should expose a short route back to Research Map/Reading Paths and, where natural, one `Continue` link to the next adjacent research problem.
- Aesthetic changes are successful only when they reduce time-to-comparison or time-to-evidence. Do not add decorative visuals to make the repository feel “designed.”

## Paper-note reading contract

Paper notes should read like compact mini reviews, not reformatted abstracts. For papers currently visible in README Latest Papers, keep this order:

`navigation → metadata → Research delta → Problem → Mechanism → Compared with → Decisive evidence → Main caveat → Memory lifecycle → Why it matters → Related reading`

The **Research delta** should state the smallest claim that makes the paper worth opening. **Compared with** should foreground the closest causal control. **Decisive evidence** should contain the minimum result/ablation set needed to support the interpretation rather than every table cell. **Main caveat** should surface the strongest alternative explanation plus concrete questions that could change the importance judgment.

Keep maintenance-only visual-generation failures, scheduler state, upload blockers, and operational provenance out of researcher-facing notes; canonical JSON and run logs remain the audit surface for those details.

## Update flow

For an accepted paper:

1. verify canonical identity and primary sources;
2. update/create `data/papers/<id>.json`;
3. update/create `papers/YYYY/<id>.md` using the paper-note reading contract for high-visibility work;
4. update the relevant category argument;
5. update README Latest Papers if the work is within the current bounded window;
6. change Reading Paths / Key Anchors only when the design map materially changes;
7. propagate corrections into due weekly/monthly/yearly compactions;
8. handle required visual publication according to the visual contract;
9. write one compact daily provenance log;
10. run repository validation before finishing.

## README contract

Keep the sibling-radar structure:

`Latest Papers → What’s Changing → Reading Paths → Research Map → How to Use This Radar → Scope/About/Contributing`

Inside **Research Map**, place **Key Anchors** before **Research Problems**. Avoid adding another top-level section for information already represented by these surfaces.

Latest Papers should stay at roughly 8–10 entries. Anchors should stay around 5–8 and should change slowly.

**What’s Changing** should lead with 2–4 cross-paper research shifts before chronological compaction links. Prefer `old assumption → new evidence → research implication` over a list of weekly summaries.

## Repository discoverability

Keep GitHub About metadata concise and research-specific. The description should explain the reader value rather than say only “paper list”. A good current description is:

> Track the latest agent memory research for LLM agents — papers, design anchors, benchmarks, visual explainers, and weekly/monthly/yearly research compactions.

Prefer specific, high-intent GitHub topics over generic labels. Recommended topic set:

`agent-memory` · `llm-agents` · `ai-agents` · `long-term-memory` · `memory-systems` · `procedural-memory` · `memory-management` · `agentic-ai` · `rag` · `retrieval-augmented-generation` · `benchmarks` · `research-papers` · `literature-review` · `multimodal-agents`

Avoid low-signal topics such as `agent`, `paper`, or `awesome-list` when more specific terms are available. The Website field is intentionally optional; this radar does not depend on personal-homepage routing.

## Validation

`python scripts/validate.py` checks the contracts that can be verified locally and deterministically, including:

- schema and taxonomy consistency;
- duplicate/file-ID mismatches;
- paper-note existence;
- repository-relative Markdown links;
- generated visual path/embed consistency;
- documented blockers for important papers without a generated visual;
- README section order, Latest Papers count, anchor count, and public terminology;
- category-page Research take / unresolved-question / next-evidence contracts;
- high-visibility paper-note navigation and mini-review section order.

External URLs are not treated as a CI hard dependency because transient network failures should not break repository validation. Verify important external paper/code/project links during curation instead.

## Visual publication

Do not stage binary fragments or use paper-ID-specific assembly workflows as a long-term publication mechanism. The canonical path is the Git data flow documented in [`../assets/README.md`](../assets/README.md), with the binary and its Markdown/JSON references committed together.

A `generated` state is only valid after reading back `main` and verifying the exact asset and references.

## Licensing

Research content and canonical data use **CC BY 4.0**. Maintenance code uses **MIT**. See [`../LICENSE.md`](../LICENSE.md).
