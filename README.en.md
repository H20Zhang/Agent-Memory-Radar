# Agent Memory Radar

[中文](README.md) | **English**

*A research map of long-term memory systems for LLM and multimodal agents.*

This Radar asks two questions: **what actually changed in Agent Memory, and which lifecycle boundary earns additional complexity?**

**Radar Family:** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 sec: Latest](#latest) · [5 min: Field Map](#field-map) · [15 min: Reading Paths](#reading-paths) · [Browse All](#library)

> **Simple model:** `experience → write → organize → localize state → access/admit → reconstruct consumer state → update/forget → govern`
>
> **Current thesis:** “Which memory architecture wins?” is too coarse. Ask **which lifecycle boundary changed, what operation it adds over the simplest matched alternative, and whether the evidence isolates that stage.**

Last updated: **2026-08-20**

<a id="latest"></a>
## Latest Papers

### [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](papers/2026/2608.17911.md)
`Retrieval & Access` · `episodic` `graph` · **4/5** · 2026-08-18

**Research delta.** A memory edge earns its cost only if it reaches evidence the host retriever would otherwise miss; CABLE makes structure a **retriever-complementary operator**.

[Paper](https://arxiv.org/abs/2608.17911) · [中文深读](papers/2026/2608.17911.zh.md) · [Research note](papers/2026/2608.17911.md)

<details><summary><strong>Understand CABLE in ~60 seconds</strong></summary>

At write time CABLE builds direct semantic neighbors and antecedent-query candidates, removes overlap, verifies only the complementary candidates, and stores directed links. At query time it runs the host retriever first and uses one-hop expansion to replace low-ranked evidence without increasing the final evidence count.

Under the **same A-MEM host and final evidence budget**, LoCoMo Qwen3.5 moves **71.23→74.81** and MA-LongMemEval Qwen **59.33→65.33**. Temporal-reasoning slices regress, and the extra ingestion-time generation/verification cost is not lifecycle-matched against a strong online-search alternative.

</details>

### [D²ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](papers/2026/2608.17756.md)
`Evaluation & Analysis` · `structured` · **4/5** · 2026-08-18

**Research delta.** A memory change is not promoted because an aggregate score rises; D²ACCI requires paired evidence, protected slices, stage traces, and deterministic promotion gates.

[Paper](https://arxiv.org/abs/2608.17756) · [中文深读](papers/2026/2608.17756.zh.md) · [Research note](papers/2026/2608.17756.md)

<details><summary><strong>Understand D²ACCI in ~60 seconds</strong></summary>

The protocol turns `typed traces → paired baseline/candidate outcomes → significance + protected slices + diagnostic coverage` into `accept | monitor | feature-flag | reject` decisions.

Several interventions show significant paired gains, while BM25/RRF remains statistically null and stays feature-flagged. The important contribution is not the DCR metric itself but making **stage attribution and non-regression part of the promotion contract**.

</details>

### [Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback](papers/2026/2608.17587.md)
`Memory Learning & Evolution` · `procedural` · **4/5** · 2026-08-18

**Research delta.** WER learns a **skill-writer policy from execution consequences**, rather than only reflecting on skill text at inference time.

[Paper](https://arxiv.org/abs/2608.17587) · [中文深读](papers/2026/2608.17587.zh.md) · [Research note](papers/2026/2608.17587.md)

<details><summary><strong>Understand WER in ~60 seconds</strong></summary>

Candidate skills are executed by a frozen agent, programmatic verifiers score outcomes, group-relative RL updates the optimizer, and mixed success/failure trajectories become the next refinement state.

With the **same Qwen3-4B optimizer backbone and refinement workflow**, BFCL v4 improves **67.28→76.63** and tau2 **40.43→50.72**. One extra refinement step regresses, so more self-editing is not monotonically better. The main boundary is reliable execution feedback and verifier cost.

</details>

### [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](papers/2026/2608.17588.md)
`Memory Learning & Evolution` · `procedural` `structured` · **4/5** · 2026-08-18

**Research delta.** A generated skill becomes an **executable artifact that must be certified before promotion**, through static obligations plus controlled shadow execution and provenance traces.

[Paper](https://arxiv.org/abs/2608.17588) · [中文深读](papers/2026/2608.17588.zh.md) · [Research note](papers/2026/2608.17588.md)

<details><summary><strong>Understand TRUSS in ~60 seconds</strong></summary>

The path is `generate → static function/safety checks → shadow execution → trace → function/safety record → refine → re-check → promote`. On matched SkillInject artifacts, the LLM checker reaches **44.64% precision / 19.05% recall**, static checking **81.55 / 94.05**, and full TRUSS **100 / 100**.

The generation gain belongs to the whole certification/refinement package, and executor dependence remains large. The safer conclusion is that procedural memory needs an explicit **promotion/governance boundary**.

</details>

### [ArborMem: Navigating Interaction States with Memory Forests](papers/2026/2608.17534.md)
`Retrieval & Access` · `episodic` `hierarchical` · **4/5** · 2026-08-18

**Research delta.** ArborMem inserts **state localization before retrieval**: identify which historical interaction branch the current turn resumes, restore it, then retrieve supplemental evidence.

[Paper](https://arxiv.org/abs/2608.17534) · [中文深读](papers/2026/2608.17534.zh.md) · [Research note](papers/2026/2608.17534.md)

<details><summary><strong>Understand ArborMem in ~60 seconds</strong></summary>

Topically relevant history may belong to the wrong project state. ArborMem uses `localize parent state → restore branch trajectory → retrieve cross-branch support → answer → commit new state`.

On a fixed LongMemEval subset, removing state localization changes the 30B setting **82→70**, but the 4B setting only **48→46**. This isolates state localization as a useful boundary more clearly than it proves a memory forest is uniquely necessary.

</details>

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `personalization` · **4/5** · 2026-08-17

**Research delta.** Retrieved history is evidence, not the final memory state: QUMem reconstructs a **query-conditioned current user state** after retrieval, and that stage has the largest ablation effect.

[Paper](https://arxiv.org/abs/2608.16168) · [中文深读](papers/2026/2608.16168.zh.md) · [Research note](papers/2026/2608.16168.md)

<details><summary><strong>Understand QUMem in ~60 seconds</strong></summary>

QUMem builds semantic episodes and typed facts/preferences/insights, decomposes the current task into information needs, retrieves by type, and jointly reconstructs the current user state.

On PersonaMem + GPT-4o-mini: **61.02 full → 58.38 without episodes → 57.11 without typed decomposition → 54.51 without reconstruction**. The decisive next test holds retrieved evidence and synthesis budget fixed.

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `graph` · **4/5** · 2026-08-17

**Research delta.** Higher-order trajectory relations are operational in retrieval, skill ranking, and maintenance; current evidence supports the structural access package more strongly than hypergraphs alone.

[Paper](https://arxiv.org/abs/2608.16114) · [中文深读](papers/2026/2608.16114.zh.md) · [Research note](papers/2026/2608.16114.md)

<details><summary><strong>Understand HyperSkill in ~60 seconds</strong></summary>

The system retrieves subtasks and trajectories, fuses hyperedges, and ranks skills through cross-trajectory relations. Qwen3 reports **52.00 / 36.97 / 50.59** on xBench / GAIA / WebWalkerQA versus **41.00 / 35.76 / 44.71** without the hypergraph path.

Because the ablation changes the access pipeline too, a stronger test holds decomposition, dual-path retrieval, ranking, and maintenance fixed while changing only the representation.

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `raw` `timeline` · **4/5** · 2026-08-13

**Research delta.** The right raw control for structured memory is not single-shot BM25 but stateful iterative search with session/time/local-context operations.

[Paper](https://arxiv.org/abs/2608.12888) · [中文深读](papers/2026/2608.12888.zh.md) · [Research note](papers/2026/2608.12888.md)

<details><summary><strong>Understand ReFind in ~60 seconds</strong></summary>

ReFind keeps raw timestamped turns and adds multi-round reformulation, session fusion, local-context expansion, temporal filtering, and seen-session state. On fixed LongMemEval-S/M it reports **93.2 / 89.3**, versus **78.7 / 82.2** for generic-agentic BM25 and **84.7 / 68.9** for one-search control.

This raises the baseline semantic preprocessing must beat. The open question is whether the advantage survives semantic/acting tasks under matched online latency, tokens, and full lifecycle cost.

</details>

<a id="changes"></a>
## What Actually Changed

| Shift | New evidence | Research implication |
|---|---|---|
| **Structure is moving from “has relations” to “changes reachability.”** | ReFind raises the raw-search baseline; CABLE asks whether stored links reach evidence the host interface misses. | Evaluate the operation/reachability added by structure, not the label “graph memory.” |
| **The read path is splitting into more causal stages.** | ArborMem puts state localization before retrieval; QUMem puts consumer-state reconstruction after retrieval. | Treat `localize state → retrieve evidence → reconstruct consumer state` as separable controls. |
| **Procedural memory is becoming learned and governed state.** | WER learns the writer from execution; TRUSS gates promotion with runtime evidence. | Separate writer learning, executor behavior, certification, and maintenance. |
| **Evaluation is beginning to govern feature promotion.** | D²ACCI retains null results and protected-slice regressions as deployment evidence. | Aggregate score increases are not enough for component attribution or promotion. |

Time view: [weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a>
## Field Map

`experience/archive → write → organize → state localization → access/admission → consumer state → update/evolve/forget → governance/cost/provenance`

| Boundary | Core question | Current signal |
|---|---|---|
| **Write** | What should persist, and how should reusable artifacts be authored? | Granularity and writer policy depend on workload and feedback. |
| **Organize** | Which relations deserve precomputation? | Relations earn cost when they alter reachability beyond the host interface. |
| **State localization** | Which historical trajectory is active now? | Relevance retrieval may need an earlier state-selection stage. |
| **Access / admission** | What should be retrieved, expanded, or withheld? | Raw search, graph expansion, and admission are different operators. |
| **Consumer state** | What should the downstream actor actually see? | Retrieved evidence may still require reconstruction or rebinding. |
| **Evolution / forgetting** | Which adaptive state changes from which feedback? | Content, writer/read policy, relations, and feedback are distinct axes. |
| **Governance / cost** | Which artifacts/features deserve promotion? | Certification, paired evidence, provenance, and lifecycle cost are becoming first-class constraints. |

[Full research-problem map →](categories/README.en.md) · [How Agent Memory is evaluated →](https://github.com/H20Zhang/Agent-Benchmark-Radar#agent-memory)

<a id="reading-paths"></a>
## Reading Paths

| Question | Read | What to learn |
|---|---|---|
| **When does structure earn its cost?** | ReFind → CABLE → ArborMem → QUMem | Move from a strong raw baseline to complementary relations, state localization, and consumer-state reconstruction; ask what operator each stage adds. |
| **How does procedural memory become a governed capability?** | HyperSkill → WER → TRUSS | Representation/relations, writer learning, and runtime certification are separate problems. |
| **How should memory features be attributed causally?** | D²ACCI → QUMem → ReFind | Start from stage traces and promotion gates, then see how reconstruction and raw controls change attribution. |

<a id="library"></a>
## Research Library

Weekly reports are not the archive. Browse long-lived work by **research problem / research line / year**:

- [English Research Library](library/README.en.md)
- [中文 Research Library](library/README.md)
- [Design anchors](papers/anchors.md)

<a id="how-to-use"></a>
## How to Use

**30 sec:** scan Research delta.  
**60–90 sec:** expand the fold for mechanism, closest comparison, decisive evidence, and caveat.  
**5–10 min:** open the Chinese or English deep note.  
**Long-term understanding:** use Field Map and Research Library; use compactions only for temporal change.

## Scope / About / Contributing

A work is in scope when information persists or is explicitly managed across interaction/reasoning steps and materially changes future agent behavior. Ordinary fixed RAG, generic long-context/KV-cache work, and unrelated continual learning are usually out of scope.

This is a **curated research map, not a keyword feed**. Negative results, baseline reversals, lifecycle-cost evidence, and attribution failures stay visible when they change the conclusion.

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)
