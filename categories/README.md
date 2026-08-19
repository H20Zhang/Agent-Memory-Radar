# Browse Agent Memory by Research Problem

[← Agent Memory Radar](../README.md) · [What’s changing](../README.md#-whats-changing) · [Reading paths](../README.md#-reading-paths)

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What should be the persistent representation, and what should actually be delivered to the current consumer? | **QUMem + QCR:** archival evidence and consumer-facing state should be separated; query-time reconstruction/rebinding can matter more than storing another schema. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, combine, and govern stored memory once representation is no longer flat? | **ReFind + RippleMem + TRACE-Memory + Skill2Query + MESA/MAP-Graph:** raw-record search is a strong control, but access can earn complexity through evidence completion, public-conditioned incremental utility/abstention, capability-grounded retrieval, selective exposure, or admissibility. |
| [Write, Update & Consolidation](write-update-consolidation.md) | What event boundary should be written, what must survive, and what should be forgotten? | **LycheeMemory V2 + FTA-Mem + Sleeping Agent:** write granularity, construction frequency, and field-level preservation are separate lifecycle controls. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned or evolved, and from what feedback? | **SkillEvo + ERSkill + HyperSkill:** evolution now spans feedback generation, executable access policy, and structure-aware retrieval/maintenance; structure matters only when the controller actually consumes it. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “good memory” mean once representation, retrieval, reuse, cost, authority, security, and downstream behavior matter? | **Demystifying Agent Skills + Practice Makes Unsafe + Total Recall:** endpoint success hides stage-specific effects; procedural representation, retrieval/invocation, lifecycle cost, and descendant-state harm need separate attribution. |

## Cross-cutting lens

The radar now reasons over:

`archive/representation → access program → evidence completion/selection/admission → consumer-facing state/reuse → update feedback/governance → lifecycle cost/provenance`

The strongest current correction is **stage attribution**. **ReFind** says semantic preprocessing must beat a competent raw-record interface; **RippleMem** says structure can still be justified when it enables a stronger read operator under matched memory-unit/evidence budgets. **TRACE-Memory** adds a different access boundary: retrieved personal evidence should be conditioned on what the public/non-memory path already provides and should support an explicit empty-set decision when memory adds no incremental utility. **QUMem** and **QCR** then show that admitted evidence is not necessarily the state an actor should consume: the system may need to reconstruct current user state or rebind stale trajectory variables. **Skill2Query** makes the same point one level earlier for procedural artifacts—retrieval supervision should align with internal capability/parameter structure, not merely document semantics. On the write side, **LycheeMemory V2** and **FTA-Mem** show that event-boundary choice is a measurable quality-cost parameter rather than a universal constant.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.
