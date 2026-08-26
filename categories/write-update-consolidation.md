# Write, Update & Consolidation

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How memory is extracted, written, compressed, merged, corrected, forgotten, or consolidated.

## Current argument

The write side is becoming a systems problem with several independent controls: **what fields must survive, what event boundary defines one persistent unit, how often expensive transformation should run, and when old state should be forgotten**. **StateMem** adds a distinct update contract: a superseded value may remain for audit while becoming inactive, and dependent state may require recomputation rather than deletion. Its strongest results credit supersession/recompute guidance, not dependency propagation, and its 165–600 ingest calls per scenario make lifecycle cost central. The Sleeping Agent shows that generic compression can selectively erase temporal anchors; LycheeMemory V2 shows that semantic boundaries can reduce consolidation frequency without the accuracy loss of eager or fixed-window alternatives; **FTA-Mem** adds a density-dependent granularity result, where situation-level units dominate coarse sessions but trade a little dense-benchmark quality for substantially lower construction cost than turn-pair memory. **Scrub Jay** makes forgetting itself a learned per-memory utility decision rather than a global recency rule.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-24 | [The Compaction Cliff](../papers/2026/2608.22752.md) | `semantic` `text` `structured` `general-agent` | 4/5 | Typed retention preserves exact constraints across repeated compression, but the closest source-fidelity control nearly ties at 50% and is absent from behavioral tests. |
| 2026-08-22 | [MemGuard](../papers/2026/2608.21867.md) | `procedural` `structured` `general-agent` | 4/5 | Persistent verifier descriptors govern later retrieval and maintenance; the verifier-only contrast favors the package but lacks a significance test. |
| 2026-08-20 | [StateMemBench / StateMem](../papers/2026/2608.19652.md) | `semantic` `structured` `timeline` `general-agent` | 4/5 | Explicit supersession and recomputation improve current-state answers, but dependency propagation is unstable and the persistent store's ingest cost is not lifecycle-matched. |
| 2026-08-17 | [FTA-Mem](../papers/2026/2608.16303.md) | `episodic` `structured` `timeline` `personalization` | 3/5 | Situation-level units beat session memory on sparse dialogue and cost less to construct than turn-pair memory, while turn-pair stays slightly stronger on denser LoCoMo. |
| 2026-08-13 | [LycheeMemory V2](../papers/2026/2608.12990.md) | `semantic` `structured` `timeline` | 4/5 | Consolidation granularity is load-bearing: semantic segment batching improves the quality-cost frontier over eager and fixed-window construction. |
| 2026-08-12 | [The Sleeping Agent](../papers/2026/2608.11775.md) | `semantic` `text` `timeline` | 3/5 | Generic gist preserved entities/events but erased temporal anchors; preservation contracts need to be explicit. |
| 2026-08-06 | [MERIT / Causal Episodic Memory](../papers/2026/2608.05906.md) | `episodic` `structured` | 3/5 | Cross-query repair memory helps, but extra polarity/type structure is not reliably better than a simpler dynamic policy. |
| 2026-08-05 | [Scrub Jay Memory](../papers/2026/2608.04746.md) | `episodic` `structured` `timeline` | 4/5 | Forgetting is modeled as per-memory future utility rather than one global decay heuristic. |

**Biggest unresolved question:** can one streaming lifecycle controller jointly discover event boundaries, preservation contracts, supersession, dependency repair, consolidation frequency, and forgetting policy without requiring an expensive model decision on every turn?

**Next decisive evidence:** longitudinal acting-agent workloads that factor consolidation frequency × memory-unit granularity × preservation contract × supersession/dependency rule × forgetting rule while reporting construction cost, retrieval cost, storage growth, conflict repair, stale-state errors, and downstream action quality.

**Continue:** [Memory Learning & Evolution →](memory-learning-evolution.md)
