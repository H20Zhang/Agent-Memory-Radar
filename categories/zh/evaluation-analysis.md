# Evaluation & Analysis

[← Research Map](../README.md) · [English](../evaluation-analysis.md) · [首页](../../README.md)

> **核心问题：** 什么样的 memory 才真正值得部署？Retrieval score、task success、lifecycle cost、authority 与 safety 应如何拆开？

## 当前判断

**“Good memory = retrieve the right item”已经不够。** Demystifying Agent Skills 显示 exact retrieval label 与 actual use / downstream utility 可以明显脱钩；authority/provenance 与 descendant-state work 又说明，语义正确的 memory 也可能因为权限、来源或后代状态而不应该被使用。

因此 deployment-facing evaluation 至少要看：

`representation → retrieval → selection/invocation → actual use → downstream utility → lifecycle cost → provenance/authority → descendant effects`

## Strongest signal

同一 source experience 换成不同 procedural representation，最终 utility 会变化；skill pool 增长后 retrieval/use precision 快速下降，但 task success 不一定同比下降。这说明“检索到 ground-truth item”并不能充分描述 memory 对 agent 的实际作用。

同样，construction/indexing/write cost 与 serving/retrieval cost 如果不放进同一 horizon，短 benchmark 很容易把昂贵 memory 看成“免费”。

## 最大未解问题

能否建立一个不把所有维度压成单一 opaque score 的 evaluation vector？特别是 long-running acting agent 里，memory 可能带来延迟效应、不可逆 action、权限变化、revocation 与 unsafe descendant state。

## 下一项 decisive evidence

长期 acting-agent trace，使用 matched：

`no memory / raw history / alternative representation / governed memory`

并做 stage-level attribution：retrieval、invocation、actual use、utility、cost、provenance、authority、revocation 与 downstream action。

## 继续读

[Demystifying Agent Skills 中文笔记](../../papers/2026/2608.14036.zh.md) · [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar)
