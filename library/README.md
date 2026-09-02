# Agent Memory Research Library

**中文** | [English](README.en.md) · [返回首页](../README.md)

可以按研究问题、研究脉络或年份查找论文；不知道论文名时，从下面的问题入口开始。

## 按研究问题浏览

| 问题 | 入口 | 当前核心张力 |
|---|---|---|
| **Representation & Organization** | [进入](../categories/zh/representation-organization.md) | 存档应该忠实保留来源，还是根据当前使用方重构状态？ |
| **Retrieval & Access** | [进入](../categories/zh/retrieval-access.md) | 原始记录搜索、状态定位和预先构建的关系分别在什么条件下值得？ |
| **Write, Update & Consolidation** | [进入](../categories/zh/write-update-consolidation.md) | 如何区分记忆单元、保留规则、更新频率和遗忘？ |
| **Memory Learning & Evolution** | [进入](../categories/zh/memory-learning-evolution.md) | 真正发生演化的是产物、写入/读取策略、关系，还是上线门槛？ |
| **Evaluation & Analysis** | [进入](../categories/zh/evaluation-analysis.md) | 如何同时评估阶段归因、效用、成本、溯源和部署门槛？ |

## 按研究脉络浏览

### 统一压缩 → Typed preservation → 持久生命周期证据

[The Compaction Cliff](../papers/2026/2608.22752.zh.md) → [MemGuard](../papers/2026/2608.21867.zh.md)

先判断哪些 memory type 必须精确保留，再判断 reliability evidence 是否在 admission 后继续控制 access 与 maintenance。两者都只有单篇证据，上游与治理成本仍未解决。

### Stateless access → 记住 relevance → Applicability-gated use

[EARM](../papers/2026/2608.22767.zh.md) → [BASM](../papers/2026/2608.22339.zh.md)

Access policy 可以积累 relevance experience，但 retrieved procedure 仍需要 current-state validity boundary。应在被打乱、可增长的 store 上配平 context 与生命周期成本。

### Outcome contrast → Curated procedure → 对抗式持久写入

[CONTRAMEM](../papers/2026/2608.22533.zh.md) → [InjecMEM](../papers/2026/2608.23471.zh.md)

Outcome diversity 可能帮助 procedure construction，普通 write path 也形成持久攻击面；需要分开 useful transfer、harmful steering、coverage 与 construction compute。

### 原始存档 → 互补 / 多源访问 → 状态定位 → 面向使用方的状态重建

[ReFind](../papers/2026/2608.12888.zh.md) → [CABLE](../papers/2026/2608.17911.zh.md) / [MemFuse](../papers/2026/2608.18704.zh.md) → [ArborMem](../papers/2026/2608.17534.zh.md) → [QUMem](../papers/2026/2608.16168.zh.md)

结构化记忆与原始记录不是一次性二选一。先用更强的原始记录接口作为基线，再检验预存关系是否改变可达性；历史若包含多条交错的轨迹，需要先定位当前状态；检索到的证据最后仍可能需要转换为 Agent 实际使用的状态。

### Candidate 承诺 → 状态取代 → 面向当前使用方的适用性判断

[Remember, Verify, or Ask?](../papers/2026/2608.19564.zh.md) → [StateMemBench / StateMem](../papers/2026/2608.19652.zh.md) → [When Stale Constraints Go Unchecked](../papers/2026/2608.25553.zh.md) → [MemTrapBench](../papers/2026/2608.20202.zh.md)

持久状态需要三种不同决策：candidate information 是否有 authority 进入 memory，哪些旧状态被它取代，以及 retrieval 后的历史是否适用于当前 consumer。现有证据仍受 benchmark 限制，还没有在一条真实执行的 lifecycle 中把三个阶段连起来。

### 学得访问 / 编写 / 课程策略 → 状态落地与定位式演化 → 经认证产物 / Harness 提交

[Hindsight Memory-PRM](../papers/2026/2608.29605.zh.md) / [SkillGate](../papers/2026/2608.18852.zh.md) / [WER](../papers/2026/2608.17587.zh.md) / [SPADE](../papers/2026/2608.19197.zh.md) → [Recuris](../papers/2026/2608.24876.zh.md) / [HiPS](../papers/2026/2608.25329.zh.md) / [KOPE](../papers/2026/2608.25570.zh.md) → [TRUSS](../papers/2026/2608.17588.zh.md) / [Harness Continual Learning](../papers/2026/2608.19013.zh.md)

程序性学习的收益可能来自 credit assignment、read/write policy、training-side experience、verified working state、invocation control、failure localization 或 promotion gate。Hindsight 进一步要求先区分 entry-presence utility 与 action-level credit，并把 audit compute 计入监督成本。Recuris 的 same-library 与 retry-matched 对照进一步说明：先定位真正改变 later behavior 的控制层，再讨论“self-improving memory”。

### 检索分数 → 阶段归因 → Gate 资格 → 功能上线证据

[Demystifying Agent Skills](../papers/2026/2608.14036.zh.md) → [Competence, Not Accuracy](../papers/2026/2608.18719.zh.md) → [D²ACCI](../papers/2026/2608.17756.zh.md)

检索标签、实际使用、下游成功和部署决策对应不同的评估对象。记忆功能最终需要成对、可定位且无回归的证据，架构层面的分数本身并不充分。

### 写入粒度 → 活跃保留 / Skill Set 选择 → 后续执行

[Break It Down, Pass It On](../papers/2026/2608.20274.zh.md) → [Weighted Memory Tree](../papers/2026/2608.20631.zh.md) / [Optimal Skill Selection](../papers/2026/2608.19993.zh.md)

被写入的单元、保持活跃的状态以及最终暴露的集合是三种不同 policy。现有研究能测到后续行为改变，但仍受 package attribution、异质结果或高监督成本限制。

### Verbatim Persistence → 可执行记忆卫生 → Provenance 效用边界

[DreamBench-SWE](../papers/2026/2608.20664.zh.md) → [Utility Under Attack](../papers/2026/2608.21230.zh.md)

先要求早期状态改变可执行结果并击败 verbatim archive，再检验 provenance defense 在 suppress poison 的同时是否保留 useful evidence。

### 固定记忆单元 → 自适应写入约束

[LeanMem](../papers/2026/2608.03463.md) → [FTA-Mem](../papers/2026/2608.16303.zh.md) → [LycheeMemory V2](../papers/2026/2608.12990.md)

写入粒度和保留/更新语义会随工作负载改变，不适合作为全局固定的 schema 选择。

### Flat interleaved history → episode reconstruction → streaming state contracts

[SCALE-QA / TSIM](../papers/2026/2608.25655.zh.md) → [VoiceMem](../papers/2026/2608.26005.zh.md)

先问当前 query 延续的是哪一个 coherent episode，再问 factual/entity state 与 affect/persona state 是否应该走不同 runtime contract。前者的 segmentation/summary/hierarchy 仍是 package，后者的低 latency 仍只覆盖 retrieval path；两者都需要完整 lifecycle cost 对照。

## 按年份浏览

- **2026：** 当前论文主要集中在 `papers/2026/`；可先沿上面的研究脉络阅读，或从 [设计锚点](../papers/anchors.md) 进入。
- **时间趋势：** [周度 / 月度 / 年度综合](../digests/README.md) 用于查看研究变化，不作为历史检索入口。

## 相关 Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)：追踪 Agent Memory **如何被评价，以及基准目标如何演化**。
- [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)：关注自适应信息获取，而非持久记忆生命周期。
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)：关注持久经验在数据工作中的使用。
