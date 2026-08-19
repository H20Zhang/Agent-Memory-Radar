# Memory Learning & Evolution

[← Research Map](README.md) · [Home](../README.md)

Learned memory policies, experience accumulation, procedural memory, and self-evolving agents.

## Current argument

The category is splitting along two axes: **where adaptive state lives** and **what feedback/evaluation surface is allowed to change it**. **SkillEvo** shows that richer multi-turn interaction can keep procedural-memory evolution informative after single-turn feedback saturates. **ERSkill** moves the adaptive state to the read policy itself: executable retrieval skills and their router co-evolve while the underlying memory substrate can remain fixed. **HyperSkill** adds a complementary structural claim: trajectory-level relations can become useful only when the retrieval and maintenance policies actually consume them, via subtask/trajectory dual-path access and structure-aware pruning/merging. AMD, HyMeS, MemoryCPT, and RoMeRL remain complementary examples where adaptation lives in teacher artifacts, executable strategy, end-to-end learned transformation, or compact utility state.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-17 | [HyperSkill](../papers/2026/2608.16114.md) | `procedural` `structured` `graph` `general-agent` | ★★★★☆ | Hypergraph structure is operationalized at retrieval and maintenance time; dual-path access is strongly ablated, though representation and access remain partially confounded. |
| 2026-08-13 | [SkillEvo](../papers/2026/2608.13120.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Multi-turn failure feedback contributes much more to skill improvement than governance; governance mainly prevents regression and bloat. |
| 2026-08-13 | [ERSkill](../papers/2026/2608.12720.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Retrieval policy becomes persistent evolvable state: executable access skills and the query router co-evolve under rollout evaluation. |
| 2026-08-10 | [HyMeS: Skills in Weights, Memory in Code](../papers/2026/2608.09410.md) | `working` `procedural` `structured` `embodied` | ★★★★☆ | Separates motor competence in VLA weights from inspectable memory strategy in code; symbolic task state directly steers action denoising. |
| 2026-08-07 | [Agent Memory Distillation](../papers/2026/2608.07169.md) | `procedural` `structured` `general-agent` | ★★★★☆ | Teacher experience transfers best when workflow/subtask/function memories align with the smaller student's decision granularity and timing. |
| 2026-08-05 | [MemoryCPT](../papers/2026/2608.04843.md) | `episodic` `semantic` `structured` | ★★★★☆ | Jointly learn construction and read-time compression under an explicit answer-quality / inference-cost objective. |
| 2026-08-03 | [RoMeRL](../papers/2026/2608.02508.md) | `episodic` `procedural` `structured` | ★★★★☆ | Rich evidence need not imply one learned utility variable per stored trajectory; bounded semantic state concentrates sparse feedback. |
| 2026-07-25 | [Lifelong AI partners for materials scientists](../papers/2026/2608.11224.md) | `semantic` `procedural` `structured` `research-agent` | ★★★★☆ | Execution-grounded facts/skills transfer across tasks and models, but transfer is asymmetric: weak-source memory can be neutral or negative. |

**Biggest unresolved question:** what should be allowed to evolve—stored content, utility/control state, executable access policy, structural relations, or the feedback generator itself—and how can we tell that an apparent improvement survives a new consumer/domain rather than overfitting the evolution environment?

**Next decisive evidence:** freeze the underlying experience corpus and consumer, then independently vary feedback richness, representation (flat/binary graph/hypergraph), retrieval policy, maintenance rule, and governance under matched rollout/judge cost; afterward transfer the resulting artifacts and router to a new domain without further tuning.
