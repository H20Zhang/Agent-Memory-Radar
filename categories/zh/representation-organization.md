# Representation & Organization

[← Research Map](../README.md) · [English](../representation-organization.md) · [首页](../../README.md)

> **核心问题：** 持久化的 archive 应该长什么样？下游 actor 最终消费的 state 是否必须和 archive 是同一个对象？

## 当前判断

**Archive fidelity 与 consumer usability 是两个目标。** 过去很多 memory system 默认把“更好的 persistent representation”直接等同于“更好的 actor context”；QUMem 与 QCR 让这个等式变得站不住。

QUMem 的阶段消融显示，query-time user-state reconstruction 的贡献大于 episode construction 或 typed decomposition；QCR 则在 trajectory reuse 中固定 selected trajectory，再通过 target-conditioned rebinding 避免 stale source binding。两者都指向同一个 boundary：**selected evidence 仍可能需要面向当前任务的 reconstruction。**

## Strongest signal

目前最强的信号不是某一种 schema 赢了，而是：

`archive evidence → selected evidence → consumer state`

这三者应该允许不同。Representation 的价值要看它是否保留足够 provenance/fidelity，让后续 reconstruction 能处理时间、冲突、binding drift，而不是只追求更容易检索。

## 最大未解问题

Transformation 越强，越容易压掉 source detail 或 hallucinate current state。真正困难的是在 preference drift、conflicting memories、revocation 与不确定性下，既能重构可用 state，又能追溯到原始 evidence。

## 下一项 decisive evidence

固定相同 retrieved evidence 与 synthesis budget，比较：

`raw evidence` vs `source-only summary` vs `target-conditioned support` vs `explicit reconstructed state`

并在 conflict/drift/authority setting 下同时测 downstream action quality 与 provenance fidelity。

## 继续读

[QUMem 中文笔记](../../papers/2026/2608.16168.zh.md) · [QCR](../../papers/2026/2608.12847.md) · [LeanMem](../../papers/2026/2608.03463.md)
