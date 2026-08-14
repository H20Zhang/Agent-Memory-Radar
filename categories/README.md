# Browse Agent Memory by Research Problem

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What memory forms should exist, and which evidence types deserve distinct structure/lifecycle semantics? | **LeanMem + PGMem:** structure is useful when it exposes lifecycle/validity relations; persona representation is more load-bearing than graph structure alone. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, combine, and govern stored memory once representation is no longer flat? | **MESA + PMCoder + MAP-Graph:** access now includes structure selection, controller conditioning, and provenance admissibility—not only similarity. |
| [Write, Update & Consolidation](write-update-consolidation.md) | What should be written, compressed, revised, retained, or forgotten? | **Scrub Jay + Sleeping Agent + MERIT:** lifecycle transforms need both utility and preservation diagnostics; extra typing is not automatically useful. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned, transferred, or externalized, and in what substrate? | **MemoryCPT / RoMeRL / AMD / HyMeS:** adaptive state can live in learned policy state, teacher memory, or executable code; consumer compatibility is now a first-class issue. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “good memory” mean once cost, authority, provenance, procedural side effects, and downstream action matter? | **Total Recall + Agent Skills + AuthMem/SkillJack:** recall alone is insufficient; lifecycle cost and marginal behavioral effect must be measured independently. |

## Cross-cutting lens

For system claims, the radar now reasons over:

`representation × write/update policy × access interface × controller/consumer state × cost × provenance/trust`

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.

The category pages are living research arguments: they should change when evidence changes, not simply accumulate paper links.
