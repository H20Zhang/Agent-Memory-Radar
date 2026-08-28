# Retrieval & Access

[English](../retrieval-access.md) · [← Research Map](../README.md) · [Research Library](../../library/README.md)

> **Core question：** Memory 应该先定位哪段 historical state、再取哪些 evidence；哪些 relation 必须预建，哪些在线 search 就能恢复？

## 当前判断

**CaSKG 把 graph access 本身拆成“有结构”和“可信结构”。** 在同一 frozen Skill1000 与同一 downstream loop 下，calibrated graph 击败 GoS；错误 edge 会放大错误 relevance，因此 relation quality 是一等 access-policy 变量。

**EARM** 把历史 query–memory relevance score 变成 persistent access-policy state，并显著减少 reranker call；但其 store、ID 与问题顺序固定，completion 的净增量较小，维护与删除成本缺失，因此保持 3/5 低置信度信号。

**Raw-state control 是起点，不是终点。** ReFind 说明 competent raw archive + stateful search 可以吃掉很多过去归因给 semantic preprocessing 的收益；CABLE 则要求 stored edge 改变 host retriever 的 **reachability**。MemFuse 进一步提醒：多源 graph/fusion 与 query-time evidence completion 必须分开归因，当前最大消融属于后者。

ArborMem 又把 read path 向前拆了一层：当历史中存在多个 interleaved/resumable trajectories 时，系统可能必须先回答“当前 turn 接续哪条 state”，再谈 evidence relevance。

SkillGate 把 procedural memory 的访问单独拉出来：skill library 已经存在，也不代表 outcome-only training 已充分训练早期 read action；但现有方法同时改变 Oracle utility、read-call masking 与 selector-mass normalization，尚未隔离 credit placement。

**Weighted Memory Tree** 在这条链之前增加 within-episode active retention，但没有测 cross-session persistence；**Optimal Skill Selection** 则说明 skill selection 需要按整个 set 的 complementarity、redundancy 与 token cost 计值，而非逐项 top-k。两者仍分别受 package attribution 与 unmatched supervision 限制。

因此更稳定的分解是：

`state localization → host/raw retrieval / skill selection → relation/expansion/admission → evidence assembly`

## Strongest signal

- **ReFind：** strong raw interface 明显强于 weak one-shot control。
- **CABLE：** 在 fixed host/final evidence budget 下，complementary linking 仍有增益，说明 graph edge 可以通过改变 reachability 赚回一部分成本。
- **MemFuse：** 多源持久组织保留 atomic provenance，但总体 gain 主要由 iterative constrained retrieval 驱动。
- **SkillGate：** 带 Oracle 监督的局部 selector package 改变 skill exposure，但 single-seed 结果尚未隔离 credit location。
- **ArborMem：** 去掉 state localization 在较强模型上造成明显下降，说明“relevant to which state?” 是独立问题。

## Biggest unresolved question

哪些关系/状态必须 write-time materialize，哪些可以 query-time 重建？稀疏 read action 又应如何得到局部 credit？如果把 **construction/training inference + online search + latency + context** 全部匹配，预建结构和 learned selector 还剩多少优势？

## Next decisive evidence

同一历史 substrate + 同一 model + 同一 total lifecycle budget，分别比较：

`raw stateful search → fused/complementary expansion → state localization + raw search → supervised selector package → structured expansion/admission`

并在 long-horizon acting tasks 上测错误 routing/edge 是否产生不可逆 side effects。
