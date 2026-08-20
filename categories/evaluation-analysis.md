# Evaluation & Analysis

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How to tell whether persistent memory is actually useful, economical, authorized, safe, and causally responsible for downstream behavior.

## Current argument

Memory evaluation is moving from **endpoint score → promotion evidence**. **D²ACCI** makes paired baseline/candidate effects, protected slices, and stage-localizable traces part of the decision to accept or feature-flag a memory change. **Explicit State Elicitation Is Not Enough** supplies the complementary negative result: an interpretable intermediate state can change model behavior without significantly improving the target policy decision. **Demystifying Agent Skills** similarly separates representation, retrieval, invocation, and execution. **Total Recall**, **AuthMem-Bench**, **SkillJack**, and **Practice Makes Unsafe** extend the evaluation vector to lifecycle cost, authority, provenance, and descendant-state harm.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-18 | [D²ACCI](../papers/2026/2608.17756.md) | `structured` `general-agent` | 4/5 | Memory interventions are promoted only with paired evidence, protected-slice monitoring, and trace localizability; null BM25/RRF remains feature-flagged instead of becoming a default. |
| 2026-08-18 | [Explicit State Elicitation Is Not Enough](../papers/2026/2608.17247.md) | `semantic` `structured` `personalization` | 3/5 | Taxonomy instructions help, but forcing an explicit intermediate state does not significantly improve policy accuracy on the matched counterfactual set. |
| 2026-08-14 | [Demystifying Agent Skills](../papers/2026/2608.14036.md) | `procedural` `text` `coding` `general-agent` | 4/5 | Same source trajectories behave differently as Workflow Memory versus standardized Skills; exact retrieval is neither sufficient nor necessary for downstream success. |
| 2026-08-13 | [Practice Makes Unsafe](../papers/2026/2608.12851.md) | `procedural` `structured` `general-agent` | 4/5 | Unsafe write state, unsafe retrieval, and clean-session harm are separate lifecycle gates. |
| 2026-08-12 | [Total Recall at What Cost?](../papers/2026/2608.11879.md) | `semantic` `text` `general-agent` | 4/5 | Dedicated memory is not automatically cheaper than full history; break-even depends on the whole lifecycle. |
| 2026-08-12 | [Agent Skills Can Be Harmful](../papers/2026/2608.11888.md) | `procedural` `text` `general-agent` | 4/5 | Topical relevance does not imply procedural utility; extra procedure can create cost and success regressions. |
| 2026-08-12 | [Towards a Formal Definition of Agent Memory](../papers/2026/2608.11654.md) | `general-agent` | 3/5 | Useful representation-agnostic vocabulary for basis/span/capacity, but empirical validation is illustrative. |
| 2026-08-04 | [SkillJack](../papers/2026/2608.03509.md) | `procedural` `structured` `general-agent` | 4/5 | Experience→skill transformation creates a descendant-artifact provenance/revocation boundary. |
| 2026-08-03 | [AuthMem-Bench](../papers/2026/2608.01679.md) | `semantic` `structured` `general-agent` | 4/5 | Semantic fidelity can remain high while source authority is lost during consolidation. |

**Biggest unresolved question:** what deployment-facing evidence vector can decide whether a memory mechanism deserves promotion without collapsing causal stage, user utility, lifecycle cost, protected-slice regressions, authorization, and descendant-state risk into one score?

**Next decisive evidence:** long-running tool-use deployments with paired interventions, stage traces, explicit protected slices, full offline+online cost, authority/revocation checks, and downstream action outcomes—plus deliberately interpretable intermediate states that are accepted only when they causally improve behavior.

**Continue:** [What’s Changing →](../README.md#whats-changing)
