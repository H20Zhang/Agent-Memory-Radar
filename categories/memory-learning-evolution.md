# Memory Learning & Evolution

Learned memory policies, experience accumulation, procedural memory, and self-evolving agents.

## Current argument

The category now spans three distinct control problems: **what memory transformation to optimize, how large the learned state should be, and whether memory can transfer capability across models without parameter updates**.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-07 | [Agent Memory Distillation](../papers/2026/2608.07169.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Teacher experience transfers best when workflow/subtask/function memories are aligned to a small student's decision granularity and retrieval timing. |
| 2026-08-05 | [MemoryCPT](../papers/2026/2608.04843.md) | `episodic` `semantic` `structured` | ★★★★☆ | Jointly learn memory construction and query-time compression under an explicit answer-quality / inference-cost objective. |
| 2026-08-03 | [RoMeRL](../papers/2026/2608.02508.md) | `episodic` `procedural` `structured` | ★★★★☆ | A growing memory pool need not imply a growing utility state; bounded semantic coordinates concentrate sparse feedback. |

**Biggest unresolved question:** which memory state deserves learning/transfer feedback when the task and consumer capability change over time?

**Next decisive evidence:** freeze learned/teacher-derived memory policies and test cross-domain transfer with matched evidence budgets and explicit marginal-memory attribution.
