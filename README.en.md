# Agent Memory Radar

[中文](README.md) | **English**

*A research map of long-term memory systems for LLM and multimodal agents.*

**Radar Family:** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 sec: Timeline](#timeline) · [3 min: 7/30-day changes](#periods) · [5 min: Field Map](#field-map) · [15 min: Reading Paths](#reading-paths) · [Browse all](#library)

Last updated: **2026-08-20**

<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>
## Latest Timeline

> **Migration notice.** These existing records lack reliable historical Radar acceptance timestamps, so they remain ordered by their original paper publication dates. Every post-v2-cutover record uses `radar_published_at`; a paper date must never be presented as a Radar acceptance time.

<a id="entry-2608-17911"></a>
<details><summary><strong>2026-08-18 · CABLE</strong> · Retrieval & Access <!-- timefirst:area=retrieval-access --> — Stored links only earn their cost when they reach evidence the host retriever misses. <!-- timefirst:delta=structure-as-retriever-complement --></summary>

**Question.** Can stored memory links reach evidence missed by the same host retriever without increasing the final evidence budget? The closest lifecycle-matched control uses the same A-MEM host and evidence count. <!-- timefirst:question=links-reach-host-missed-evidence -->

**Evidence.** Under a matched A-MEM host budget and the same final evidence budget, LoCoMo Qwen3.5 moves **71.23→74.81** and MA-LongMemEval Qwen moves **59.33→65.33**. <!-- timefirst:evidence=same-host-budget-locomo-and-ma-longmemeval-gains~matched-a-mem-host-budget -->

**Caveat.** Temporal-reasoning slices regress, and the extra write-time generation and verification have not been lifecycle-cost-matched against a strong online-search control. <!-- timefirst:caveat=temporal-regression-and-unmatched-ingestion-cost~temporal-reasoning-slices -->

**Map.** `early_signal` — At the organize → access boundary, a relation must change reachability relative to the host interface; one paper does not rewrite the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.17911) · [中文深读](papers/2026/2608.17911.zh.md) · [English note](papers/2026/2608.17911.md)

</details>

<a id="entry-2608-17756"></a>
<details><summary><strong>2026-08-18 · D²ACCI</strong> · Evaluation & Governance <!-- timefirst:area=evaluation-governance --> — Memory features face paired evidence, protected slices, and stage-level promotion gates instead of aggregate-score promotion. <!-- timefirst:delta=aggregate-score-to-promotion-contract --></summary>

**Question.** How should a memory feature be promoted only when stage attribution and protected-slice non-regression both hold? The closest control is a paired baseline and candidate in the same runtime. <!-- timefirst:question=promotion-under-stage-and-non-regression-evidence -->

**Evidence.** Supplement extraction, session-memory retrieval, and Forget Guard show significant paired gains, while the **BM25/RRF null result** on LoCoMo / LongMemEval remains a monitored flag. <!-- timefirst:evidence=paired-gains-and-bm25-rrf-null-results~bm25-rrf-null-result -->

**Caveat.** This is deployment evidence from a diagnostic protocol, not an isolated effect of a new memory architecture; trace coverage dependence, evaluators, and promotion thresholds constrain the conclusion. <!-- timefirst:caveat=protocol-evidence-not-new-architecture~trace-coverage-dependence -->

**Map.** `early_signal` — At the governance boundary, null results and non-regression begin to constrain feature promotion, but one protocol does not rewrite the map.

