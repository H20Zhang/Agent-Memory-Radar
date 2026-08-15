# Browse Agent Memory by Research Problem

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What should be the persistent representation, and what should actually be delivered to the current consumer? | **QCR + LeanMem:** archival fidelity and actor-facing memory need not be the same object; representation earns complexity only when it exposes a useful downstream operation. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, combine, and govern stored memory once representation is no longer flat? | **ReFind + MESA + MAP-Graph:** a competent stateful access interface can rival pre-built semantic structure; selection and admissibility are first-class controls. |
| [Write, Update & Consolidation](write-update-consolidation.md) | When should memory be transformed, what must survive, and what should be forgotten? | **LycheeMemory V2 + Sleeping Agent:** consolidation frequency/granularity and field-level preservation are separate lifecycle decisions. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned, transferred, or externalized, and in what substrate? | **MemoryCPT / RoMeRL / AMD / HyMeS:** adaptive state can live in learned policy, teacher memory, or executable code; consumer compatibility remains central. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “good memory” mean once cost, authority, procedural side effects, and persistent adaptation matter? | **Practice Makes Unsafe + Total Recall + Agent Skills:** endpoint recall/success hides lifecycle cost and state-transition failures; marginal effect needs stage-level attribution. |

## Cross-cutting lens

The radar now reasons over:

`archive/representation → access policy → selected evidence → consumer-facing reuse → lifecycle update/cost → provenance & revocation`

The newest correction is important: **preprocessing and retrieval are not the whole memory system**. ReFind says rich preprocessing must beat a competent raw-record interface; QCR says correct retrieval still does not guarantee correct reuse; LycheeMemory says write-side consolidation frequency changes the cost/quality frontier.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.
