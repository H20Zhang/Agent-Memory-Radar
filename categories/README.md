# Browse Agent Memory by Research Problem

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What memory forms should exist, and which evidence types deserve different structure/lifecycle semantics? | LeanMem + Activity Frames: strongest current signal is typed / heterogeneous memory rather than one universal store. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, query, navigate, and combine stored memory once representation is no longer flat? | No current paper clears the radar's precision threshold as a primary contribution; richer access semantics remain an open gap. |
| [Write, Update & Consolidation](write-update-consolidation.md) | What should be written, merged, revised, compressed, retained, or forgotten? | Scrub Jay Memory: retention/forgetting is becoming an explicit utility-aware lifecycle decision. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned rather than hand-designed, and under what objective? | MemoryCPT: construction and query-time compression become trainable under a cost × quality objective. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “correct memory” mean once cost, provenance, authority, security, and downstream behavior matter? | AuthMem-Bench + MAFIA: persistent state introduces authority and integrity invariants beyond relevance. |

## Cross-cutting lens

For system claims, the radar tries to reason over:

`representation × write/update policy × access interface × forgetting/compression × cost × trust`

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.

The category pages are living research views: they should change when evidence changes, not simply accumulate paper links.
