# Agent Memory Research Library

**中文** | [English](README.en.md) · [返回首页](../README.md)

这里不是周报归档，而是**长期可检索的研究地图**。不知道论文名、只知道自己想研究什么时，从这里开始。

## 按 Research Problem 浏览

| 问题 | 入口 | 当前核心张力 |
|---|---|---|
| **Representation & Organization** | [进入](../categories/zh/representation-organization.md) | archive 应该忠实保留，还是为当前 consumer 重构？ |
| **Retrieval & Access** | [进入](../categories/zh/retrieval-access.md) | raw search、state localization 与 pre-built relation 分别什么时候值得？ |
| **Write, Update & Consolidation** | [进入](../categories/zh/write-update-consolidation.md) | memory unit、preservation contract、update/forgetting 应如何分开？ |
| **Memory Learning & Evolution** | [进入](../categories/zh/memory-learning-evolution.md) | artifact、writer/read policy、relation 与 promotion gate 哪个在 evolve？ |
| **Evaluation & Analysis** | [进入](../categories/zh/evaluation-analysis.md) | stage attribution、utility、cost、provenance 与 deployment gate 怎么一起测？ |

## 按 Research Line 浏览

### 1. Raw archive → complementary structure → state localization → consumer-state reconstruction

[ReFind](../papers/2026/2608.12888.zh.md) → [CABLE](../papers/2026/2608.17911.zh.md) → [ArborMem](../papers/2026/2608.17534.zh.md) → [QUMem](../papers/2026/2608.16168.zh.md)

**带走的结论：** “structured vs raw”不是二元选择。先抬高 raw interface baseline，再问 stored relation 是否改变 reachability；如果历史存在多条并行 trajectory，还要先 localize active state；最后 retrieved evidence 与 actor-facing state 仍可能不同。

### 2. Static procedural memory → operational relations → learned writer → certified capability

[HyperSkill](../papers/2026/2608.16114.zh.md) → [WER](../papers/2026/2608.17587.zh.md) → [TRUSS](../papers/2026/2608.17588.zh.md)

**带走的结论：** procedural-memory gain 可能来自 relation structure、writer policy learning、execution feedback 或 runtime certification。把它们都叫“skill memory”会掩盖真正的 causal variable。

### 3. Retrieval score → stage attribution → feature-promotion evidence

[Demystifying Agent Skills](../papers/2026/2608.14036.zh.md) → [D²ACCI](../papers/2026/2608.17756.zh.md)

**带走的结论：** retrieval label、actual use、downstream success 与 deployment decision 不是同一个指标。Memory feature 最终需要 paired、localized、non-regressing evidence，而不是 architecture-level score。

### 4. Fixed memory unit → adaptive write contract

[LeanMem](../papers/2026/2608.03463.md) → [FTA-Mem](../papers/2026/2608.16303.zh.md) → [LycheeMemory V2](../papers/2026/2608.12990.md)

**带走的结论：** write granularity 和 preservation/update semantics 更像 workload-dependent control，而不是一次定死的 schema 选择。

## 按年份浏览

- **2026：** 当前主要工作集中在 `papers/2026/`；优先从上面的 research line 或 [design anchors](../papers/anchors.md) 进入。
- **时间趋势：** [Weekly / Monthly / Yearly synthesis](../digests/README.md) 只回答“什么发生了变化”，不承担历史检索。

## Cross-Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)：看 Agent Memory **如何被评价、benchmark target 如何演化**。
- [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)：当核心变成 adaptive information acquisition，而不是 persistent memory lifecycle。
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)：当 persistent experience 被用于 data work。
