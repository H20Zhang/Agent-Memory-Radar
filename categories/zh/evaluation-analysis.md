# Evaluation & Analysis

[English](../evaluation-analysis.md) · [← Research Map](../README.md) · [Research Library](../../library/README.md)

> **Core question：** 什么证据足以说明一个 memory feature 真正有用，而且值得被部署？

## 当前判断

Endpoint accuracy / recall 太粗。**Demystifying Agent Skills** 已经说明 representation、retrieval、selection、actual use 与 downstream success 可以明显解耦；**D²ACCI** 把 paired evidence、protected slices 与 stage-localizable traces 带到 feature promotion。**Competence, Not Accuracy** 又把 reference-free gate 自身当作被审计对象：marginal accuracy 可能被题目难度抬高，真正相关的是同题判别能力。

这意味着 memory evaluation 至少要同时回答：

`哪个 stage 变了？→ gate 在实际候选上能否判别？→ gain 是否 paired/causal？→ 哪些 slice 回退？→ lifecycle cost 多大？→ evidence 是否足以 promotion？`

## Strongest signal

D²ACCI 中 BM25/RRF 这种直觉上合理的改动，因为 paired result 不显著而只保留为 feature flag；trace-rich audit 的 root-cause agreement 也明显高于 result-only artifact。Competence 的 within-question audit 则显示，Factual QA 的 AUC 会从 **0.855 降至 0.735**，而 research math 只有 **0.489**。

这比再多一个 architecture leaderboard 更有用：**null result 与 rejected intervention 也成为可复用的研究/工程知识。**

## Biggest unresolved question

Trace coverage 与 diagnostic metric 本身会奖励 instrumentation；如何证明这些 protocol 能预测真实 deployment utility，而不只是错误类型或更容易解释 benchmark failure？

## Next decisive evidence

在多个独立 memory stacks 上复用同一个 promotion protocol，并先用同题 probe 审计 gate，再追踪：

`benchmark decision → offline replay → online behavior / regression / cost`

如果 stage-level gate 对真实 deployment failure 没有预测力，就不能把“更可解释”误当成“更可靠”。
