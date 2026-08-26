# Evaluation & Analysis

[English](../evaluation-analysis.md) · [← Research Map](../README.md) · [Research Library](../../library/README.md)

> **Core question：** 什么证据足以说明一个 memory feature 真正有用，而且值得被部署？

## 当前判断

**InjecMEM** 把一次普通 write、later retrieval 与 consumer steering 串成端到端安全测试。MemoryOS joint success 为 35.6%，且 strongest setting white-box、跨 held-out family transfer 失败；它证明攻击面存在，不代表部署中的普遍成功率。

Endpoint accuracy / recall 太粗。**Demystifying Agent Skills** 已经说明 representation、retrieval、selection、actual use 与 downstream success 可以明显解耦；**D²ACCI** 把 paired evidence、protected slices 与 stage-localizable traces 带到 feature promotion。**Competence, Not Accuracy** 又把 reference-free gate 自身当作被审计对象：marginal accuracy 可能被题目难度抬高，真正相关的是同题判别能力。**Remember, Verify, or Ask?** 把 authority check 移到写入之前；**MemTrapBench** 则在 retrieval 之后直接测 memory use 是否伤害当前 consumer。两者都是 synthetic early signal：前者不执行 commitment action，后者专门构造无需历史即可回答、但 prior history 含 trap 的压力测试。

**Utility Under Attack** 把 provenance ranking 变成双边 utility test：既测 poison suppression，也测 untrusted channel 中的正确证据是否被误删。**DreamBench-SWE** 则要求先前 session 的状态改变后续 executable patch；它支持 persistent state，却没有让 typed sleep 在 preregistered test 中胜过 verbatim archive。

这意味着 memory evaluation 至少要同时回答：

`哪个 stage 变了？→ commitment 是否有 authority？→ gate 在实际候选上能否判别？→ memory use 是否保留有用信息并拒绝 trap？→ 哪些 slice 回退？→ lifecycle cost 多大？→ evidence 是否足以 promotion？`

## Strongest signal

D²ACCI 中 BM25/RRF 这种直觉上合理的改动，因为 paired result 不显著而只保留为 feature flag；trace-rich audit 的 root-cause agreement 也明显高于 result-only artifact。Competence 的 within-question audit 则显示，Factual QA 的 AUC 会从 **0.855 降至 0.735**，而 research math 只有 **0.489**。

这比再多一个 architecture leaderboard 更有用：**null result 与 rejected intervention 也成为可复用的研究/工程知识。**

## Biggest unresolved question

Trace coverage 与 diagnostic metric 本身会奖励 instrumentation；如何证明这些 protocol 能预测真实 deployment utility，而不只是 rubric following、trap-rich benchmark failure 或更容易解释的 trace？

## Next decisive evidence

在多个独立 memory stacks 上复用同一个 promotion protocol，并先用同题 probe 审计 gate；真实执行 write/check/clarify，同时用 memory-required、neutral 与 trap case 测试 admission，再追踪：

`benchmark decision → offline replay → online behavior / regression / cost`

如果 stage-level gate 对真实 deployment failure 没有预测力，就不能把“更可解释”误当成“更可靠”。
