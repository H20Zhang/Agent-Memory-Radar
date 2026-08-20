# Agent Memory Radar

[中文](README.md) | **English**

*A research map of long-term memory systems for LLM and multimodal agents.*

[Latest Papers](#latest) · [Recent Changes](#changes) · [Field Map](#field-map) · [Reading Paths](#reading-paths) · [Research Library](#library)

Last updated: **2026-08-20**

<a id="latest-papers"></a>
<a id="latest"></a>
## Latest Papers

### [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](papers/2026/2608.17911.md)
`Retrieval & Access` · `episodic` `graph` · **4/5** · 2026-08-18

CABLE retains a memory edge only when it reaches evidence the host retriever would otherwise miss, making structure a **retriever-complementary operator**.

[Paper](https://arxiv.org/abs/2608.17911) · [中文深读](papers/2026/2608.17911.zh.md) · [Research note](papers/2026/2608.17911.md)

<details><summary><strong>CABLE's complementary expansion</strong></summary>

At write time CABLE builds direct semantic neighbors and antecedent-query candidates, removes overlap, verifies only the complementary candidates, and stores directed links. At query time it runs the host retriever first and uses one-hop expansion to replace low-ranked evidence without increasing the final evidence count.

Under the same A-MEM host and final evidence budget, LoCoMo Qwen3.5 moves **71.23→74.81** and MA-LongMemEval Qwen **59.33→65.33**. Temporal-reasoning slices regress, and the extra ingestion-time generation/verification cost is not lifecycle-matched against a strong online-search alternative.

</details>

### [D²ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](papers/2026/2608.17756.md)
`Evaluation & Analysis` · `structured` · **4/5** · 2026-08-18

D²ACCI does not promote a memory change because an aggregate score rises; paired evidence, protected slices, stage traces, and deterministic promotion gates must support the deployment decision together.

[Paper](https://arxiv.org/abs/2608.17756) · [中文深读](papers/2026/2608.17756.zh.md) · [Research note](papers/2026/2608.17756.md)

<details><summary><strong>D²ACCI's promotion gate</strong></summary>

The protocol turns `typed traces → paired baseline/candidate outcomes → significance + protected slices + diagnostic coverage` into `accept | monitor | feature-flag | reject` decisions.

Supplement extraction, session-memory retrieval, and Forget Guard show significant paired gains. BM25/RRF is statistically null on both LoCoMo and LongMemEval and remains a monitored flag. The main contribution is making **stage attribution and non-regression part of the promotion contract**; the DCR metric itself is secondary.

</details>

### [Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback](papers/2026/2608.17587.md)
`Memory Learning & Evolution` · `procedural` · **4/5** · 2026-08-18

WER learns a **skill-writer policy from execution consequences** instead of limiting refinement to inference-time reflection on existing skill text.

[Paper](https://arxiv.org/abs/2608.17587) · [中文深读](papers/2026/2608.17587.zh.md) · [Research note](papers/2026/2608.17587.md)

<details><summary><strong>Learning a writer from execution feedback</strong></summary>

Candidate skills are executed by a frozen agent, programmatic verifiers score outcomes, group-relative RL updates the optimizer, and mixed success/failure trajectories become the next refinement state.

With the **same Qwen3-4B optimizer backbone and refinement workflow**, BFCL v4 improves **67.28→76.63** and tau2 **40.43→50.72**. One extra refinement step regresses, so more self-editing is not monotonically better. The main boundary is reliable execution feedback and verifier cost.

</details>

### [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](papers/2026/2608.17588.md)
`Memory Learning & Evolution` · `procedural` `structured` · **4/5** · 2026-08-18

TRUSS treats a generated skill as an **executable artifact that must be certified before it persists**, using static obligations, controlled shadow execution, and provenance traces.

[Paper](https://arxiv.org/abs/2608.17588) · [中文深读](papers/2026/2608.17588.zh.md) · [Research note](papers/2026/2608.17588.md)

<details><summary><strong>Certification before skill promotion</strong></summary>

The path is `generate → static function/safety checks → shadow execution → trace → function/safety record → refine → re-check → promote`. On matched SkillInject artifacts, the LLM checker reaches **44.64% precision / 19.05% recall**, static checking **81.55 / 94.05**, and full TRUSS **100 / 100**.

The generation gain belongs to the whole certification/refinement package, and executor dependence remains large. The evidence supports an explicit **promotion/governance boundary** for procedural memory; plausible-looking text alone is not sufficient evidence of reusable capability.

</details>

### [ArborMem: Navigating Interaction States with Memory Forests](papers/2026/2608.17534.md)
`Retrieval & Access` · `episodic` `hierarchical` · **4/5** · 2026-08-18

ArborMem inserts **state localization before retrieval**: identify which historical interaction branch the current turn resumes, restore its branch-local trajectory, then retrieve supplemental evidence.

[Paper](https://arxiv.org/abs/2608.17534) · [中文深读](papers/2026/2608.17534.zh.md) · [Research note](papers/2026/2608.17534.md)

<details><summary><strong>State localization before retrieval</strong></summary>

Topically relevant history may belong to the wrong project state. ArborMem uses `localize parent state → restore branch trajectory → retrieve cross-branch support → answer → commit new state`.

On a fixed LongMemEval subset, removing state localization changes the 30B setting **82→70**, but the 4B setting only **48→46**. This isolates state localization as a useful boundary more clearly than it proves a memory forest is uniquely necessary.

</details>

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `personalization` · **4/5** · 2026-08-17

QUMem treats retrieved history as evidence and reconstructs a **query-conditioned current user state** after retrieval; that read-side reconstruction has the largest ablation effect.

[Paper](https://arxiv.org/abs/2608.16168) · [中文深读](papers/2026/2608.16168.zh.md) · [Research note](papers/2026/2608.16168.md)

<details><summary><strong>Query-conditioned user-state reconstruction</strong></summary>

QUMem builds semantic episodes and typed facts/preferences/insights, decomposes the current task into information needs, retrieves by type, and jointly reconstructs the current user state.

On PersonaMem + GPT-4o-mini: **61.02 full → 58.38 without episodes → 57.11 without typed decomposition → 54.51 without reconstruction**. The decisive next test holds retrieved evidence and synthesis budget fixed.

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `graph` · **4/5** · 2026-08-17

HyperSkill makes higher-order trajectory relations operational in retrieval, skill ranking, and maintenance. Current evidence supports the structural access package but does not establish that the hypergraph representation itself is irreplaceable.

[Paper](https://arxiv.org/abs/2608.16114) · [中文深读](papers/2026/2608.16114.zh.md) · [Research note](papers/2026/2608.16114.md)

<details><summary><strong>Higher-order relations in the access path</strong></summary>

The system retrieves subtasks and trajectories, fuses hyperedges, and ranks skills through cross-trajectory relations. Qwen3 reports **52.00 / 36.97 / 50.59** on xBench / GAIA / WebWalkerQA versus **41.00 / 35.76 / 44.71** without the hypergraph path.

Because the ablation changes the access pipeline too, a stronger test holds decomposition, dual-path retrieval, ranking, and maintenance fixed while changing only the representation.

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `raw` `timeline` · **4/5** · 2026-08-13

ReFind shows that structured memory should be compared with stateful iterative search that includes session, time, and local-context operations, not only with single-shot BM25.

[Paper](https://arxiv.org/abs/2608.12888) · [中文深读](papers/2026/2608.12888.zh.md) · [Research note](papers/2026/2608.12888.md)

<details><summary><strong>A stronger raw-search control</strong></summary>

ReFind keeps raw timestamped turns and adds multi-round reformulation, session fusion, local-context expansion, temporal filtering, and seen-session state. On fixed LongMemEval-S/M it reports **93.2 / 89.3**, versus **78.7 / 82.2** for generic-agentic BM25 and **84.7 / 68.9** for one-search control.

This raises the baseline semantic preprocessing must beat. The open question is whether the advantage survives semantic/acting tasks under matched online latency, tokens, and full lifecycle cost.

</details>

<a id="whats-changing"></a>
<a id="changes"></a>
## What Actually Changed

| Shift | New evidence | Research implication |
|---|---|---|
| **Structure is moving from “has relations” to “changes reachability.”** | ReFind raises the raw-search baseline; CABLE asks whether stored links reach evidence the host interface misses. | Evaluate the operation/reachability added by structure, not the label “graph memory.” |
| **The read path is splitting into more causal stages.** | ArborMem puts state localization before retrieval; QUMem puts consumer-state reconstruction after retrieval. | Treat `localize state → retrieve evidence → reconstruct consumer state` as separable controls. |
| **Procedural memory is moving toward learning, certification, and governance.** | WER learns the writer from execution; TRUSS gates promotion with runtime evidence. | Separate writer learning, executor behavior, certification, and maintenance. |
| **Evaluation is beginning to govern feature promotion.** | D²ACCI brings null results, protected slices, and trace localizability into deployment gates. | Aggregate score increases are not enough; default experiments also need stage attribution and non-regression. |

Time view: [weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="research-map"></a>
<a id="field-map"></a>
## Field Map

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
| **When does structure earn its cost?** | ReFind → CABLE → ArborMem → QUMem | Move from a strong raw baseline to complementary relations, state localization, and consumer-state reconstruction; ask whether each stage adds an operator that a cheaper alternative cannot provide. |
| **How does procedural memory become a governed capability?** | HyperSkill → WER → TRUSS | Representation/relations, writer learning, and runtime certification are separate problems. |
| **How should memory features be attributed causally?** | D²ACCI → QUMem → ReFind | Start from stage traces and promotion gates, then see how reconstruction and raw controls change attribution. |

<a id="library"></a>
## Research Library

- [English Research Library](library/README.en.md)
- [中文 Research Library](library/README.md)
- [Design anchors](papers/anchors.md)

## Scope and Contributing

A work is in scope when information persists or is explicitly managed across interaction/reasoning steps and materially changes future agent behavior. Ordinary fixed RAG, generic long-context/KV-cache work, and unrelated continual learning are usually out of scope.

Negative results, baseline reversals, lifecycle-cost evidence, and attribution failures stay visible when they change the research conclusion.

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)

Related Radars: [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)