**Links.** [Paper](https://arxiv.org/abs/2608.17756) · [中文深读](papers/2026/2608.17756.zh.md) · [English note](papers/2026/2608.17756.md)

</details>

<a id="entry-2608-17587"></a>
<details><summary><strong>2026-08-18 · WER</strong> · Memory Learning & Evolution <!-- timefirst:area=memory-learning-evolution --> — Execution outcomes train the skill-writer policy rather than merely prompting another inference-time reflection. <!-- timefirst:delta=execution-feedback-trains-writer-policy --></summary>

**Question.** Can a procedural-memory writer policy learn from a frozen executor's successful and failed trajectories rather than only reflecting on skill text? The closest control fixes the optimizer backbone and refinement workflow. <!-- timefirst:question=writer-policy-learning-from-execution -->

**Evidence.** With the same Qwen3-4B optimizer and workflow, BFCL v4 moves **67.28→76.63** and tau2 **40.43→50.72**; an extra refinement regression appears in the additional round. <!-- timefirst:evidence=same-backbone-gains-then-extra-refinement-regresses~extra-refinement-regression -->

**Caveat.** More expensive rollouts and programmatic verifier cost are the main alternative explanation; verifier availability and cost govern whether the writer-learning loop transfers. <!-- timefirst:caveat=rollout-and-verifier-cost~programmatic-verifier-cost -->

**Map.** `early_signal` — At the write/update boundary, the learned writer becomes persistent procedural state, but one work does not establish a durable trend.

**Links.** [Paper](https://arxiv.org/abs/2608.17587) · [中文深读](papers/2026/2608.17587.zh.md) · [English note](papers/2026/2608.17587.md)

</details>

<a id="entry-2608-17588"></a>
<details><summary><strong>2026-08-18 · TRUSS</strong> · Procedural Memory Governance <!-- timefirst:area=procedural-memory-governance --> — Generated skills become executable artifacts that must pass static and shadow-execution certification before persistence. <!-- timefirst:delta=generated-text-to-certified-artifact --></summary>

**Question.** Before a generated skill enters persistent procedural memory, can static obligations, controlled shadow execution, and provenance traces certify it reliably? The closest controls are LLM and static checkers on matched SkillInject artifacts. <!-- timefirst:question=certify-generated-skills-before-persistence -->

**Evidence.** On matched SkillInject artifacts, the LLM checker reaches **44.64% precision / 19.05% recall**, static checking **81.55 / 94.05**, and full TRUSS certification **100 / 100**. <!-- timefirst:evidence=matched-skillinject-certification-results~full-truss-certification -->

**Caveat.** The gain belongs to the full executor-dependent package; it cannot be isolated to skill representation or one checker. <!-- timefirst:caveat=package-and-executor-confounding~executor-dependent-package -->

**Map.** `early_signal` — At the write → promotion/governance boundary, plausible text is not yet a reusable capability; this does not independently rewrite the durable map.

**Links.** [Paper](https://arxiv.org/abs/2608.17588) · [中文深读](papers/2026/2608.17588.zh.md) · [English note](papers/2026/2608.17588.md)

</details>

<a id="entry-2608-17534"></a>
<details><summary><strong>2026-08-18 · ArborMem</strong> · State Localization <!-- timefirst:area=state-localization --> — The read path first identifies the active historical branch, then restores its trajectory before supplemental retrieval. <!-- timefirst:delta=localize-state-before-retrieval --></summary>

**Question.** In a long-running interaction, can the agent localize the historical trajectory resumed by the current turn before branch-local restoration and supplemental retrieval? The closest control removes localization from the same pipeline. <!-- timefirst:question=localize-active-trajectory-before-retrieval -->

**Evidence.** On a fixed LongMemEval subset, removing state localization changes the 30B setting **82→70**, but the 4B setting only **48→46**, a model-dependent localization effect rather than a uniform gain. <!-- timefirst:evidence=localization-ablation-model-dependent~model-dependent-localization-effect -->

**Caveat.** Forest representation not isolated: the ablation supports only the localization boundary, while a cheaper state index remains a strong alternative. <!-- timefirst:caveat=forest-representation-not-isolated~forest-representation-not-isolated -->

**Map.** `early_signal` — State localization becomes a boundary before access; one model-dependent result is insufficient to promote a durable map node.

**Links.** [Paper](https://arxiv.org/abs/2608.17534) · [中文深读](papers/2026/2608.17534.zh.md) · [English note](papers/2026/2608.17534.md)

</details>

<a id="entry-2608-16168"></a>
<details><summary><strong>2026-08-17 · QUMem</strong> · Consumer-State Reconstruction <!-- timefirst:area=consumer-state-reconstruction --> — Retrieved history becomes evidence for reconstructing a query-conditioned current user state after retrieval. <!-- timefirst:delta=retrieval-to-consumer-state-reconstruction --></summary>

**Question.** Does an explicit stage still need to reconstruct a query-conditioned current user state after evidence retrieval? The closest control removes reconstruction from the same typed-retrieval pipeline. <!-- timefirst:question=reconstruct-current-user-state-after-retrieval -->

**Evidence.** Reconstruction largest ablation: PersonaMem + GPT-4o-mini moves from **61.02 full → 58.38** without episodes → **57.11** without typed decomposition → **54.51** without reconstruction, the largest drop. <!-- timefirst:evidence=reconstruction-largest-ablation-on-personamem~reconstruction-largest-ablation -->

**Caveat.** A matched evidence synthesis budget is missing, so some reconstruction gain may come from additional downstream computation rather than a distinct state abstraction. <!-- timefirst:caveat=retrieval-and-synthesis-budget-not-matched~matched-evidence-synthesis-budget -->

**Map.** `early_signal` — At the access → consumer-state boundary, retrieval does not automatically equal reuse; independent evidence is still needed to revise the map.

**Links.** [Paper](https://arxiv.org/abs/2608.16168) · [中文深读](papers/2026/2608.16168.zh.md) · [English note](papers/2026/2608.16168.md)

</details>

<a id="entry-2608-16114"></a>
<details><summary><strong>2026-08-17 · HyperSkill</strong> · Procedural Memory Structure <!-- timefirst:area=procedural-memory-structure --> — Higher-order trajectory relations participate in retrieval, skill ranking, and maintenance as one structural access package. <!-- timefirst:delta=higher-order-relations-in-access-package --></summary>

**Question.** Do higher-order trajectory relations materially change retrieval, skill ranking, and maintenance in procedural memory? The closest control removes the hypergraph path in a system ablation. <!-- timefirst:question=higher-order-relations-in-skill-access -->

**Evidence.** Hypergraph path ablation: Qwen3 reports **52.00 / 36.97 / 50.59** on xBench / GAIA / WebWalkerQA, versus **41.00 / 35.76 / 44.71** without the hypergraph path. <!-- timefirst:evidence=hypergraph-path-ablation-across-three-benchmarks~hypergraph-path-ablation -->

**Caveat.** Representation access confounded: the ablation changes representation and the access pipeline together; decomposition, dual-path retrieval, ranking, and maintenance must be fixed for attribution. <!-- timefirst:caveat=representation-and-access-pipeline-confounded~representation-access-confounded -->

**Map.** `early_signal` — At the organize → access/maintenance boundary, current evidence supports the structural package rather than proving hypergraphs uniquely necessary.

**Links.** [Paper](https://arxiv.org/abs/2608.16114) · [中文深读](papers/2026/2608.16114.zh.md) · [English note](papers/2026/2608.16114.md)

</details>

<a id="entry-2608-12888"></a>
<details><summary><strong>2026-08-13 · ReFind</strong> · Raw-State Retrieval <!-- timefirst:area=raw-state-retrieval --> — Structured memory must beat stateful iterative search over raw logs, not a single-shot BM25 straw control. <!-- timefirst:delta=stronger-raw-control-for-structure --></summary>

**Question.** What raw-state control should structured memory beat? ReFind's closest matched alternative is iterative search with session, time, local-context operations, and seen-session state. <!-- timefirst:question=strongest-raw-control-for-structured-memory -->

**Evidence.** Stateful raw-search advantage: on fixed LongMemEval-S/M, ReFind reports **93.2 / 89.3**, versus **78.7 / 82.2** for generic-agentic BM25 and **84.7 / 68.9** for a one-search control. <!-- timefirst:evidence=stateful-raw-search-outperforms-weaker-controls~stateful-raw-search-advantage -->

**Caveat.** Semantic and acting tasks still lack strictly matched online latency, token use, and **full lifecycle cost**, so raw search cannot yet be claimed to dominate structured memory generally. <!-- timefirst:caveat=semantic-tasks-and-lifecycle-cost-unmatched~full-lifecycle-cost -->

**Map.** `early_signal` — It raises the raw baseline at the access boundary and constrains structure claims without establishing a durable conclusion alone.

**Links.** [Paper](https://arxiv.org/abs/2608.12888) · [中文深读](papers/2026/2608.12888.zh.md) · [English note](papers/2026/2608.12888.md)

</details>

<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>
## 7 days / 30 days: What Changed in the Memory Lifecycle

> **Timing basis.** Rolling-window membership uses only `radar_published_at`. The eight migrated records above have no reconstructable Radar acceptance time, so they remain historical Field Map context and never count as current-window support.

<a id="last-7-days"></a>
### Last 7 days: 2026-08-14—2026-08-20

- **`no_material_change` · Memory Radar acceptance time has no attributable new direction.** Supports: **none**; confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (require native v2 times for period claims): only records with native v2 Radar acceptance timestamps may support a rolling-window judgment; CABLE, D²ACCI, WER, TRUSS, ArborMem, QUMem, HyperSkill, and ReFind remain historical lifecycle Field Map context. Exact synthesis time: `2026-08-20T00:00:00Z`. <!-- timefirst:direction key="memory-radar-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->

<a id="last-30-days"></a>
### Last 30 days: 2026-07-22—2026-08-20

- **`no_material_change` · Memory Radar acceptance time has no attributable new direction.** Supports: **none**; confidence: **high**; timing basis: `radar_published_at`; prior map evidence: `none`. Research-design implication (require native v2 times for period claims): only records with native v2 Radar acceptance timestamps may support a rolling-window judgment; the eight explicit migration records can explain lifecycle boundaries but cannot be backfilled as acceptance events in this window. Exact synthesis time: `2026-08-20T00:00:00Z`. <!-- timefirst:direction key="memory-radar-acceptance-time" state="no_material_change" supports="none" confidence="high" implication="require-native-v2-times-for-period-claims" timing="radar_published_at" synthesized="2026-08-20T00:00:00Z" prior="none" -->

Time view: [weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a><a id="research-map"></a>
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

[Full research-problem map →](categories/README.en.md) · [How Agent Memory is evaluated →](https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-memory)

<a id="reading-paths"></a>
## Reading Paths

| Question | Read | What to learn |
|---|---|---|
| **When does structure earn its cost?** | ReFind → CABLE → ArborMem → QUMem | Move from a strong raw baseline to complementary relations, state localization, and consumer-state reconstruction; ask whether each stage adds an operation that a cheaper alternative cannot provide. |
| **How does procedural memory become a governed capability?** | HyperSkill → WER → TRUSS | Representation/relations, writer learning, and runtime certification are separate problems. |
| **How should memory features be attributed causally?** | D²ACCI → QUMem → ReFind | Start from stage traces and promotion gates, then see how reconstruction and raw controls change attribution. |

<a id="library"></a>
## Research Library

Browse long-lived work by research problem, research line, or year. If you know the question but not the paper title, start with the problem index:

- [English Research Library](library/README.en.md)
- [中文 Research Library](library/README.md)
- [Design anchors](papers/anchors.md)

<a id="how-to-use"></a>
## How to Use

Scan the Timeline summaries first. Open a disclosure in place when you need the question, closest control, decisive evidence, caveat, and map status. Use the 7-day / 30-day synthesis for recent movement, or Field Map, Reading Paths, and Research Library to follow a research problem over time.

## Scope / About / Contributing

A work is in scope when information persists or is explicitly managed across interaction/reasoning steps and materially changes future agent behavior. Ordinary fixed RAG, generic long-context/KV-cache work, and unrelated continual learning are usually out of scope.

This is a **curated research map, not a keyword feed**. Negative results, baseline reversals, lifecycle-cost evidence, and attribution failures stay visible when they change the conclusion.

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)

Related Radars: [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)
