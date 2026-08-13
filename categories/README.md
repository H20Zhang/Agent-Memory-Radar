# Browse Agent Memory by Research Problem

The taxonomy is organized by **which part of the memory lifecycle changes**, not primarily by application domain.

| Category | Research question | Current signal |
|---|---|---|
| [Representation & Organization](representation-organization.md) | What memory forms should exist, and which evidence types deserve different structure/lifecycle semantics? | **LeanMem** remains the strongest lifecycle anchor. The new correction from MERIT is that structure must earn its complexity: extra typing/polarity is not automatically better than simpler dynamic memory. |
| [Retrieval & Access](retrieval-access.md) | How should an agent locate, query, navigate, and combine stored memory once representation is no longer flat? | **V-Mem + PMCoder**: access increasingly depends on relations and controller state, from same-round multimodal binding to planner-phase-conditioned episodic retrieval. |
| [Write, Update & Consolidation](write-update-consolidation.md) | What should be written, merged, revised, compressed, retained, or forgotten? | **Scrub Jay + MERIT**: explicit lifecycle policy matters, but structured write schemas need matched simple baselines; MERIT's extra typing is not reliably load-bearing. |
| [Memory Learning & Evolution](memory-learning-evolution.md) | Which memory decisions should be learned or transferred, and under what objective? | **MemoryCPT + RoMeRL + AMD**: policy learning now spans cost-aware transformation, bounded runtime utility state, and training-free teacher→student capability transfer. |
| [Evaluation & Analysis](evaluation-analysis.md) | What does “correct memory” mean once cost, provenance, authority, security, and downstream behavior matter? | **AuthMem-Bench + MAFIA + SkillJack**: correctness includes authority, persistent-state integrity, and transitive provenance/revocation across derived artifacts. |

## Cross-cutting lens

For system claims, the radar now asks:

`representation × access operator × controller state × write/update policy × cost × trust`

The emerging caution is equally important: **a richer memory representation is not evidence of a better memory system unless an ablation shows which downstream decision exploits that structure**.

Orthogonal tags in [`../taxonomy.yaml`](../taxonomy.yaml) capture memory type, substrate, and application without turning them into mutually exclusive primary categories.
