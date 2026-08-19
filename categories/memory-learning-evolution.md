# Memory Learning & Evolution

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How memory content, utility state, retrieval policy, structural relations, or feedback mechanisms adapt over time.

## Current argument

The category is splitting along two axes: **where adaptive state lives** and **what feedback surface is allowed to change it**. **SkillEvo** shows that richer multi-turn interaction can keep procedural-memory evolution informative after single-turn feedback saturates. **ERSkill** moves adaptive state into the read policy itself: executable retrieval skills and their router co-evolve while the underlying substrate can remain fixed. **HyperSkill** adds a structural claim: higher-order trajectory relations matter only when retrieval and maintenance actually consume them. AMD, HyMeS, MemoryCPT, and RoMeRL occupy complementary points where adaptation lives in teacher artifacts, executable strategy, end-to-end transformation, or bounded utility state.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-17 | [HyperSkill](../papers/2026/2608.16114.md) | `procedural` `structured` `graph` `general-agent` | 4/5 | Hypergraph structure is operationalized at retrieval and maintenance time; dual-path access is strongly ablated, though representation and access remain partially confounded. |
| 2026-08-13 | [SkillEvo](../papers/2026/2608.13120.md) | `procedural` `structured` `general-agent` | 4/5 | Multi-turn failure feedback contributes more to skill improvement than governance; governance mainly limits regression and bloat. |
| 2026-08-13 | [ERSkill](../papers/2026/2608.12720.md) | `procedural` `structured` `general-agent` | 4/5 | Retrieval policy becomes persistent evolvable state: executable access skills and the query router co-evolve under rollout evaluation. |
| 2026-08-10 | [HyMeS: Skills in Weights, Memory in Code](../papers/2026/2608.09410.md) | `working` `procedural` `structured` `embodied` | 4/5 | Separates motor competence in weights from inspectable memory strategy in code; symbolic task state directly steers action generation. |
| 2026-08-07 | [Agent Memory Distillation](../papers/2026/2608.07169.md) | `procedural` `structured` `general-agent` | 4/5 | Teacher experience transfers best when memory granularity and timing match the smaller student's decision structure. |
| 2026-08-05 | [MemoryCPT](../papers/2026/2608.04843.md) | `episodic` `semantic` `structured` | 4/5 | Construction and read-time compression are learned jointly under an explicit answer-quality / inference-cost objective. |
| 2026-08-03 | [RoMeRL](../papers/2026/2608.02508.md) | `episodic` `procedural` `structured` | 4/5 | Rich evidence need not imply one utility variable per stored trajectory; bounded semantic state can concentrate sparse feedback. |
| 2026-07-25 | [Lifelong AI partners for materials scientists](../papers/2026/2608.11224.md) | `semantic` `procedural` `structured` `research-agent` | 4/5 | Execution-grounded facts/skills transfer across tasks and models, but transfer is asymmetric: weak-source memory can be neutral or negative. |

**Biggest unresolved question:** what should be allowed to evolve—stored content, utility/control state, executable access policy, structural relations, or the feedback generator itself—and how can we tell that improvement survives a new consumer/domain rather than overfitting the evolution environment?

**Next decisive evidence:** freeze the underlying experience corpus and consumer, independently vary feedback richness, representation, retrieval policy, maintenance rule, and governance under matched rollout/judge cost, then transfer the resulting artifacts and router to a new domain without further tuning.

**Continue:** [Evaluation & Analysis →](evaluation-analysis.md)