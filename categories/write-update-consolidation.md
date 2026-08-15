# Write, Update & Consolidation

How memory is extracted, written, compressed, merged, corrected, forgotten, or consolidated.

## Current argument

The write side now has a clearer systems decomposition: **what fields must survive** and **how often expensive transformation should run** are separate questions. The Sleeping Agent shows a compression prompt can selectively erase temporal anchors; LycheeMemory V2 shows semantic segment boundaries can reduce consolidation frequency without paying the accuracy penalty of eager or fixed-window alternatives.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-13 | [LycheeMemory V2](../papers/2026/2608.12990.md) | `semantic` `structured` `timeline` | ★★★★☆ | Consolidation granularity is load-bearing: semantic segment batching gets 89.22 with 204.1K construction tokens; eager is 81.88/849.9K and fixed-window 82.40/174.7K. |
| 2026-08-12 | [The Sleeping Agent](../papers/2026/2608.11775.md) | `semantic` `text` `timeline` | ★★★☆☆ | Generic gist preserved entities/events but erased temporal anchors; explicit temporal protection raised preservation 3.05%→62.39%. |
| 2026-08-06 | [MERIT / Causal Episodic Memory](../papers/2026/2608.05906.md) | `episodic` `structured` | ★★★☆☆ | Cross-query repair memory helps, but polarity/type structure is not reliably better than untyped dynamic retrieval. |
| 2026-08-05 | [Scrub Jay Memory](../papers/2026/2608.04746.md) | `episodic` `structured` `timeline` | ★★★★☆ | Treat forgetting as per-memory future utility rather than one global recency heuristic. |

**Biggest unresolved question:** can a lifecycle controller jointly discover semantic boundaries, preservation contracts, and forgetting policy under real streaming updates without requiring one expensive LLM decision per turn?

**Next decisive evidence:** longitudinal acting-agent workloads that factor consolidation frequency × boundary policy × field preservation while reporting construction cost, retrieval cost, conflict repair, storage growth, and downstream action quality.
