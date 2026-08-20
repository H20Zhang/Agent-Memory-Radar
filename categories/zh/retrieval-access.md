# Retrieval & Access

[English](../retrieval-access.md) · [← Research Map](../README.md) · [Research Library](../../library/README.md)

> **Core question：** Memory 应该先定位哪段 historical state、再取哪些 evidence；哪些 relation 必须预建，哪些在线 search 就能恢复？

## 当前判断

**Raw-state control 是起点，不是终点。** ReFind 说明 competent raw archive + stateful search 可以吃掉很多过去归因给 semantic preprocessing 的收益；CABLE 则给 structure 一个更严格的存在理由：stored edge 应改变 host retriever 的 **reachability**，而不是复制 semantic neighborhood。

ArborMem 又把 read path 向前拆了一层：当历史中存在多个 interleaved/resumable trajectories 时，系统可能必须先回答“当前 turn 接续哪条 state”，再谈 evidence relevance。

因此更稳定的分解是：

`state localization → host/raw retrieval → relation/expansion/admission → evidence assembly`

## Strongest signal

- **ReFind：** strong raw interface 明显强于 weak one-shot control。
- **CABLE：** 在 fixed host/final evidence budget 下，complementary linking 仍有增益，说明 graph edge 可以通过改变 reachability 赚回一部分成本。
- **ArborMem：** 去掉 state localization 在较强模型上造成明显下降，说明“relevant to which state?” 是独立问题。

## Biggest unresolved question

哪些关系/状态必须 write-time materialize，哪些可以 query-time 重建？如果把 **construction inference + online search + latency + context** 全部匹配，CABLE/ArborMem 这样的预建结构还剩多少优势？

## Next decisive evidence

同一历史 substrate + 同一 model + 同一 total lifecycle budget，分别比较：

`raw stateful search → complementary graph expansion → state localization + raw search → state localization + structured expansion`

并在 long-horizon acting tasks 上测错误 routing/edge 是否产生不可逆 side effects。
