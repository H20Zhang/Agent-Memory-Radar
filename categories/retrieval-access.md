# Retrieval & Access

How an agent locates, queries, navigates, or reasons over stored memory.

## Current argument

The strongest current signal is moving from “retrieve the most similar memory” toward **access conditioned on preserved relations or controller state**.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-07 | [PMCoder](../papers/2026/2608.06811.md) | `episodic` `structured` `coding` | ★★★★☆ | Planner phase conditions memory retrieval, while memory statistics can trigger replanning; the +2.1pp interaction is the load-bearing result. |
| 2026-08-02 | [V-Mem](../papers/2026/2608.01543.md) | `episodic` `multimodal` `timeline` | ★★★★☆ | Modality routing plus same-round binding beats relying on one cross-modal similarity space; shared-round matching dominates its ablation. |

**Biggest unresolved question:** can controller-conditioned access survive open-ended domains where the useful state variable is not a hand-designed phase or obvious modality?

**Next decisive evidence:** hold evidence and base model fixed while varying only access operators/controller state across acting-agent workloads.
