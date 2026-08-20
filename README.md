# Agent Memory Radar

**中文** | [English](README.en.md)

*面向 LLM 与多模态 Agent 的长期记忆研究地图。*

这个 Radar 主要回答两个问题：**Agent Memory 最近真正变了什么？Memory lifecycle 的哪一个阶段值得付出额外复杂度？**

**Radar Family：** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：最新工作](#latest) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

> **先建立一个简单模型：** `experience → write → organize → localize state → access/admit → reconstruct consumer state → update/forget → govern`
>
> **当前判断：** “哪种 memory architecture 最好”太粗。更有判别力的问题是：**到底改了哪个 lifecycle boundary、相比最简单且公平的替代方案多做了什么、实验是否真的隔离了这一阶段的贡献。**

最后更新：**2026-08-20**

<a id="latest"></a>
## 最新论文

### [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](papers/2026/2608.17911.md)
`Retrieval & Access` · `episodic` `graph` · **4/5** · 2026-08-18

**Research delta.** Memory edge 不再因为“语义相关”就值得存；CABLE 要求它能到达 host retriever 原本到不了的证据，让 structure 成为 **retriever-complementary operator**。

[Paper](https://arxiv.org/abs/2608.17911) · [中文深读](papers/2026/2608.17911.zh.md) · [English note](papers/2026/2608.17911.md)

<details><summary><strong>约 60 秒理解 CABLE</strong></summary>

CABLE 在 write time 同时构造 direct semantic neighborhood 与 antecedent-query candidates，先去掉 overlap，再只验证剩余候选并写 directed links。Query time 仍先跑原 host retriever，再从 seed 做 one-hop expansion；最终 evidence count 不增加。

最有判别力的是 **同一 A-MEM host + 同一最终 evidence budget**：LoCoMo Qwen3.5 **71.23→74.81**，MA-LongMemEval Qwen **59.33→65.33**。但 temporal-reasoning slices 有下降，且 write-time query generation / verification 尚未与强 online-search baseline 做 lifecycle-matched 成本比较。

</details>

### [D²ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](papers/2026/2608.17756.md)
`Evaluation & Analysis` · `structured` · **4/5** · 2026-08-18

**Research delta.** Memory feature 不再因为 aggregate score 上涨就被 promote；D²ACCI 要求 paired evidence、protected slices、stage traces 与确定性的 promotion gate 一起支持部署决定。

[Paper](https://arxiv.org/abs/2608.17756) · [中文深读](papers/2026/2608.17756.zh.md) · [English note](papers/2026/2608.17756.md)

<details><summary><strong>约 60 秒理解 D²ACCI</strong></summary>

它把 instrumented memory runtime 包在 diagnostic loop 里：`typed traces → paired baseline/candidate → significance + protected slices + diagnostic coverage → accept | monitor | feature-flag | reject`。

Supplement extraction、session-memory retrieval、Forget Guard 有显著 paired gain；相反 BM25/RRF 在 LoCoMo / LongMemEval 均不显著，因此只保留为 monitored flag。价值不在 DCR 这个指标本身，而在**把 stage-level attribution 和 non-regression 变成 promotion contract**。

</details>

### [Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback](papers/2026/2608.17587.md)
`Memory Learning & Evolution` · `procedural` · **4/5** · 2026-08-18

**Research delta.** WER 从 execution consequences 训练 **skill writer policy**，而不是只让模型在 inference time 反思一份 skill 文本。

[Paper](https://arxiv.org/abs/2608.17587) · [中文深读](papers/2026/2608.17587.zh.md) · [English note](papers/2026/2608.17587.md)

<details><summary><strong>约 60 秒理解 WER</strong></summary>

Candidate skill 交给 frozen agent 多次执行，programmatic verifier 评分，group-relative RL 更新 optimizer；同一 skill/task 中 mixed success/failure 的 trajectories 会进入下一轮 refinement state。

在同一个 Qwen3-4B optimizer backbone 与 refinement workflow 下，BFCL v4 **67.28→76.63**，tau2 **40.43→50.72**。额外再 refinement 一轮反而回落，说明“持续自我修改”并非单调更好。主要局限是昂贵 rollout 与可靠 verifier 的可得性。

</details>

### [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](papers/2026/2608.17588.md)
`Memory Learning & Evolution` · `procedural` `structured` · **4/5** · 2026-08-18

**Research delta.** Generated skill 被当成**需要认证后才能持久化的 executable artifact**：static obligations 之后还要经过 controlled shadow execution 与 provenance-preserving trace。

[Paper](https://arxiv.org/abs/2608.17588) · [中文深读](papers/2026/2608.17588.zh.md) · [English note](papers/2026/2608.17588.md)

<details><summary><strong>约 60 秒理解 TRUSS</strong></summary>

流程是 `generate → static function/safety checks → shadow execution → trace → function/safety record → refine → re-check → promote`。在 matched SkillInject artifacts 上，LLM checker 为 **44.64% precision / 19.05% recall**，static checker **81.55 / 94.05**，full TRUSS **100 / 100**。

但 generation gain 属于整个 certification/refinement package，而且 executor dependence 很大。更稳妥的结论是：procedural memory 需要一个**promotion/governance boundary**，不能把“文本看起来合理”当成 reusable capability 的充分条件。

</details>

### [ArborMem: Navigating Interaction States with Memory Forests](papers/2026/2608.17534.md)
`Retrieval & Access` · `episodic` `hierarchical` · **4/5** · 2026-08-18

**Research delta.** ArborMem 在 retrieval 前增加 **state localization**：先确定当前 turn 恢复历史中的哪条 interaction branch，再恢复 branch-local trajectory，最后才找 supplemental evidence。

[Paper](https://arxiv.org/abs/2608.17534) · [中文深读](papers/2026/2608.17534.zh.md) · [English note](papers/2026/2608.17534.md)

<details><summary><strong>约 60 秒理解 ArborMem</strong></summary>

Long-running interaction 里，topically relevant history 不一定属于当前恢复的 trajectory。ArborMem 把 read path 拆成 `localize parent state → restore branch trajectory → retrieve cross-branch support → answer → commit new state`。

固定 LongMemEval subset 上，30B 模型去掉 state localization **82→70**，4B 只有 **48→46**；效果明显 model-dependent。证据支持“state localization 是独立 boundary”，但不能证明 forest representation 本身不可替代。

</details>

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `personalization` · **4/5** · 2026-08-17

**Research delta.** QUMem 把 retrieved history 当证据，在 query 到来后重建**当前 user state**；在它的消融中，这个 read-side reconstruction 也是贡献最大的阶段。

[Paper](https://arxiv.org/abs/2608.16168) · [中文深读](papers/2026/2608.16168.zh.md) · [English note](papers/2026/2608.16168.md)

<details><summary><strong>约 60 秒理解 QUMem</strong></summary>

QUMem 先形成 semantic episodes 和 typed facts/preferences/insights，再把当前任务拆成 information needs，做 typed retrieval，最后联合证据重建 current user state。

PersonaMem + GPT-4o-mini 消融为 **61.02 full → 58.38 去掉 episodes → 57.11 去掉 typed decomposition → 54.51 去掉 reconstruction**。下一步应在 retrieved evidence 与 synthesis budget 都匹配时验证显式 reconstruction 是否仍值得。

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `graph` · **4/5** · 2026-08-17

**Research delta.** HyperSkill 让 trajectory 高阶关系真正参与 retrieval、skill ranking 和 maintenance；当前证据更支持这套 structural access package，而不是“hypergraph 表示本身不可替代”。

[Paper](https://arxiv.org/abs/2608.16114) · [中文深读](papers/2026/2608.16114.zh.md) · [English note](papers/2026/2608.16114.md)

<details><summary><strong>约 60 秒理解 HyperSkill</strong></summary>

Full system 同时检索 subtask 与 trajectory，融合 hyperedges，再用跨 trajectory relation 排名 skill。Qwen3 在 xBench / GAIA / WebWalkerQA 为 **52.00 / 36.97 / 50.59**；去掉 hypergraph 后 **41.00 / 35.76 / 44.71**。

但 ablation 同时改了 access pipeline，因此下一步应固定 decomposition、dual-path retrieval、ranking 与 maintenance，只替换 representation。

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `raw` `timeline` · **4/5** · 2026-08-13

**Research delta.** Structured memory 应该击败的 raw control 不是 single-shot BM25，而是带 session/time/local-context control 的 stateful iterative search。

[Paper](https://arxiv.org/abs/2608.12888) · [中文深读](papers/2026/2608.12888.zh.md) · [English note](papers/2026/2608.12888.md)

<details><summary><strong>约 60 秒理解 ReFind</strong></summary>

ReFind 保留原始 timestamped turns，并提供 multi-round reformulation、session fusion、local context、temporal filtering 与 seen-session state。在固定 LongMemEval-S/M 上报告 **93.2 / 89.3**，generic-agentic BM25 **78.7 / 82.2**，one-search control **84.7 / 68.9**。

它抬高了所有 semantic preprocessing 必须击败的 baseline；真正未解决的是在 semantic/acting tasks 上，strictly matched online latency、token 与 lifecycle cost 后 raw-state search 是否仍占优。

</details>

<a id="changes"></a>
## 最近真正发生了什么变化

| 变化 | 新证据 | 对研究设计的含义 |
|---|---|---|
| **Structure 的价值正在从“有关系”变成“改变可达性”。** | ReFind 抬高 raw-search baseline；CABLE 要求 stored edge 到达 host retriever 原本到不了的 evidence。 | 评估 structure 时直接问：它增加了什么 operation / reachability，代价是什么。 |
| **Memory read path 被继续拆分。** | ArborMem 把 state localization 放在 retrieval 前；QUMem 把 consumer-state reconstruction 放在 retrieval 后。 | `localize state → retrieve evidence → reconstruct consumer state` 应成为三个可独立消融的 stage。 |
| **Procedural memory 从“生成/编辑”走向“学习 + 认证 + governance”。** | WER 从 execution feedback 学 writer policy；TRUSS 用 runtime evidence gate skill promotion。 | Skill quality 不能只看文本或 task success，要区分 writer learning、executor、certification 和 maintenance。 |
| **Evaluation 开始约束 feature promotion，而不只是排名 architecture。** | D²ACCI 让 null result、protected slice 与 trace localizability 进入部署 gate。 | “分数涨了”不足以支持 component claim；stage attribution 和 non-regression 应进入默认实验设计。 |

时间视角：[weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a>
## 领域地图

`experience/archive → write → organize → state localization → access/admission → consumer state → update/evolve/forget → governance/cost/provenance`

| Boundary | 核心问题 | 当前信号 |
|---|---|---|
| **Write** | 什么值得持久化？如何生成可复用 artifact？ | Granularity 与 writer policy 都是 workload/feedback-dependent control。 |
| **Organize** | 哪些 relation 值得预计算？ | Relation 只有改变相对 host interface 的 reachability 才真正赚回成本。 |
| **State localization** | 当前 turn 恢复的是哪条历史 trajectory？ | Relevance retrieval 之前可能先需要定位 active interaction state。 |
| **Access / admission** | 什么应该检索、扩展或拒绝进入 context？ | Raw search、graph expansion、admission 是不同 operator。 |
| **Consumer state** | 下游 actor 最终应该看到什么？ | Retrieved evidence 可能还需要 reconstruction / rebinding。 |
| **Evolution / forgetting** | 哪类 adaptive state 应改变？ | Content、writer/read policy、relation 与 feedback surface 需要分开。 |
| **Governance / cost** | 哪些 artifact/feature 可以被 promote？ | Certification、paired evidence、provenance 与 lifecycle cost 正成为一等约束。 |

[进入完整 research-problem map →](categories/README.md) · [看这个方向如何被评价 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#agent-memory)

<a id="reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该带走什么 |
|---|---|---|
| **Structure 什么时候真正值得？** | ReFind → CABLE → ArborMem → QUMem | 从 raw baseline 到 complementary relation，再到 state localization 与 consumer-state reconstruction，逐层问每个 stage 是否提供不可便宜替代的 operator。 |
| **Procedural memory 如何从 artifact 变成可治理 capability？** | HyperSkill → WER → TRUSS | Representation/relations、writer learning、runtime certification 是三个不同问题。 |
| **Memory feature 怎么做 causal attribution？** | D²ACCI → QUMem → ReFind | 从 stage trace / promotion gate 出发，再看 reconstruction 与 raw-control 如何改变 attribution。 |

<a id="library"></a>
## Research Library

Weekly 不是 archive。长期找工作请按 **research problem / research line / year** 浏览：

- [中文 Research Library](library/README.md)
- [English Research Library](library/README.en.md)
- [Design anchors](papers/anchors.md)

<a id="how-to-use"></a>
## 如何使用

**30 秒：**扫 Latest 的 Research delta。  
**60–90 秒：**展开 fold，看 mechanism、closest comparison、decisive evidence、caveat。  
**5–10 分钟：**进入中文/英文 deep note 做 evidence audit。  
**长期理解：**用 Field Map 与 Research Library；只有想知道“最近怎么变”时才看 compaction。

## Scope / About / Contributing

收录标准：信息需要跨 interaction/reasoning step 持久存在或被显式管理，并实质改变 Agent 后续行为。普通 fixed RAG、单纯 long-context/KV-cache 优化、与 persistent agent state 无关的 continual learning 通常不在范围内。

这个仓库是**curated research map，不是 keyword feed**。负结果、baseline reversal 和不利的 cost/attribution 证据会被保留。

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)
