# Evaluation & Analysis

Benchmarks, surveys, empirical studies, and failure analyses of agent memory.

## Current argument

Memory quality is not recall. The current evidence requires at least **marginal behavioral effect, lifecycle cost, and state-lineage safety** to be measured separately. Practice Makes Unsafe sharpens the security side by resolving persistent adaptation into authoring → retrieval → fresh-session harm; Total Recall and Agent Skills independently show why endpoint quality or relevance can hide system-level regressions.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-13 | [Practice Makes Unsafe](../papers/2026/2608.12851.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Skill misevolution is a lifecycle failure: unsafe write state, unsafe retrieval, and clean-session harm are distinct gates that need attribution and revocation. |
| 2026-08-12 | [Total Recall at What Cost?](../papers/2026/2608.11879.md) | `semantic` `text` `general-agent` | ★★★★☆ | Dedicated memory is not automatically cheaper than full history; sustained break-even ranges from immediate to beyond 400 turns. |
| 2026-08-12 | [Agent Skills Can Be Harmful](../papers/2026/2608.11888.md) | `procedural` `text` `general-agent` | ★★★★☆ | Matched executions show topical relevance does not imply procedural utility; induced extra procedure dominates many cost regressions. |
| 2026-08-12 | [Towards a Formal Definition of Agent Memory](../papers/2026/2608.11654.md) | `general-agent` | ★★★☆☆ | Useful representation-agnostic vocabulary for basis/span/capacity, but empirical validation is illustrative. |
| 2026-08-04 | [SkillJack](../papers/2026/2608.03509.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Experience→skill transformation creates a descendant-artifact provenance/revocation boundary. |
| 2026-08-03 | [AuthMem-Bench](../papers/2026/2608.01679.md) | `semantic` `structured` `general-agent` | ★★★★☆ | Semantic fidelity can remain high while source authority is lost during consolidation. |

**Biggest unresolved question:** what deployment-facing evaluation vector can predict whether persistent memory is actually worth using without collapsing task utility, total cost, unsafe writes, unsafe reads, and descendant effects into one score?

**Next decisive evidence:** matched long-running tool-use deployments with explicit no-memory/alternative-memory counterfactuals and per-stage attribution for write, retrieve, execute, cost, authorization, and revocation outcomes.
