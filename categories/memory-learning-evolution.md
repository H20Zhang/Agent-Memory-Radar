# Memory Learning & Evolution

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How memory content, writer policy, retrieval policy, structural relations, or feedback mechanisms adapt over time.

## Current argument

“Self-improving memory” hides several adaptive states. **SkillEvo** improves the feedback surface; **WER** trains the skill-writer policy; **TRUSS** certifies candidate artifacts; **ERSkill** evolves the read policy; **HyperSkill** operationalizes relations. **Harness Continual Learning** then widens the boundary to jointly version memory, interface, capability map, and router under a commit gate. The question is **what state changes, from which evidence, and under what promotion/governance rule**.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-19 | [Harness Continual Learning](../papers/2026/2608.19013.md) | `episodic` `procedural` `structured` `general-agent` | 4/5 | Jointly versions four harness components and gates commits on current utility, retention, and validity; package gains cannot be assigned to memory alone. |
| 2026-08-18 | [WER](../papers/2026/2608.17587.md) | `procedural` `text` `general-agent` | 4/5 | Same optimizer backbone/workflow gains 9.35/10.29 points after training from execution feedback; deeper refinement can regress. |
| 2026-08-18 | [TRUSS](../papers/2026/2608.17588.md) | `procedural` `structured` `general-agent` | 4/5 | Candidate skills are statically checked, shadow-executed, traced, refined, and re-certified before promotion; runtime safety is executor-dependent. |
| 2026-08-17 | [HyperSkill](../papers/2026/2608.16114.md) | `procedural` `structured` `graph` `general-agent` | 4/5 | Hypergraph structure is consumed by retrieval and maintenance, though representation and access remain partially confounded. |
| 2026-08-13 | [SkillEvo](../papers/2026/2608.13120.md) | `procedural` `structured` `general-agent` | 4/5 | Multi-turn failure feedback drives more improvement than governance; governance mainly limits regression and bloat. |
| 2026-08-13 | [ERSkill](../papers/2026/2608.12720.md) | `procedural` `structured` `general-agent` | 4/5 | Retrieval policy becomes persistent evolvable state: executable access skills and the query router co-evolve. |
| 2026-08-10 | [HyMeS](../papers/2026/2608.09410.md) | `working` `procedural` `structured` `embodied` | 4/5 | Separates motor competence in weights from inspectable memory strategy in code. |
| 2026-08-07 | [Agent Memory Distillation](../papers/2026/2608.07169.md) | `procedural` `structured` `general-agent` | 4/5 | Teacher experience transfers best when memory granularity/timing match the student's decision structure. |
| 2026-08-05 | [MemoryCPT](../papers/2026/2608.04843.md) | `episodic` `semantic` `structured` | 4/5 | Construction and read-time compression are learned jointly under quality/cost pressure. |
| 2026-08-03 | [RoMeRL](../papers/2026/2608.02508.md) | `episodic` `procedural` `structured` | 4/5 | Bounded semantic utility state can concentrate sparse feedback over richer experience stores. |

**Biggest unresolved question:** which adaptive-state location—artifact, writer, read policy, structure, or whole harness—transfers across new consumers/domains strongly enough to justify acquisition, rollout, verification, retention testing, and maintenance cost?

**Next decisive evidence:** freeze source experiences, target tasks, and executor; independently vary feedback richness, writer learning, artifact refinement, read-policy evolution, and commit governance under matched compute, then transfer the artifact/policy to a new domain and longer state stream without further tuning.

**Continue:** [Evaluation & Analysis →](evaluation-analysis.md)
