# Design Anchors

[Research Map](../README.md#research-map) · [Reading Paths](../README.md#reading-paths) · [What’s Changing](../README.md#whats-changing)

These are **durable design points, not a ranking**. An anchor stays only while it represents a distinct control boundary that helps compare newer work.

| Boundary | Paper | Design point |
|---|---|---|
| Lifecycle contract | **[LeanMem](2026/2608.03463.md)** | Different evidence types should not share one persistence/update contract. |
| Cross-modal access | **[V-Mem](2026/2608.01543.md)** | Same-round identity is an access operator when similarity cannot bridge modalities. |
| Raw-state control | **[ReFind](2026/2608.12888.md)** | Raw archival state + competent query-time search is the control for semantic preprocessing. |
| Consumer state | **[QCR](2026/2608.12847.md)** | Correctly retrieved history may still require target-conditioned rebinding before execution. |
| Controller coupling | **[PMCoder](2026/2608.06811.md)** | Retrieval and controller state can influence one another bidirectionally. |
| Learned utility state | **[RoMeRL](2026/2608.02508.md)** | Sparse feedback can be concentrated in a bounded semantic utility state. |
| Authority | **[AuthMem-Bench](2026/2608.01679.md)** | Semantically faithful memory can still be wrong when source authority is lost. |
| Descendant revocation | **[SkillJack](2026/2608.03509.md)** | Provenance must survive experience → skill transformation and deletion. |

## How to read the anchor set

`what persists → how it is accessed → what the consumer receives → what adaptive state learns → whether lifecycle trust survives`

A useful sequence is **LeanMem / ReFind → V-Mem → QCR / PMCoder → RoMeRL → AuthMem-Bench / SkillJack**. The sequence is more important than individual ranking: it turns “agent memory” into a set of separable design decisions.

### Current challengers

- **QUMem** strengthens the consumer-state boundary by reconstructing current user state after retrieval.
- **RippleMem** strengthens the access boundary by using first-hop memories to search for missing evidence.
- **ERSkill** may eventually replace an older control-state anchor if evolved read policies survive broader acting-agent evaluation.
- **HyperSkill** strengthens the case for operational structure but still needs a representation-matched structural controller.
- **Demystifying Agent Skills** strengthens procedural-memory evaluation without introducing a new durable control boundary.

### Rotated out, still important

**MemoryCPT** remains a strong learned cost×quality pipeline; **Scrub Jay Memory** remains a clean per-memory temporal-utility design. They are omitted only to keep the anchor set bounded.

[Back to the Research Map →](../README.md#research-map)