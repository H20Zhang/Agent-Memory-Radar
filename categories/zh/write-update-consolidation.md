# Write, Update & Consolidation

[← Research Map](../README.md) · [English](../write-update-consolidation.md) · [首页](../../README.md)

> **核心问题：** 一个 persistent memory unit 应该多大？什么时候写、保留、更新、合并或忘记？

## 当前判断

Write side 至少包含四个不同 control：

`boundary / granularity × preservation contract × transformation frequency × forgetting`

把它们统一叫“memory construction”会掩盖真正 trade-off。FTA-Mem 直接显示 preferred granularity 会随 evidence density 改变；LeanMem 一类工作则说明不同 evidence type 可能需要不同 lifecycle semantics。

## Strongest signal

FTA-Mem 在 sparse dialogue 中用 situation-level unit 同时改善 quality/cost，但 LoCoMo 上更细 turn-pair memory 略高准确率、代价更高。这个 reversal 很重要：**不存在明显的全局最优 memory unit。**

另一方面，compression/consolidation 如果没有 field-preservation contract，会把 later query 才需要的细节永久擦掉。因此“写得更短”不能只按 token/storage 衡量。

## 最大未解问题

真正需要的是 streaming controller：根据 evidence density、conflict、query distribution、budget 与 field importance 动态决定 boundary 与 preservation，而不是每 turn 都做一次昂贵 LLM judgment，也不是全局固定 segmentation。

## 下一项 decisive evidence

构造同时包含 sparse/dense evidence、preference drift、conflict 与 delayed-use fields 的 long-running acting traces，独立变化：

`granularity × write budget × preservation rule × update frequency × forgetting`

同时测 storage/construction cost、retrieval quality 与 downstream action。

## 继续读

[FTA-Mem 中文笔记](../../papers/2026/2608.16303.zh.md) · [LeanMem](../../papers/2026/2608.03463.md) · [LycheeMemory V2](../../papers/2026/2608.09424.md)
