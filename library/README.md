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

### 原始存档 → 互补结构 → 状态定位 → 面向使用方的状态重建

[ReFind](../papers/2026/2608.12888.zh.md) → [CABLE](../papers/2026/2608.17911.zh.md) → [ArborMem](../papers/2026/2608.17534.zh.md) → [QUMem](../papers/2026/2608.16168.zh.md)

结构化记忆与原始记录不是一次性二选一。先用更强的原始记录接口作为基线，再检验预存关系是否改变可达性；历史若包含多条交错的轨迹，需要先定位当前状态；检索到的证据最后仍可能需要转换为 Agent 实际使用的状态。

### 静态程序性记忆 → 可参与执行的关系 → 学得的技能编写策略 → 经认证的能力

[HyperSkill](../papers/2026/2608.16114.zh.md) → [WER](../papers/2026/2608.17587.zh.md) → [TRUSS](../papers/2026/2608.17588.zh.md)

程序性记忆的收益可能来自关系结构、写入策略学习、执行反馈或运行时认证。若把这些变化都称为“技能记忆”，真正的因果变量就会被掩盖。

### 检索分数 → 阶段归因 → 功能上线证据

[Demystifying Agent Skills](../papers/2026/2608.14036.zh.md) → [D²ACCI](../papers/2026/2608.17756.zh.md)

检索标签、实际使用、下游成功和部署决策对应不同的评估对象。记忆功能最终需要成对、可定位且无回归的证据，架构层面的分数本身并不充分。

### 固定记忆单元 → 自适应写入约束

[LeanMem](../papers/2026/2608.03463.md) → [FTA-Mem](../papers/2026/2608.16303.zh.md) → [LycheeMemory V2](../papers/2026/2608.12990.md)

写入粒度和保留/更新语义会随工作负载改变，不适合作为全局固定的 schema 选择。

## 按年份浏览

- **2026：** 当前论文主要集中在 `papers/2026/`；可先沿上面的研究脉络阅读，或从 [设计锚点](../papers/anchors.md) 进入。
- **时间趋势：** [周度 / 月度 / 年度综合](../digests/README.md) 用于查看研究变化，不作为历史检索入口。

## 相关 Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)：追踪 Agent Memory **如何被评价，以及基准目标如何演化**。
- [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)：关注自适应信息获取，而非持久记忆生命周期。
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)：关注持久经验在数据工作中的使用。
