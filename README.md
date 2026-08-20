# Agent Memory Radar

**中文** | [English](README.en.md)

*面向 LLM 与多模态 Agent 的长期记忆研究地图。*

[最新论文](#latest) · [最近变化](#changes) · [领域地图](#field-map) · [阅读路径](#reading-paths) · [完整资料库](#library)

最后更新：**2026-08-20**

<a id="latest-papers"></a>
<a id="latest"></a>
## 最新论文

### [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](papers/2026/2608.17911.md)
`Retrieval & Access` · `episodic` `graph` · **4/5** · 2026-08-18

只有当记忆边能到达宿主检索器原本漏掉的证据时，CABLE 才保留这条边，从而让结构成为 **retriever-complementary operator**。

[论文](https://arxiv.org/abs/2608.17911) · [中文深读](papers/2026/2608.17911.zh.md) · [英文深读](papers/2026/2608.17911.md)

<details><summary><strong>CABLE 的互补扩展</strong></summary>

CABLE 在写入时同时构造直接语义邻域和 antecedent-query candidates，去掉两者的重叠项，只验证余下候选并写入有向链接。查询时，系统先运行原有的宿主检索器，再从种子结果做一跳扩展；最终证据数量不变。

在 A-MEM 宿主与最终证据预算均相同的设置下，LoCoMo Qwen3.5 从 **71.23 升至 74.81**，MA-LongMemEval Qwen 从 **59.33 升至 65.33**。不过时序推理子集出现下降，而且论文尚未在全生命周期成本匹配的条件下，把写入时的查询生成/验证与强在线搜索基线比较。

</details>

### [D²ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](papers/2026/2608.17756.md)
`Evaluation & Analysis` · `structured` · **4/5** · 2026-08-18

D²ACCI 不以总分上涨作为记忆功能的上线依据；成对证据、受保护子集、阶段轨迹和确定性的上线门槛必须共同支持部署决定。

[论文](https://arxiv.org/abs/2608.17756) · [中文深读](papers/2026/2608.17756.zh.md) · [英文深读](papers/2026/2608.17756.md)

<details><summary><strong>D²ACCI 的上线门槛</strong></summary>

D²ACCI 在带监测的记忆运行时之外构建诊断循环：`typed traces → paired baseline/candidate → significance + protected slices + diagnostic coverage → accept | monitor | feature-flag | reject`。

论文报告 Supplement extraction、session-memory retrieval 和 Forget Guard 均有显著的成对增益；BM25/RRF 在 LoCoMo 与 LongMemEval 上都不显著，因此只作为监控标记保留。它的主要贡献是**让阶段级归因和无回归要求成为上线约束**；DCR 指标本身居于次要位置。

</details>

### [Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback](papers/2026/2608.17587.md)
`Memory Learning & Evolution` · `procedural` · **4/5** · 2026-08-18

WER 根据执行结果训练**技能写入策略**；它不只让模型在推理时反思现有的技能文本。

[论文](https://arxiv.org/abs/2608.17587) · [中文深读](papers/2026/2608.17587.zh.md) · [英文深读](papers/2026/2608.17587.md)

<details><summary><strong>用执行反馈学习技能编写策略</strong></summary>

候选技能由冻结的 Agent 多次执行，程序化验证器对结果评分，再由 group-relative RL 更新优化器；同一技能/任务中成功与失败混合的轨迹会进入下一轮细化状态。

在使用同一个 Qwen3-4B 优化器模型和同一套细化流程的比较中，BFCL v4 从 **67.28 升至 76.63**，tau2 从 **40.43 升至 50.72**。再增加一轮细化后成绩反而回落，说明“持续自我修改”并非单调更好。Rollout 成本高且依赖可靠的验证器，是这套方法的主要局限。

</details>

### [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](papers/2026/2608.17588.md)
`Memory Learning & Evolution` · `procedural` `structured` · **4/5** · 2026-08-18

TRUSS 把生成的技能视为**须先认证、再持久化的可执行产物**：通过静态约束后，还要完成受控影子执行并保留溯源记录。

[论文](https://arxiv.org/abs/2608.17588) · [中文深读](papers/2026/2608.17588.zh.md) · [英文深读](papers/2026/2608.17588.md)

<details><summary><strong>技能持久化之前的认证</strong></summary>

流程是 `generate → static function/safety checks → shadow execution → trace → function/safety record → refine → re-check → promote`。在匹配的 SkillInject 产物上，LLM 检查器为 **44.64% precision / 19.05% recall**，静态检查器为 **81.55 / 94.05**，完整 TRUSS 为 **100 / 100**。

论文中的生成收益来自认证与细化的整套方案，并明显受执行器影响。现有证据支持为程序性记忆设置**上线/治理边界**，但不能把“文本看起来合理”当成可复用能力的充分条件。

</details>

### [ArborMem: Navigating Interaction States with Memory Forests](papers/2026/2608.17534.md)
`Retrieval & Access` · `episodic` `hierarchical` · **4/5** · 2026-08-18

ArborMem 在检索之前增加**状态定位**：先判断当前轮次接续哪条历史交互分支，恢复分支内轨迹后，再检索补充证据。

[论文](https://arxiv.org/abs/2608.17534) · [中文深读](papers/2026/2608.17534.zh.md) · [英文深读](papers/2026/2608.17534.md)

<details><summary><strong>检索之前的状态定位</strong></summary>

在长期交互中，主题相关的历史记录未必属于当前要恢复的轨迹。ArborMem 把读取路径拆成 `localize parent state → restore branch trajectory → retrieve cross-branch support → answer → commit new state`。

在固定的 LongMemEval 子集上，30B 模型去掉状态定位后从 **82 降至 70**，4B 模型则从 **48 降至 46**，效果明显受模型规模影响。这组结果将状态定位隔离为一个独立边界，但还不能证明记忆森林表示不可替代。

</details>

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `personalization` · **4/5** · 2026-08-17

QUMem 把检索到的历史作为证据，并在查询到来后重建**当前用户状态**；消融结果显示，读取端重建是贡献最大的阶段。

[论文](https://arxiv.org/abs/2608.16168) · [中文深读](papers/2026/2608.16168.zh.md) · [英文深读](papers/2026/2608.16168.md)

<details><summary><strong>面向查询的用户状态重建</strong></summary>

QUMem 先形成 semantic episodes 和 typed facts/preferences/insights，再把当前任务拆成信息需求，按类型检索，最后联合证据重建当前用户状态。

在 PersonaMem + GPT-4o-mini 上，完整系统得分为 **61.02**；去掉 episodes 后为 **58.38**，去掉 typed decomposition 后为 **57.11**，去掉 reconstruction 后为 **54.51**。下一步需要在检索证据与综合预算均匹配的条件下，验证显式状态重建是否仍然值得。

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `graph` · **4/5** · 2026-08-17

HyperSkill 让轨迹之间的高阶关系直接参与检索、技能排序和维护。现有证据支持整套结构化访问方案，尚不能单独证明超图表示不可替代。

[论文](https://arxiv.org/abs/2608.16114) · [中文深读](papers/2026/2608.16114.zh.md) · [英文深读](papers/2026/2608.16114.md)

<details><summary><strong>访问路径中的高阶关系</strong></summary>

完整系统同时检索子任务与轨迹，融合超边，再用跨轨迹关系对技能排序。Qwen3 在 xBench / GAIA / WebWalkerQA 上分别得到 **52.00 / 36.97 / 50.59**；去掉超图后分别为 **41.00 / 35.76 / 44.71**。

这项消融同时改变了访问流程。下一步需要固定任务分解、双路径检索、排序和维护，只替换表示方式。

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `raw` `timeline` · **4/5** · 2026-08-13

ReFind 表明，结构化记忆需要击败的原始记录对照不应只是单次 BM25 检索，而应包括具有会话、时间和局部上下文控制的有状态迭代搜索。

[论文](https://arxiv.org/abs/2608.12888) · [中文深读](papers/2026/2608.12888.zh.md) · [英文深读](papers/2026/2608.12888.md)

<details><summary><strong>更强的原始记录搜索对照</strong></summary>

ReFind 保留带时间戳的原始对话轮次，并提供多轮改写、会话融合、局部上下文、时间过滤和已读会话状态。论文在固定的 LongMemEval-S/M 上报告 **93.2 / 89.3**；generic-agentic BM25 为 **78.7 / 82.2**，one-search 对照为 **84.7 / 68.9**。

这组结果抬高了语义预处理必须击败的基线。尚未解决的问题是：在语义/行动任务上匹配在线延迟、token 和完整的全生命周期成本后，原始状态搜索是否仍占优。

</details>

<a id="whats-changing"></a>
<a id="changes"></a>
## 最近真正发生了什么变化

| 变化 | 新证据 | 对研究设计的含义 |
|---|---|---|
| **衡量结构的价值，重点正从“是否包含关系”转向“是否改变可达性”。** | ReFind 抬高了原始搜索基线；CABLE 要求预存边到达宿主检索器原本漏掉的证据。 | 评估结构时，应明确它增加了哪种操作或可达性，以及相应代价。 |
| **记忆的读取流程被进一步拆分。** | ArborMem 把状态定位放在检索前；QUMem 把面向使用方的状态重建放在检索后。 | `定位状态 → 检索证据 → 重建使用方状态` 应作为三个可独立消融的阶段。 |
| **程序性记忆开始同时纳入学习、认证和治理。** | WER 用执行反馈学习写入策略；TRUSS 用运行时证据控制技能上线。 | 评估技能质量时，不能只看文本或任务成功率，还要区分技能编写策略学习、执行器、认证和维护。 |
| **评估开始约束功能上线，而不只用于架构排名。** | D²ACCI 把无显著结果、受保护子集和轨迹可定位性纳入部署门槛。 | 分数上涨不足以支持组件归因；默认实验设计还应包含阶段归因和无回归要求。 |

时间视角：[周度](digests/README.md) · [月度](digests/monthly/2026-08.md) · [年度](digests/yearly/2026.md)

<a id="research-map"></a>
<a id="field-map"></a>
## 领域地图

| 阶段 | 核心问题 | 当前信号 |
|---|---|---|
| **Write** | 什么值得持久化？如何生成可复用产物？ | 粒度和写入策略的选择都取决于工作负载与反馈。 |
| **Organize** | 哪些关系值得预先计算？ | 只有关系能扩展宿主接口的可达性时，成本才可能合理。 |
| **State localization** | 当前轮次接续哪条历史轨迹？ | 在相关性检索之前，系统可能需要先定位当前交互状态。 |
| **Access / admission** | 哪些内容应该被检索、扩展或拒绝进入上下文？ | 原始记录搜索、图扩展和准入属于不同操作。 |
| **Consumer state** | 下游 Agent 最终应该看到什么？ | 检索到的证据可能仍需经过重建或重新绑定。 |
| **Evolution / forgetting** | 哪类自适应状态应根据哪些反馈改变？ | 内容、写入/读取策略、关系和反馈界面需要分别考察。 |
| **Governance / cost** | 哪些产物或功能可以上线？ | 认证、成对证据、溯源和全生命周期成本正成为一等约束。 |

[进入完整研究问题地图 →](categories/README.md) · [看这个方向如何被评价 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#agent-memory)

<a id="reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该带走什么 |
|---|---|---|
| **结构何时值得额外成本？** | ReFind → CABLE → ArborMem → QUMem | 从原始记录基线、互补关系读到状态定位和面向使用方的状态重建，逐层检查每个阶段是否提供了无法低成本替代的操作。 |
| **程序性记忆如何从产物变成可治理的能力？** | HyperSkill → WER → TRUSS | 表示/关系、技能编写策略学习和运行时认证分别对应不同问题。 |
| **如何对记忆功能做因果归因？** | D²ACCI → QUMem → ReFind | 先看阶段轨迹与上线门槛，再考察状态重建和原始记录对照如何改变归因。 |

<a id="library"></a>
## 研究资料库

- [中文研究资料库](library/README.md)
- [English Research Library](library/README.en.md)
- [设计锚点](papers/anchors.md)

## 收录范围与贡献

收录标准：信息需要跨交互/推理步骤持久存在或被显式管理，并实质改变 Agent 后续行为。普通固定 RAG、单纯的长上下文/KV-cache 优化，以及与持久 Agent 状态无关的持续学习通常不在范围内。

负结果、基线反转和不利的成本/归因证据，只要会改变研究结论，就会保留。

[推荐论文](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [报告勘误](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [贡献指南](CONTRIBUTING.md)

相关 Radar：[Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)
