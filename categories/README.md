# Agent Memory Research Problems

**中文** | [English](README.en.md) · [首页](../README.md) · [Research Library](../library/README.md)

这里按 **memory lifecycle boundary** 组织问题，而不是按 method 名或 application domain 分类。

`archive → write → organize → state localization → access/admission → consumer state → update/evolution → governance/cost/provenance`

| Research problem | 核心问题 | 当前判断 |
|---|---|---|
| [Representation & Organization](zh/representation-organization.md) | 什么应该持久化？最终 consumer 应看到什么？ | **QUMem / QCR：** archival evidence 与 actor-facing state 不是同一个对象；retrieval 后的 reconstruction / rebinding 可能比再加一种 schema 更关键。 |
| [Retrieval & Access](zh/retrieval-access.md) | 什么时候 raw search 足够？structure / state localization 何时值得？ | **ReFind → CABLE → ArborMem：**先抬高 raw baseline，再要求 structure 改变 reachability；有些 workload 甚至需要在 retrieval 前先定位 active historical state。 |
| [Write, Update & Consolidation](zh/write-update-consolidation.md) | 一个 persistent unit 应多大、保留什么、何时更新/忘记？ | Granularity、preservation contract、transformation frequency 与 forgetting 是不同控制点，不能一起打包。 |
| [Memory Learning & Evolution](zh/memory-learning-evolution.md) | 到底什么在 evolve：artifact、writer/read policy、relations 还是 governance？ | **HyperSkill / WER / TRUSS：** relation、writer learning 与 runtime certification 已经分化成三个独立研究问题。 |
| [Evaluation & Analysis](zh/evaluation-analysis.md) | 什么证据足以说明 memory feature 值得部署？ | **D²ACCI + Demystifying：** endpoint score/retrieval label 不够；stage trace、paired control、protected slice、utility 与 lifecycle cost 需要同时进入判断。 |

## Cross-cutting correction

当前最重要的变化是 **stage attribution 越来越细**：

`localize historical state → retrieve/admit evidence → reconstruct consumer state`

ReFind 说明 semantic preprocessing 必须先击败 competent raw interface；CABLE 进一步要求 graph edge 改变 host retriever 的 reachability；ArborMem 把 state localization 提到 retrieval 之前；QUMem 则把 current-state reconstruction 放到 retrieval 之后。

因此 future comparison 不应只问“哪个 architecture 分高”，而要问：**哪个 stage 改了、其他 stage 是否 held fixed、额外 lifecycle cost 在哪里。**

## Researcher checklist

1. **Representation：** raw evidence 与 preservation fidelity 是否相同？
2. **State localization / access：** active state、query interface、candidate/evidence budget 与 iteration 是否相同？
3. **Consumer state：** retrieved evidence 是否固定，只改变 reconstruction/rebinding？
4. **Evolution：** feedback、writer/read policy、update budget 与 governance 是否匹配？
5. **Lifecycle：** construction + serving cost、provenance、authority、promotion/revocation 是否一起计费？

如果多个 stage 同时变化，实验首先支持的是**整个 package**，不是其中最显眼的 module。
