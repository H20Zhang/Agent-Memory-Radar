# Browse Agent Memory by Research Problem

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What memory forms should exist, and which evidence types deserve different structure/lifecycle semantics? | **LeanMem** is the strongest current anchor for typed lifecycles. **Activity Frames** and, more tentatively, **Muscle Memory** widen the design space from deterministic compiled state to executable procedural specialists. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, query, navigate, and combine stored memory once representation is no longer flat? | **V-Mem**: modality-specific routing plus shared interaction structure can matter more than a universal similarity space; the biggest unresolved question is how to generalize this beyond heuristic modality routing. |
| [Write, Update & Consolidation](write-update-consolidation.md) | What should be written, merged, revised, compressed, retained, or forgotten? | **Scrub Jay Memory**: retention/forgetting is becoming an explicit per-memory utility decision. The missing evidence is whether such policies remain stable under conflicting, nonstationary real-world state. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned rather than hand-designed, and under what objective? | **MemoryCPT + RoMeRL**: policy learning now spans cost-aware construction/compression and bounded runtime utility state. The key tension is richer learned control versus feedback sparsity and attribution error. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “correct memory” mean once cost, provenance, authority, security, and downstream behavior matter? | **AuthMem-Bench + MAFIA + SkillJack**: correctness increasingly includes authority, persistent-state integrity, and transitive provenance/revocation across derived artifacts. |

## Cross-cutting lens

For system claims, the radar tries to reason over:

`representation × write/update policy × access interface × forgetting/compression × cost × trust`

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.

The category pages are living research views: they should change when evidence changes, not simply accumulate paper links.
