# Retrieval & Access

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How an agent locates, composes, filters, or withholds stored memory.

## Current argument

The read-side debate is no longer **flat vs structured memory**. **ReFind** raises the raw-record baseline by showing that a competent stateful search interface can recover much of the value attributed to pre-built semantic structure. **RippleMem** supplies the counterweight: structure can still earn its cost when it changes the operator from isolated matching into controlled evidence completion. **TRACE-Memory** adds a different control: even relevant personal evidence may be redundant once public context is considered, so the access layer should optimize **incremental utility and abstention**, not relevance alone. **Skill2Query**, **MESA**, and **MAP-Graph** expose adjacent questions about capability-aware retrieval, selective representation exposure, and admissibility.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-17 | [Skill2Query](../papers/2026/2608.16071.md) | `procedural` `structured` `text` `general-agent` | 3/5 | Capability/parameter structure improves pseudo-query supervision and retrieval, but online expansion is inconsistent and end-to-end evidence is still narrow. |
| 2026-08-13 | [RippleMem](../papers/2026/2608.13334.md) | `episodic` `graph` `structured` `general-agent` | 4/5 | Retrieved memories become anchors for missing-evidence search; the matched RF-Mem control suggests the gain is not only better extraction. |
| 2026-08-13 | [ReFind](../papers/2026/2608.12888.md) | `episodic` `text` `timeline` | 4/5 | Raw chat + iterative lexical search + chat-native controls is a serious structured-memory baseline; interface quality can dominate representation complexity. |
| 2026-08-11 | [MAP-Graph](../papers/2026/2608.10509.md) | `semantic` `graph` `general-agent` | 4/5 | Separates semantic relevance from hard read eligibility, recursive provenance trust, and action-risk gating. |
| 2026-08-10 | [MESA](../papers/2026/2608.10108.md) | `episodic` `structured` `general-agent` | 4/5 | Selective exposure beats reading every memory view: the controller must decide which representation is worth consuming. |
| 2026-08-09 | [TRACE-Memory](../papers/2026/2608.08446.md) | `semantic` `text` `personalization` | 4/5 | Conditions access on what the public-only path is missing, then admits a source-traceable subset—or EMPTY—by incremental utility. |
| 2026-08-07 | [PMCoder](../papers/2026/2608.06811.md) | `episodic` `structured` `coding` | 4/5 | Planner phase conditions retrieval and memory statistics can trigger replanning; controller↔memory interaction is the key result. |
| 2026-08-02 | [V-Mem](../papers/2026/2608.01543.md) | `episodic` `multimodal` `timeline` | 4/5 | Same-round identity is a structural access operator that bridges cross-modal evidence when similarity alone fails. |

**Biggest unresolved question:** when should memory stay as a raw archive searched online, when should structure support stronger evidence-completion operators, and when should the access layer abstain because memory adds no incremental value beyond current context?

**Next decisive evidence:** freeze the base model and raw evidence, then compare raw-record agentic search, matched associative/graph recollection, structure-aware skill retrieval, public-conditioned evidence admission, and learned routing under equal end-to-end latency/token budgets on long-horizon acting tasks.

**Continue:** [Write, Update & Consolidation →](write-update-consolidation.md)