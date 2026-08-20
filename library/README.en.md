# Agent Memory Research Library

[中文](README.md) | **English** · [Home](../README.en.md)

This is the long-lived research index, not a weekly archive. Start here when you know the **question** but not the paper title.

## Browse by Research Problem

| Problem | Entry | Current tension |
|---|---|---|
| **Representation & Organization** | [Open](../categories/representation-organization.md) | Should the archive preserve source evidence faithfully, or reconstruct state for the current consumer? |
| **Retrieval & Access** | [Open](../categories/retrieval-access.md) | When is raw search enough, and when do state localization or pre-built relations earn their cost? |
| **Write, Update & Consolidation** | [Open](../categories/write-update-consolidation.md) | How should memory-unit granularity, preservation contract, update frequency, and forgetting be separated? |
| **Memory Learning & Evolution** | [Open](../categories/memory-learning-evolution.md) | Is the artifact, writer/read policy, relational structure, or promotion gate actually evolving? |
| **Evaluation & Analysis** | [Open](../categories/evaluation-analysis.md) | How should stage attribution, utility, cost, provenance, and deployment gates be evaluated together? |

## Browse by Research Line

### 1. Raw archive → complementary structure → state localization → consumer-state reconstruction

[ReFind](../papers/2026/2608.12888.md) → [CABLE](../papers/2026/2608.17911.md) → [ArborMem](../papers/2026/2608.17534.md) → [QUMem](../papers/2026/2608.16168.md)

**Takeaway:** “structured vs raw” is not one decision. Raise the raw-interface baseline first; then ask whether stored relations change reachability; if history contains interleaved trajectories, localize the active state; finally separate retrieved evidence from actor-facing state.

### 2. Static procedural memory → operational relations → learned writer → certified capability

[HyperSkill](../papers/2026/2608.16114.md) → [WER](../papers/2026/2608.17587.md) → [TRUSS](../papers/2026/2608.17588.md)

**Takeaway:** procedural-memory gains can come from relational structure, writer-policy learning, execution feedback, or runtime certification. Treating all of them as “skill memory” hides the causal variable.

### 3. Retrieval score → stage attribution → feature-promotion evidence

[Demystifying Agent Skills](../papers/2026/2608.14036.md) → [D²ACCI](../papers/2026/2608.17756.md)

**Takeaway:** retrieval labels, actual use, downstream success, and deployment decisions are different objects. A memory feature ultimately needs paired, localized, non-regressing evidence—not an architecture-level score alone.

### 4. Fixed memory unit → adaptive write contract

[LeanMem](../papers/2026/2608.03463.md) → [FTA-Mem](../papers/2026/2608.16303.md) → [LycheeMemory V2](../papers/2026/2608.12990.md)

**Takeaway:** write granularity and preservation/update semantics are workload-dependent controls, not one schema choice to freeze globally.

## Browse by Year

- **2026:** the current corpus lives mainly under `papers/2026/`; use the research lines above or [design anchors](../papers/anchors.md) before browsing by date.
- **Temporal movement:** [weekly / monthly / yearly synthesis](../digests/README.md) answers what changed; it is not the historical retrieval layer.

## Cross-Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar): how Agent Memory is evaluated and how benchmark targets evolve.
- [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar): when the central problem is adaptive information acquisition rather than persistent-memory lifecycle.
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar): when persistent experience is used inside data work.
