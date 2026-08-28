# Memory Learning & Evolution

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How memory content, writer policy, retrieval policy, structural relations, or feedback mechanisms adapt over time.

## Current argument

“Self-improving memory” hides several adaptive states. **SkillEvo** improves the feedback surface; **WER** trains the skill-writer policy; **SPADE** lets a bounded environment buffer condition future curriculum generation; **TRUSS** certifies candidate artifacts; **ERSkill** evolves the read policy; **HyperSkill** operationalizes relations. **Recuris** now separates persistent skills from verified working state and state-grounded invocation, then uses structured traces for component-local evolution. **Harness Continual Learning** widens the boundary further to jointly version memory, interface, capability map, and router under a commit gate. The question is **what state changes, from which evidence, and under what promotion/governance rule**.

**HiPS** adds a different adaptive-state boundary: the memory-management policy itself can split into shared rules and persona-local deltas, with matched ablations showing that rule flow and gating matter especially OOD. **KOPE** makes execution outcomes persistent experience state under a frozen model and fixed prompt budget; its evidence supports reusable external control state, while graph structure, ranking, compression, and injection are not yet fully separated.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-26 | [HiPS](../papers/2026/2608.25329.md) | `procedural` `structured` `personalization` | 4/5 | Shared-plus-persona rule state transfers across foundation models; matched ablations make rule flow/gating more credible than the heterogeneous headline leaderboard. |
| 2026-08-26 | [KOPE](../papers/2026/2608.25570.md) | `episodic` `procedural` `graph` `structured` `general-agent` | 4/5 | Execution-grounded experience changes later kernel decisions under a fixed model, but graph memory and active-context packaging remain partially confounded. |
| 2026-08-25 | [Recuris](../papers/2026/2608.24876.md) | `procedural` `working` `structured` `general-agent` | 4/5 | Same-library controls make verified working state and state-grounded invocation the clearest gain; cross-task patches transfer, while retry-matched Terminal-Bench adaptation is null. |
| 2026-08-23 | [CONTRAMEM](../papers/2026/2608.22533.md) | `procedural` `structured` `web-agent` `general-agent` | 4/5 | Heterogeneous outcome contrast plus localized curation improves transfer, but the frozen bank and coverage confound block an online self-evolution claim. |
| 2026-08-23 | [BASM](../papers/2026/2608.22339.md) | `procedural` `text` `structured` `general-agent` | 4/5 | Validity boundaries can suppress wrong-tool imitation after retrieval; the full package is not Pareto-improving and changes several stages. |
| 2026-08-20 | [Break It Down, Pass It On](../papers/2026/2608.20274.md) | `procedural` `text` `structured` `general-agent` | 4/5 | Whole-task skills reduce average success while subtask skills add small average gains; heterogeneous cells and unmatched lifecycle cost prevent a universal granularity claim. |
| 2026-08-19 | [Harness Continual Learning](../papers/2026/2608.19013.md) | `episodic` `procedural` `structured` `general-agent` | 4/5 | Jointly versions four harness components and gates commits on current utility, retention, and validity; package gains cannot be assigned to memory alone. |
| 2026-08-19 | [SPADE](../papers/2026/2608.19197.md) | `procedural` `structured` `general-agent` | 3/5 | A bounded environment buffer conditions later curriculum prompts; one no-memory run supports the package path, not regret retrieval or FIFO as isolated causes. |
| 2026-08-18 | [WER](../papers/2026/2608.17587.md) | `procedural` `text` `general-agent` | 4/5 | Same optimizer backbone/workflow gains 9.35/10.29 points after training from execution feedback; deeper refinement can regress. |
| 2026-08-18 | [TRUSS](../papers/2026/2608.17588.md) | `procedural` `structured` `general-agent` | 4/5 | Candidate skills are statically checked, shadow-executed, traced, refined, and re-certified before promotion; runtime safety is executor-dependent. |
| 2026-08-17 | [HyperSkill](../papers/2026/2608.16114.md) | `procedural` `structured` `graph` `general-agent` | 4/5 | Hypergraph structure is consumed by retrieval and maintenance, though representation and access remain partially confounded. |
| 2026-08-13 | [SkillEvo](../papers/2026/2608.13120.md) | `procedural` `structured` `general-agent` | 4/5 | Multi-turn failure feedback drives more improvement than governance; governance mainly limits regression and bloat. |
| 2026-08-13 | [ERSkill](../papers/2026/2608.12720.md) | `procedural` `structured` `general-agent` | 4/5 | Retrieval policy becomes persistent evolvable state: executable access skills and the query router co-evolve. |
| 2026-08-10 | [HyMeS](../papers/2026/2608.09410.md) | `working` `procedural` `structured` `embodied` | 4/5 | Separates motor competence in weights from inspectable memory strategy in code. |
| 2026-08-07 | [Agent Memory Distillation](../papers/2026/2608.07169.md) | `procedural` `structured` `general-agent` | 4/5 | Teacher experience transfers best when memory granularity/timing match the student's decision structure. |
| 2026-08-05 | [MemoryCPT](../papers/2026/2608.04843.md) | `episodic` `semantic` `structured` | 4/5 | Construction and read-time compression are learned jointly under quality/cost pressure. |
| 2026-08-03 | [RoMeRL](../papers/2026/2608.02508.md) | `episodic` `procedural` `structured` | 4/5 | Bounded semantic utility state can concentrate sparse feedback over richer experience stores. |

**Biggest unresolved question:** which adaptive-state location—artifact, writer, read policy, training-experience generator, structure, or whole harness—transfers across new consumers/domains strongly enough to justify acquisition, rollout, verification, retention testing, and maintenance cost?

**Next decisive evidence:** freeze source experiences, target tasks, and executor; independently vary feedback richness, writer learning, token-matched curriculum memory, artifact refinement, read-policy evolution, and commit governance under matched compute, then transfer the artifact/policy to a new domain and longer state stream without further tuning.

**Continue:** [Evaluation & Analysis →](evaluation-analysis.md)
