# Retrieval & Access

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How an agent localizes active state, locates evidence, expands beyond first-hop retrieval, and decides what memory to expose.

## Current argument

The read side is no longer one operation called retrieval. **ReFind** establishes a competent raw-record/search control. **ArborMem** moves one boundary earlier by localizing which interaction state is being resumed before retrieving support. **CABLE** then asks whether pre-built relations expose evidence outside the host retriever's direct neighborhood. **RippleMem** continues the process after first-hop recall by using retrieved memories as anchors for missing-evidence search. **TRACE-Memory** adds the final admission decision: relevant personal evidence can still be unnecessary once current/public context is sufficient.

The useful decomposition is now:

`state localization → direct retrieval → complementary expansion / recollection → evidence admission`

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-18 | [CABLE](../papers/2026/2608.17911.md) | `episodic` `graph` `structured` `general-agent` | 4/5 | Link construction subtracts direct semantic neighbors before verification, so stored edges are designed to extend host-retriever reach rather than duplicate it. |
| 2026-08-18 | [ArborMem](../papers/2026/2608.17534.md) | `episodic` `hierarchical` `timeline` `general-agent` | 4/5 | Localizes the resumed interaction state before evidence retrieval; the localization ablation is strong for the 30B setting but much smaller for 4B. |
| 2026-08-17 | [Skill2Query](../papers/2026/2608.16071.md) | `procedural` `structured` `text` `general-agent` | 3/5 | Capability/parameter structure improves pseudo-query supervision, but online expansion is inconsistent and end-to-end evidence is narrow. |
| 2026-08-13 | [RippleMem](../papers/2026/2608.13334.md) | `episodic` `graph` `structured` `general-agent` | 4/5 | First-hop memories become anchors for missing-evidence search; a matched RF-Mem control suggests the gain is not only better extraction. |
| 2026-08-13 | [ReFind](../papers/2026/2608.12888.md) | `episodic` `text` `timeline` | 4/5 | Raw chat + iterative lexical search + chat-native controls is a serious structured-memory baseline. |
| 2026-08-11 | [MAP-Graph](../papers/2026/2608.10509.md) | `semantic` `graph` `general-agent` | 4/5 | Separates semantic relevance from hard read eligibility, provenance trust, and action-risk gating. |
| 2026-08-10 | [MESA](../papers/2026/2608.10108.md) | `episodic` `structured` `general-agent` | 4/5 | Selective exposure beats reading every memory view; the controller decides which representation is worth consuming. |
| 2026-08-09 | [TRACE-Memory](../papers/2026/2608.08446.md) | `semantic` `text` `personalization` | 4/5 | Conditions access on what the public-only path is missing, then admits a source-traceable subset—or EMPTY—by incremental utility. |
| 2026-08-07 | [PMCoder](../papers/2026/2608.06811.md) | `episodic` `structured` `coding` | 4/5 | Planner state conditions retrieval and memory statistics can trigger replanning; controller↔memory coupling is the delta. |
| 2026-08-02 | [V-Mem](../papers/2026/2608.01543.md) | `episodic` `multimodal` `timeline` | 4/5 | Same-round identity is a structural access operator when similarity cannot bridge modalities. |

**Biggest unresolved question:** which read operators should be precomputed versus reconstructed online, and where is the crossover once write cost, query latency/tokens, error propagation, and downstream action risk are matched?

**Next decisive evidence:** freeze raw history, base model, and task set; independently toggle state localization, raw agentic search, complementary link expansion, recollection, and admission under one end-to-end budget, then evaluate both evidence quality and acting-agent outcomes.

**Continue:** [Write, Update & Consolidation →](write-update-consolidation.md)
