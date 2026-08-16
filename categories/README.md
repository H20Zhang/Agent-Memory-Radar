# Browse Agent Memory by Research Problem

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What should be the persistent representation, and what should actually be delivered to the current consumer? | **QCR + LeanMem:** archival fidelity and actor-facing memory need not be the same object; representation earns complexity only when it exposes a useful downstream operation. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, combine, and govern stored memory once representation is no longer flat? | **ReFind + RippleMem + MESA/MAP-Graph:** raw-record search is a strong control, but structure can earn its cost when it enables evidence completion, selective exposure, or admissibility. |
| [Write, Update & Consolidation](write-update-consolidation.md) | When should memory be transformed, what must survive, and what should be forgotten? | **LycheeMemory V2 + Sleeping Agent:** consolidation frequency/granularity and field-level preservation are separate lifecycle decisions. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned or evolved, and from what feedback? | **SkillEvo + ERSkill + AMD/RoMeRL:** evolution quality depends on the feedback surface, consumer compatibility, and whether adaptation changes stored content, control state, or the access program itself. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “good memory” mean once cost, authority, procedural side effects, and persistent adaptation matter? | **Practice Makes Unsafe + Total Recall + Agent Skills:** endpoint recall/success hides lifecycle cost and state-transition failures; marginal effect needs stage-level attribution. |

## Cross-cutting lens

The radar now reasons over:

`archive/representation → access program → evidence completion/selection → consumer-facing reuse → update feedback/governance → lifecycle cost/provenance`

The current correction has two sides. **ReFind** says semantic preprocessing must beat a competent raw-record interface; **RippleMem** says structure can still be justified when it enables a stronger read operation under a matched memory-unit/evidence budget. **SkillEvo** and **ERSkill** then move the question downstream: self-improvement depends on what failures the system can observe and whether the retrieval policy itself is evolvable.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.
