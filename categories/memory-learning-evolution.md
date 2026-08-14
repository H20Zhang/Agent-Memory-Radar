# Memory Learning & Evolution

Learned memory policies, experience accumulation, procedural memory, and self-evolving agents.

## Current argument

The category is splitting by **where adaptive state lives**: learned memory-control variables, teacher-derived external memory, executable code-space memory strategy, or portable fact/skill artifacts. The important question is no longer simply “can memory improve?” but **which substrate matches the consumer's capabilities and can be revised safely**.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-10 | [HyMeS: Skills in Weights, Memory in Code](../papers/2026/2608.09410.md) | `working` `procedural` `structured` `embodied` | ★★★★☆ | Separates motor competence in VLA weights from inspectable memory strategy in code; symbolic task state directly steers action denoising. |
| 2026-08-07 | [Agent Memory Distillation](../papers/2026/2608.07169.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Teacher experience transfers best when workflow/subtask/function memories align with the smaller student's decision granularity and timing. |
| 2026-08-05 | [MemoryCPT](../papers/2026/2608.04843.md) | `episodic` `semantic` `structured` | ★★★★☆ | Jointly learn construction and read-time compression under an explicit answer-quality / inference-cost objective. |
| 2026-08-03 | [RoMeRL](../papers/2026/2608.02508.md) | `episodic` `procedural` `structured` | ★★★★☆ | Rich evidence need not imply one learned utility variable per stored trajectory; bounded semantic state concentrates sparse feedback. |
| 2026-07-25 | [Lifelong AI partners for materials scientists](../papers/2026/2608.11224.md) | `semantic` `procedural` `structured` `research-agent` | ★★★★☆ | Execution-grounded facts/skills transfer across tasks and models, but transfer is asymmetric: weak-source memory can be neutral or negative. |

**Biggest unresolved question:** when should adaptive memory live in model weights, explicit learned state, executable code, or external artifacts—and how should compatibility be tested when the consumer model/task changes?

**Next decisive evidence:** matched cross-domain/cross-model experiments that freeze the memory artifact and vary only the consumer, with provenance, marginal utility, and revision cost reported.
