# Agent Memory Research Problems

**中文** | [English](README.en.md) · [返回首页](../README.md) · [Research Library](../library/README.md)

这里按**哪一个 memory lifecycle boundary 被改变**组织研究问题，而不是按应用场景堆 paper。

| Research problem | 核心问题 | 当前判断 |
|---|---|---|
| [Representation & Organization](zh/representation-organization.md) | 什么应该持久化？当前 consumer 最终应该看到什么？ | **QUMem + QCR：** archival evidence 与 actor-facing state 是不同对象；reconstruction / rebinding 可能比再加一层 storage schema 更关键。 |
| [Retrieval & Access](zh/retrieval-access.md) | Memory 什么时候保留 raw、什么时候预建 structure、什么时候应该 withheld？ | **ReFind + RippleMem：** 先建立 competent raw-state control；structure 只有在提供额外 operator / admission value 时才真正赚回成本。 |
| [Write, Update & Consolidation](zh/write-update-consolidation.md) | 一个 persistent unit 应多大？什么该保留、修改或忘掉？ | **FTA-Mem + LeanMem / LycheeMemory：** granularity、preservation contract、update frequency、forgetting 是不同控制点。 |
| [Memory Learning & Evolution](zh/memory-learning-evolution.md) | 到底什么 adaptive state 应 evolve？依据什么 feedback？ | **SkillEvo + ERSkill + HyperSkill：** feedback、read policy、relation structure、maintenance 不能打包归因。 |
| [Evaluation & Analysis](zh/evaluation-analysis.md) | 什么样的 memory 才值得部署？ | **Demystifying Agent Skills + authority/safety/cost work：** retrieval quality 远远不够，还要看 actual use、utility、lifecycle cost、provenance 与 descendant effects。 |

## Cross-cutting model

`archive / representation → access / admission → consumer state → update / evolution → governance / cost / provenance`

目前最强的共同修正是 **stage attribution**：ReFind 抬高 raw access baseline；RippleMem 说明 structure 可以通过 stronger read operator 重新证明自己；QUMem/QCR 把下一道 boundary 推到 retrieved evidence 与 consumer state 之间；FTA-Mem 则说明 write-side boundary 本身是可测的 quality–cost parameter。

## 比较两个 memory system 时先问什么

1. **Representation：** raw evidence 与 preservation fidelity 是否一致？
2. **Access：** query interface、candidate/evidence budget、iteration 是否匹配？
3. **Consumer state：** retrieved evidence 是否相同，只改变 reconstruction/rebinding？
4. **Update：** feedback、write budget、maintenance frequency 是否一致？
5. **Lifecycle：** construction + serving cost、provenance、authority、revocation 是否一起算？

如果多个 stage 同时变化，实验首先支持的是**整套 package**，而不是其中某一个 mechanism。
