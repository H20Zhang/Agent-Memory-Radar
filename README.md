# 🧠 Agent Memory Radar

**A living research map of memory for AI agents.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-14 · [Research compactions](#-research-compactions) · [Latest papers](#-latest-papers) · [Browse by research problem](#-browse-by-research-problem)

## 🧭 Research Compactions

The archive deliberately becomes coarser with time: `recent month → weekly` · `recent quarter → monthly` · `all years → yearly`.

### Recent Month · Weekly

**[2026-W32 · Structure only matters when control can use it](digests/weekly/2026-W32.md)**  
The closed Aug 3–9 week established the first correction to “more structure is better”: controller↔memory coupling and consumer-compatible granularity matter, while plausible extra typing can fail to beat a simpler dynamic policy. **W33 (Aug 10–16) is still open**, so no partial weekly report is presented as finished.

### Recent Quarter · Monthly

**[2026-08 · Rolling through Aug 14](digests/monthly/2026-08.md)**  
The August map now separates six stages: **archive/representation → access policy → selected evidence → consumer-facing reuse → lifecycle update/cost → provenance & revocation**. ReFind raises the baseline for semantic preprocessing, QCR isolates post-retrieval reuse, LycheeMemory V2 makes consolidation granularity explicit, and Practice Makes Unsafe resolves persistent adaptation into auditable lifecycle gates.

The main correction is methodological: **credit memory complexity only at the stage where a matched simpler alternative fails.**

### All Years · Yearly

**[2026 · Rolling, incomplete research map](digests/yearly/2026.md)**  
Active curation starts in August with one July backfill, so this is **not a full-year reconstruction**. Within current coverage, agent memory is becoming a multi-stage state interface whose transformations, access, consumer adaptation, cost, and provenance need separate accounting.

[Browse all compactions →](digests/README.md)

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **When structure is actually necessary** | [ReFind](papers/2026/2608.12888.md) → [MESA](papers/2026/2608.10108.md) → [MAP-Graph](papers/2026/2608.10509.md) | Preprocessing must beat a competent raw-record interface; access policy also decides which view to expose and whether evidence is admissible. |
| **What happens after retrieval succeeds** | [QCR](papers/2026/2608.12847.md) → [PMCoder](papers/2026/2608.06811.md) → [Agent Skills Can Be Harmful](papers/2026/2608.11888.md) | Selection is not reuse: current bindings, controller state, and marginal procedural effect determine whether retrieved experience helps. |
| **Why memory is a lifecycle system** | [LycheeMemory V2](papers/2026/2608.12990.md) → [Total Recall](papers/2026/2608.11879.md) → [Practice Makes Unsafe](papers/2026/2608.12851.md) | Write cadence changes cost, serving economics are end-to-end, and persistent updates require attribution/revocation. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**ReFind** raises the baseline for every structured-memory paper: raw chat plus competent stateful search can recover much of the value credited to semantic preprocessing.

**QCR** exposes the next bottleneck: even the correct long trajectory can be the wrong actor-facing representation when source bindings are stale.

**LycheeMemory V2** adds the write-side systems knob: when consolidation runs can matter as much as what it stores.

Together they move the field from “design a better memory store” toward **accounting for each transformation and interface separately**.

</details>

## 🔥 Latest Papers

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `episodic` `text` `timeline` · **★★★★☆** · 2026-08-13

**AI take:** The strongest new negative control for structured memory. A raw chat archive plus iterative lexical search and chat-native controls beats the compared graph/tree systems on precise refinding; the result is about **interface quality**, not “BM25 beats semantics.”

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2026/2608.12888.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Structured memory may be credited for gains that actually come from a better retrieval interface than the flat baseline.

**Core mechanism.** Raw timestamped turns → turn-level BM25 → multi-round ReAct search → session-RRF + ±2 context + time filter + seen-session dedup → saved verbatim notes → separate answer stage.

**Compared with.** Single-shot BM25, matched generic-agentic BM25 with the same controller but no chat-native controls, and graph/tree/note memory systems.

**Evidence to remember.** On fixed LongMemEval-S/M: **93.2/89.3 ReFind vs 78.7/82.2 generic-agentic BM25 vs 84.7/68.9 one-search**. On six MemoryAgentBench tasks ReFind averages 58.2 vs HippoRAG 2 at 53.2.

**Open question.** Does raw-record agentic search still win when online token/latency budgets are strictly matched on semantic or tool-acting tasks?

</details>

### [Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories](papers/2026/2608.12847.md)
`Representation & Organization` · `procedural` `text` `web-agent` · **★★★★☆** · 2026-08-13

**AI take:** Retrieval and reuse are different stages. With the same selected trajectory, a compact target-bound support object beats direct trace injection by forcing stale source bindings to be reacquired from current state.

[Paper](https://arxiv.org/abs/2608.12847) · [Research note](papers/2026/2608.12847.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A relevant past trajectory can still mislead the actor when users, files, IDs, dates, or environment state changed.

**Core mechanism.** Fixed retrieval/selection → QCR writes `workflow invariant + bindings to re-obtain + applicability conditions + verification guardrail` from the selected trajectory, target query, and initial state → actor grounds current values before execution.

**Compared with.** No memory, the same Full Trajectory, and a length-matched source-only Generic Summary under matched actor/target/tool conditions.

**Evidence to remember.** **62.3% Success, +10.7pp over Full Trajectory, −48.9% online tokens**; under large binding shift, stale-binding errors **46.9%→10.9%** and correct rebinding **31.7%→77.8%**.

**Open question.** Can target-conditioned reuse remain faithful when multiple memories conflict or the support writer itself can hallucinate missing constraints?

</details>

### [Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents](papers/2026/2608.12851.md)
`Evaluation & Analysis` · `procedural` `structured` `general-agent` · **★★★★☆** · 2026-08-13

**AI take:** Persistent adaptation has multiple safety gates. Unsafe skill authoring, later retrieval, and fresh-session harm are not the same event; governance needs attribution and revocation across the whole evolution lifecycle.

[Paper](https://arxiv.org/abs/2608.12851) · [Code](https://github.com/henrymao2004/misevolve) · [Research note](papers/2026/2608.12851.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** “Successful” trajectories can contain unsafe shortcuts that self-improvement turns into persistent reusable policy.

**Core mechanism.** Version skill state across malicious exposure → evolution → later retrieval → clean-session execution; SafeEvolve adds lineage-aware repair, risk-aware retrieval, outcome attribution, and retirement.

**Compared with.** No evolution, multiple native skill-evolution methods, raw evolution, and utility-only/alternative governance conditions.

**Evidence to remember.** All **21 evolved configurations** author unsafe artifacts, but only **15** cause fresh-session harm. Three malicious tasks raise carryover ASR **16.0%→35.3%**; SafeEvolve reduces unsafe retrieval **35.33%→8.67%** and carryover ASR **21.33%→4.00%** averaged over two methods.

**Open question.** Can lifecycle governance generalize from controlled skill libraries to implicit memory/policy updates over months of real agent use?

</details>

### [LycheeMemory V2: Efficient Long-Term Memory via Semantic Segment-Level Consolidation](papers/2026/2608.12990.md)
`Write, Update & Consolidation` · `semantic` `structured` `timeline` · **★★★★☆** · 2026-08-13

**AI take:** Consolidation granularity is a first-class systems parameter. Batching cuts write-side LLM frequency; semantic boundaries—not batching alone—preserve the quality that fixed windows lose.

[Paper](https://arxiv.org/abs/2608.12990) · [Research note](papers/2026/2608.12990.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Per-turn LLM consolidation is expensive; arbitrary batching is cheap but can split coherent events and erase temporal/reference evidence.

**Core mechanism.** Online semantic boundary detection → one LLM encode per finalized segment → typed self-contained records + provenance/indexes → planned multi-route retrieval and deterministic fusion.

**Compared with.** Eager per-turn construction, fixed-window batching, and A-Mem/Mem0/TiMem/MemoryOS-style conversational memory.

**Evidence to remember.** LoCoMo: **89.22 / 204.1K construction tokens** full vs **81.88 / 849.9K** eager and **82.40 / 174.7K** fixed-window. Relative to A-Mem, construction tokens fall **86.0%**.

**Open question.** Do embedding-defined semantic boundaries survive tool events, conflicts, asynchronous state, and other non-conversational agent streams?

</details>

### [Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems](papers/2026/2608.11879.md)
`Evaluation & Analysis` · `semantic` `text` `general-agent` · **★★★★☆** · 2026-08-12

**AI take:** Dedicated memory is not automatically cheaper than resending history. Break-even is a workload- and architecture-dependent lifecycle property, not a consequence of smaller retrieved context.

[Paper](https://arxiv.org/abs/2608.11879) · [Research note](papers/2026/2608.11879.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Answer-context size ignores ingest, reflection, consolidation, and retrieval model calls.

**Core mechanism.** Replay matched conversations through Mem0, Hindsight, Mastra OM, rolling window, and full history; meter native lifecycle cost and compute sustained break-even.

**Compared with.** Full-history resubmission and a ten-turn rolling window under matched workload/backbone settings where controllable.

**Evidence to remember.** Break-even spans **0–86 turns (Mastra), 0–342 (Mem0), 60–never (Hindsight)**; a simple depth/message-size model misses memory-system cost by **18–69%**.

**Open question.** What changes when memory ingest/reflection runs locally or orders of magnitude cheaper than the answer model?

</details>

### [Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents](papers/2026/2608.11888.md)
`Evaluation & Analysis` · `procedural` `text` `general-agent` · **★★★★☆** · 2026-08-12

**AI take:** Topical relevance is a weak admission test for procedural memory. A matching skill can impose the wrong implementation detail or a disproportionately expensive execution path.

[Paper](https://arxiv.org/abs/2608.11888) · [Research note](papers/2026/2608.11888.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Outcome comparisons confound skill effect with task/model/environment differences and can hide large efficiency regressions.

**Core mechanism.** Hold task/harness/model/environment fixed → compare target skill with no skill or matched alternative → inspect paired trajectories/outcomes/cost.

**Compared with.** Skill benchmarks that report endpoint success without matched mechanism-level attribution.

**Evidence to remember.** Among **307 confirmed cases**, Task-Implementation Fault is **86/125** functional failures; Excessive Procedure is **114/182** efficiency failures.

**Open question.** Can a selector estimate the *marginal effect* of a procedural memory before paying the execution cost?

</details>

### [The Sleeping Agent: What Gist-Based Context Compression Loses and Why](papers/2026/2608.11775.md)
`Write, Update & Consolidation` · `semantic` `text` `timeline` · **★★★☆☆** · 2026-08-12

**AI take:** Compression is selective forgetting. A generic gist prompt preserved entities/events while systematically deleting temporal anchors that later “when?” questions required.

[Paper](https://arxiv.org/abs/2608.11775) · [Code](https://github.com/kyrkewood/sleeping-agent) · [Research note](papers/2026/2608.11775.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Aggregate compression quality can hide a low-volume but decision-critical field being systematically erased.

**Core mechanism.** Diagnose preservation by content type, then change only the gist prompt to explicitly protect temporal expressions.

**Compared with.** The same SWC compression pipeline before temporal protection plus truncation/sliding/full-context controls.

**Evidence to remember.** Temporal-expression preservation rises **3.05%→62.39% (~20×)** and temporal judge accuracy improves **+0.314**.

**Open question.** Which other sparse fields—authority, identifiers, provenance, constraints—are silently deleted by mainstream compressors?

</details>

### [Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem](papers/2026/2608.11654.md)
`Evaluation & Analysis` · `general-agent` · **★★★☆☆** · 2026-08-12

**AI take:** A useful attempt to separate the stored event basis from the knowledge it can generate and to define capacity-constrained memory independently of one implementation. Current value is conceptual rather than empirical.

[Paper](https://arxiv.org/abs/2608.11654) · [Research note](papers/2026/2608.11654.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Different memory systems use incompatible representations and metrics, so “optimal memory” is difficult to state cleanly.

**Core mechanism.** Define stored events as a basis, a generation operator as span, capacity-constrained utility as a frontier, and sequential writing as an MDP with delayed query-time reward.

**Compared with.** Representative systems mapped into one formal write/read framework rather than empirically outperformed.

**Evidence to remember.** Under decomposable span assumptions, capacity-constrained writing reduces to weighted maximum coverage with the classical greedy **(1−1/e)** guarantee; cross-event synergy breaks it.

**Open question.** Does the proposed capacity frontier predict actual system quality once answer-time composition and reasoner error matter?

</details>

### [MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows](papers/2026/2608.10509.md)
`Retrieval & Access` · `semantic` `graph` `general-agent` · **★★★★☆** · 2026-08-11

**AI take:** The contribution is not “memory as a graph.” It separates **may read**, **how much inherited trust**, and **is sufficient for this action** into distinct memory-control boundaries.

[Paper](https://arxiv.org/abs/2608.10509) · [Research note](papers/2026/2608.10509.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Relevant derived evidence can inherit restrictions not visible in local text/metadata.

**Core mechanism.** Semantic candidates → hard `CanRead` filtering → `semantic × recursive path trust` reranking → action-risk gate, with lineage-aware revocation.

**Compared with.** Shared/isolated vector memory and a flat-provenance control with rich local metadata but no recursive ancestry propagation.

**Evidence to remember.** Removing trust propagation lowers task success **94.96%→87.37%** and raises adverse action **1.52%→8.56%**; removing permission filtering makes conditional unauthorized access **100%**.

**Open question.** Do these boundaries remain useful over months-long real workflows rather than a synthetic short multi-agent setting?

</details>

### [MESA: Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory](papers/2026/2608.10108.md)
`Retrieval & Access` · `episodic` `structured` `general-agent` · **★★★★☆** · 2026-08-10

**AI take:** Multi-memory should not mean route-to-one or read-everything. The useful result is that many queries need **several structures but not all of them**; a strong coarse router is already close, so do not over-credit selector sophistication.

[Paper](https://arxiv.org/abs/2608.10108) · [Research note](papers/2026/2608.10108.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** One representation loses complementary evidence; all representations add noise and context cost.

**Core mechanism.** Build fixed summary/temporal/graph/vector/raw views → query-adaptive subset selection → native retrieval from selected views → evidence composition.

**Compared with.** Route-to-one, all-five, random/zero-shot selection, and coarse domain/capability routing.

**Evidence to remember.** **57.0% route-to-one → 63.7% all-five / 18.7k tokens → 65.1% MESA / 11.0k**; coarse domain routing already reaches 64.4%.

**Open question.** How much benefit survives when views evolve online rather than being fixed and hand-chosen?

</details>

## 📌 Design Anchors

Design anchors are durable **design points, not a ranking**.

| Anchor | Design point |
|---|---|
| [LeanMem](papers/2026/2608.03463.md) | heterogeneous lifecycle contracts |
| [V-Mem](papers/2026/2608.01543.md) | structural same-round cross-modal access |
| [ReFind](papers/2026/2608.12888.md) | raw archive + stateful query-time search |
| [QCR](papers/2026/2608.12847.md) | post-retrieval target-conditioned reuse |
| [PMCoder](papers/2026/2608.06811.md) | bidirectional controller↔memory coupling |
| [RoMeRL](papers/2026/2608.02508.md) | reduced-order feedback-bearing state |
| [AuthMem-Bench](papers/2026/2608.01679.md) | authority as memory correctness |
| [SkillJack](papers/2026/2608.03509.md) | transitive provenance/revocation across derived skills |

[How the anchors fit together →](papers/anchors.md)

## 🔬 Browse by Research Problem

| Category | Current argument |
|---|---|
| [Representation & Organization](categories/representation-organization.md) | Archival fidelity and actor-facing memory can be different objects; QCR makes post-selection representation explicit. |
| [Retrieval & Access](categories/retrieval-access.md) | ReFind raises the baseline from one-shot top-k to stateful raw-record search; MESA/MAP-Graph add selection and admissibility. |
| [Write, Update & Consolidation](categories/write-update-consolidation.md) | LycheeMemory V2 separates consolidation frequency from semantic boundary quality; Sleeping Agent exposes field-level preservation. |
| [Memory Learning & Evolution](categories/memory-learning-evolution.md) | Learned/transferred memory needs bounded policy state and consumer-compatible substrate. |
| [Evaluation & Analysis](categories/evaluation-analysis.md) | Cost, marginal behavioral effect, unsafe write/read state, and revocation are independent axes—not one recall score. |

<details><summary><strong>Representation & Organization — living argument</strong></summary>

**Current anchors:** QCR, LeanMem, PGMem.  
**Strongest signal:** the persistent record and the consumer-facing support can be different representations.  
**Biggest unresolved question:** when does target-conditioned transformation preserve provenance rather than hallucinate procedure?  
**Next decisive evidence:** matched raw/source-summary/target-conditioned/executable representations under binding shift and multi-memory conflict.

</details>

<details><summary><strong>Retrieval & Access — living argument</strong></summary>

**Current anchors:** ReFind, MESA, MAP-Graph, PMCoder, V-Mem.  
**Strongest signal:** access policy can dominate representation complexity; it also controls structure choice, controller conditioning, and admissibility.  
**Biggest unresolved question:** does precomputed semantic memory still win when online compute/latency is matched to strong raw-record search?  
**Next decisive evidence:** factorial representation × access-policy experiments on acting-agent tasks with matched budgets.

</details>

<details><summary><strong>Write, Update & Consolidation — living argument</strong></summary>

**Current anchors:** LycheeMemory V2, Sleeping Agent, Scrub Jay, MERIT.  
**Strongest signal:** write cadence/granularity and field preservation are separate policy decisions.  
**Biggest unresolved question:** can boundaries/preservation/forgetting be learned cheaply under streaming conflicts?  
**Next decisive evidence:** long-running update benchmarks reporting construction cost, conflicts, preserved fields, storage growth, and action quality.

</details>

<details><summary><strong>Memory Learning & Evolution — living argument</strong></summary>

**Current anchors:** RoMeRL, Agent Memory Distillation, HyMeS, MemoryCPT.  
**Strongest signal:** rich evidence does not imply one adaptive variable per record; transferable memory must match the consumer's control granularity.  
**Biggest unresolved question:** which adaptive state belongs in learned scores, symbolic state, code, or external artifacts?  
**Next decisive evidence:** cross-model/task transfer under matched retrieval and explicit negative-transfer accounting.

</details>

<details><summary><strong>Evaluation & Analysis — living argument</strong></summary>

**Current anchors:** Practice Makes Unsafe, Total Recall, Agent Skills, AuthMem-Bench, SkillJack.  
**Strongest signal:** endpoint success can hide lifecycle cost, unsafe writes, invalid reads, and harmful descendant state.  
**Biggest unresolved question:** what small evaluation vector predicts real deployment value without collapsing these axes?  
**Next decisive evidence:** long-running tool-use deployments with no-memory/alternative-memory counterfactuals and per-stage attribution.

</details>

<details><summary><strong>Scope and ratings</strong></summary>

**In scope:** persistent or cross-step state that materially changes a language/multimodal agent's future behavior. Generic RAG, KV-cache work, long-context modeling, or continual learning is excluded unless memory is a central agent mechanism.

**Importance:** ★★★★★ field-shaping · ★★★★☆ notable technical/empirical delta · ★★★☆☆ useful but narrower/incremental · ★★☆☆☆ peripheral · ★☆☆☆☆ archival. Relevance and importance are scored separately.

</details>
