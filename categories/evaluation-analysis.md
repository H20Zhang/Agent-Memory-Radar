# Evaluation & Analysis

Benchmarks, surveys, empirical studies, and failure analyses of agent memory.

## Current argument

Memory quality is no longer well described by recall alone. The strongest new evidence adds **marginal cost, procedural side effects, authority/provenance, and read-boundary correctness** as independent evaluation axes.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-12 | [Total Recall at What Cost?](../papers/2026/2608.11879.md) | `semantic` `text` `general-agent` | ★★★★☆ | Dedicated memory is not automatically cheaper than full history; sustained break-even ranges from immediate to beyond 400 turns depending on system/backbone/workload. |
| 2026-08-12 | [Agent Skills Can Be Harmful](../papers/2026/2608.11888.md) | `procedural` `text` `general-agent` | ★★★★☆ | Matched executions show topical relevance does not imply procedural utility; most cost regressions come from induced extra procedure, not prompt length alone. |
| 2026-08-12 | [Towards a Formal Definition of Agent Memory](../papers/2026/2608.11654.md) | `general-agent` | ★★★☆☆ | Useful representation-agnostic vocabulary for memory basis/span/capacity, but empirical validation is still illustrative. |
| 2026-08-04 | [SkillJack](../papers/2026/2608.03509.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Experience→skill transformation creates a descendant-artifact provenance/revocation boundary. |
| 2026-08-04 | [MAFIA](../papers/2026/2608.03844.md) | `semantic` `text` `general-agent` | ★★★★☆ | Persistent memory turns one interaction into delayed state-integrity risk. |
| 2026-08-03 | [AuthMem-Bench](../papers/2026/2608.01679.md) | `semantic` `structured` `general-agent` | ★★★★☆ | Semantic fidelity can remain high while source authority is lost during consolidation. |

**Biggest unresolved question:** what is the smallest evaluation vector that predicts real deployment value without collapsing cost, action correctness, read authorization, provenance, and long-horizon utility into one misleading score?

**Next decisive evidence:** matched long-running tool-use deployments that report utility, lifecycle cost, read/action boundary violations, provenance retention, and counterfactual no-memory / alternative-memory controls.
