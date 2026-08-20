# Agent Memory Research Library

**中文** | [English](README.en.md) · [返回首页](../README.md)

这里不是周报归档，而是**长期可检索的研究地图**。不知道论文名、只知道自己想研究什么时，从这里开始。

## 按 Research Problem 浏览

| 问题 | 入口 | 当前核心张力 |
|---|---|---|
| **Representation & Organization** | [进入](../categories/zh/representation-organization.md) | archive 应该忠实保留，还是为当前 consumer 重构？ |
| **Retrieval & Access** | [进入](../categories/zh/retrieval-access.md) | raw-state search 能做到什么，structure 什么时候才真正赚回成本？ |
| **Write, Update & Consolidation** | [进入](../categories/zh/write-update-consolidation.md) | memory unit、更新频率、preservation contract、forgetting 应如何分开设计？ |
| **Memory Learning & Evolution** | [进入](../categories/zh/memory-learning-evolution.md) | 到底是 content、read policy、relation 还是 governance 在 evolve？ |
| **Evaluation & Analysis** | [进入](../categories/zh/evaluation-analysis.md) | retrieval quality 之外，utility、cost、authority、provenance 和 descendant effects 怎么测？ |

## 按 Research Line 浏览

### 1. Raw archive → structured access → consumer-state reconstruction

[ReFind](../papers/2026/2608.12888.zh.md) → [RippleMem](../papers/2026/2608.13334.zh.md) → [QUMem](../papers/2026/2608.16168.zh.md) → [QCR](../papers/2026/2608.12847.md)

**你应该带走的结论：**“要不要 structure”不是一个二元选择。先问 raw interface 能否在线恢复需要的信息，再问预建 relation 是否提供了额外 operator，最后区分 retrieved evidence 和 actor 最终消费的 state。

### 2. Static procedural memory → evolving skill → evolving read policy

[Demystifying Agent Skills](../papers/2026/2608.14036.zh.md) → [SkillEvo](../papers/2026/2608.13120.zh.md) → [ERSkill](../papers/2026/2608.12720.md) → [HyperSkill](../papers/2026/2608.16114.zh.md)

**你应该带走的结论：** procedural memory 的增益不能只归因给“有 skill”。表示、feedback surface、retrieval policy、relation 和 maintenance 都可能是独立变量。

### 3. Fixed memory unit → adaptive write contract

[LeanMem](../papers/2026/2608.03463.md) → [FTA-Mem](../papers/2026/2608.16303.zh.md) → [LycheeMemory V2](../papers/2026/2608.09424.md)

**你应该带走的结论：** write granularity 和 preservation/update semantics 是 workload-dependent control，而不是一个可以一次定死的 schema 选择。

## 按年份浏览

- **2026：** 当前主要工作集中在 `papers/2026/`；优先从上面的 research line 或 [design anchors](../papers/anchors.md) 进入，而不是按日期顺序扫文件。
- **时间趋势：** [Weekly / Monthly / Yearly synthesis](../digests/README.md) 只负责回答“什么发生了变化”，不承担历史检索。

## Cross-Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)：看 Agent Memory **如何被评价、benchmark target 如何演化**。
- [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)：当问题核心变成 adaptive information acquisition，而不是 persistent memory lifecycle。
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar)：当 persistent experience 被用于数据分析/数据工程工作流。
