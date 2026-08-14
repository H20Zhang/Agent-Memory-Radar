# 🧠 Agent Memory Radar

**A living research map of memory for AI agents.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-13 · [Research compactions](#-research-compactions) · [Latest papers](#-latest-papers) · [Browse by research problem](categories/README.md)

## 🧭 Research Compactions

If you only have a few minutes, **start here**. The archive deliberately becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

### Recent Month · Weekly

**[2026-W32 · Structure only matters when control can use it](digests/weekly/2026-W32.md)**  
The closed Aug 3–9 week shifted the radar away from “more structure is better.” PMCoder showed controller↔memory coupling, AMD showed consumer-granularity alignment, and MERIT supplied counter-evidence that plausible extra typing need not beat a simpler dynamic memory.

**W33 (Aug 10–16) is still open**, so no partial weekly report is presented as a finished compaction.

[Read W32 synthesis →](digests/weekly/2026-W32.md)

### Recent Quarter · Monthly

**[2026-08 · Rolling research map through Aug 13](digests/monthly/2026-08.md)**  
The August map now points to a sharper state-control thesis: **select the representation the current decision needs, govern whether derived evidence may be used, measure the whole lifecycle cost, and treat reusable memory as having a consumer-compatibility contract**. MESA, MAP-Graph, Total Recall, and the new skill-failure analysis add independent evidence for those four boundaries.

The important correction is negative as well as positive: neither “more structured memory” nor “smaller retrieved context” is sufficient evidence of a better system.

[Explore the rolling August map →](digests/monthly/2026-08.md)

### All Years · Yearly

**[2026 · Rolling, incomplete research map](digests/yearly/2026.md)**  
Active radar curation starts in August, with one accepted July backfill, so this is **not a full-year reconstruction**. Within that narrow coverage, the strongest durable hypothesis is that memory is becoming a selective state-control layer whose representation, access, consumer state, lifecycle cost, and provenance must be co-designed.

[Explore the 2026 rolling map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes and disagreements while they are fresh. **Monthly** compresses several weeks into design-space movement. **Yearly** keeps only shifts that survive broader evidence and explicitly records where earlier narratives weaken or fail.

</details>

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Why memory access is becoming a control problem** | [MESA](papers/2026/2608.10108.md) → [PMCoder](papers/2026/2608.06811.md) → [MAP-Graph](papers/2026/2608.10509.md) | Access now decides which structure to expose, how controller state conditions retrieval, and whether evidence is admissible—not merely which item is most similar. |
| **Where adaptive memory should live** | [Agent Memory Distillation](papers/2026/2608.07169.md) → [HyMeS](papers/2026/2608.09410.md) → [Materials-science lifelong memory](papers/2026/2608.11224.md) | Reusable memory can live as teacher experience, executable code-space policy, or external fact/skill artifacts; transfer depends on the consumer. |
| **Why recall is not enough to evaluate memory** | [Total Recall at What Cost?](papers/2026/2608.11879.md) → [Agent Skills Can Be Harmful](papers/2026/2608.11888.md) → [SkillJack](papers/2026/2608.03509.md) | A memory can be relevant yet too expensive, behaviorally counterproductive, or unsafe across derived artifacts. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**MESA** gives the cleanest new read-side result: the useful memory configuration is often **several views but not all views**.

**MAP-Graph** gives the strongest new trust-boundary decomposition: **read permission, inherited trust, and action sufficiency are different memory decisions**.

**Total Recall at What Cost?** gives the strongest evaluation correction: a dedicated memory system is **not automatically cheaper** than full history; lifecycle maintenance determines break-even.

Together they change the question from “how should the agent remember more?” to **“which state should reach this decision, under what constraints, and at what total cost?”**

</details>

## 🔥 Latest Papers

### [Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems](papers/2026/2608.11879.md)
`Evaluation & Analysis` · `semantic` `text` `general-agent` · **★★★★☆** · 2026-08-12

**AI take:** Dedicated memory is not automatically cheaper than resending history. The break-even point is a workload- and architecture-dependent lifecycle property, not a consequence of smaller retrieved context.

[Paper](https://arxiv.org/abs/2608.11879) · [Research note](papers/2026/2608.11879.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Memory benchmarks usually measure answer quality or payload size while ignoring ingest, reflection, consolidation, and retrieval model calls.

**Core mechanism.** Replay matched conversations through Mem0, Hindsight, Mastra Observational Memory, a ten-turn rolling window, and full history; meter end-to-end serving cost and compute sustained break-even against full history.

**Cost loop.** `conversation → native ingest/update → native retrieval → answer → billed lifecycle cost → break-even surface`

**Compared with.** Full-history resubmission and rolling-window prompting under matched workload/backbone settings where controllable.

**Evidence to remember.** Break-even spans **0–86 turns (Mastra OM), 0–342 (Mem0), 60–never (Hindsight)** across the measured grid; a simple depth/message-size model misses memory-system cost by **18–69%**.

**Open question.** Do these cost surfaces persist when ingest/reflection models run locally or much more cheaply than the answer model?

</details>

### [Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents](papers/2026/2608.11888.md)
`Evaluation & Analysis` · `procedural` `text` `general-agent` · **★★★★☆** · 2026-08-12

**AI take:** Topical relevance is a weak admission test for procedural memory. A skill can match the task yet impose the wrong implementation detail or a disproportionately expensive execution procedure.

[Paper](https://arxiv.org/abs/2608.11888) · [Research note](papers/2026/2608.11888.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A worse skill-guided run does not isolate the skill from the base agent/task/environment; a passing run can also hide large token/time regressions.

**Core mechanism.** Hold task/harness/model/environment fixed and compare a target skill with no skill or a semantically matched alternative; attribute differences from paired execution trajectories.

**Control loop.** `same task → alternative skill condition → matched trajectory/outcome/cost → differential attribution`

**Compared with.** SkillsBench / SWE-Skills-Bench outcome comparisons without mechanism-level matched attribution.

**Evidence to remember.** Among **307 confirmed cases**, Task-Implementation Fault is **86/125** functional cases; Excessive Procedure is **114/182** efficiency cases, larger than context-bloat explanations.

**Open question.** Can an online selector predict marginal skill effect before paying the cost of executing both alternatives?

</details>

### [The Sleeping Agent: What Gist-Based Context Compression Loses and Why](papers/2026/2608.11775.md)
`Write, Update & Consolidation` · `semantic` `text` `timeline` · **★★★☆☆** · 2026-08-12

**AI take:** Gist compression is selective forgetting. A generic abstraction prompt preserved entities/events while systematically deleting the temporal anchors that later “when?” questions needed.

[Paper](https://arxiv.org/abs/2608.11775) · [Code](https://github.com/kyrkewood/sleeping-agent) · [Research note](papers/2026/2608.11775.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Aggregate compression quality can hide a small but decision-critical semantic field being systematically erased.

**Core mechanism.** Diagnose Salience-Weighted Consolidation by content type, then change only the gist prompt to explicitly preserve dates/times.

**Memory loop.** `history → salience tiers → gist abstraction → compressed context`; the intervention changes only the abstraction contract.

**Compared with.** Truncation, sliding-window summarization, full context on a limited subset, and the same SWC pipeline without temporal protection.

**Evidence to remember.** Temporal-expression preservation rises **3.05% → 62.39% (~20×)** and temporal judge accuracy improves **+0.314**, while entity/event preservation barely changes.

**Open question.** Which other low-volume fields—authority, identifiers, provenance, constraints—are silently deleted by mainstream memory compressors?

</details>

### [Towards a Formal Definition of Agent Memory: Basis, Span, Optimality, and the Sequential Memory Problem](papers/2026/2608.11654.md)
`Evaluation & Analysis` · `general-agent` · **★★★☆☆** · 2026-08-12

**AI take:** A useful attempt to separate the **stored event basis** from the knowledge it can generate and to compare memory under a capacity budget. The current value is conceptual; empirical validation is still illustrative.

[Paper](https://arxiv.org/abs/2608.11654) · [Research note](papers/2026/2608.11654.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Memory systems use incompatible representations/metrics, making “optimal memory” hard to state independently of implementation.

**Core mechanism.** Define stored events as a basis, a generation operator as the memory span, capacity-constrained utility as a frontier, and sequential writing as an MDP with delayed query-time reward.

**Compared with.** Representative memory systems are mapped into one formal write/read framework rather than empirically outperformed.

**Evidence to remember.** Under decomposable span assumptions, capacity-constrained writing reduces to weighted maximum coverage with the classical greedy **(1−1/e)** guarantee; cross-event synergy breaks that result.

**Open question.** Does the proposed capacity frontier predict real system quality once answer-time composition and reasoner error matter?

</details>

### [MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows](papers/2026/2608.10509.md)
`Retrieval & Access` · `semantic` `graph` `general-agent` · **★★★★☆** · 2026-08-11

**AI take:** The contribution is not “memory as a graph.” It separates **may read**, **how much inherited trust**, and **is sufficient for this action** into different memory-control boundaries.

[Paper](https://arxiv.org/abs/2608.10509) · [Research note](papers/2026/2608.10509.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Relevant derived evidence can inherit restrictions not visible in its local text/metadata.

**Core mechanism.** Semantic candidates → hard `CanRead` filtering → `semantic × recursive path trust` reranking → action-risk gate, with lineage-aware revocation.

**Memory loop.** `write provenance → retrieve candidates → enforce eligibility → propagate trust → gate action → retain lineage`

**Compared with.** Shared/isolated vector memory and a strong flat-provenance control that has rich local metadata but no recursive ancestry propagation.

**Evidence to remember.** Removing trust propagation lowers task success **94.96% → 87.37%** and changes the adverse-action rate **1.52% → 8.56%**; removing the permission filter makes conditional unauthorized access **100%** despite higher aggregate utility.

**Open question.** Do these boundaries still help over months-long workflows with real external actions rather than one synthetic four-agent round?

</details>

### [MESA: Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory](papers/2026/2608.10108.md)
`Retrieval & Access` · `episodic` `structured` `general-agent` · **★★★★☆** · 2026-08-10

**AI take:** Multi-memory should not mean route-to-one or read-everything. MESA's useful result is that the best query often needs **several structures but not all of them**.

[Paper](https://arxiv.org/abs/2608.10108) · [Research note](papers/2026/2608.10108.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** One structure loses complementary evidence; all structures add redundant/noisy context and cost.

**Core mechanism.** Build fixed summary/temporal/graph/vector/raw views, then learn an explicit query-adaptive subset selector and compose evidence from each selected native retriever.

**Memory loop.** `trajectory → five fixed views → subset selection → per-view retrieval → evidence composition → frozen answer model`

**Compared with.** AMA-Agent, route-to-one, all-five, zero-shot/random selection, and coarse domain/capability routing.

**Evidence to remember.** **57.0% route-to-one → 63.7% all-five / 18.7k tokens → 65.1% MESA / 11.0k tokens**; a coarse domain selector already reaches 64.4%.

**Open question.** How much of MESA's benefit survives when structures are continuously updated or the representation library is not hand-selected?

</details>

### [Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation](papers/2026/2608.09410.md)
`Memory Learning & Evolution` · `working` `procedural` `structured` `embodied` · **★★★★☆** · 2026-08-10

**AI take:** HyMeS makes a clean substrate split: reusable motor competence stays in VLA weights, while inspectable memory strategy lives in executable code and symbolic task state.

[Paper](https://arxiv.org/abs/2608.09410) · [Research note](papers/2026/2608.09410.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** End-to-end memory-augmented VLAs entangle motor learning with history-management logic and need demonstrations spanning combinatorial history states.

**Core mechanism.** A coding agent learns constraint-selection / event-verification / memory-update rules from development rollouts; at runtime symbolic state selects a differentiable constraint that steers frozen VLA denoising.

**Memory loop.** `execution feedback → code-space memory strategy → symbolic stage state → constraint-guided VLA action → multimodal completion check → state update`

**Compared with.** Same-weight reactive π0.5 and PrediMem on the corrected RoboMemArena protocol.

**Evidence to remember.** On the corrected 12-task protocol HyMeS reports **66.2% cumulative / 60.1% task success**, versus **52.5/41.3** for π0.5 and **61.7/45.6** for PrediMem.

**Open question.** Does code-space memory strategy transfer across robots/policies, or is it tightly coupled to one VLA and hand-designed state abstraction?

</details>

### [Muscle Memory for Agents: Compile not Merely Retrieve](papers/2026/2608.08995.md)
`Representation & Organization` · `procedural` `structured` `personalization` · **★★★☆☆** · 2026-08-10

**AI take:** Stable recurring intent may be better represented as **executable specialist capability** than text repeatedly retrieved into a general controller. Current evidence is synthetic and lacks a strong matched retrieval-vs-compilation baseline.

[Paper](https://arxiv.org/abs/2608.08995) · [Code](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/personalized-agent-swarms) · [Research note](papers/2026/2608.08995.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Recurrent user tasks repeatedly pay interpretation cost when remembered procedure is injected as text.

**Core mechanism.** Mine repeated patterns, compile them into quality-gated specialist mini-agents, and route matching future requests to the specialist.

**Compared with.** An unaugmented general assistant empirically; retrieval-centric procedural memory conceptually.

**Evidence to remember.** Specialists fire in 36/90 held-out synthetic scenarios and win **32/36 (88.9%)** of those comparisons.

**Open question.** Does compilation beat a strong matched retrieval-based skill system on real long-lived users?

</details>

### [Agent Memory Distillation: Training-Free Memory Transfer from Stronger to Weaker Agents](papers/2026/2608.07169.md)
`Memory Learning & Evolution` · `procedural` `structured` `general-agent` · **★★★★☆** · 2026-08-07

**AI take:** Teacher experience becomes useful to a smaller student when memory is decomposed to the **decision granularity and retrieval timing** the student can actually consume.

[Paper](https://arxiv.org/abs/2608.07169) · [Research note](papers/2026/2608.07169.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Raw strong-agent trajectories are too entangled/noisy to transfer directly to a weaker frozen agent at inference time.

**Core mechanism.** Distill teacher experience into workflow-, subtask-, and function-level memory, then expose each level proactively or reactively at the corresponding student decision point.

**Compared with.** The same students without transferred memory and flatter / mismatched memory granularity variants.

**Evidence to remember.** Across 4B–8B students, reported average gains are **+27.2pp AppWorld, +11.2pp BFCL V3, +3.4pp ToolSandbox**; subtask memory is the largest ablation contributor.

**Open question.** How robust is teacher memory when teacher experience or student capability shifts outside the training/task distribution?

</details>

### [PMCoder: Planning-Memory Coupling for Repository-Level Code Repair](papers/2026/2608.06811.md)
`Retrieval & Access` · `episodic` `structured` `coding` · **★★★★☆** · 2026-08-07

**AI take:** The interesting mechanism is **bidirectional planner↔memory coupling**: plan phase shapes retrieval, while memory trajectory statistics can trigger stuck detection and replanning.

[Paper](https://arxiv.org/abs/2608.06811) · [Research note](papers/2026/2608.06811.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Repository repair agents often retrieve memory independently of their current repair phase, while planners ignore signals that repeated memory-assisted execution is stuck.

**Core mechanism.** Phase-conditioned retrieval selects different memory evidence for planning/coding, and accumulated memory statistics feed back into stuck detection / replanning.

**Control loop.** `plan state → memory retrieval → code action → trajectory statistics → stuck detection → replan`

**Compared with.** Plan-only and memory-only variants under a factorial study.

**Evidence to remember.** The full system reports **+5.0pp on SWE-bench Verified**; the planner×memory interaction is about **+2.1pp**, supporting coupling beyond independent component gains.

**Open question.** Does the coupling survive domains without hand-designed repair phases and clearer execution-grounding ablations?

</details>

## ⭐ Design Anchors

These are **design points, not a ranking**. New papers do not automatically displace a durable anchor after one preprint cycle.

| Work | Why it is a useful design point |
|---|---|
| **[LeanMem](papers/2026/2608.03463.md)** | Heterogeneous evidence types with different lifecycle semantics. |
| **[V-Mem](papers/2026/2608.01543.md)** | Modality-routed, structure-aware access rather than one universal similarity operation. |
| **[PMCoder](papers/2026/2608.06811.md)** | Bidirectional controller↔memory coupling: phase-conditioned retrieval plus memory-driven replanning. |
| **[MemoryCPT](papers/2026/2608.04843.md)** | Learned construction + read-time compression under an explicit cost × quality objective. |
| **[RoMeRL](papers/2026/2608.02508.md)** | Reduced-order semantic utility state for runtime memory learning. |
| **[Scrub Jay Memory](papers/2026/2608.04746.md)** | Per-memory future utility as a retention / forgetting abstraction. |
| **[AuthMem-Bench](papers/2026/2608.01679.md)** | Authority/provenance preservation as a memory correctness invariant. |
| **[SkillJack](papers/2026/2608.03509.md)** | Provenance and revocation across experience→skill transformation. |

<details><summary><strong>How these anchors fit together</strong></summary>

A useful current stack is:

`construction → representation → access → controller/consumer coupling → lifecycle policy → cost → provenance / trust`

**LeanMem / V-Mem** ask which relations should survive representation and be exposed by access. **PMCoder** asks how memory participates in the controller loop. **MemoryCPT / RoMeRL / Scrub Jay** ask which lifecycle decisions deserve optimization and feedback. **AuthMem-Bench / SkillJack** ask which correctness invariants survive memory transformations.

**MESA, MAP-Graph, Total Recall, HyMeS, and Agent Skills** are strong current candidates for future anchor changes, but the anchor set intentionally changes more slowly than Latest Papers.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Current argument |
|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | **Anchor:** LeanMem. **Strongest signal:** representation earns complexity only when it exposes a useful lifecycle/validity relation; PGMem shows persona representation is more load-bearing than graph structure alone. **Unresolved:** which distinctions survive matched access budgets? **Next:** factorial flat-vs-typed/graph tests. |
| **[Retrieval & Access](categories/retrieval-access.md)** | **Anchors:** V-Mem, PMCoder. **Strongest signal:** access now chooses structure, controller-conditioned evidence, and admissibility. **Unresolved:** can one policy do all three without hand-designed routing? **Next:** acting-agent tests with frozen evidence/base model. |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | **Anchor:** Scrub Jay; MERIT/Sleeping Agent are counter-discipline. **Strongest signal:** lifecycle transforms need explicit utility and field-preservation evidence. **Unresolved:** can systems discover what must be preserved? **Next:** longitudinal field-level preservation + matched append-only baselines. |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | **Anchors:** MemoryCPT, RoMeRL; AMD/HyMeS widen the substrate. **Strongest signal:** useful adaptive state may live in learned policy, teacher memory, code, or external artifacts depending on the consumer. **Unresolved:** compatibility under model/task shift. **Next:** freeze memory, vary consumer. |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | **Anchors:** AuthMem-Bench, SkillJack. **Strongest signal:** recall misses lifecycle cost, procedural marginal effect, authority, and read/action correctness. **Unresolved:** a deployment-predictive evaluation vector. **Next:** matched multi-session tool use with cost + provenance + counterfactual memory controls. |

<details><summary><strong>Scope, ratings, and what is intentionally excluded</strong></summary>

A work belongs here when memory **persists or manages information across interaction/reasoning steps and materially affects a language or multimodal agent's future behavior**. Generic RAG, KV-cache optimization, long-context modeling, or non-agent recurrent memory is excluded unless persistent agent memory is central.

**Relevance and importance are separate.** Relevance asks whether the paper belongs; importance asks whether it changes a design point or is worth prioritizing. ★★★★★ is field-shaping; ★★★★☆ notable; ★★★☆☆ useful; ★★☆☆☆ peripheral; ★☆☆☆☆ archival.

Numeric results are surfaced only when they materially change interpretation. Full research notes carry richer evidence, caveats, and provenance.

</details>

---

**Agent Memory Radar is a living bibliography, but the primary reading interface is the research map — not the daily stream.**
