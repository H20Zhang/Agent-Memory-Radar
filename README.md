# Agent Memory Radar

*A living research map of memory systems for LLM and multimodal agents.*

Track the latest work on long-term memory, episodic/semantic/procedural memory, retrieval and access, memory evolution, benchmarks, cost, provenance, and safety.

[Latest Papers](#latest-papers) · [What’s Changing](#whats-changing) · [Reading Paths](#reading-paths) · [Research Map](#research-map)

> **Field thesis.** Agent memory is best understood as a sequence of control boundaries: `archive / representation → access / admission → consumer state → update / evolution → governance / cost`. The useful question is not “which memory architecture wins?” but **which stage earns its complexity against the simplest matched alternative**.

Last updated: **2026-08-19** · Follow updates by starring the repository · Related: [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar)

## Latest Papers

### [QUMem: Personalized Memory for Query-Conditioned User-State Inference in LLM Agents](papers/2026/2608.16168.md)
`Representation & Organization` · `semantic` `structured` `timeline` `personalization` · **4/5** · 2026-08-17

**Research take.** The important delta is not another typed store. QUMem treats retrieved history as evidence for **query-conditioned user-state reconstruction**, and that read-side reconstruction is the largest component in its ablation.

[Paper](https://arxiv.org/abs/2608.16168) · [Research note](papers/2026/2608.16168.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Fixed memory boundaries and one-shot retrieval can split coherent events, bind unrelated user signals together, and miss preference evolution/contextual validity.

**Core mechanism.** `history → semantic episodes → typed facts/preferences/insights → information needs → typed multi-query retrieval → user-state inference → personalized response/action`.

**Compared with.** A-MEM, Mem0, Zep, plus ablations removing episode construction, typed decomposition, or user-state reconstruction.

**Evidence to remember.** PersonaMem GPT-4o-mini: **61.02** overall vs **52.99** strongest baseline; ablation **61.02 full → 58.38 w/o episodes → 57.11 w/o decomposition → 54.51 w/o reconstruction**. KnowU-Bench success: **17.4% vs 12.8%** strongest baseline.

**Open question.** Does explicit state reconstruction still win when retrieved evidence and synthesis budget are matched against a simpler provenance-aware alternative?

</details>

### [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](papers/2026/2608.16114.md)
`Memory Learning & Evolution` · `procedural` `structured` `graph` · **4/5** · 2026-08-17

**Research take.** The interesting part is not “hypergraphs beat vectors.” HyperSkill makes trajectory relations operational in **dual-path retrieval, cross-trajectory skill ranking, and maintenance**; the main caveat is that its no-hypergraph ablation also changes the access pipeline.

[Paper](https://arxiv.org/abs/2608.16114) · [Research note](papers/2026/2608.16114.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Flat trajectory/skill stores lose the higher-order relation among subtasks, reusable skills, and outcomes, while growing libraries accumulate redundant or low-utility guidance.

**Core mechanism.** `task → subtask + trajectory retrieval → fuse trajectory hyperedges → co-occurrence-ranked skills → execute → extract/update → prune/merge by utility + structure`.

**Compared with.** No Memory, experiential-memory baselines including PlugMem, and an internal flat-skill ablation that removes the hypergraph/dual-path structural pipeline.

**Evidence to remember.** Qwen3 success is **52.00 / 36.97 / 50.59** on xBench / GAIA / WebWalkerQA; **w/o hypergraph 41.00 / 35.76 / 44.71**, **w/o subtask retrieval 43.00 / 32.73 / 47.06**, **w/o trajectory retrieval 48.00 / 35.76 / 43.53**.

**Open question.** Does a hypergraph still win against a flat or binary-graph store when decomposition, the dual-path controller, co-occurrence ranking, and maintenance budget are held fixed?

</details>

### [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](papers/2026/2608.16071.md)
`Retrieval & Access` · `procedural` `structured` `text` · **3/5** · 2026-08-17

**Research take.** Procedural-memory relevance should align with **capability + parameter structure**, not just the outer skill document. The retrieval gains are real, but online query expansion is inconsistent and the end-to-end evidence is still narrow.

[Paper](https://arxiv.org/abs/2608.16071) · [Code](https://github.com/MatZaharia/Skill2Query) · [Research note](papers/2026/2608.16071.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Users describe goals while skill documents describe developer-facing functions/parameters; document-level pseudo-queries can be topical but functionally invalid.

**Core mechanism.** `skill → capability/parameter/example graph → style imitation → capability template → parameter filling/validation → offline augmentation / online expansion / retriever training`.

**Compared with.** Zero-shot, Few-shot, SkillFlow-style pseudo-query generation and BM25/dense/SkillRouter retrieval.

**Evidence to remember.** ToolQA offline SkillRouter R@1 **35.80%→47.34%**; removing the skill graph drops pseudo-query Exec-Pass **42.85%→22.63%** and functional coverage **11.32%→2.41%**. Online expansion helps some settings and hurts others.

**Open question.** Can capability-grounded skill retrieval improve long-horizon tool execution once retrieval, invocation, and skill utility are measured separately?

</details>

### [FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue](papers/2026/2608.16303.md)
`Write, Update & Consolidation` · `episodic` `structured` `timeline` `personalization` · **3/5** · 2026-08-17

**Research take.** Memory-unit granularity is a workload-dependent systems parameter. Situation-level units beat coarse sessions on sparse dialogue and cost less than turn-pair memory, but turn-pair is slightly more accurate on denser LoCoMo.

[Paper](https://arxiv.org/abs/2608.16303) · [Research note](papers/2026/2608.16303.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Sparse long-term dialogue makes session memory too coarse and turn-pair memory redundant/expensive.

**Core mechanism.** `dialogue → boundary-preserving situation windows → Fact-Time-Affect units → carry/fuse unresolved boundary evidence → temporal links → retrieve + structured context`.

**Compared with.** Standard dialogue-memory systems plus direct session-level and turn-pair construction controls.

**Evidence to remember.** ES-MemEval: session **31.76 F1 / 1.58M tokens**, turn-pair **37.06 / 6.40M**, FTA-Mem **38.71 / 4.99M**. On LoCoMo, turn-pair is **38.28 vs 37.35 F1** but costs **7.04M vs 3.39M** construction tokens.

**Open question.** Can a write controller adapt memory-unit granularity online as evidence density changes instead of using one global segmentation policy?

</details>

### [Demystifying Agent Skills: Why They Work—Until They Don’t](papers/2026/2608.14036.md)
`Evaluation & Analysis` · `procedural` `text` `coding` · **4/5** · 2026-08-14

**Research take.** Same source experience, different representation: standardized Skills outperform Workflow Memory and mostly work as **procedural anchors**, while exact retrieval labels remain a weak proxy for downstream utility.

[Paper](https://arxiv.org/abs/2608.14036) · [Research note](papers/2026/2608.14036.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Aggregate skill success conflates representation, outcome annotations, framework transfer, retrieval, invocation, and execution.

**Core mechanism.** Hold prior trajectories fixed → build Workflow Memory or SKILL.md → compare matched executions → separately measure retrieval, selection, actual use, and final success.

**Compared with.** Raw execution and Workflow Memory built from the same source trajectories.

**Evidence to remember.** Skills beat Workflow Memory by **6.06 points**; **65.7%** of skill cases are procedural anchoring vs **4.5%** knowledge injection. With pool size **5→100**, actual-use precision falls **29.6%→3.3%** while downstream success remains comparatively stable.

**Open question.** Does standardized procedural anchoring still win in large evolving skill libraries and non-software domains where “ground-truth skill” is less well defined?

</details>

### [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](papers/2026/2608.13334.md)
`Retrieval & Access` · `episodic` `graph` `structured` · **4/5** · 2026-08-13

**Research take.** First-hop memories become **anchors for missing-evidence search**, and a matched RF-Mem control suggests the gain survives after holding memory units and evidence budget fixed.

[Paper](https://arxiv.org/abs/2608.13334) · [Research note](papers/2026/2608.13334.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A relevant first-hop memory may be incomplete when answer evidence is distributed across sessions.

**Core mechanism.** Cue-rich event memories + sparse associations → first-hop recall → detect missing support → choose anchors + target → bounded local expansion → budgeted evidence assembly.

**Compared with.** RF-Mem using RippleMem's extracted units and the same evidence budget, plus standard flat/graph memory baselines.

**Evidence to remember.** LoCoMo LLM-judge: **87.14** full vs **83.83** matched RF-Mem; removing graph expansion gives **83.12**.

**Open question.** Does associative recollection still justify build/query cost on acting agents when online latency is matched to raw-record search?

</details>

### [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](papers/2026/2608.13120.md)
`Memory Learning & Evolution` · `procedural` `structured` · **4/5** · 2026-08-13

**Research take.** The strongest result is a feedback-source ablation: **multi-turn interaction keeps exposing useful defects after single-turn feedback saturates**. Governance mainly limits regression and bloat.

[Paper](https://arxiv.org/abs/2608.13120) · [Research note](papers/2026/2608.13120.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Procedural-memory evolution can plateau once obvious single-turn defects are fixed, while repeated editing accumulates regression and bloat.

**Core mechanism.** Multi-turn interaction → failure attribution → evidence-bounded skill edits → governance → persist checkpoint → repeat.

**Compared with.** Original Skills, multi-round self-reflection, and single-turn-QA-driven evolution under otherwise aligned update machinery.

**Evidence to remember.** Four-round task success reaches **81.8%** vs **66.4%** for matched single-turn QA; without governance it is **78.6%**, but bloat rises **+2.8%→+16.2%**.

**Open question.** Does the multi-turn advantage survive real-user feedback outside a high-fidelity simulator?

</details>

### [ERSkill: Evolving for Skill-Guided Adaptive Memory Retrieval](papers/2026/2608.12720.md)
`Memory Learning & Evolution` · `procedural` `structured` · **4/5** · 2026-08-13

**Research take.** ERSkill makes the **read policy itself persistent evolvable state**: executable retrieval skills and the router co-evolve, while deployment quality depends on whether the controller can reliably activate a useful skill.

[Paper](https://arxiv.org/abs/2608.12720) · [Research note](papers/2026/2608.12720.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Self-evolving memory often changes stored content while leaving query-time retrieval behavior fixed.

**Core mechanism.** Memory atoms + retrieval primitives → candidate retrieval skills → capability/deploy frontiers → learned query-conditioned router → selected skill constructs evidence.

**Compared with.** Standard memory systems and self-evolving experience/prompt systems, plus no-skill-evolution and router ablations.

**Evidence to remember.** The largest ablation losses come from removing **skill evolution** or the **learned router**; LoCoMo-trained skills/router transfer to LongMemEval without further training.

**Open question.** Does rollout-trained retrieval policy still pay off on tool-using agents versus a cheaper online adaptive controller?

</details>

### [When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory](papers/2026/2608.12888.md)
`Retrieval & Access` · `episodic` `text` `timeline` · **4/5** · 2026-08-13

**Research take.** The strongest current negative control for structured memory. A raw chat archive plus iterative lexical search and chat-native controls beats the compared graph/tree systems on precise refinding.

[Paper](https://arxiv.org/abs/2608.12888) · [Research note](papers/2026/2608.12888.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Structured memory may be credited for gains that actually come from comparing against a weak flat retrieval interface.

**Core mechanism.** Raw timestamped turns → turn-level BM25 → multi-round search → session fusion + local context/time controls → saved verbatim notes → answer.

**Compared with.** Single-shot BM25, matched generic-agentic BM25, and graph/tree/note memory systems.

**Evidence to remember.** Fixed LongMemEval-S/M: **93.2/89.3 ReFind vs 78.7/82.2 generic-agentic BM25 vs 84.7/68.9 one-search**.

**Open question.** Does raw-record search still win once online token/latency budgets are strictly matched on semantic or acting-agent tasks?

</details>

### [Beyond Retrieval: Query-Conditioned Reuse of Long-Horizon Agent Trajectories](papers/2026/2608.12847.md)
`Representation & Organization` · `procedural` `text` `web-agent` · **4/5** · 2026-08-13

**Research take.** Retrieval and reuse are different stages. With the same selected trajectory, a compact target-bound support object beats direct trace injection by forcing stale source bindings to be reacquired from current state.

[Paper](https://arxiv.org/abs/2608.12847) · [Research note](papers/2026/2608.12847.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A relevant past trajectory can still mislead the actor when users, files, IDs, dates, or environment state changed.

**Core mechanism.** Fixed retrieval/selection → write `workflow invariant + bindings to re-obtain + applicability conditions + verification guardrail` → actor grounds current values before execution.

**Compared with.** No memory, the same Full Trajectory, and a length-matched source-only Generic Summary under matched actor/target/tool conditions.

**Evidence to remember.** **62.3% success, +10.7pp over Full Trajectory, −48.9% online tokens**; under large binding shift, stale-binding errors **46.9%→10.9%**.

**Open question.** Can target-conditioned reuse remain faithful when multiple memories conflict or the support writer hallucinates missing constraints?

</details>

## What’s Changing

The useful unit here is a **design-space shift**, not a paper count.

| Current shift | Evidence | Research implication |
|---|---|---|
| **Structure must beat a competent raw-state control.** | ReFind ↔ RippleMem; TRACE-Memory | Separate representation value from the stronger operator or admission policy that structure enables. |
| **Retrieval is not the final consumer state.** | QUMem + QCR | Hold retrieval fixed and measure reconstruction, rebinding, and applicability as separate stages. |
| **Adaptive memory has multiple state variables.** | SkillEvo + ERSkill + HyperSkill | Distinguish feedback quality, evolvable read policy, representation, and maintenance instead of calling the whole loop “self-improving memory.” |
| **Lifecycle quality includes cost and trust.** | FTA-Mem + LycheeMemory V2 + Total Recall + AuthMem-Bench/SkillJack | Construction, serving, forgetting, authority, provenance, and descendant artifacts belong in the same systems accounting. |

### Current compactions

| Horizon | Current synthesis | What to take away |
|---|---|---|
| **Weekly** | [2026-W33](digests/weekly/2026-W33.md) · [2026-W32](digests/weekly/2026-W32.md) | W33 decomposes “memory architecture” into stage-specific controls; W32 is the correction that structure matters only when control can exploit it. |
| **Monthly** | [2026-08 · rolling through Aug 19](digests/monthly/2026-08.md) | The August map separates archive/representation, access/admission, consumer state, evolution, and lifecycle cost/provenance. |
| **Yearly** | [2026 · rolling, incomplete](digests/yearly/2026.md) | Current coverage supports a multi-stage state-interface view, but it is not a full-year reconstruction. |

[Browse all research compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes while fresh. **Monthly** rebuilds the field map. **Yearly** keeps durable shifts, defining papers, weakened ideas, evidence standards, and open problems. Lower-level reports remain in the repository for provenance.

</details>

## Reading Paths

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **When structure actually earns its cost** | [ReFind](papers/2026/2608.12888.md) → [RippleMem](papers/2026/2608.13334.md) → [MESA](papers/2026/2608.10108.md) | A competent raw-record interface is the baseline; structure matters when it enables evidence completion or selective access that online search cannot cheaply recover. |
| **Why retrieval is not the final state** | [QUMem](papers/2026/2608.16168.md) → [QCR](papers/2026/2608.12847.md) → [Demystifying Agent Skills](papers/2026/2608.14036.md) | Retrieved evidence may still need current-state reconstruction, rebinding, or procedural reshaping before an actor can use it reliably. |
| **How memory becomes self-improving state** | [SkillEvo](papers/2026/2608.13120.md) → [ERSkill](papers/2026/2608.12720.md) → [HyperSkill](papers/2026/2608.16114.md) | Evolution depends on the feedback surface, the read policy being evolved, and whether stored structure is operational during retrieval and maintenance. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**ReFind** raises the baseline for structured memory: raw chat plus competent stateful search can recover much of the value often credited to semantic preprocessing.

**RippleMem** supplies the necessary counterexample: pre-built associations can justify themselves when they turn a retrieved memory into a query for missing evidence and beat a matched recollection control.

**QUMem** exposes the next boundary: even after the right historical evidence is retrieved, the system may still need to infer the *current* state that the evidence jointly supports.

Together they replace “what is the best memory architecture?” with a better question: **what operation is enabled at each stage, and does it beat the simplest matched alternative?**

</details>

## Research Map

A compact systems view:

`archive / representation → access / admission → consumer state → update / evolution → governance / cost / provenance`

### Key Anchors

These are **design points, not a ranking**. The set changes slowly.

| Boundary | Work | Why it is a useful design point |
|---|---|---|
| Lifecycle contract | **[LeanMem](papers/2026/2608.03463.md)** | Different evidence types need different persistence/update semantics. |
| Cross-modal access | **[V-Mem](papers/2026/2608.01543.md)** | Same-round identity is an access operator when similarity cannot bridge modalities. |
| Raw-state control | **[ReFind](papers/2026/2608.12888.md)** | A raw archive with stateful query-time search is the control for semantic preprocessing. |
| Consumer state | **[QCR](papers/2026/2608.12847.md)** | The selected memory can still require target-conditioned rebinding before use. |
| Controller coupling | **[PMCoder](papers/2026/2608.06811.md)** | Retrieval and controller state can influence one another bidirectionally. |
| Learned utility state | **[RoMeRL](papers/2026/2608.02508.md)** | Sparse feedback can be concentrated in a bounded semantic utility state. |
| Authority | **[AuthMem-Bench](papers/2026/2608.01679.md)** | Semantically correct memory can still be wrong when authority is lost. |
| Descendant revocation | **[SkillJack](papers/2026/2608.03509.md)** | Provenance must survive experience → skill transformation and deletion. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

A useful reading order is **LeanMem / ReFind → V-Mem → QCR / PMCoder → RoMeRL → AuthMem-Bench / SkillJack**.

**QUMem, RippleMem, ERSkill, HyperSkill, and Demystifying Agent Skills** are current challengers without yet forcing extra anchors. QUMem strengthens the consumer-state boundary; RippleMem sharpens the access boundary; ERSkill may eventually replace an older control-state anchor if evolved access policies survive broader acting-agent evaluation; HyperSkill still needs a representation-matched structural controller; Demystifying strengthens procedural-reuse evaluation rather than adding a new durable boundary.

[See the full anchor notes →](papers/anchors.md)

</details>

### Research Problems

| Research problem | Core question | Current claim |
|---|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | What should persist, and what should reach the current consumer? | Archival evidence and actor-facing state are different objects. |
| **[Retrieval & Access](categories/retrieval-access.md)** | When should memory stay raw, become structured, or be withheld? | Strong raw-state controls are mandatory; structure earns cost through stronger operators or admission. |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | What persistent unit should be written, preserved, corrected, or forgotten? | Granularity, preservation contract, and transformation frequency are separate controls. |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | What adaptive state should evolve, and from which feedback? | Content, access policy, structural relations, and feedback source should not be conflated. |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | What makes memory worth deploying? | Retrieval quality alone misses behavioral utility, lifecycle cost, authority, and descendant effects. |

<details>
<summary><strong>Representation & Organization — archive faithfully, or optimize for the consumer?</strong></summary>

**Current evidence.** LeanMem and QCR as anchors; QUMem is the strongest current challenger.

**Strongest signal.** The archival object and the actor-facing state need not be identical. QUMem's largest ablation comes from removing query-time state reconstruction; QCR shows the same selected trajectory becomes more useful after target-conditioned rebinding.

**Biggest unresolved question.** Which transformations preserve enough provenance and fidelity to infer current state safely when preferences, bindings, or constraints conflict?

**Next decisive evidence.** Hold retrieval fixed and compare raw evidence, source-only summaries, target-conditioned support, and reconstructed user state under drift/conflict and matched synthesis cost.

</details>

<details>
<summary><strong>Retrieval & Access — when does structure beat a competent raw archive?</strong></summary>

**Current evidence.** ReFind, V-Mem, and PMCoder as anchors; RippleMem, Skill2Query, MESA, MAP-Graph, and TRACE-Memory as current challengers.

**Strongest signal.** ReFind raises the raw baseline; RippleMem shows structure can still win when it enables controlled evidence completion; TRACE-Memory adds public-conditioned admission/abstention; Skill2Query shows procedural retrieval can depend on capability/parameter structure.

**Biggest unresolved question.** Which relations must be pre-built, which can be reconstructed online, and when should the system abstain because memory adds no marginal utility?

**Next decisive evidence.** Compare raw-record search, associative recollection, structure-aware skill routing, public-conditioned admission, and learned routing under equal end-to-end compute on long-horizon acting tasks.

</details>

<details>
<summary><strong>Write, Update & Consolidation — what should one persistent unit be?</strong></summary>

**Current evidence.** LeanMem as an anchor; LycheeMemory V2, FTA-Mem, Scrub Jay, and Sleeping Agent expose complementary write-side controls.

**Strongest signal.** Boundary/granularity, transformation frequency, field preservation, and forgetting are separate decisions. FTA-Mem shows the preferred granularity can flip with evidence density; Sleeping Agent shows compact representations can selectively erase critical fields.

**Biggest unresolved question.** Can a streaming controller adapt write granularity and preservation contracts to changing density without one expensive LLM decision per turn?

**Next decisive evidence.** Sparse+dense acting-agent streams with controlled write budgets, conflicts, temporal drift, field-preservation metrics, and downstream action quality.

</details>

<details>
<summary><strong>Memory Learning & Evolution — what exactly should evolve?</strong></summary>

**Current evidence.** RoMeRL as an anchor; SkillEvo, ERSkill, HyperSkill, AMD, MemoryCPT, and HyMeS move adaptive state to different places.

**Strongest signal.** Evolution quality depends on **what receives adaptive state, what failures are observable, and whether stored relations are operational**. SkillEvo improves the feedback surface; ERSkill evolves the access program/router; HyperSkill uses higher-order trajectory structure during retrieval and maintenance.

**Biggest unresolved question.** Do evolved artifacts, policies, and structures transfer to new consumers and domains strongly enough to justify rollout, decomposition, and maintenance cost?

**Next decisive evidence.** Independently vary feedback richness, representation, update rule, access-policy evolution, governance, and cross-domain transfer under matched cost.

</details>

<details>
<summary><strong>Evaluation & Analysis — what does “good memory” mean after retrieval?</strong></summary>

**Current evidence.** AuthMem-Bench and SkillJack as anchors; Demystifying Agent Skills, Total Recall, Agent Skills Can Be Harmful, and Practice Makes Unsafe expose different failure surfaces.

**Strongest signal.** Endpoint recall/success hides stage-level effects: the same experience behaves differently as Workflow Memory vs Skill, exact retrieval can decouple from utility, lifecycle cost can move break-even by hundreds of turns, and descendant state can remain unsafe after its source is removed.

**Biggest unresolved question.** Can one deployment-facing evaluation vector expose representation, retrieval, invocation/reuse, utility, cost, provenance, authority, descendant state, and downstream action without collapsing them into one opaque score?

**Next decisive evidence.** Long-running acting-agent traces with stage-level attribution and matched no-memory / raw-history / alternative-representation / governed-memory controls.

</details>

[Explore the full research-problem map →](categories/README.md)

## How to Use This Radar

- **Scan:** title, category, importance, date, and **Research take** tell you whether a paper is worth opening.
- **Compare:** expand the 60-second view for the mechanism, closest comparison, one decisive result, and the open question most likely to change the importance judgment.
- **Deep dive:** open the research note for the full memory lifecycle (`write / organize / read / update-forget`), evidence, limitations, provenance, and verified visual explainer when available.
- **Build a mental model:** use [Reading Paths](#reading-paths) for sequence, [Research Map](#research-map) for design space, and [What’s Changing](#whats-changing) for temporal movement.

## What Counts as Agent Memory?

A work is included when **information persists or is explicitly managed across interaction/reasoning steps and materially changes a language or multimodal agent’s future behavior**.

Typical in-scope work changes at least one lifecycle boundary: what gets written, how memory is organized, how it is retrieved/admitted, how it is transformed for the current consumer, how it is updated/forgotten, how memory policy evolves, or how persistent state is evaluated for cost, authority, safety, and downstream effect.

Usually out of scope: ordinary fixed RAG with no persistent memory contribution, generic long-context modeling, KV-cache optimization, or unrelated continual learning. Work at the retrieval/memory boundary may also appear in [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) when adaptive information acquisition is itself the research contribution.

## About the Radar

This is a **curated research map, not an exhaustive keyword feed**. Every strong entry should help answer:

1. **What memory boundary actually changed?**
2. **Compared with what — especially the simplest matched alternative?**
3. **Does the evidence isolate that stage rather than crediting the whole architecture?**

Negative results and baseline reversals are kept when they change the interpretation. Relevance and importance are scored separately.

Research notes, digests, category maps, canonical paper data, and original radar figures are available under **CC BY 4.0**; maintenance code is under **MIT**. See [LICENSE.md](LICENSE.md) and [CITATION.cff](CITATION.cff).

## Contributing

The most valuable contributions change a research conclusion: a missing paper, stronger baseline, wrong taxonomy/importance, incorrect benchmark number, unsupported mechanism claim, broken provenance, or misleading visual.

[Suggest a paper](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=suggest-paper.yml) · [Report a correction](https://github.com/H20Zhang/Agent-Memory-Radar/issues/new?template=correction.yml) · [Contribution guide](CONTRIBUTING.md)

<details>
<summary><strong>Methodology & maintenance</strong></summary>

See the [maintainer guide](docs/MAINTENANCE.md), [curation protocol](CURATION.md), [compaction protocol](COMPACTION.md), [visual grounding rules](VISUAL_POLICY.md), [taxonomy](taxonomy.yaml), and [structured paper records](data/papers/).

</details>