# Agent Memory Research Library

[中文](README.md) | **English** · [Home](../README.en.md)

Browse by research problem, research line, or year. If you know the question but not the paper title, start with the problem index below.

## Browse by Research Problem

| Problem | Entry | Current tension |
|---|---|---|
| **Representation & Organization** | [Open](../categories/representation-organization.md) | Should the archive preserve source evidence faithfully, or reconstruct state for the current consumer? |
| **Retrieval & Access** | [Open](../categories/retrieval-access.md) | When is raw search enough, and when do state localization or pre-built relations earn their cost? |
| **Write, Update & Consolidation** | [Open](../categories/write-update-consolidation.md) | How should memory-unit granularity, preservation contract, update frequency, and forgetting be separated? |
| **Memory Learning & Evolution** | [Open](../categories/memory-learning-evolution.md) | Is the artifact, writer/read policy, relational structure, or promotion gate actually evolving? |
| **Evaluation & Analysis** | [Open](../categories/evaluation-analysis.md) | How should stage attribution, utility, cost, provenance, and deployment gates be evaluated together? |

## Browse by Research Line

### Raw archive → complementary structure → state localization → consumer-state reconstruction

[ReFind](../papers/2026/2608.12888.md) → [CABLE](../papers/2026/2608.17911.md) → [ArborMem](../papers/2026/2608.17534.md) → [QUMem](../papers/2026/2608.16168.md)

“Structured vs raw” is not one decision. Start with a stronger raw-interface baseline, then test whether stored relations change reachability. If history contains interleaved trajectories, localize the active state; retrieved evidence may still need to be converted into actor-facing state.

### Static procedural memory → operational relations → learned writer → certified capability

[HyperSkill](../papers/2026/2608.16114.md) → [WER](../papers/2026/2608.17587.md) → [TRUSS](../papers/2026/2608.17588.md)

Procedural-memory gains can come from relational structure, writer-policy learning, execution feedback, or runtime certification. Treating all of these changes as “skill memory” hides the causal variable.

### Retrieval score → stage attribution → feature-promotion evidence

[Demystifying Agent Skills](../papers/2026/2608.14036.md) → [D²ACCI](../papers/2026/2608.17756.md)

Retrieval labels, actual use, downstream success, and deployment decisions are different evaluation objects. A memory feature ultimately needs paired, localized, non-regressing evidence; an architecture-level score alone is insufficient.

### Fixed memory unit → adaptive write contract

[LeanMem](../papers/2026/2608.03463.md) → [FTA-Mem](../papers/2026/2608.16303.md) → [LycheeMemory V2](../papers/2026/2608.12990.md)

Write granularity and preservation/update semantics vary with the workload and should not be frozen as one global schema choice.

## Browse by Year

- **2026:** the current corpus lives mainly under `papers/2026/`; start with the research lines above or [design anchors](../papers/anchors.md).
- **Temporal movement:** [weekly / monthly / yearly synthesis](../digests/README.md) tracks changes in the field rather than serving as the historical index.

## Related Radars

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar): how Agent Memory is evaluated and how benchmark targets evolve.
- [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar): when the central problem is adaptive information acquisition rather than persistent-memory lifecycle.
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar): when persistent experience is used inside data work.
