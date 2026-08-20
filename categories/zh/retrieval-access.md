# Retrieval & Access

[← Research Map](../README.md) · [English](../retrieval-access.md) · [首页](../../README.md)

> **核心问题：** Memory 什么时候应保持 raw、什么时候预建 structure、什么时候即使 relevant 也不该进入当前 context？

## 当前判断

**Structure 必须先击败 competent raw-state access。** ReFind 表明，raw chat + session/time/local-context controls + result-conditioned iteration 可以回收很多过去被归因给 semantic preprocessing 的收益。

但这不等于 structure 没价值。RippleMem 给出相反边界：预建 association 如果让 first-hop memory 变成 missing-evidence search 的 anchor，并在 matched recollection control 下仍有剩余 gain，那么 structure 提供的是一个额外 read operator，而不只是“更像 query 的 representation”。

## Strongest signal

现在更稳定的 decomposition 是：

`representation × access interface × iteration × admission × evidence budget`

而不是 `flat memory vs graph memory`。

同样 relevant 的 memory 也未必值得注入。Admission/abstention 应单独看 marginal utility，而不能把 retrieval relevance 当作 downstream usefulness。

## 最大未解问题

哪些 relation 必须离线预建，哪些可以在线通过 search/reasoning 重构？不同 workload 下，预计算 structure 的 build/update cost 与 query-time iterative search 的 token/latency cost 如何换算？

## 下一项 decisive evidence

同一 raw history、同 model、同 online latency/token/evidence budget 下比较：

`raw iterative search → associative expansion → structure-aware routing → admission-aware retrieval`

同时把 offline construction/update cost 纳入 lifecycle accounting。

## 继续读

[ReFind 中文笔记](../../papers/2026/2608.12888.zh.md) · [RippleMem 中文笔记](../../papers/2026/2608.13334.zh.md) · [Skill2Query 中文笔记](../../papers/2026/2608.16071.zh.md)
