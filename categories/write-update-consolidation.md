# Write, Update & Consolidation

[← Research Map](README.md) · [Home](../README.md)

How memory is extracted, written, compressed, merged, corrected, forgotten, or consolidated.

## Current argument

The write side now has a clearer systems decomposition: **what fields must survive, what event boundary defines one persistent unit, and how often expensive transformation should run** are separate questions. The Sleeping Agent shows a compression prompt can selectively erase temporal anchors; LycheeMemory V2 shows semantic segment boundaries can reduce consolidation frequency without paying the accuracy penalty of eager or fixed-window alternatives; **FTA-Mem** adds a density-dependent granularity result, where situation-level units dominate coarse session memory but trade a small amount of dense-benchmark quality for much lower construction cost than turn-pair memory.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-17 | [FTA-Mem](../papers/2026/2608.16303.md) | `episodic` `structured` `timeline` `personalization` | ★★★☆☆ | Situation-level Fact-Time-Affect units beat session memory on sparse dialogue and use fewer construction tokens than turn-pair memory, but turn-pair is slightly stronger on denser LoCoMo. |
| 2026-08-13 | [LycheeMemory V2](../papers/2026/2608.12990.md) | `semantic` `structured` `timeline` | ★★★★☆ | Consolidation granularity is load-bearing: semantic segment batching gets 89.22 with 204.1K construction tokens; eager is 81.88/849.9K and fixed-window 82.40/174.7K. |
| 2026-08-12 | [The Sleeping Agent](../papers/2026/2608.11775.md) | `semantic` `text` `timeline` | ★★★☆☆ | Generic gist preserved entities/events but erased temporal anchors; explicit temporal protection raised preservation 3.05%→62.39%. |
| 2026-08-06 | [MERIT / Causal Episodic Memory](../papers/2026/2608.05906.md) | `episodic` `structured` | ★★★☆☆ | Cross-query repair memory helps, but polarity/type structure is not reliably better than untyped dynamic retrieval. |
| 2026-08-05 | [Scrub Jay Memory](../papers/2026/2608.04746.md) | `episodic` `structured` `timeline` | ★★★★☆ | Treat forgetting as per-memory future utility rather than one global recency heuristic. |

**Biggest unresolved question:** can a lifecycle controller jointly discover event boundaries, preservation contracts, and forgetting policy under real streaming updates without requiring one expensive LLM decision per turn—and can it adapt granularity to evidence density rather than fixing one global unit size?

**Next decisive evidence:** longitudinal acting-agent workloads that factor consolidation frequency × boundary/granularity policy × field preservation while reporting construction cost, retrieval cost, conflict repair, storage growth, and downstream action quality across both sparse and dense event streams.
