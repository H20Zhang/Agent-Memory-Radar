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

### Uniform compaction → typed preservation → persistent lifecycle evidence

[The Compaction Cliff](../papers/2026/2608.22752.md) → [MemGuard](../papers/2026/2608.21867.md)

First ask which memory types require exact retention, then whether reliability evidence survives admission to govern later access and maintenance. Both are one-paper signals with unresolved upstream and governance cost.

### Stateless access → remembered relevance → applicability-gated use

[EARM](../papers/2026/2608.22767.md) → [BASM](../papers/2026/2608.22339.md)

Access can accumulate relevance experience, but a retrieved procedure still needs a current-state validity boundary. Test both on shuffled, growing stores under matched context and lifecycle cost.

### Outcome contrast → curated procedures → adversarial persistent write

[CONTRAMEM](../papers/2026/2608.22533.md) → [InjecMEM](../papers/2026/2608.23471.md)

Procedural construction benefits from outcome diversity, while ordinary write paths also create a persistent attack surface. Separate useful transfer, harmful steering, coverage, and construction compute.

### Raw archive → complementary/multi-source access → state localization → consumer-state reconstruction

[ReFind](../papers/2026/2608.12888.md) → [CABLE](../papers/2026/2608.17911.md) / [MemFuse](../papers/2026/2608.18704.md) → [ArborMem](../papers/2026/2608.17534.md) → [QUMem](../papers/2026/2608.16168.md)

“Structured vs raw” is not one decision. Start with a stronger raw-interface baseline, then test whether stored relations change reachability. If history contains interleaved trajectories, localize the active state; retrieved evidence may still need to be converted into actor-facing state.

### Candidate commitment → supersession → applicability-aware consumption

[Remember, Verify, or Ask?](../papers/2026/2608.19564.md) → [StateMemBench / StateMem](../papers/2026/2608.19652.md) → [MemTrapBench](../papers/2026/2608.20202.md)

Persistent state needs three different decisions: whether candidate information is authorized to enter memory, which older state it supersedes, and whether the resulting retrieved history is applicable to the current consumer. Current evidence is benchmark-bounded and does not yet join these stages in one executed lifecycle.

### Learned access/writer/curriculum → certified artifact → guarded harness commit

[SkillGate](../papers/2026/2608.18852.md) / [WER](../papers/2026/2608.17587.md) / [SPADE](../papers/2026/2608.19197.md) → [TRUSS](../papers/2026/2608.17588.md) → [Harness Continual Learning](../papers/2026/2608.19013.md)

Procedural-learning gains can come from relational structure, writer-policy learning, training-side experience memory, execution feedback, or runtime certification. Treating all of these changes as “memory” hides the causal variable.

### Retrieval score → stage attribution → gate qualification → feature-promotion evidence

[Demystifying Agent Skills](../papers/2026/2608.14036.md) → [Competence, Not Accuracy](../papers/2026/2608.18719.md) → [D²ACCI](../papers/2026/2608.17756.md)

Retrieval labels, actual use, downstream success, and deployment decisions are different evaluation objects. A memory feature ultimately needs paired, localized, non-regressing evidence; an architecture-level score alone is insufficient.

### Write granularity → active retention / skill-set selection → later execution

[Break It Down, Pass It On](../papers/2026/2608.20274.md) → [Weighted Memory Tree](../papers/2026/2608.20631.md) / [Optimal Skill Selection](../papers/2026/2608.19993.md)

The unit written, the state kept active, and the set exposed are separate policies. Current evidence shows direct later behavior but remains package-level, heterogeneous, or dependent on expensive supervision.

### Verbatim persistence → executable hygiene → provenance utility frontier

[DreamBench-SWE](../papers/2026/2608.20664.md) → [Utility Under Attack](../papers/2026/2608.21230.md)

First require earlier state to change an executable outcome and beat a verbatim archive; then test whether provenance defenses retain useful evidence as well as suppressing poison.

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
