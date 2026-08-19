# 🧠 Agent Memory Radar

**A living research map of agent memory for LLM and multimodal agents.**  
Track the latest agent memory papers, long-term memory systems, procedural memory, benchmarks, design anchors, visual explainers, and weekly/monthly/yearly research compactions.

**Last updated:** 2026-08-19 · [Latest papers](#-latest-papers) · [Start here](#-start-here) · [Browse by research problem](#-browse-by-research-problem) · [Research compactions](#-research-compactions)

**Current field thesis:** agent memory is not one store. The sharper systems question is **where state should remain raw, where structure should be materialized, how evidence should be selected or admitted, how selected evidence becomes current consumer state, what should evolve, and what lifecycle cost/provenance each choice creates**. Credit complexity only at the stage where it beats a matched simpler alternative.

⭐ **If this radar saves you research time, star the repo to follow new papers and compactions.** Also tracking adaptive retrieval? See [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar).

## 🔥 Latest Papers

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `semantic` `structured` `timeline` `personalization` · **★★★★☆** · 2026-08-17

**AI take:** The important delta is not another typed store. QUMem treats retrieved history as evidence for **query-conditioned user-state reconstruction**, and that read-side reconstruction is the largest component in its ablation.

[Paper](https://arxiv.org/abs/2608.16168) · [Research note](papers/2026/2608.16168.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Fixed memory boundaries and one-shot retrieval can split coherent events, bind unrelated user signals together, and miss preference evolution/contextual validity.

**Core mechanism.** `history → semantic episodes → typed facts/preferences/insights → information needs → typed multi-query retrieval → user-state inference → personalized response/action`.

**Compared with.** A-MEM, Mem0, Zep, plus ablations removing episode construction, typed decomposition, or user-state reconstruction.

**Evidence to remember.** PersonaMem GPT-4o-mini: **61.02** overall vs **52.99** strongest baseline; ablation **61.02 full → 58.38 w/o episodes → 57.11 w/o decomposition → 54.51 w/o reconstruction**. KnowU-Bench success: **17.4% vs 12.8%** strongest baseline.

**Open question.** Does explicit state reconstruction still win when retrieved evidence and synthesis budget are matched against a simpler provenance-aware alternative?

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `structured` `graph` · **★★★★☆** · 2026-08-17

**AI take:** The interesting part is not “hypergraphs beat vectors.” HyperSkill makes trajectory relations operational in **dual-path retrieval, cross-trajectory skill ranking, and maintenance**; the main caveat is that its no-hypergraph ablation also changes the access pipeline.

[Paper](https://arxiv.org/abs/2608.16114) · [Research note](papers/2026/2608.16114.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Flat trajectory/skill stores lose the higher-order relation among subtasks, reusable skills, and outcomes, while growing libraries accumulate redundant or low-utility guidance.

**Core mechanism.** `task → subtask + trajectory retrieval → fuse trajectory hyperedges → co-occurrence-ranked skills → execute → extract/update → prune/merge by utility + structure`.

**Compared with.** No Memory, experiential-memory baselines including PlugMem, and an internal flat-skill ablation that removes the hypergraph/dual-path structural pipeline.

**Evidence to remember.** Qwen3 success is **52.00 / 36.97 / 50.59** on xBench / GAIA / WebWalkerQA; **w/o hypergraph 41.00 / 35.76 / 44.71**, **w/o subtask retrieval 43.00 / 32.73 / 47.06**, **w/o trajectory retrieval 48.00 / 35.76 / 43.53**.

**Open question.** Does a hypergraph still win against a flat or binary-graph store when decomposition, the dual-path controller, co-occurrence ranking, and maintenance budget are held fixed?

</details>

### [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](papers/2026/2608.16071.md)
`Retrieval & Access` · `procedural` `structured` `text` · **★★★☆☆** · 2026-08-17

**AI take:** Procedural-memory relevance should align with **capability + parameter structure**, not just the outer skill document. The retrieval gains are real, but online query expansion is inconsistent and the end-to-end evidence is still narrow.

[Paper](https://arxiv.org/abs/2608.16071) · [Code](https://github.com/MatZaharia/Skill2Query) · [Research note](papers/2026/2608.16071.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Users describe goals while skill documents describe developer-facing functions/parameters; document-level pseudo-queries can be topical but functionally invalid.

**Core mechanism.** `skill → capability/parameter/example graph → style imitation → capability template → parameter filling/validation → offline augmentation / online expansion / retriever training`.

**Compared with.** Zero-shot, Few-shot, SkillFlow-style pseudo-query generation and BM25/dense/SkillRouter retrieval.

**Evidence to remember.** ToolQA offline SkillRouter R@1 **35.80%→47.34%**; removing the skill graph drops pseudo-query Exec-Pass **42.85%→22.63%** and functional coverage **11.32%→2.41%**. Online expansion helps some settings and hurts others.

**Open question.** Can capability-grounded skill retrieval improve long-horizon tool execution once retrieval, invocation, and skill utility are measured separately?

</details>

### [FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue](papers/2026/2608.16303.md)
`Write, Update & Consolidation` · `episodic` `structured` `timeline` `personalization` · **★★★☆☆** · 2026-08-17

**AI take:** Memory-unit granularity is a workload-dependent systems parameter. Situation-level units beat coarse sessions on sparse dialogue and cost less than turn-pair memory, but turn-pair is slightly more accurate on denser LoCoMo.

[Paper](https://arxiv.org/abs/2608.16303) · [Research note](papers/2026/2608.16303.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Sparse long-term dialogue makes session memory too coarse and turn-pair memory redundant/expensive.

**Core mechanism.** `dialogue → boundary-preserving situation windows → Fact-Time-Affect units → carry/fuse unresolved boundary evidence → temporal links → retrieve + structured context`.

**Compared with.** Standard dialogue-memory systems plus direct session-level and turn-pair construction controls.

**Evidence to remember.** ES-MemEval: session **31.76 F1 / 1.58M tokens**, turn-pair **37.06 / 6.40M**, FTA-Mem **38.71 / 4.99M**. On LoCoMo, turn-pair is **38.28 vs 37.35 F1** but costs **7.04M vs 3.39M** construction tokens.

**Open question.** Can a write controller adapt memory-unit granularity online as evidence density changes instead of using one global segmentation policy?

</details>

### [Demystifying Agent Skills: Why They Work—Until They Don’t](papers/2026/2608.14036.md)
`Evaluation & Analysis` · `procedural` `text` `coding` · **★★★★☆** · 2026-08-14

**AI take:** Same source experience, different representation: standardized Skills outperform Workflow Memory and mostly work as **procedural anchors**, while exact retrieval labels remain a weak proxy for downstream utility.

[Paper](https://arxiv.org/abs/2608.14036) · [Research note](papers/2026/2608.14036.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Aggregate skill success conflates representation, outcome annotations, framework transfer, retrieval, invocation, and execution.

**Core mechanism.** Hold prior trajectories fixed → build Workflow Memory or SKILL.md → compare matched executions → separately measure retrieval, selection, actual use, and final success.

**Compared with.** Raw execution and Workflow Memory built from the same source trajectories.

**Evidence to remember.** Skills beat Workflow Memory by **6.06 points**; **65.7%** of skill cases are procedural anchoring vs **4.5%** knowledge injection. With pool size **5→100**, actual-use precision falls **29.6%→3.3%** while downstream success remains comparatively stable.

**Open question.** Does standardized procedural anchoring still win in large evolving skill libraries and non-software domains where “ground-truth skill” is less well defined?

</details>

### [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](papers/2026/2608.13334.md)
`Retrieval & Access` · `episodic` `graph` `structured` · **★★★★☆** · 2026-08-13

**AI take:** First-hop memories become **anchors for missing-evidence search**, and a matched RF-Mem control suggests the gain survives after holding memory units and evidence budget fixed.

[Paper](https://arxiv.org/abs/2608.13334) · [Research note](papers/2026/2608.13334.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A relevant first-hop memory may be incomplete when answer evidence is distributed across sessions.

**Core mechanism.** Cue-rich event memories + sparse associations → first-hop recall → detect missing support → choose anchors + target → bounded local expansion → budgeted evidence assembly.

**Compared with.** RF-Mem using RippleMem's extracted units and the same evidence budget, plus standard flat/graph memory baselines.

**Evidence to remember.** LoCoMo LLM-judge: **87.14** full vs **83.83** matched RF-Mem; removing graph expansion gives **83.12**.

**Open question.** Does associative recollection still justify build/query cost on acting agents when online latency is matched to raw-record search?

</details>

### [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](papers/2026/2608.13120.md)
`Memory Learning & Evolution` · `procedural` `structured` · **★★★★☆** · 2026-08-13

**AI take:** The strongest result is a feedback-source ablation: **multi-turn interaction keeps exposing useful defects after single-turn feedback saturates**. Governance mainly limits regression and bloat.

[Paper](https://arxiv.org/abs/2608.13120) · [Research note](papers/2026/2608.13120.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Procedural-memory evolution can plateau once obvious single-turn defects are fixed, while repeated editing accumulates regression and bloat.

**Core mechanism.** Multi-turn interaction → failure attribution → evidence-bounded skill edits → governance → persist checkpoint → repeat.

**Compared with.** Original Skills, multi-round self-reflection, and single-turn-QA-driven evolution under otherwise aligned update machinery.

**Evidence to remember.** Four-round task success reaches **81.8%** vs **66.4%** for matched single-turn QA; without governance it is **78.6%**, but bloat rises **+2.8%→+16.2%**.

**Open question.** Does the multi-turn advantage survive real-user feedback outside a high-fidelity simulator?

</details>

### [ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval](papers/2026/2608.12720.md)
`Memory Learning & Evolution` · `procedural` `structured` · **★★★★☆** · 2026-08-13

**AI take:** ERSkill makes the **read policy itself persistent evolvable state**: executable retrieval skills and the router co-evolve, while deployment quality depends on whether the controller can reliably activate a useful skill.

[Paper](https://arxiv.org/abs/2608.12720) · [Research note](papers/2026/2608.12720.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Self-evolving memory often changes stored content while leaving query-time retrieval behavior fixed.

**Core mechanism.** Memory atoms + retrieval primitives → candidate retrieval skills → capability/deploy frontiers → learned query-conditioned router → selected skill constructs evidence.

**Compared with.** Standard memory systems and self-evolving experience/prompt systems, plus no-skill-evolution and router ablations.

**Evidence to remember.** The largest ablation losses come from removing **skill evolution** or the **learned router**; LoCoMo-trained skills/router transfer to LongMemEval without further training.

**Open question.** Does rollout-trained retrieval policy still pay off on tool-using agents versus a cheaper online adaptive controller?

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `episodic` `text` `timeline` · **★★★★☆** · 2026-08-13

**AI take:** The strongest current negative control for structured memory. A raw chat archive plus iterative lexical search and chat-native controls beats the compared graph/tree systems on precise refinding.

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2026/2608.12888.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Structured memory may be credited for gains that actually come from comparing against a weak flat retrieval interface.

**Core mechanism.** Raw timestamped turns → turn-level BM25 → multi-round search → session fusion + local context/time controls → saved verbatim notes → answer.

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

**Open question.** Can target-conditioned reuse remain faithful when multiple memories conflict or the support writer hallucinates missing constraints?

</details>

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **When structure actually earns its cost** | [ReFind](papers/2026/2608.12888.md) → [RippleMem](papers/2026/2608.13334.md) → [MESA](papers/2026/2608.10108.md) | A competent raw-record interface is the baseline; structure matters when it enables evidence completion or selective access that online search cannot cheaply recover. |
| **Why retrieval is not the final state** | [QUMem](papers/2026/2608.16168.md) → [QCR](papers/2026/2608.12847.md) → [Demystifying Agent Skills](papers/2026/2608.14036.md) | Retrieved evidence may still need current-state reconstruction, rebinding, or procedural reshaping before an actor can use it reliably. |
| **How memory becomes self-improving state** | [SkillEvo](papers/2026/2608.13120.md) → [ERSkill](papers/2026/2608.12720.md) → [HyperSkill](papers/2026/2608.16114.md) | Evolution depends on the feedback surface, the read policy being evolved, and whether stored structure is operational during retrieval and maintenance. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**ReFind** raises the baseline for every structured-memory paper: raw chat plus competent stateful search can recover much of the value credited to semantic preprocessing.

**RippleMem** supplies the necessary counterexample: pre-built associations can still justify themselves when they turn a retrieved memory into a query for missing evidence and beat a more matched recollection control.

**QUMem** exposes the next boundary from personalization: even after the right historical evidence is retrieved, the system may still need to infer the *current* user state that the evidence jointly supports.

Together they frame a sharper question than “what is the best memory architecture?”: **what operation is enabled at each stage, and does it beat the simplest matched alternative?**

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

`what state exists → whether to pre-structure it → how to access it → how selected evidence becomes current consumer state → how control state learns → whether authority/provenance survive lifecycle transforms`

**QUMem, RippleMem, ERSkill, HyperSkill, and Demystifying Agent Skills** are important challengers but do not yet force extra anchors. QUMem strengthens the QCR consumer-state boundary; RippleMem sharpens the access boundary represented by ReFind/V-Mem; ERSkill should displace an older control-state anchor only if access-policy evolution survives broader acting-agent evaluation; HyperSkill strengthens the case for operational structure but still needs a matched flat/binary representation with the same structural controller; Demystifying strengthens procedural-reuse evaluation without creating a new durable control point.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Question |
|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | What should be stored persistently, and what should actually be delivered to the current consumer? |
| **[Retrieval & Access](categories/retrieval-access.md)** | How should the agent search, compose, and govern evidence once memory is not one flat store? |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | What event boundary should be written, transformed, corrected, or forgotten? |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | Which memory decisions should be learned/evolved, and from what feedback? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | How do we measure memory once representation, retrieval, reuse, cost, provenance, side effects, and persistence matter? |

<details>
<summary><strong>Representation & Organization — archive faithfully, or optimize for the consumer?</strong></summary>

**Current anchors.** LeanMem and QCR; current evidence from QUMem.

**Strongest signal.** The archival object and the actor-facing state need not be identical. QUMem's largest ablation comes from removing query-time state reconstruction, while QCR shows the same selected trajectory becomes more useful after target-conditioned rebinding.

**Biggest unresolved question.** Which transformations preserve enough provenance/fidelity to infer current state safely when preferences, bindings, or constraints conflict?

**Next decisive evidence.** Hold retrieval fixed and compare raw evidence, source-only summaries, target-conditioned support, and reconstructed user state under drift/conflict and matched synthesis cost.

</details>

<details>
<summary><strong>Retrieval & Access — when does structure beat a competent raw archive?</strong></summary>

**Current anchors.** ReFind, V-Mem, PMCoder; current challengers RippleMem, Skill2Query, MESA, MAP-Graph.

**Strongest signal.** ReFind raises the raw baseline, RippleMem shows structure can still win when it enables controlled evidence completion, and Skill2Query shows procedural artifacts benefit when retrieval aligns with internal capability/parameter structure rather than document semantics.

**Biggest unresolved question.** Which relations must be pre-built, which can be reconstructed online, and when should the system switch between offline semantic bridging and online adaptive expansion?

**Next decisive evidence.** Raw-record search vs matched associative recollection vs structure-aware skill routing under equal end-to-end compute on long-horizon acting tasks.

</details>

<details>
<summary><strong>Write, Update & Consolidation — what should one persistent unit be?</strong></summary>

**Current anchors.** LeanMem; current evidence from LycheeMemory V2, FTA-Mem, and Sleeping Agent.

**Strongest signal.** Boundary/granularity, transformation frequency, and field preservation are separate controls. FTA-Mem shows the best granularity can flip with evidence density; Sleeping Agent shows a compact representation can selectively erase critical fields.

**Biggest unresolved question.** Can a streaming controller adapt write granularity and preservation contracts to changing density without one expensive LLM decision per turn?

**Next decisive evidence.** Sparse+dense acting-agent streams with controlled write budgets, conflicts, temporal drift, and explicit field-preservation metrics.

</details>

<details>
<summary><strong>Memory Learning & Evolution — what exactly should evolve?</strong></summary>

**Current anchors.** RoMeRL; current evidence from SkillEvo, ERSkill, HyperSkill, AMD, MemoryCPT, and HyMeS.

**Strongest signal.** Evolution quality depends on **what receives adaptive state, what failures the system can observe, and whether stored relations are operational**. SkillEvo improves the feedback surface; ERSkill evolves the access program/router; HyperSkill uses higher-order trajectory structure during retrieval and maintenance.

**Biggest unresolved question.** Do evolved artifacts/policies/structures transfer to new consumers and domains strongly enough to justify rollout, decomposition, and maintenance cost?

**Next decisive evidence.** Matched experiments that independently vary feedback richness, representation (flat/binary/hypergraph), update rule, access-policy evolution, governance, and cross-domain transfer.

</details>

<details>
<summary><strong>Evaluation & Analysis — what does “good memory” mean after retrieval?</strong></summary>

**Current anchors.** AuthMem-Bench and SkillJack; current evidence from Demystifying Agent Skills, Total Recall, Agent Skills Can Be Harmful, and Practice Makes Unsafe.

**Strongest signal.** Endpoint recall/success hides stage-level effects: the same experience behaves differently as Workflow Memory vs Skill, exact retrieval can decouple from utility, lifecycle cost can move break-even by hundreds of turns, and persistent state can be authored without later harm.

**Biggest unresolved question.** Can one benchmark jointly expose representation, retrieval, invocation/reuse, utility, cost, provenance, authority, descendant state, and downstream action without collapsing them into one opaque score?

**Next decisive evidence.** Long-running acting-agent traces with stage-level attribution and matched no-memory / raw-history / alternative-representation / governed-memory controls.

</details>

<details>
<summary><strong>Scope and ratings</strong></summary>

**In scope:** persistent or managed information across interaction/reasoning steps that materially changes a language or multimodal agent's future behavior. Generic RAG, long-context modeling, KV-cache optimization, or unrelated continual learning are excluded unless memory is a central mechanism.

**Importance:** ★★★★★ field-shaping · ★★★★☆ notable · ★★★☆☆ useful · ★★☆☆☆ peripheral · ★☆☆☆☆ archival. Relevance is scored separately from importance.

</details>

[Explore the full research map →](categories/README.md)

## 🧭 Research Compactions

The archive deliberately becomes coarser with time: `recent month → weekly` · `recent quarter → monthly` · `all years → yearly`.

### Recent Month · Weekly

**[2026-W33 · Memory architecture decomposes into stage-specific controls](digests/weekly/2026-W33.md)**  
Aug 10–16 made “best memory architecture” a weaker question. The sharper comparison is now **archive/representation → access program → evidence completion/selection → consumer-facing state/reuse → update/governance → lifecycle cost**. ReFind raises the raw-record baseline; RippleMem shows where structure still earns complexity; QCR separates retrieval from reuse; Demystifying Agent Skills separates procedural representation from retrieval/invocation; SkillEvo and ERSkill split self-improvement into feedback quality and evolvable read policy.

**Suggested reading:** ReFind → RippleMem → QCR → Demystifying Agent Skills → SkillEvo.  
[Read the W33 synthesis →](digests/weekly/2026-W33.md)

**[2026-W32 · Structure only matters when control can use it](digests/weekly/2026-W32.md)**  
Aug 3–9 established the first correction to “more structure is better”: controller↔memory coupling and consumer-compatible granularity matter, while plausible extra typing can fail to beat a simpler dynamic policy.

### Recent Quarter · Monthly

**[2026-08 · Rolling through Aug 19](digests/monthly/2026-08.md)**  
The August map now separates **archive/representation → access program → evidence completion/selection → consumer-facing state/reuse → update feedback/governance → lifecycle cost/provenance**. The methodological rule is getting stricter: **credit memory complexity only at the stage where a matched simpler alternative fails.** QUMem strengthens the post-retrieval state-reconstruction boundary; Skill2Query sharpens procedural-memory retrieval supervision; FTA-Mem makes write granularity explicitly density- and cost-dependent; HyperSkill shows relational structure only matters when retrieval and maintenance actually consume it.

### All Years · Yearly

**[2026 · Rolling, incomplete research map](digests/yearly/2026.md)**  
Active curation starts in August with one July backfill, so this is **not a full-year reconstruction**. Within current coverage, agent memory is becoming a multi-stage state interface whose access programs, consumer-state transforms, evolution signals, cost, and provenance need separate accounting.

[Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes while they are fresh. **Monthly** rebuilds the field map across several weeks. **Yearly** keeps only durable shifts, corrections, unresolved trade-offs, and evidence standards that survive broader coverage.

</details>

## 🖼️ How to Read a Paper Here

- **30-second scan:** title, category, importance, date, AI take, and verified links.
- **60-second expand:** problem, actual mechanism/control flow, closest comparison, one decisive result or ablation, and the open question most likely to change the importance judgment.
- **Deep dive:** open the research note for memory design, evidence, limitations, provenance, and a verified visual explainer when available.

## About the Radar

This is a **curated living survey of agent memory research**, not an exhaustive keyword feed. It covers persistent state for LLM and multimodal agents across long-term memory, procedural memory, retrieval/access, write/update/consolidation, memory learning/evolution, benchmarks, cost, provenance, and safety.

Every included work should help answer three questions: **what changed, compared with what, and what evidence actually isolates the claimed cause?** Negative results and baseline reversals are kept when they change the research interpretation.

## 🤝 Contributing

Corrections are especially welcome when they change the conclusion: a missing baseline, unfair resource budget, wrong taxonomy, broken link, unsupported claim, or a visual that implies more than the paper shows. Open an [issue](https://github.com/H20Zhang/Agent-Memory-Radar/issues) or send a pull request.

## 🔭 Related Radar

**[Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)** tracks adaptive retrieval, information-seeking agents, retrieval control, and agentic RAG. The two radars deliberately overlap at the boundary where retrieval becomes persistent memory state.

---

If this radar saves you research time, consider starring the repo.