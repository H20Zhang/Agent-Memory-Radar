# Browse Agent Memory by Research Problem

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What should be the persistent representation, and what should actually be delivered to the current consumer? | **QCR + LeanMem:** archival fidelity and actor-facing memory need not be the same object; representation earns complexity only when it exposes a useful downstream operation. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, combine, and govern stored memory once representation is no longer flat? | **ReFind + RippleMem + MESA/MAP-Graph:** raw-record search is a strong control, but structure can earn its cost when it enables evidence completion, selective exposure, or admissibility. |
| [Write, Update & Consolidation](write-update-consolidation.md) | When should memory be transformed, what must survive, and what should be forgotten? | **LycheeMemory V2 + Sleeping Agent:** consolidation frequency/granularity and field-level preservation are separate lifecycle decisions. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned or evolved, and from what feedback? | **SkillEvo + ERSkill + HyperSkill:** evolution now spans feedback generation, executable access policy, and structure-aware retrieval/maintenance; structure matters only when the controller actually consumes it. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “good memory” mean once representation, retrieval, reuse, cost, authority, security, and downstream behavior matter? | **Demystifying Agent Skills + Practice Makes Unsafe + Total Recall:** endpoint success hides stage-specific effects; procedural representation, retrieval/invocation, lifecycle cost, and descendant-state harm need separate attribution. |

## Cross-cutting lens

The radar now reasons over:

`archive/representation → access program → evidence completion/selection → consumer-facing reuse → update feedback/governance → lifecycle cost/provenance`

The current correction has two sides. **ReFind** says semantic preprocessing must beat a competent raw-record interface; **RippleMem** says structure can still be justified when it enables a stronger read operation under a matched memory-unit/evidence budget. **Demystifying Agent Skills** extends the same discipline downstream: even with the same source experience, representation changes procedural reuse, while exact retrieval labels do not reliably predict execution utility. **SkillEvo**, **ERSkill**, and **HyperSkill** then move the question into adaptation: self-improvement depends on what failures the system can observe, which retrieval policy can evolve, and whether relational structure is actually exploited during both retrieval and maintenance rather than merely stored.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.
