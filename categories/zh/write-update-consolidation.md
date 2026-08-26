# Write, Update & Consolidation

[← Research Map](../README.md) · [English](../write-update-consolidation.md) · [首页](../../README.md)

> **核心问题：** 一个 persistent memory unit 应该多大？什么时候写、保留、更新、合并或忘记？

## 当前判断

**The Compaction Cliff** 将 preservation contract 变成可测对象，但最强 source-fidelity 对照在 50% 压缩时几乎打平，且没有进入行为实验。**MemGuard** 则让 verifier descriptor 跨过 admission 持续控制 retrieval、merge、summary 与 archival；相对 verifier-only 的均值一致为正，却没有匹配的显著性检验。两者都是单篇 early signal。

Write side 至少包含四个不同 control：

`boundary / granularity × preservation contract × transformation frequency × forgetting`

把它们统一叫“memory construction”会掩盖真正 trade-off。**StateMem** 增加了 supersession contract：旧值可以保留用于 audit，但必须退出 active state；dependent state 则需要重算，而不是简单删除。它的正向证据主要来自 supersession 与 recompute guidance，dependency propagation 并不稳定，而且每个 scenario 需要 165–600 次 ingest call。FTA-Mem 直接显示 preferred granularity 会随 evidence density 改变；LeanMem 一类工作则说明不同 evidence type 可能需要不同 lifecycle semantics。

## Strongest signal

FTA-Mem 在 sparse dialogue 中用 situation-level unit 同时改善 quality/cost，但 LoCoMo 上更细 turn-pair memory 略高准确率、代价更高。这个 reversal 很重要：**不存在明显的全局最优 memory unit。**

另一方面，compression/consolidation 如果没有 field-preservation contract，会把 later query 才需要的细节永久擦掉；supersession 如果没有 anti-trap control，也可能过度退休仍有效的信息。因此“写得更短”或“更新得更多”都不能只按 endpoint score 衡量。

## 最大未解问题

真正需要的是 streaming controller：根据 evidence density、conflict、supersession、query distribution、budget 与 field importance 动态决定 boundary、preservation 与 recomputation，而不是每 turn 都做一次昂贵 LLM judgment，也不是全局固定 segmentation。

## 下一项 decisive evidence

构造同时包含 sparse/dense evidence、preference drift、conflict 与 delayed-use fields 的 long-running acting traces，独立变化：

`granularity × write budget × preservation rule × supersession/dependency policy × update frequency × forgetting`

同时测 storage/construction cost、stale-state error、retrieval quality 与 downstream action。

## 继续读

[FTA-Mem 中文笔记](../../papers/2026/2608.16303.zh.md) · [LeanMem](../../papers/2026/2608.03463.md) · [LycheeMemory V2](../../papers/2026/2608.12990.md)
