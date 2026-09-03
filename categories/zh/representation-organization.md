# Representation & Organization

[← Research Map](../README.md) · [English](../representation-organization.md) · [首页](../../README.md)

> **核心问题：** persistent archive、当前 episode/state 与最终 actor context，是否应该是同一个对象？

## 当前判断

**Agent Zero Memory** 又补了一条“来源与准入”边界：同一段历史同时保留为时间线、图和文档三种视图，而 citation lock 只允许最终回答使用本轮真正打开过的证据。现有 matched ablation 只证明混合检索优于单一检索通道，还没有隔离三存储组织本身；要给架构记功，仍需固定 reader / evidence / budget 后做 store/provenance 干预，并补齐构建与维护成本。

Representation 现在至少要拆成 **archive organization → state localization → consumer reconstruction** 三层。**SCALE-QA / TSIM** 说明 flat interleaved turn stream 先要恢复 coherent episode，普通 similarity search 才有机会拿到正确状态；**QCR** 与 **QUMem** 又说明 selected evidence 本身仍可能不是 actor 最适合消费的形式，需要 target-conditioned rebinding 或 current-user-state reconstruction。

**VoiceMem** 再增加一条 streaming multimodal boundary：factual/entity state 与 affect/persona state 可以走不同 representation / access path，而 upper organization/routing layer 又能跨 Mem0、LangMem、Zep backend 复用。这里真正重要的不是“dual brain” 命名，而是 **不同 state contract 是否在同样 write/query cost 下改变下游行为。**

## Strongest signal

目前更合理的抽象是：

`source stream → archival units → episode/state localization → selected evidence → actor-facing state`

这几个对象应该允许不同。TSIM 把 episode reconstruction 放到 retrieval 前；QUMem/QCR 把 reconstruction 放到 retrieval 后；VoiceMem 则提醒 factual 与 affect/persona state 甚至可能需要不同的在线路径。

## 最大未解问题

Transformation 越多，越容易引入 hallucination、丢 provenance，或者把 cost 从 query path 偷移到异步 write path。当前证据还没有把 segmentation、summary、routing、reconstruction、backend 与完整 lifecycle cost 真正配平。

## 下一项 decisive evidence

固定相同 source stream、consumer 与总预算，独立比较：

`flat turns vs episode localization × raw evidence vs reconstructed state × unified vs factual/affective split`

同时测 conflict/drift 下的 downstream action、provenance fidelity、write backlog、query latency 与完整 maintenance cost。

## 继续读

[Agent Zero Memory](../../papers/2026/2608.29606.zh.md) · [TSIM 中文笔记](../../papers/2026/2608.25655.zh.md) · [VoiceMem 中文笔记](../../papers/2026/2608.26005.zh.md) · [QUMem 中文笔记](../../papers/2026/2608.16168.zh.md) · [QCR](../../papers/2026/2608.12847.md)