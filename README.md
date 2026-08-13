# 🧠 Agent Memory Radar

**A living research map of memory for AI agents.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-12 · [Research compactions](#-research-compactions) · [Latest papers](#-latest-papers) · [Browse by research problem](categories/README.md)

## 🧭 Research Compactions

If you only have a few minutes, **start here**. The archive deliberately becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

### Recent Month · Weekly

**[2026-W32 · Structure only matters when control can use it](digests/weekly/2026-W32.md)**  
The week now supports a sharper thesis than “memory is becoming structured.” RoMeRL shows that feedback-bearing state should stay bounded; PMCoder shows that planner state can condition retrieval and memory can trigger replanning; AMD shows that teacher memory transfers better when task/subtask/function granularity matches a weak student's decisions. MERIT is the useful counterexample: extra typing/polarity is not reliably better than untyped dynamic retrieval.

**Suggested reading:** PMCoder → RoMeRL → Agent Memory Distillation → MemoryCPT → SkillJack.  
[Read the full weekly synthesis →](digests/weekly/2026-W32.md)

### Recent Quarter · Monthly

**[2026-08 · Rolling research map through Aug 12](digests/monthly/2026-08.md)**  
The August map now points to four control boundaries: **relation-aware representation/access**, **memory↔controller coupling**, **bounded learned policy state**, and **provenance across artifact lineage**. The new correction is important: structure is not intrinsically valuable; it needs a downstream decision boundary that exploits it.

[Explore the rolling August research map →](digests/monthly/2026-08.md)

### All Years · Yearly

**[2026 · Rolling, incomplete year-to-date map](digests/yearly/2026.md)**  
Coverage begins on **2026-08-02**, so this is not a full-year reconstruction. Within this narrow window, the strongest current hypothesis is that agent memory is becoming a **controlled state system whose representation, access operator, controller state, lifecycle policy, and trust semantics must be co-designed**.

[Explore the 2026 rolling map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes and disagreements while they are fresh. **Monthly** compresses several weeks into design-space movement. **Yearly** keeps only shifts that survive broader evidence and explicitly records where earlier narratives weaken or fail.

</details>

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Why memory needs more than one access contract** | [LeanMem](papers/2026/2608.03463.md) → [V-Mem](papers/2026/2608.01543.md) → [PMCoder](papers/2026/2608.06811.md) | Typed lifecycle semantics matter when the access interface preserves useful relations or controller state. |
| **How memory becomes a learned / transferred control problem** | [MemoryCPT](papers/2026/2608.04843.md) → [RoMeRL](papers/2026/2608.02508.md) → [Agent Memory Distillation](papers/2026/2608.07169.md) | Memory policy needs an objective, a bounded feedback-bearing state, and a representation that the consumer model can operationalize. |
| **Why persistent memory changes correctness and security** | [AuthMem-Bench](papers/2026/2608.01679.md) → [MAFIA](papers/2026/2608.03844.md) → [SkillJack](papers/2026/2608.03509.md) | Semantic fidelity is insufficient once authority, poisoning, transformation, and revocation persist across sessions and artifacts. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**PMCoder** gives the clearest current evidence that memory and controller state should be co-designed rather than placed side by side.

**RoMeRL** gives the strongest correction to learned-memory scaling: the evidence pool may grow without letting feedback-bearing utility state grow with every trajectory.

**SkillJack** gives the strongest lineage warning: experience can be transformed into a descendant artifact whose risk and lifetime no longer match its source record.

Together they frame the current radar thesis: **memory is becoming controller-coupled state, not simply a better retrieval store.**

</details>

## 🔥 Latest Papers

### [Muscle Memory for Agents: Compile not Merely Retrieve](papers/2026/2608.08995.md)
`Representation & Organization` · `procedural` `structured` `personalization` · **★★★☆☆** · 2026-08-10

**AI take:** Stable recurring intent may sometimes be better represented as **executable specialist capability** than as text repeatedly retrieved into a general controller. But the evidence is synthetic and does not isolate compilation against a strong matched retrieval-based procedural-memory baseline.

[Paper](https://arxiv.org/abs/2608.08995) · [Code](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/personalized-agent-swarms) · [Research note](papers/2026/2608.08995.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Recurring user tasks still incur repeated prompting when remembered preferences are retrieved and reinterpreted by a generic assistant.

**Core mechanism.** Mine repeated task patterns, compile them into quality-gated mini-agents, keep behavioral style separately, and route matching future requests to a specialist.

**Control loop.** `history → pattern mining → specialist compilation → trigger matching → specialist execution`

**Compared with.** An unaugmented general assistant empirically; conceptually, retrieval-centric procedural memory interpreted by one general controller.

**Evidence to remember.** Specialists fire in 36/90 held-out synthetic scenarios and win **32/36 (88.9%)** of those comparisons.

**Open question.** Does compilation still win against a strong retrieval-based skill system with matched prompts/models/budget on real long-lived users?

</details>

### [Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory](papers/2026/2608.07169.md)
`Memory Learning & Evolution` · `procedural` `structured` `general-agent` · **★★★★☆** · 2026-08-07

**AI take:** The important contribution is **memory as training-free teacher→student capability transfer**. Workflow/subtask/function hierarchy helps because each level is delivered at a different control point; the hierarchy is valuable only insofar as the weaker student can operationalize it.

[Paper](https://arxiv.org/abs/2608.07169) · [Research note](papers/2026/2608.07169.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Small agents cannot easily bootstrap useful self-memory because they generate too few successful trajectories; flat teacher experience can also mismatch student capability.

**Core mechanism.** Distill successful teacher trajectories into workflow, subtask, and function memories. Retrieve workflow+subtask guidance proactively at task start and function memory reactively after tool-call errors.

**Control loop.** `teacher successes → hierarchy → proactive task/subtask context + reactive function repair → small student`

**Compared with.** ReasoningBank, MemP, and SASM adapted to the **same teacher trajectories**.

**Evidence to remember.** Average absolute gains over zero-shot across four students are **+27.2pp AppWorld, +11.2pp BFCL V3, +3.4pp ToolSandbox**; Subtask memory is the largest contributor.

**Open question.** Does the transfer survive teacher/student distribution shift?

</details>

### [Coupling Planning with Episodic Memory in LLM Agents for Software Issue Resolution](papers/2026/2608.06811.md)
`Retrieval & Access` · `episodic` `structured` `coding` · **★★★★☆** · 2026-08-07

**AI take:** PMCoder's strongest result is not “memory helps coding.” It is **bidirectional memory↔controller coupling**: planner phase changes retrieval, and memory statistics can trigger replanning. The 2×2 interaction is the evidence to watch.

[Paper](https://arxiv.org/abs/2608.06811) · [Research note](papers/2026/2608.06811.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Planning and memory are often added independently, causing stale evidence, repeated failed edits, and verification based on the model's own completion claims.

**Core mechanism.** A hierarchical repair planner conditions episodic retrieval; edit/read/repetition statistics from memory drive stuck detection and replanning; reproduction verdicts ground verification when available.

**Control loop.** `plan phase → retrieval → actions/observations → memory statistics → stuck detection / replan`

**Compared with.** A harness-matched baseline plus plan-only and memory-only variants.

**Evidence to remember.** SWE-bench Verified improves **142.33 → 167.33 / 500 (+5.0pp)**. Plan-only is +1.3pp, memory-only +1.7pp, full +5.0pp; reported interaction **+2.1pp (p=.011)**.

**Open question.** Does bidirectional coupling still help when controller state is not a hand-designed phase machine?

</details>

### [Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay](papers/2026/2608.05784.md)
`Representation & Organization` · `episodic` `structured` `timeline` · **★★★☆☆** · 2026-08-06

**AI take:** High-volume personal activity can sometimes be **compiled deterministically before retrieval**, preserving evidence pointers and auditability while avoiding an LLM in the construction path.

[Paper](https://arxiv.org/abs/2608.05784) · [Code](https://github.com/nossa-y/activity-frames) · [Research note](papers/2026/2608.05784.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Raw desktop activity is verbose; free-form LLM summaries are compact but can be lossy, costly, and hard to audit.

**Core mechanism.** Deterministically compile passive screen events into chronological Activity Frames with application/site, time, input volume, measured observations, and evidence pointers.

**Memory loop.** `capture → deterministic frame compilation → preserve evidence/gaps → retrieve/replay`

**Compared with.** Raw activity rows and LLM-generated summaries.

**Evidence to remember.** Across eight evaluated days, the strongest setting reaches **98.4% QA accuracy**, versus **82.1–91.1%** for raw rows and **66.1–80.4%** for LLM summaries.

**Open question.** Does deterministic compilation remain effective across months, devices, users, and changing applications?

</details>

### [Causal Episodic Memory for Feedback-Driven Agent Repair](papers/2026/2608.05906.md)
`Write, Update & Consolidation` · `episodic` `structured` · **★★★☆☆** · 2026-08-06

**AI take:** The useful result is skeptical: **cross-query repair memory helps, but MERIT's extra typing/polarity is not reliably better than untyped dynamic retrieval**. More structure is not automatically better memory.

[Paper](https://arxiv.org/abs/2608.05906) · [Research note](papers/2026/2608.05906.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Repair agents discard finalized corrections, forcing later related tasks to rediscover similar fixes.

**Core mechanism.** Store positive oracle-verified corrections and negative final failed directions; classify failure type; retrieve only causally prior finalized episodes with hybrid dense+BM25 search.

**Memory loop.** `finalized episode → positive/negative memory → type-conditioned retrieval → next repair`

**Compared with.** Stateless iterative repair, untyped dynamic retrieval, and higher-cost Reflexion-style memory.

**Evidence to remember.** Spider improves **66.34% → 69.79%**, BIRD **47.35% → 48.44%** over stateless repair—but MERIT is **not reliably separated from untyped dynamic retrieval**.

**Open question.** Which memory structure is actually worth maintaining once a strong dynamic-retrieval baseline sees the same finalized experience?

</details>

### [MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off](papers/2026/2608.04843.md)
`Memory Learning & Evolution` · `episodic` `semantic` `structured` · **★★★★☆** · 2026-08-05

**AI take:** MemoryCPT turns memory into an **end-to-end systems optimization problem**: write-time construction and query-time compression become trainable under an explicit answer-quality / inference-cost objective.

[Paper](https://arxiv.org/abs/2608.04843) · [Research note](papers/2026/2608.04843.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Multi-stage memory pipelines repeatedly invoke LLMs without jointly optimizing cost and quality.

**Core mechanism.** QAD learns episodic/semantic construction; QAR combines dense+sparse retrieval with GRPO-trained query-aware compression before a frozen answer model.

**Memory loop.** `history → learned construction → episodic/semantic stores → fused retrieval → learned compression → answer`

**Compared with.** LightMem/MemoryOS, Memory-R1-style learned policy, and BudgetMem-style cost-aware baselines.

**Evidence to remember.** Removing QAR raises cost **5.02 → 11.10** while F1 falls **0.482 → 0.309** in the reported aggregate ablation.

**Open question.** Do learned policies transfer beyond conversational memory-QA to acting agents?

</details>

### [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](papers/2026/2608.04746.md)
`Write, Update & Consolidation` · `episodic` `structured` `timeline` · **★★★★☆** · 2026-08-05

**AI take:** The clean abstraction is **per-memory future utility**: a durable preference and an expiring appointment should not share one global recency function.

[Paper](https://arxiv.org/abs/2608.04746) · [Research note](papers/2026/2608.04746.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Similarity retrieval ignores time; global recency assumes every memory ages identically.

**Core mechanism.** Store What-Where-When context plus perishability and a utility horizon per memory; combine semantic relevance, contextual fit, and time-dependent utility at retrieval.

**Memory loop.** `write structured episode → estimate local utility horizon → retrieve with semantic + temporal utility → revise / decay`

**Compared with.** Mem0, dense embedding retrieval, and global-recency / temporal-prompt baselines.

**Evidence to remember.** EventQA-64k reports **+2.66 F1 over Mem0** and **+3.09 over Qwen3-Embedding-4B**; removing decay degrades the controlled metric by roughly **5.7×**.

**Open question.** Does per-memory utility still help when conflict/provenance/consolidation matter as much as temporal expiry?

</details>

### [SkillJack: Persistent Skill Backdoors in Self-Evolving Agents](papers/2026/2608.03509.md)
`Evaluation & Analysis` · `procedural` `structured` · **★★★★☆** · 2026-08-04

**AI take:** Experience can be **transformed into a descendant skill**, become less inspectable, and survive deletion of its source. That makes provenance and revocation a lineage property.

[Paper](https://arxiv.org/abs/2608.03509) · [Code](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/SkillJack) · [Research note](papers/2026/2608.03509.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Self-evolving agents turn experience into reusable skills, so defending only source memory misses failures created by the transformation itself.

**Core mechanism.** Poison experience, let the unmodified experience-to-skill pipeline extract a skill, then measure whitewashing, promotion, and persistence after source deletion.

**Attack loop.** `poisoned experience → skill extraction → separate skill artifact → later routing → behavior proxy`

**Compared with.** Retrieval-time memory poisoning and direct-context injection.

**Evidence to remember.** A judge flags **98.5%** of poisoned trajectories but only **11.4%** of derived skills; **80.0%** of matched skill-mediated triggers persist after source deletion.

**Open question.** Can practical agents preserve transitive provenance/revocation across arbitrary transformations?

</details>

### [MAFIA: Memory Attacks via Fully Indirect Access for LLM Agents](papers/2026/2608.03844.md)
`Evaluation & Analysis` · `semantic` `text` · **★★★★☆** · 2026-08-04

**AI take:** Persistent memory turns prompt injection into a **state-integrity problem**: malicious content can be planted through ordinary interactions and influence a later benign-looking query.

[Paper](https://arxiv.org/abs/2608.03844) · [Code](https://github.com/JiamingChen1234/MAFIA) · [Research note](papers/2026/2608.03844.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A malicious payload can enter memory now, persist, and be retrieved into an apparently normal future interaction.

**Core mechanism.** Black-box probes estimate where malicious memory should land; factual-looking cloaks aim to pass write-time auditing while preserving later retrieval and influence.

**Attack loop.** `probe retriever → craft cloak → write normally → persist → retrieve on future query`

**Compared with.** Ordinary prompt injection and query-only memory attacks such as MINJA.

**Evidence to remember.** Attack-success rates reach **90.7%**; the strongest tested write-time audit catches at most **7.4%** in the highlighted setting.

**Open question.** How much survives typed, provenance-constrained, graph, or hierarchical memory architectures?

</details>

### [LeanMem: Simple and Efficient Long-Term Memory for LLM Agents](papers/2026/2608.03463.md)
`Representation & Organization` · `episodic` `semantic` `structured` `timeline` · **★★★★☆** · 2026-08-04

**AI take:** The contribution is not “three stores.” It is **heterogeneous lifecycle semantics**: stable profile facts, evolving events, and source-grounded records should not share one write/update/read contract.

[Paper](https://arxiv.org/abs/2608.03463) · [Research note](papers/2026/2608.03463.md)

<details><summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Long-term histories mix facts with different temporal dynamics/fidelity requirements; one universal store either wastes context or destroys detail.

**Core mechanism.** Filter low-value dialogue, route evidence into profile/event/record memory, evolve only event memory, and plan retrieval using memory-type and token budgets.

**Memory loop.** `filter → classify evidence type → route to typed stores → selectively evolve → compose query-specific evidence`

**Compared with.** SimpleMem, LightMem, MemoryOS, and A-MEM-style systems.

**Evidence to remember.** Gains over the strongest memory baseline reach up to **5.54 points on LoCoMo** and **15.07 on LongMemEval-S**; heterogeneous storage is the largest ablation contributor.

**Open question.** How brittle is routing when evidence changes type, conflicts, or drifts over months?

</details>

## ⭐ Design Anchors

These are **design points, not a ranking**.

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

`construction → representation → access → controller coupling → lifecycle policy → cost / utility → provenance / trust`

**LeanMem** asks which state deserves different lifecycle semantics. **V-Mem** asks which access operators exploit preserved relations. **PMCoder** asks what happens when access and controller state form a feedback loop. **MemoryCPT / RoMeRL / Scrub Jay** ask what memory decisions deserve optimization and feedback. **AuthMem-Bench / SkillJack** ask which correctness invariants must survive state transformations.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Current argument |
|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | **Anchor:** LeanMem. **Strongest signal:** lifecycle semantics matter when representation exposes a useful downstream operation. **Unresolved:** is typed storage intrinsically useful or just extra preprocessing? **Next evidence:** matched flat-vs-typed ablations with the same access/controller budget. |
| **[Retrieval & Access](categories/retrieval-access.md)** | **Anchors:** V-Mem, PMCoder. **Strongest signal:** access can depend on preserved relations or controller state, not only similarity. **Unresolved:** which state variables generalize beyond modality and hand-designed phases? **Next evidence:** acting-agent tests that vary controller-conditioned access while holding evidence fixed. |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | **Anchor:** Scrub Jay; MERIT is counter-evidence. **Strongest signal:** lifecycle policy can matter, but extra typing is not automatically load-bearing. **Unresolved:** can richer writes beat strong append-only dynamic retrieval under matched budgets? **Next evidence:** longitudinal conflict/update tests with provenance and cost. |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | **Anchors:** MemoryCPT, RoMeRL; AMD adds cross-model transfer. **Strongest signal:** learned/teacher-derived memory needs both a sensible objective and a carefully chosen consumer/control state. **Unresolved:** causal credit and transfer under distribution shift. **Next evidence:** cross-domain freeze/transfer with marginal-memory attribution. |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | **Anchors:** AuthMem-Bench, SkillJack; MAFIA is complementary. **Strongest signal:** correctness includes authority, persistent-state integrity, and descendant lineage. **Unresolved:** how to preserve transitive provenance/revocation cheaply. **Next evidence:** consequential multi-session tool-use with auditable artifact lineage. |

<details><summary><strong>Scope, ratings, and what is intentionally excluded</strong></summary>

A work belongs here when memory **persists or manages information across interaction/reasoning steps and materially affects an agent's future behavior**. Generic RAG, KV-cache optimization, or long-context work is excluded unless persistent agent memory is central.

**Relevance and importance are separate.** Relevance asks whether the paper belongs; importance asks whether it changes a design point or is worth prioritizing. ★★★★★ is field-shaping; ★★★★☆ notable; ★★★☆☆ useful; ★★☆☆☆ peripheral; ★☆☆☆☆ archival.

Numeric results are surfaced only when they materially change interpretation. Full research notes carry richer evidence, caveats, and provenance.

</details>

---

**Agent Memory Radar is a living bibliography, but the primary reading interface is the research map — not the daily stream.**
