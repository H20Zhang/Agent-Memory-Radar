# Agent Memory Research Library

[中文](README.md) | **English** · [Home](../README.en.md)

This is the long-lived research index, not a weekly archive. Start here when you know the **question** but not the paper title.

## Browse by Research Problem

| Problem | Entry | Current tension |
|---|---|---|
| **Representation & Organization** | [Open](../categories/representation-organization.md) | Should the archive preserve source evidence faithfully, or reconstruct state for the current consumer? |
| **Retrieval & Access** | [Open](../categories/retrieval-access.md) | What can competent raw-state search recover, and when does structure earn its cost? |
| **Write, Update & Consolidation** | [Open](../categories/write-update-consolidation.md) | How should memory-unit granularity, update frequency, preservation contract, and forgetting be separated? |
| **Memory Learning & Evolution** | [Open](../categories/memory-learning-evolution.md) | Is content, read policy, relational structure, or governance actually evolving? |
| **Evaluation & Analysis** | [Open](../categories/evaluation-analysis.md) | How should utility, lifecycle cost, authority, provenance, and descendant effects be measured beyond retrieval quality? |

## Browse by Research Line

### 1. Raw archive → structured access → consumer-state reconstruction

[ReFind](../papers/2026/2608.12888.md) → [RippleMem](../papers/2026/2608.13334.md) → [QUMem](../papers/2026/2608.16168.md) → [QCR](../papers/2026/2608.12847.md)

**Takeaway:** “structured or not” is too coarse. First ask what a strong raw interface can recover online; then ask which operator pre-built relations enable; finally separate retrieved evidence from the state consumed by the actor.

### 2. Static procedural memory → evolving skill → evolving read policy

[Demystifying Agent Skills](../papers/2026/2608.14036.md) → [SkillEvo](../papers/2026/2608.13120.md) → [ERSkill](../papers/2026/2608.12720.md) → [HyperSkill](../papers/2026/2608.16114.md)

**Takeaway:** procedural-memory gains should not be credited to “having skills” as one package. Representation, feedback surface, retrieval policy, relations, and maintenance can each be causal variables.

### 3. Fixed memory unit → adaptive write contract

[LeanMem](../papers/2026/2608.03463.md) → [FTA-Mem](../papers/2026/2608.16303.md) → [LycheeMemory V2](../papers/2026/2608.09424.md)

**Takeaway:** write granularity and preservation/update semantics are workload-dependent controls, not one schema choice to freeze globally.

## Browse by Year

- **2026:** the current corpus lives mainly under `papers/2026/`; use the research lines above or [design anchors](../papers/anchors.md) before browsing by date.
- **Temporal movement:** [weekly / monthly / yearly synthesis](../digests/README.md) answers what changed; it is not the historical retrieval layer.

## Cross-Radar

- [Agent Benchmark Radar](https://github.com/H20Zhang/Agent-Benchmark-Radar): how Agent Memory is evaluated and how benchmark targets evolve.
- [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar): when the central problem is adaptive information acquisition rather than persistent-memory lifecycle.
- [Data Agent Radar](https://github.com/H20Zhang/Data-Agent-Radar): when persistent experience is used inside data-analysis or data-engineering workflows.
