# Agent Memory Radar

[中文](README.md) | **English**

*A living research map of memory systems for LLM and multimodal agents.*

Use this radar to answer two questions: **what changed in agent memory research, and which stage of the memory lifecycle actually earns its complexity?**

**Research Radar family:** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 sec: Latest](#latest) · [5 min: Field Map](#field-map) · [15 min: Reading Paths](#reading-paths) · [Browse all](#library)

> **Mental model.** `experience → write → organize → access/admit → reconstruct consumer state → update/forget → govern`
>
> **Current thesis.** “Memory architecture” is too coarse a unit of comparison. The useful question is **which lifecycle boundary changed, compared with the simplest matched alternative, and whether the evidence isolates that stage**.

Last updated: **2026-08-20**

<a id="latest"></a>
## Latest Papers

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `semantic` `structured` `personalization` · **4/5** · 2026-08-17

**Research delta.** QUMem treats retrieved history as evidence and reconstructs a **query-conditioned current user state** before acting; that read-side reconstruction is also the largest component in its ablation.

[Paper](https://arxiv.org/abs/2608.16168) · [Research note](papers/2026/2608.16168.md)

<details><summary><strong>Understand QUMem in ~60 seconds</strong></summary>

Fixed session/turn boundaries and one-shot retrieval can return fragments that are individually relevant but jointly fail to represent the user's current state. QUMem first builds semantic episodes and typed facts/preferences/insights, then turns the current task into information needs, retrieves typed evidence, and reconstructs user state before response or action.

The closest evidence is internal stage attribution rather than the headline baseline table: on PersonaMem with GPT-4o-mini, **61.02 full → 58.38 without episode construction → 57.11 without typed decomposition → 54.51 without user-state reconstruction**. The remaining question is whether explicit reconstruction still wins when retrieved evidence and synthesis budget are matched against a simpler provenance-aware alternative.

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `structured` `graph` · **4/5** · 2026-08-17

**Research delta.** HyperSkill makes higher-order trajectory relations operational during retrieval, skill ranking, and maintenance instead of storing them as passive metadata.

[Paper](https://arxiv.org/abs/2608.16114) · [Research note](papers/2026/2608.16114.md)

<details><summary><strong>Understand HyperSkill in ~60 seconds</strong></summary>

Flat skill stores can lose relations among subtasks, reusable procedures, and outcomes. HyperSkill retrieves both subtasks and trajectories, fuses the retrieved hyperedges, ranks co-occurring skills, then updates and prunes the skill structure after execution.

The reported no-hypergraph ablation drops Qwen3 success from **52.00/36.97/50.59** to **41.00/35.76/44.71** on xBench/GAIA/WebWalkerQA. But that ablation also changes the access pipeline. The decisive follow-up is a representation-matched control that holds decomposition, dual-path retrieval, ranking, and maintenance fixed.

</details>

### [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](papers/2026/2608.16071.md)
`Retrieval & Access` · `procedural` `structured` · **3/5** · 2026-08-17

**Research delta.** Skill retrieval improves when relevance is modeled around **capability and parameter structure**, not only the outer skill document; online expansion remains inconsistent.

[Paper](https://arxiv.org/abs/2608.16071) · [Code](https://github.com/MatZaharia/Skill2Query) · [Research note](papers/2026/2608.16071.md)

### [FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue](papers/2026/2608.16303.md)
`Write, Update & Consolidation` · `episodic` `timeline` · **3/5** · 2026-08-17

**Research delta.** Memory-unit granularity behaves like a workload parameter: situation-level units help sparse dialogue, while denser dialogue can favor finer turn-pair memory at higher construction cost.

[Paper](https://arxiv.org/abs/2608.16303) · [Research note](papers/2026/2608.16303.md)

### [Demystifying Agent Skills: Why They Work—Until They Don’t](papers/2026/2608.14036.md)
`Evaluation & Analysis` · `procedural` `coding` · **4/5** · 2026-08-14

**Research delta.** With source experience held fixed, standardized Skills beat Workflow Memory mainly as **procedural anchors**; exact retrieval labels are a weak proxy for downstream utility.

[Paper](https://arxiv.org/abs/2608.14036) · [Research note](papers/2026/2608.14036.md)

<details><summary><strong>Understand the result in ~60 seconds</strong></summary>

This paper is useful because it separates representation from source experience. The same prior trajectories are converted either into Workflow Memory or standardized SKILL.md artifacts, then retrieval, selection, actual use, and final task success are measured separately.

Skills outperform Workflow Memory by **6.06 points**; **65.7%** of successful skill cases are categorized as procedural anchoring versus **4.5%** knowledge injection. As the pool grows from **5 to 100**, actual-use precision falls **29.6%→3.3%** while downstream success is more stable. The open issue is whether this behavior survives large evolving skill libraries outside software tasks.

</details>

### [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](papers/2026/2608.13334.md)
`Retrieval & Access` · `episodic` `graph` · **4/5** · 2026-08-13

**Research delta.** A retrieved memory becomes an **anchor for searching missing evidence**; a matched RF-Mem control suggests some gain survives after memory units and evidence budget are held fixed.

[Paper](https://arxiv.org/abs/2608.13334) · [Research note](papers/2026/2608.13334.md)

<details><summary><strong>Understand RippleMem in ~60 seconds</strong></summary>

A first-hop memory may be relevant but incomplete when evidence is distributed across sessions. RippleMem builds sparse associations, detects missing support after first-hop recall, then expands locally around selected anchors under a bounded evidence budget.

On LoCoMo LLM-judge, the paper reports **87.14** for full RippleMem versus **83.83** for a matched RF-Mem control and **83.12** without graph expansion. That is stronger evidence than an unmatched flat-memory baseline, but deployment value still depends on whether build/query cost pays off on acting agents under matched latency.

</details>

### [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](papers/2026/2608.13120.md)
`Memory Learning & Evolution` · `procedural` · **4/5** · 2026-08-13

**Research delta.** Multi-turn interaction continues to expose actionable skill defects after matched single-turn feedback begins to saturate; governance mainly controls regression and bloat.

[Paper](https://arxiv.org/abs/2608.13120) · [Research note](papers/2026/2608.13120.md)

<details><summary><strong>Understand SkillEvo in ~60 seconds</strong></summary>

The key variable is the feedback surface. SkillEvo repeatedly executes multi-turn tasks, attributes failures, applies bounded edits, and persists governed skill checkpoints. Four-round task success reaches **81.8%** versus **66.4%** for matched single-turn-QA evolution. Removing governance lowers success to **78.6%** and increases bloat from **+2.8% to +16.2%**.

The result supports richer feedback more clearly than any specific editing algorithm. The next test is real-user feedback outside a simulator, with rollout and maintenance cost charged explicitly.

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `episodic` `raw` `timeline` · **4/5** · 2026-08-13

**Research delta.** A raw timestamped archive plus competent iterative search is a much stronger control for structured memory than single-shot lexical retrieval.

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2026/2608.12888.md)

<details><summary><strong>Understand ReFind in ~60 seconds</strong></summary>

Structured memory can look useful simply because it is compared with a weak raw-history interface. ReFind instead keeps raw turns and exposes turn-level BM25, multi-round reformulation, session fusion, neighboring context, temporal filters, and seen-session state.

On fixed LongMemEval-S/M, ReFind reports **93.2/89.3**, versus **78.7/82.2** for generic agentic BM25 and **84.7/68.9** for a one-search control. The result raises the baseline for semantic preprocessing; the unresolved boundary is whether raw-state search still wins when semantic tasks, acting tasks, latency, and token budgets are jointly matched.

</details>

<a id="changes"></a>
## What’s Changing

| Shift | What changed | Research implication |
|---|---|---|
| **Structure now needs a strong raw-state control.** | ReFind shows that stateful access over raw history can recover value often attributed to semantic preprocessing; RippleMem shows structure can still earn cost when it enables a stronger operator. | Compare operations and budgets, not “structured vs unstructured” labels. |
| **Retrieved evidence is not necessarily consumer state.** | QUMem reconstructs current user state after retrieval; trajectory-reuse work similarly rebinds stale source context before acting. | Evaluate retrieval and downstream state construction as separate stages. |
| **What evolves matters as much as how it evolves.** | SkillEvo changes the feedback surface; ERSkill evolves access policy; HyperSkill makes relational structure active during retrieval/maintenance. | Attribute gains to feedback, representation, read policy, and governance separately. |

Temporal views: [weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a>
## Field Map

`experience/archive → write → organize → access/admission → consumer state → update/evolve/forget → governance/cost/provenance`

| Boundary | Core question | Current signal |
|---|---|---|
| **Write** | What should become persistent, and at what granularity? | Granularity depends on workload density; one universal memory unit is unlikely to be optimal. |
| **Organize** | Which relations or representations deserve precomputation? | Structure must enable an operator that a competent raw-state interface cannot recover cheaply. |
| **Access / admission** | What should be retrieved, expanded, or withheld? | Relevance alone is insufficient; iterative access and admission policy are distinct controls. |
| **Consumer state** | What should the downstream actor actually receive? | Retrieved evidence may require reconstruction or rebinding before use. |
| **Evolution / forgetting** | What adaptive state should change, from which feedback? | Content, access policy, relational structure, and governance are separate axes. |
| **Governance / cost** | Is memory worth deploying over its lifecycle? | Endpoint recall misses provenance, authority, descendant effects, construction cost, and serving cost. |

[Explore the research-problem map →](categories/README.md) · [Evaluation view →](https://github.com/H20Zhang/Agent-Benchmark-Radar#agent-memory)

<a id="reading-paths"></a>
## Reading Paths

| Question | Suggested path | What to learn |
|---|---|---|
| **When does structure earn its cost?** | [ReFind](papers/2026/2608.12888.md) → [RippleMem](papers/2026/2608.13334.md) → [MESA](papers/2026/2608.10108.md) | A strong raw-state control comes first; structure is justified by the extra operation it enables. |
| **Why is retrieval not the final state?** | [QUMem](papers/2026/2608.16168.md) → [QCR](papers/2026/2608.12847.md) → [Demystifying Agent Skills](papers/2026/2608.14036.md) | Selection, reconstruction/rebinding, and procedural reuse are different stages. |
| **How does memory become self-improving state?** | [SkillEvo](papers/2026/2608.13120.md) → [ERSkill](papers/2026/2608.12720.md) → [HyperSkill](papers/2026/2608.16114.md) | Feedback source, read policy, structure, and maintenance must be separated. |

<a id="library"></a>
## Research Library

Old work should be discoverable without knowing its publication week.

- **[Browse by research problem / research line / year](library/README.en.md)**
- **[Research problem map](categories/README.md)**
- **[Durable design anchors](papers/anchors.md)**
- **[Temporal synthesis](digests/README.md)**

## How to Use This Radar

**Scan** Latest Papers for the one-sentence delta. **Expand** a high-value entry for a 60–90 second causal explanation. **Deep dive** into the research note for mechanism, closest comparison, evidence, caveat, and lifecycle interpretation. Use the Field Map and Library when you do not know a paper name yet.

## Scope

Included work changes persistent information that materially affects an agent's later behavior: writing, organization, access/admission, consumer-state construction, updating/forgetting, policy evolution, or deployment-facing evaluation. Ordinary fixed RAG, generic long-context modeling, KV-cache optimization, and unrelated continual learning are normally outside scope.

## About / Contributing

This is a curated research map, not an exhaustive keyword feed. Strong claims should answer **what changed, compared with what, and what the evidence does not isolate**.

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Maintainer docs](docs/MAINTENANCE.md)
