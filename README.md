# 🧠 Agent Memory Radar

**A living research map of memory for AI agents.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-16 · [Research compactions](#-research-compactions) · [Latest papers](#-latest-papers) · [Browse by research problem](#-browse-by-research-problem)

## 🧭 Research Compactions

The archive deliberately becomes coarser with time: `recent month → weekly` · `recent quarter → monthly` · `all years → yearly`.

### Recent Month · Weekly

**[2026-W32 · Structure only matters when control can use it](digests/weekly/2026-W32.md)**  
The closed Aug 3–9 week established the first correction to “more structure is better”: controller↔memory coupling and consumer-compatible granularity matter, while plausible extra typing can fail to beat a simpler dynamic policy. **W33 (Aug 10–16) is still open at the current UTC+8 run time**, so no partial weekly report is presented as finished.

### Recent Quarter · Monthly

**[2026-08 · Rolling through Aug 16](digests/monthly/2026-08.md)**  
The August map now separates **archive/representation → access program → evidence completion/selection → consumer-facing reuse → update feedback/governance → lifecycle cost/provenance**. ReFind raises the raw-record baseline; RippleMem shows when structure still earns complexity through evidence completion; SkillEvo and ERSkill move self-improvement into the feedback surface and the read policy itself.

The methodological rule is getting stricter: **credit memory complexity only at the stage where a matched simpler alternative fails.**

### All Years · Yearly

**[2026 · Rolling, incomplete research map](digests/yearly/2026.md)**  
Active curation starts in August with one July backfill, so this is **not a full-year reconstruction**. Within current coverage, agent memory is becoming a multi-stage state interface whose access programs, reuse transforms, evolution signals, cost, and provenance need separate accounting.

[Browse all compactions →](digests/README.md)

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **When structure actually earns its cost** | [ReFind](papers/2026/2608.12888.md) → [RippleMem](papers/2026/2608.13334.md) → [MESA](papers/2026/2608.10108.md) | A competent raw-record interface is the baseline; structure matters when it enables evidence completion or selective access that online search cannot cheaply recover. |
| **What happens after retrieval succeeds** | [QCR](papers/2026/2608.12847.md) → [PMCoder](papers/2026/2608.06811.md) → [Agent Skills Can Be Harmful](papers/2026/2608.11888.md) | Selection is not reuse: current bindings, controller state, and marginal procedural effect determine whether retrieved experience helps. |
| **How memory becomes self-improving state** | [SkillEvo](papers/2026/2608.13120.md) → [ERSkill](papers/2026/2608.12720.md) → [Practice Makes Unsafe](papers/2026/2608.12851.md) | Evolution depends on the feedback surface, the policy being evolved, and governance of the persistent descendants it creates. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**ReFind** raises the baseline for every structured-memory paper: raw chat plus competent stateful search can recover much of the value credited to semantic preprocessing.

**RippleMem** supplies the necessary counterexample: pre-built associations can still justify themselves when they turn a retrieved memory into a query for missing evidence and beat a more matched recollection control.

**QCR** exposes the next bottleneck: even the correct trajectory can be the wrong actor-facing representation when source bindings are stale.

Together they frame a sharper question than “what is the best memory architecture?”: **what operation is enabled at each stage, and does it beat the simplest matched alternative?**

</details>

## 🔥 Latest Papers

### [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](papers/2026/2608.13334.md)
`Retrieval & Access` · `episodic` `graph` `structured` · **★★★★☆** · 2026-08-13

**AI take:** The useful result is not “graphs beat flat memory.” First-hop memories become **anchors for missing-evidence search**, and a matched RF-Mem control suggests the gain survives after holding RippleMem's memory units and evidence budget fixed.

[Paper](https://arxiv.org/abs/2608.13334) · [Research note](papers/2026/2608.13334.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A relevant first-hop memory may be incomplete when answer evidence is distributed across sessions; unguided expansion can retrieve related but non-supporting memories.

**Core mechanism.** Cue-rich event memories + sparse semantic/structural graph → hybrid first-hop recall → controller decides whether support is missing → choose anchors + missing-support target → bounded local graph expansion → budgeted evidence assembly.

**Memory loop.** `event extraction → sparse associations → first-hop recall → planned recollection → evidence completion → answer`

**Compared with.** RF-Mem using RippleMem's extracted units and the same evidence budget, plus SimpleMem/Mem0/Zep/MemOS-style and graph-memory baselines.

**Evidence to remember.** LoCoMo LLM-judge: **87.14** full vs **83.83** matched RF-Mem; removing graph expansion gives **83.12**, and removing planned recollection **84.35**.

**Open question.** Does associative recollection still justify build/query cost on acting agents when online latency is matched to raw-record search?

</details>

### [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](papers/2026/2608.13120.md)
`Memory Learning & Evolution` · `procedural` `structured` · **★★★★☆** · 2026-08-13

**AI take:** The strongest result is a feedback-source ablation: **multi-turn interaction keeps exposing useful defects after single-turn feedback saturates**. Governance matters too, but mainly by limiting regression and bloat rather than driving most of the score gain.

[Paper](https://arxiv.org/abs/2608.13120) · [Research note](papers/2026/2608.13120.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Procedural-memory evolution can plateau once obvious single-turn defects are fixed, while repeated editing can accumulate factual regression and structural bloat.

**Core mechanism.** Multi-turn user simulation → failure attribution → evidence-bounded skill/reference edits → independent governance → persist inspected checkpoint → repeat.

**Memory loop.** `interaction → diagnose skill defect → revise persistent skill → govern → evaluate → next interaction`

**Compared with.** Original production Skills, multi-round self-reflection, and single-turn-QA-driven evolution with attribution/revision/governance otherwise matched.

**Evidence to remember.** Four-round task success reaches **81.8%** vs **66.4%** for the matched single-turn-QA condition; without governance it is **78.6%**, but cumulative bloat rises **+2.8%→+16.2%**.

**Open question.** Does the multi-turn advantage survive real-user feedback outside cloud technical support, rather than a high-fidelity simulator?

</details>

### [ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval](papers/2026/2608.12720.md)
`Memory Learning & Evolution` · `procedural` `structured` · **★★★★☆** · 2026-08-13

**AI take:** ERSkill makes the **read policy itself persistent evolvable state**: executable retrieval skills and the router co-evolve, while capability/deploy frontiers acknowledge that an oracle-good skill is useless if the controller cannot reliably activate it.

[Paper](https://arxiv.org/abs/2608.12720) · [Research note](papers/2026/2608.12720.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Self-evolving memory often changes stored content while leaving query-time retrieval behavior fixed.

**Core mechanism.** Structured memory atoms + executable retrieval primitives → experience trie → candidate retrieval skills → capability/deploy frontiers → learned query-conditioned router → selected skill executes evidence construction.

**Control loop.** `rollout → propose/evaluate retrieval skill → update frontiers + router → route future query → execute skill`

**Compared with.** A-Mem/MemoryOS/LightMem and self-evolving experience/prompt systems, plus internal no-skill-evolution and router ablations.

**Evidence to remember.** The largest ablation losses come from removing **skill evolution** or the **learned router**; LoCoMo-trained skills/router transfer to LongMemEval without additional training and still lead the reported table for both backbones.

**Open question.** Does an expensive rollout-trained retrieval program still pay off on tool-using agents versus a cheaper online adaptive controller?

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `episodic` `text` `timeline` · **★★★★☆** · 2026-08-13

**AI take:** The strongest current negative control for structured memory. A raw chat archive plus iterative lexical search and chat-native controls beats the compared graph/tree systems on precise refinding; the result is about **interface quality**, not “BM25 beats semantics.”

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2026/2608.12888.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Structured memory may be credited for gains that actually come from comparing against a weak flat retrieval interface.

**Core mechanism.** Raw timestamped turns → turn-level BM25 → multi-round ReAct search → session-RRF + local context + time filter + seen-session dedup → saved verbatim notes → answer.

**Compared with.** Single-shot BM25, matched generic-agentic BM25, and graph/tree/note memory systems.

**Evidence to remember.** Fixed LongMemEval-S/M: **93.2/89.3 ReFind vs 78.7/82.2 generic-agentic BM25 vs 84.7/68.9 one-search**.

**Open question.** Does raw-record search still win once online token/latency budgets are strictly matched on semantic or acting-agent tasks?

</details>

### [Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories](papers/2026/2608.12847.md)
`Representation & Organization` · `procedural` `text` `web-agent` · **★★★★☆** · 2026-08-13

**AI take:** Retrieval and reuse are different stages. With the same selected trajectory, a compact target-bound support object beats direct trace injection by forcing stale source bindings to be reacquired from current state.

[Paper](https://arxiv.org/abs/2608.12847) · [Research note](papers/2026/2608.12847.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A relevant past trajectory can still mislead the actor when users, files, IDs, dates, or environment state changed.

**Core mechanism.** Fixed retrieval/selection → write `workflow invariant + bindings to re-obtain + applicability conditions + verification guardrail` → actor grounds current values before execution.

**Compared with.** No memory, the same Full Trajectory, and a length-matched source-only Generic Summary under matched actor/target/tool conditions.

**Evidence to remember.** **62.3% success, +10.7pp over Full Trajectory, −48.9% online tokens**; under large binding shift, stale-binding errors **46.9%→10.9%**.

**Open question.** Can target-conditioned reuse remain faithful when multiple memories conflict or the support writer itself can hallucinate missing constraints?

</details>

### [Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents](papers/2026/2608.12851.md)
`Evaluation & Analysis` · `procedural` `structured` · **★★★★☆** · 2026-08-13

**AI take:** Persistent adaptation has multiple safety gates. Unsafe skill authoring, later retrieval, and fresh-session harm are not the same event; governance needs attribution and revocation across the whole evolution lifecycle.

[Paper](https://arxiv.org/abs/2608.12851) · [Code](https://github.com/henrymao2004/misevolve) · [Research note](papers/2026/2608.12851.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** “Successful” trajectories can contain unsafe shortcuts that self-improvement turns into persistent reusable policy.

**Core mechanism.** Version skill state across malicious exposure → evolution → later retrieval → clean-session execution; SafeEvolve adds lineage-aware repair, risk-aware retrieval, attribution, and retirement.

**Compared with.** No evolution, native skill-evolution methods, raw evolution, and utility-only/alternative governance conditions.

**Evidence to remember.** All **21 evolved configurations** author unsafe artifacts, but only **15** cause fresh-session harm; SafeEvolve reduces unsafe retrieval **35.33%→8.67%** in the reported aggregate.

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

**Evidence to remember.** LoCoMo: **89.22 / 204.1K construction tokens** full vs **81.88 / 849.9K** eager and **82.40 / 174.7K** fixed-window.

**Open question.** Do embedding-defined semantic boundaries survive tool events, conflicts, asynchronous state, and other non-conversational streams?

</details>

### [Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems](papers/2026/2608.11879.md)
`Evaluation & Analysis` · `semantic` `text` `general-agent` · **★★★★☆** · 2026-08-12

**AI take:** Dedicated memory is not automatically cheaper than resending history. Break-even is a workload- and architecture-dependent lifecycle property, not a consequence of smaller retrieved context.

[Paper](https://arxiv.org/abs/2608.11879) · [Research note](papers/2026/2608.11879.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Answer-context size ignores ingest, reflection, consolidation, and retrieval model calls.

**Core mechanism.** Replay matched conversations through multiple memory systems, rolling window, and full history; meter native lifecycle cost and compute sustained break-even.

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

**Compared with.** The same compression pipeline before temporal protection plus truncation/sliding/full-context controls.

**Evidence to remember.** Temporal-expression preservation rises **3.05%→62.39% (~20×)** and temporal judge accuracy improves **+0.314**.

**Open question.** Which other sparse fields—authority, identifiers, provenance, constraints—are silently deleted by mainstream compressors?

</details>

## ⭐ Design Anchors

These are **design points, not a ranking**. The set changes slowly so the radar does not become a recency leaderboard.

| Work | Design point |
|---|---|
| **[LeanMem](papers/2026/2608.03463.md)** | Heterogeneous lifecycle contracts for different evidence types. |
| **[V-Mem](papers/2026/2608.01543.md)** | Structural same-round access across modalities. |
| **[ReFind](papers/2026/2608.12888.md)** | Raw archival record + stateful query-time search as the semantic-structure control. |
| **[QCR](papers/2026/2608.12847.md)** | Target-conditioned post-retrieval reuse / rebinding. |
| **[PMCoder](papers/2026/2608.06811.md)** | Bidirectional controller↔memory coupling. |
| **[RoMeRL](papers/2026/2608.02508.md)** | Reduced-order feedback-bearing utility state. |
| **[AuthMem-Bench](papers/2026/2608.01679.md)** | Authority/provenance as memory correctness. |
| **[SkillJack](papers/2026/2608.03509.md)** | Provenance/revocation across experience→skill transformation. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

`what state exists → whether to pre-structure it → how to access it → how selected evidence is adapted to the current decision → how control state learns → whether authority/provenance survive lifecycle transforms`

**RippleMem** and **ERSkill** are important current additions but do not yet force a ninth/tenth anchor: RippleMem sharpens the access boundary already represented by ReFind/V-Mem, while ERSkill is a strong candidate to replace an older control-state anchor if access-policy evolution survives broader acting-agent evaluation.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Question |
|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | What should be stored persistently, and what should actually be delivered to the current consumer? |
| **[Retrieval & Access](categories/retrieval-access.md)** | How should the agent search, compose, and govern evidence once memory is not one flat store? |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | When should memory be transformed, consolidated, corrected, or forgotten? |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | Which memory decisions should be learned/evolved, and from what feedback? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we measure memory once cost, provenance, side effects, and persistence matter? |

<details>
<summary><strong>Representation & Organization — archive faithfully, or optimize for the consumer?</strong></summary>

**Current anchors.** LeanMem and QCR.

**Strongest signal.** The archival object and the actor-facing object need not be identical; representation earns complexity only when it exposes a useful downstream operation.

**Biggest unresolved question.** Which transformations preserve enough provenance/fidelity to be safely regenerated for a new consumer months later?

**Next decisive evidence.** Hold retrieval fixed and compare raw evidence, source-only summaries, and target-conditioned support across binding drift and conflicting memories.

</details>

<details>
<summary><strong>Retrieval & Access — when does structure beat a competent raw archive?</strong></summary>

**Current anchors.** ReFind, V-Mem, PMCoder; current challengers RippleMem, MESA, MAP-Graph.

**Strongest signal.** ReFind raises the baseline, while RippleMem shows structure can still win when it enables controlled evidence completion under a matched memory-unit/evidence budget.

**Biggest unresolved question.** Which relations must be pre-built, and which can be reconstructed cheaply enough at query time?

**Next decisive evidence.** Raw-record agentic search vs matched associative recollection vs learned routing under equal end-to-end compute on acting tasks.

</details>

<details>
<summary><strong>Write, Update & Consolidation — what should memory spend effort preserving?</strong></summary>

**Current anchors.** LeanMem; current evidence from LycheeMemory V2 and Sleeping Agent.

**Strongest signal.** Consolidation frequency and field-level preservation are separate controls: cheap batching can destroy evidence even when total token cost falls.

**Biggest unresolved question.** Can semantic boundaries and protected fields survive tool events, conflicting state, asynchronous updates, and non-conversational streams?

**Next decisive evidence.** Streaming-agent workloads with controlled write budgets, conflicts, temporal drift, and explicit field-preservation metrics.

</details>

<details>
<summary><strong>Memory Learning & Evolution — what exactly should evolve?</strong></summary>

**Current anchors.** RoMeRL; current evidence from SkillEvo, ERSkill, AMD, MemoryCPT, and HyMeS.

**Strongest signal.** Evolution quality depends on both **what receives adaptive state** and **what failures the system can observe**. SkillEvo improves the feedback surface; ERSkill evolves the access program and router.

**Biggest unresolved question.** Do evolved artifacts/policies transfer to new consumers and domains strongly enough to justify rollout/judge cost?

**Next decisive evidence.** Matched experiments that independently vary feedback richness, update rule, access-policy evolution, governance, and cross-domain transfer.

</details>

<details>
<summary><strong>Evaluation & Analysis — what does “good memory” mean after retrieval?</strong></summary>

**Current anchors.** AuthMem-Bench and SkillJack; current evidence from Total Recall, Agent Skills Can Be Harmful, and Practice Makes Unsafe.

**Strongest signal.** Endpoint recall/success hides lifecycle failures: cost can move break-even by hundreds of turns, relevant skills can worsen execution, and unsafe state may be authored without later harm—or later harm without obvious current-session evidence.

**Biggest unresolved question.** Can one benchmark jointly expose utility, cost, provenance, authority, descendant state, and downstream action without collapsing them into one opaque score?

**Next decisive evidence.** Long-running acting-agent traces with stage-level attribution and matched no-memory / raw-history / governed-memory controls.

</details>

<details>
<summary><strong>Scope and ratings</strong></summary>

**In scope:** persistent or managed information across interaction/reasoning steps that materially changes a language or multimodal agent's future behavior. Generic RAG, long-context modeling, KV-cache optimization, or unrelated continual learning are excluded unless memory is a central mechanism.

**Importance:** ★★★★★ field-shaping · ★★★★☆ notable · ★★★☆☆ useful · ★★☆☆☆ peripheral · ★☆☆☆☆ archival. Relevance is scored separately from importance.

Daily provenance is archived under [`runs/daily/`](runs/daily/). Taxonomy and curation rules live in [`taxonomy.yaml`](taxonomy.yaml) and [`CURATION.md`](CURATION.md).

</details>
