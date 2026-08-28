# Evaluation & Analysis

[English](../evaluation-analysis.md) · [← Research Map](../README.md) · [Research Library](../../library/README.md)

> **Core question：** 什么证据足以说明一个 memory feature 真正有用，而且值得被部署？

## 当前判断

**When Stale Constraints Go Unchecked** 把一个长期容易混在一起的问题拆干净了：**有 provenance ≠ consumer 会在有限预算下核验 provenance。** 在固定 `k=2` verification budget 下，只把一个已有 slot 重分配到 critical path，就能让 current-record-consistent decision 提高 61.3–74.0pp；memory 本来仍有效时只改变 0–2pp。这个结果定位的是 verification allocation failure；forced-critical 依赖实验者知道关键路径，还不是可部署 scheduler。

**InjecMEM** 把一次普通 write、later retrieval 与 consumer steering 串成端到端安全测试。**D²ACCI** 把 paired evidence、protected slices 与 stage-localizable traces 带到 feature promotion；**Competence, Not Accuracy** 又要求 gate 在同题候选上真的有判别力。**Remember, Verify, or Ask?** 把 authority check 移到写入之前；**MemTrapBench** 在 retrieval 后测 memory use 是否伤害当前 consumer。它们一起说明 endpoint score / recall 远远不够。

**Utility Under Attack** 进一步把 provenance ranking 变成双边 utility test：既测 poison suppression，也测 untrusted channel 中的正确证据是否被误删。**DreamBench-SWE** 则要求先前 session 的状态改变后续 executable patch；它支持 persistent state，却没有让 typed sleep 在 preregistered test 中胜过 verbatim archive。

这意味着 memory evaluation 至少要同时回答：

`哪个 stage 变了？→ commitment 是否有 authority？→ freshness 是否需要核验？→ gate 在实际候选上能否判别？→ memory use 是否保留有用信息并拒绝 trap？→ 哪些 slice 回退？→ lifecycle cost 多大？→ evidence 是否足以 promotion？`

## Strongest signal

目前最干净的新证据来自 stale-memory verification：同预算、同 memory、同 world，只改变 verification slot 去哪里，行为就发生 61.3–74.0pp 的变化；valid-world 基本不动。这比再加一个 architecture leaderboard 更能定位 causal stage。

D²ACCI 中 BM25/RRF 这种直觉上合理的改动，因为 paired result 不显著而只保留为 feature flag；Competence 的 within-question audit 则显示，Factual QA 的 AUC 会从 **0.855 降至 0.735**，而 research math 只有 **0.489**。**null result、rejected intervention 与 under-verified state 都应该成为可复用的工程知识。**

## Biggest unresolved question

forced-critical 用的是 oracle path。真正需要证明的是：一个可部署 scheduler 能否在不知道答案的情况下，以 `cost-of-being-wrong × freshness risk × evidence authority` 分配有限 verification budget，并在真实 stale prevalence 下取得净收益。

## Next decisive evidence

在多个独立 memory stacks 上复用同一个 promotion protocol；真实执行 write/check/clarify，并混合 fresh、stale、memory-required、neutral、trap case。在固定 verification/context budget 下比较 relevance-only、learned freshness scheduler 与 oracle upper bound，再追踪：

`benchmark decision → offline replay → online behavior / regression / lifecycle cost`

如果 stage-level gate 与 verification policy 对真实 deployment failure 没有预测力，就不能把“更可解释”误当成“更可靠”。
