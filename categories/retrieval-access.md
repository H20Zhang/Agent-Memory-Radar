# Retrieval & Access

How an agent locates, queries, navigates, or reasons over stored memory.

## Current argument

The read-side debate is no longer **flat vs structured memory**. **ReFind** raises the raw-record baseline by showing that a competent stateful search interface can recover much of the value attributed to pre-built semantic structure. **RippleMem** supplies the counterweight: structure can still earn its cost when it changes the operator from isolated matching into controlled evidence completion. **TRACE-Memory** adds another orthogonal control: even relevant personal evidence may be redundant or unjustified once public context is considered, so the access layer should optimize **incremental utility and abstention**, not relevance alone. **Skill2Query** sharpens the same issue for procedural memory: a skill document is not one semantic blob, and retrieval supervision improves when capability, parameter, and example structure become explicit—but online query expansion is not uniformly positive. **MESA** and **MAP-Graph** expose adjacent controls over which representation to expose and whether evidence is admissible.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-17 | [Skill2Query](../papers/2026/2608.16071.md) | `procedural` `structured` `text` `general-agent` | ★★★☆☆ | Capability/parameter structure improves pseudo-query supervision and retrieval, but online expansion is inconsistent and end-to-end evidence is still narrow. |
| 2026-08-13 | [RippleMem](../papers/2026/2608.13334.md) | `episodic` `graph` `structured` `general-agent` | ★★★★☆ | Retrieved memories become anchors for missing-evidence search; the matched RF-Mem control suggests the graph/recollection gain is not only better extraction. |
| 2026-08-13 | [ReFind](../papers/2026/2608.12888.md) | `episodic` `text` `timeline` | ★★★★☆ | Raw chat + iterative lexical search + chat-native controls is a serious structured-memory baseline; interface quality can dominate representation complexity. |
| 2026-08-11 | [MAP-Graph](../papers/2026/2608.10509.md) | `semantic` `graph` `general-agent` | ★★★★☆ | Separates semantic relevance from hard read eligibility, recursive provenance trust, and action-risk gating. |
| 2026-08-10 | [MESA](../papers/2026/2608.10108.md) | `episodic` `structured` `general-agent` | ★★★★☆ | The right policy is often several memory structures but not all: 65.1% with 2.8 views / 11.0k tokens vs 63.7% reading all five / 18.7k. |
| 2026-08-09 | [TRACE-Memory](../papers/2026/2608.08446.md) | `semantic` `text` `personalization` | ★★★★☆ | Conditions memory access on what the public-only path is missing, then admits a compact source-traceable subset—or EMPTY—by incremental response utility rather than relevance alone. |
| 2026-08-07 | [PMCoder](../papers/2026/2608.06811.md) | `episodic` `structured` `coding` | ★★★★☆ | Planner phase conditions retrieval and memory statistics can trigger replanning; controller↔memory interaction is the key result. |
| 2026-08-02 | [V-Mem](../papers/2026/2608.01543.md) | `episodic` `multimodal` `timeline` | ★★★★☆ | Same-round identity is a structural access operator that bridges cross-modal evidence when similarity alone fails. |

**Biggest unresolved question:** when should memory stay as a raw archive searched online, when should structure support stronger evidence-completion operators, and when should the access layer **abstain** because retrieved memory adds no incremental value beyond the current non-memory context?

**Next decisive evidence:** freeze the base model and raw evidence, then compare raw-record agentic search, matched associative/graph recollection, structure-aware skill retrieval, public-conditioned evidence admission, and learned routing under equal end-to-end latency/token budgets on long-horizon acting tasks—not only conversational QA, personalized generation, or one-step skill selection.
