# Agent Memory Radar

**中文** | [English](README.en.md)

*面向 LLM 与多模态 Agent 的长期记忆研究地图。*

这个 Radar 主要回答两个问题：**Agent Memory 最近真正变了什么？Memory lifecycle 的哪一个阶段值得付出额外复杂度？**

**Radar Family：** [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar) · **Agent Memory** · [Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar) · [Data Agent](https://github.com/H20Zhang/Data-Agent-Radar)

[30 秒：最新工作](#latest) · [5 分钟：领域地图](#field-map) · [15 分钟：阅读路径](#reading-paths) · [浏览全部](#library)

> **先建立一个简单模型：** `experience → write → organize → access/admit → reconstruct consumer state → update/forget → govern`
>
> **当前判断：** “哪种 memory architecture 最好”这个问题太粗。更有判别力的问题是：**到底改了哪个 lifecycle boundary、相比最简单且公平的替代方案多做了什么、实验是否真的隔离了这一阶段的贡献。**

最后更新：**2026-08-20**

<a id="latest"></a>
## 最新论文

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `semantic` `structured` `personalization` · **4/5** · 2026-08-17

**Research delta.** QUMem 不把检索结果直接当成最终 memory state，而是把历史记录当证据，在 query 到来后重建**当前 user state**；它的消融里，这个 read-side reconstruction 也是贡献最大的阶段。

[Paper](https://arxiv.org/abs/2608.16168) · [英文研究笔记](papers/2026/2608.16168.md)

<details><summary><strong>约 60 秒理解 QUMem</strong></summary>

固定 session/turn 边界和一次性 retrieval 可能返回“单条都相关、合起来却不能代表当前用户状态”的碎片。QUMem 先构建 semantic episodes，并抽取 facts / preferences / insights；query 到来后，再把任务拆成 information needs，做 typed retrieval，最后联合历史证据重建当前 user state 后再回答或行动。

最有信息量的不是 headline baseline，而是阶段消融：PersonaMem + GPT-4o-mini 上，**61.02 full → 58.38 去掉 episode construction → 57.11 去掉 typed decomposition → 54.51 去掉 user-state reconstruction**。真正未解决的问题是：如果把 retrieved evidence 和 synthesis budget 都严格匹配，显式 reconstruction 是否仍然优于更简单的 provenance-aware 聚合。

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `structured` `graph` · **4/5** · 2026-08-17

**Research delta.** HyperSkill 的关键不是“hypergraph 比 vector 更高级”，而是让高阶 trajectory 关系真正参与 retrieval、skill ranking 和 maintenance。

[Paper](https://arxiv.org/abs/2608.16114) · [英文研究笔记](papers/2026/2608.16114.md)

<details><summary><strong>约 60 秒理解 HyperSkill</strong></summary>

Flat skill store 容易丢掉 subtask、可复用 skill 与结果之间的高阶关系。HyperSkill 同时检索 subtask 和 trajectory，把命中的 hyperedges 合并，再按跨 trajectory 共现关系排名 skill，执行后继续更新和裁剪结构。

Qwen3 上，论文报告 full system 在 xBench / GAIA / WebWalkerQA 为 **52.00 / 36.97 / 50.59**；去掉 hypergraph 后为 **41.00 / 35.76 / 44.71**。但这个 ablation 同时改变了 access pipeline，因此它更支持“整套 structural retrieval package 有效”，还不能干净证明 hypergraph 表示本身不可替代。下一步应固定 decomposition、dual-path retrieval、ranking 和 maintenance，只替换表示结构。

</details>

### [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](papers/2026/2608.16071.md)
`Retrieval & Access` · `procedural` `structured` · **3/5** · 2026-08-17

**Research delta.** Procedural memory 的 relevance 更适合围绕 **capability + parameter structure** 建模，而不是只看整个 skill document；不过在线 query expansion 的收益并不稳定。

[Paper](https://arxiv.org/abs/2608.16071) · [Code](https://github.com/MatZaharia/Skill2Query) · [英文研究笔记](papers/2026/2608.16071.md)

### [FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue](papers/2026/2608.16303.md)
`Write, Update & Consolidation` · `episodic` `timeline` · **3/5** · 2026-08-17

**Research delta.** Memory-unit granularity 更像一个 workload parameter：稀疏对话里 situation-level memory 更合适，而更密集的对话可能让 turn-pair memory 略占准确率优势，但代价更高。

[Paper](https://arxiv.org/abs/2608.16303) · [英文研究笔记](papers/2026/2608.16303.md)

### [Demystifying Agent Skills: Why They Work—Until They Don’t](papers/2026/2608.14036.md)
`Evaluation & Analysis` · `procedural` `coding` · **4/5** · 2026-08-14

**Research delta.** 固定同一批 source trajectories 后，标准化 Skills 仍优于 Workflow Memory，主要作用像**procedural anchor**；同时，exact retrieval label 和 downstream utility 明显不是同一个量。

[Paper](https://arxiv.org/abs/2608.14036) · [英文研究笔记](papers/2026/2608.14036.md)

<details><summary><strong>约 60 秒理解这篇结果</strong></summary>

这篇工作的价值在于把 representation 和 source experience 分开：同一批历史 trajectory 分别变成 Workflow Memory 或 SKILL.md，然后单独测 retrieval、selection、actual use 和最终成功率。

Skills 相比 Workflow Memory 高 **6.06 points**；作者把 **65.7%** 的 skill 成功案例归为 procedural anchoring，而 knowledge injection 只有 **4.5%**。当 pool size 从 **5→100** 时，actual-use precision 从 **29.6%→3.3%**，但 downstream success 相对稳定。这说明“是否命中所谓 ground-truth skill”可能不是最好的 utility proxy。真正需要验证的是大规模、持续演化 skill library 以及非软件任务。

</details>

### [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](papers/2026/2608.13334.md)
`Retrieval & Access` · `episodic` `graph` · **4/5** · 2026-08-13

**Research delta.** RippleMem 把第一次召回到的 memory 变成**继续寻找缺失证据的 anchor**；而 matched RF-Mem control 说明，在 memory unit 和 evidence budget 更接近时，仍有一部分收益存在。

[Paper](https://arxiv.org/abs/2608.13334) · [英文研究笔记](papers/2026/2608.13334.md)

<details><summary><strong>约 60 秒理解 RippleMem</strong></summary>

跨 session 证据分散时，first-hop memory 即使相关，也可能不完整。RippleMem 预先建立稀疏 association；第一次 recall 后检测缺失支持，再围绕选中的 anchor 做 bounded local expansion，把补齐的证据组装到固定预算内。

LoCoMo LLM-judge 上，论文报告 full system **87.14**，matched RF-Mem **83.83**，去掉 graph expansion **83.12**。这比“graph vs 一个很弱的 flat baseline”更有判别力，但是否值得部署仍取决于 build/query cost，在 acting agent 上尤其需要严格匹配 latency 和 lifecycle cost。

</details>

### [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](papers/2026/2608.13120.md)
`Memory Learning & Evolution` · `procedural` · **4/5** · 2026-08-13

**Research delta.** Multi-turn interaction 在 single-turn feedback 已开始饱和后，仍会继续暴露可修复的 skill 缺陷；governance 的主要价值是限制 regression 和 bloat。

[Paper](https://arxiv.org/abs/2608.13120) · [英文研究笔记](papers/2026/2608.13120.md)

<details><summary><strong>约 60 秒理解 SkillEvo</strong></summary>

这里最值得看的变量是 feedback surface。SkillEvo 在 multi-turn task 中反复执行、做 failure attribution、进行 bounded edits，再通过 governance 持久化 checkpoint。四轮 task success 达到 **81.8%**，matched single-turn-QA evolution 为 **66.4%**；去掉 governance 后成功率为 **78.6%**，但 bloat 从 **+2.8%** 增加到 **+16.2%**。

因此当前证据更强地支持“更丰富的交互反馈有价值”，而不是某个具体 editing algorithm 已经被证明最优。下一步需要真实用户反馈，并把 rollout 与 maintenance cost 一起计费。

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `episodic` `raw` `timeline` · **4/5** · 2026-08-13

**Research delta.** 对 structured memory 来说，真正应该比较的 raw baseline 不是 single-shot BM25，而是带 session/time/local-context control 的 stateful iterative search。

[Paper](https://arxiv.org/abs/2608.12888) · [英文研究笔记](papers/2026/2608.12888.md)

<details><summary><strong>约 60 秒理解 ReFind</strong></summary>

很多 structured-memory gain 可能来自 baseline 太弱。ReFind 保留原始 timestamped turns，并提供 turn-level BM25、multi-round reformulation、session fusion、邻接 context、temporal filter 和 seen-session state。

在固定 LongMemEval-S/M 上，ReFind 报告 **93.2 / 89.3**，generic-agentic BM25 为 **78.7 / 82.2**，one-search control 为 **84.7 / 68.9**。这直接抬高了 semantic preprocessing 必须击败的 baseline。尚未解决的是：在 semantic/acting tasks 上，如果严格匹配 online token、latency 和 total lifecycle cost，raw-state search 是否仍然占优。

</details>

<a id="changes"></a>
## 最近真正发生了什么变化

| 变化 | 新证据 | 对研究设计的含义 |
|---|---|---|
| **Structure 必须先击败一个 competent raw-state control。** | ReFind 表明 raw history + stateful search 能回收很多过去归因给 semantic preprocessing 的收益；RippleMem 又说明 structure 在提供额外 operator 时仍可能值得。 | 不再比较“structured vs unstructured”标签，而比较它们真正多提供了什么操作，以及为此付出多少成本。 |
| **Retrieved evidence 不等于 consumer state。** | QUMem 在 retrieval 后重建当前 user state；trajectory reuse 也显示 stale binding 需要重新绑定。 | Retrieval quality 和 downstream state construction 应分开评估。 |
| **Memory evolution 首先要问：到底什么在 evolve？** | SkillEvo 改 feedback surface；ERSkill 改 read policy；HyperSkill 让 relation 进入 retrieval/maintenance。 | Content、access policy、structure、feedback 与 governance 不应打包成一个“self-evolving memory”分数。 |

时间视角：[weekly](digests/README.md) · [monthly](digests/monthly/2026-08.md) · [yearly](digests/yearly/2026.md)

<a id="field-map"></a>
## 领域地图

`experience/archive → write → organize → access/admission → consumer state → update/evolve/forget → governance/cost/provenance`

| Boundary | 核心问题 | 当前信号 |
|---|---|---|
| **Write** | 什么值得持久化？一个 memory unit 应该多大？ | Granularity 会随 evidence density 改变，很难有一个全局最优单位。 |
| **Organize** | 哪些 relation / representation 值得预计算？ | Structure 只有在提供 raw-state interface 无法便宜恢复的 operator 时才真正赚回成本。 |
| **Access / admission** | 什么应该检索、扩展，什么应该拒绝进入 context？ | Relevance、iterative access、admission 是不同控制点。 |
| **Consumer state** | 下游 actor 最终应该看到什么？ | Retrieved evidence 可能还需要 reconstruction / rebinding。 |
| **Evolution / forgetting** | 哪一类 adaptive state 应改变？依据什么 feedback？ | Content、read policy、relation、governance 是不同轴。 |
| **Governance / cost** | 整个生命周期里 memory 值不值得部署？ | Endpoint recall 看不到 provenance、authority、descendant effects、construction 与 serving cost。 |

[进入完整 research-problem map →](categories/README.md) · [看这个方向如何被评价 →](https://github.com/H20Zhang/Agent-Benchmark-Radar#agent-memory)

<a id="reading-paths"></a>
## 阅读路径

| 你想回答的问题 | 建议顺序 | 应该学到什么 |
|---|---|---|
| **Structure 什么时候真正值得？** | [ReFind](papers/2026/2608.12888.md) → [RippleMem](papers/2026/2608.13334.md) → [MESA](papers/2026/2608.10108.md) | 先建立强 raw-state baseline；然后问 structure 到底提供了什么额外 operator。 |
| **为什么 retrieval 不是最后一步？** | [QUMem](papers/2026/2608.16168.md) → [QCR](papers/2026/2608.12847.md) → [Demystifying Agent Skills](papers/2026/2608.14036.md) | Selection、reconstruction/rebinding、procedural reuse 是不同阶段。 |
| **Memory 怎么变成 self-improving state？** | [SkillEvo](papers/2026/2608.13120.md) → [ERSkill](papers/2026/2608.12720.md) → [HyperSkill](papers/2026/2608.16114.md) | 分开看 feedback source、read policy、structure 与 maintenance。 |

<a id="library"></a>
## Research Library

历史工作不应该只能按某一周找到。

- **[按 research problem / research line / year 浏览](library/README.md)**
- **[Research problem map](categories/README.md)**
- **[长期 design anchors](papers/anchors.md)**
- **[时间维度 synthesis](digests/README.md)**

## 怎么用这个 Radar

**先扫** Latest Papers 的一句 Research delta；**再展开**重要论文的 60–90 秒解释；真正要判断 claim 是否站得住，再进入 research note 看 mechanism、closest comparison、decisive evidence、caveat 和 lifecycle attribution。没有具体 paper 名时，从 Field Map 或 Research Library 进入，而不是从周报倒着翻。

## Scope

纳入的工作需要让某类信息**跨 interaction / reasoning step 持续存在或被显式管理，并改变 Agent 之后的行为**。通常包括 write、organization、access/admission、consumer-state construction、update/forget、policy evolution，以及 deployment-facing memory evaluation。

普通 fixed RAG、泛化 long-context modeling、KV-cache optimization、与 persistent agent state 无关的 continual learning 通常不纳入。

## About / Contributing

这是一个**研究判断地图，不是关键词 exhaust feed**。强结论至少要回答：**改了什么？相比什么？实验没有隔离出什么？**

[推荐论文](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [报告修正](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [维护文档](docs/MAINTENANCE.md)
