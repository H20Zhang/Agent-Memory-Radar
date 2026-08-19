# Curation Protocol

Agent Memory Radar is maintained as a **reader-facing living survey backed by auditable structured records**. Curated updates are written directly to `main`; repository automation exists only as a consistency guardrail.

## Public surface policy

`README.md` is the landing page for researchers, not a maintainer manual. Keep its structure aligned with the sibling [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) while preserving agent-memory-specific research questions.

### README information architecture

Default order:

1. **Latest Papers** — the newest accepted evidence is the first substantive section.
2. **What’s Changing** — weekly/monthly/yearly compactions; synthesis before chronology.
3. **Reading Paths** — about three short paths plus an optional “if you only read three papers” foldout.
4. **Research Map** — durable Key Anchors followed by Research Problems and their current arguments.
5. **How to Read a Paper Here** — explain the 30-second / 60-second / deep-dive layers.
6. **What Counts as Agent Memory? / About / Contributing** — compact scope, evidence standard, citation/reuse, and contribution entry points.

The first screenful may include one concise current-field thesis and a light star/cross-radar call to action. Optimize discoverability naturally around terms such as agent memory, LLM agents, long-term memory, procedural memory, benchmarks, and memory systems; never turn the page into a keyword list.

Do not expose scheduling, subagent internals, schema mechanics, binary-upload details, prompt text, backfill queues, or operational provenance on README.

### Latest-paper presentation

Use progressive disclosure:

- visible by default: title, primary category/tags, importance, date, a 1–2 sentence **AI take**, and verified paper/code/research-note links;
- inside `<details><summary><strong>Understand this paper in 60 seconds</strong></summary>`: **Problem**, **Core mechanism**, a compact memory/data/control loop when useful, **Compared with**, **Evidence to remember**, and **Open question**.

Keep roughly **8–10 latest papers**. The foldout should reveal the real delta without duplicating the full research note. Prefer one decisive ablation/result and one assumption that could change the importance judgment.

### What’s Changing / compactions

The public archive deliberately becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

Show every available weekly compaction from roughly the last 31 days, monthly maps from the last 3 calendar months, and all sufficiently covered yearly maps. Each entry must state a research conclusion, not merely link a file. Open months/years must be labeled rolling or incomplete.

### Reading Paths and Research Map

Maintain about **3 reading paths**. Each path should teach a tension or design boundary, not act as a topic dump.

Maintain about **5–8 durable anchors** in README and `papers/anchors.md`. Anchors are design points, not rankings or a recency leaderboard.

For each research problem on README and its category page, maintain:

- Current anchors / current evidence;
- Strongest signal;
- Biggest unresolved question;
- Next decisive evidence.

Category pages are living arguments rather than append-only paper lists.

## Inclusion boundary

Include work when **information persists or is explicitly managed across interaction/reasoning steps and materially changes a language or multimodal agent’s future behavior**.

Typical in-scope changes affect one or more of:

- write / event boundaries / extraction;
- persistent representation and organization;
- retrieval, navigation, evidence completion, selection, or admission;
- consumer-facing reconstruction/rebinding/reuse;
- update, consolidation, conflict repair, forgetting, or revocation;
- learned/evolved memory state or policy;
- evaluation of lifecycle cost, authority, provenance, safety, or marginal behavioral effect.

Do not include generic fixed RAG, generic long-context modeling, KV-cache optimization, or unrelated continual learning unless persistent agent memory is central to the research contribution.

## Multi-role daily process

Use independent roles when the execution environment supports them. Their judgments should be formed separately before synthesis.

1. **Discovery Agent** — broad overlapping recent discovery; optimize recall and search beyond the literal phrase `agent memory`.
2. **Relevance / Taxonomy Agent** — decide semantic inclusion and assign one primary research problem plus orthogonal tags.
3. **Research Analyst** — read the full paper deeply enough to identify the mechanism, memory lifecycle, comparison, evidence, limitations, and provenance.
4. **Skeptical Reviewer** — challenge novelty, closest comparison, causal attribution, importance, resource matching, unsupported claims, duplicate versions, and link quality.
5. **Visual Editor / Visual QA Reviewer** — only for required visuals; ground briefs in the full paper and reject generic or fabricated images.
6. **Research Editor** — publish only after seeing disagreements and corrections from the independent roles.

Relevant papers that are not sufficiently reviewed remain deferred/backfill candidates rather than being silently rejected.

## Canonical paper contract

For every accepted paper:

1. maintain `data/papers/<id>.json` as the canonical structured record;
2. maintain `papers/YYYY/<id>.md` as the researcher-facing note;
3. preserve TL;DR, Problem, Core Idea, Memory Design (`write / organize / read / update-forget`), Compared to What, Evidence, Why It Matters, Limitations/Questions, and confidence;
4. keep relevance separate from importance;
5. preserve provenance and add code/project links only when verified;
6. propagate a material correction upward to category pages, anchors, README, and affected compactions.

## Evidence discipline

The default causal lens is stage-specific:

`archive/representation → access program → evidence completion/selection/admission → consumer-facing state/reuse → update feedback/governance → lifecycle cost/provenance`

For every strong claim ask:

- **What actually changed?**
- **Compared with what?** Prefer the simplest matched alternative, not a weak straw baseline.
- **Which stage caused the gain?** Do not credit the whole architecture when several stages changed together.
- **What would falsify the interpretation?** Preserve negative results and stronger alternative explanations.

Unknowns remain unknown rather than being filled with plausible text.

## Importance scale

`relevance ∈ [0,1]` measures topical fit. `importance ∈ {1,...,5}` measures expected research significance.

- **5 — field-shaping:** changes an important abstraction, benchmark, or dominant research direction with unusually strong evidence.
- **4 — notable:** clear reusable technical/empirical delta researchers in agent memory should know.
- **3 — useful:** meaningful contribution but narrower delta, weaker attribution, or limited external validity.
- **2 — peripheral:** relevant but weak novelty/evidence or narrow scope.
- **1 — archival:** technically in scope but little reason to prioritize reading.

Recency and relevance do not imply importance.

## Visuals

Follow [`VISUAL_POLICY.md`](VISUAL_POLICY.md) and [`assets/README.md`](assets/README.md). A generated status is a publication claim: it is valid only when the exact WebP exists on `main`, the paper page embeds it, the image passed grounding/visual QA, and canonical metadata matches the published path.

## Compaction

Follow [`COMPACTION.md`](COMPACTION.md). Weekly/monthly/yearly reports are synthesis layers, not repeated paper summaries. A one-paper observation must be labeled an early signal.

## Validation and final QC

Before completing a maintenance run, reason against `scripts/validate.py` and the repository contracts. Check schema/taxonomy consistency, duplicate IDs/versions, paper-note existence, relative links, visual paths/embeds, important-paper visual blockers, README section order/bounds, and due compactions.

Daily provenance belongs under `runs/daily/YYYY/MM/DD.md` and should remain compact.

## Licensing and contributions

Research notes, category maps, compactions, canonical paper data, and original radar visuals are licensed under **CC BY 4.0**. Maintenance code is licensed under **MIT**. See [`LICENSE.md`](LICENSE.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).