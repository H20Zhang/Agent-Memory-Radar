# 🧠 Agent Memory Radar

**A living research map of memory for AI agents.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical research notes and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-12 · [Research compactions](#-research-compactions) · [Latest papers](#-latest-papers) · [Browse by research problem](categories/README.md)

## 🧭 Research Compactions

If you only have a few minutes, **start here**. The archive deliberately becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

### Recent Month · Weekly

**[2026-W32 · Memory becomes a controlled state problem](digests/weekly/2026-W32.md)**  
The week strengthened three shifts: memory policy now has a **state-dimension problem** rather than only a retrieval problem; heterogeneous evidence is receiving different lifecycle semantics; and trust must survive memory transformations, not only the source record. RoMeRL is the key correction to naive memory-policy scaling, while SkillJack extends provenance from stored records to derived skills.

**Suggested reading:** RoMeRL → MemoryCPT → LeanMem → SkillJack → AuthMem-Bench / MAFIA.  
[Read the full weekly synthesis →](digests/weekly/2026-W32.md)

### Recent Quarter · Monthly

**[2026-08 · Rolling research map through Aug 12](digests/monthly/2026-08.md)**  
The current August map is more specific than “agent memory is becoming state management.” It now points to four control boundaries: **typed evidence**, **structure-aware access**, **bounded learned policy state**, and **provenance across artifact lineage**. V-Mem supplies a real access-interface result; RoMeRL challenges one utility variable per stored trajectory; SkillJack shows why revocation must propagate through derived skills.

A more tentative early signal is that mature procedural memory may sometimes be **compiled into executable capability** rather than retrieved as text, but current evidence is not yet strong enough to treat that as a trend.

[Explore the rolling August research map →](digests/monthly/2026-08.md)

### All Years · Yearly

**[2026 · Rolling, incomplete year-to-date map](digests/yearly/2026.md)**  
Coverage currently begins on **2026-08-02**, so this is deliberately not presented as a full-year reconstruction. Within that narrow window, the strongest durable hypothesis is that agent memory is becoming a **controlled state system** where representation, access, policy state, cost, authority, and provenance must be co-designed.

[Explore the 2026 rolling map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** preserves local changes and disagreements while they are fresh. **Monthly** compresses several weeks into design-space movement. **Yearly** keeps only shifts that survive broader evidence and explicitly records where earlier narratives weaken or fail.

</details>

## 🚀 Start Here

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Why memory needs more than one representation or access operator** | [LeanMem](papers/2026/2608.03463.md) → [V-Mem](papers/2026/2608.01543.md) → [Activity Frames](papers/2026/2608.05784.md) | How lifecycle semantics, structural relations, and deterministic compilation challenge the default “one flat store + top-k” abstraction. |
| **How memory becomes a learned control problem** | [MemoryCPT](papers/2026/2608.04843.md) → [RoMeRL](papers/2026/2608.02508.md) → [Scrub Jay Memory](papers/2026/2608.04746.md) | Why memory policy needs explicit objectives, but also a carefully chosen feedback-bearing state rather than one adaptive variable per stored item. |
| **Why persistent memory changes correctness and security** | [AuthMem-Bench](papers/2026/2608.01679.md) → [MAFIA](papers/2026/2608.03844.md) → [SkillJack](papers/2026/2608.03509.md) | Why semantic fidelity is insufficient once authority, poisoning, transformation, and revocation can persist across sessions and artifacts. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**LeanMem** gives the cleanest current representation/lifecycle abstraction: heterogeneous evidence should not share one universal memory contract.

**RoMeRL** gives the strongest current correction to learned memory scaling: the evidence pool may grow without letting the learned utility state grow with every trajectory.

**SkillJack** gives the strongest current lineage warning: experience can be transformed into a new artifact whose risk and lifetime no longer match its source record.

Together they frame the current radar thesis: **agent memory is increasingly a typed, policy-controlled state system whose correctness includes both utility and provenance across transformations.**

</details>

## 🔥 Latest Papers

### [Muscle Memory for Agents: Compile not Merely Retrieve](papers/2026/2608.08995.md)
`Representation & Organization` · `procedural` `structured` `personalization` · **★★★☆☆** · 2026-08-10

**AI take:** The design idea is provocative: stable recurring intent may be better represented as **executable specialist capability** than as text repeatedly retrieved into a general controller. But the evidence is synthetic and does not isolate compilation against a strong matched retrieval-based procedural-memory baseline.

[Paper](https://arxiv.org/abs/2608.08995) · [Code](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/personalized-agent-swarms) · [Research note](papers/2026/2608.08995.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Recurring user tasks still incur repeated prompting when remembered preferences are retrieved as context and reinterpreted by a generic assistant.

**Core mechanism.** Mine repeated task patterns from conversation history, compile them into quality-gated mini-agents, keep behavioral style separately, and route matching future requests to a specialist.

**Control loop.** `history → pattern mining → specialist compilation → trigger matching → specialist execution`

**Compared with.** An unaugmented general assistant empirically; conceptually, retrieval-centric procedural memory interpreted by one general controller.

**Evidence to remember.** Specialists fire in 36/90 held-out synthetic scenarios and win **32/36 (88.9%)** of those comparisons; similar-scenario activation is **72%** and different-domain false positives are **20%**.

**Open question.** Does compilation still win when compared with a strong retrieval-based skill system using the same specialist prompts, models, and inference budget on real long-lived users?

</details>

### [Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay](papers/2026/2608.05784.md)
`Representation & Organization` · `episodic` `structured` `timeline` · **★★★☆☆** · 2026-08-06

**AI take:** The interesting result is not another retriever. High-volume personal activity can sometimes be **compiled deterministically before retrieval**, preserving evidence pointers and auditability while avoiding an LLM in the construction path.

[Paper](https://arxiv.org/abs/2608.05784) · [Code](https://github.com/nossa-y/activity-frames) · [Research note](papers/2026/2608.05784.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Raw desktop activity is too verbose; free-form LLM summaries are compact but can be lossy, costly, and difficult to audit.

**Core mechanism.** Deterministically compile passive screen events into chronological Activity Frames with application/site, time, input volume, measured observations, and evidence pointers.

**Memory loop.** `capture → deterministic frame compilation → preserve evidence/gaps → retrieve/replay`

**Compared with.** Raw activity rows and LLM-generated summaries.

**Evidence to remember.** Across eight evaluated days, the strongest reported setting reaches **98.4% QA accuracy**, versus **82.1–91.1%** for raw rows and **66.1–80.4%** for LLM summaries; compilation is reported at **68 ms**.

**Open question.** Does deterministic compilation remain effective across months, devices, users, and changing applications?

</details>

### [MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off](papers/2026/2608.04843.md)
`Memory Learning & Evolution` · `episodic` `semantic` `structured` · **★★★★☆** · 2026-08-05

**AI take:** MemoryCPT turns memory into an **end-to-end systems optimization problem**: both write-time construction and query-time compression become trainable under an explicit answer-quality / inference-cost objective.

[Paper](https://arxiv.org/abs/2608.04843) · [Research note](papers/2026/2608.04843.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Multi-stage memory pipelines repeatedly invoke LLMs for construction, retrieval, and summarization without jointly optimizing their cost-quality trade-off.

**Core mechanism.** QAD learns episodic/semantic construction operations; QAR combines dense+sparse retrieval with GRPO-trained query-aware compression before a frozen answer model.

**Memory loop.** `history → learned construction → episodic/semantic stores → fused retrieval → learned compression → answer`

**Compared with.** LightMem/MemoryOS-style modular systems, learned memory-policy approaches such as Memory-R1, and cost-aware baselines such as BudgetMem.

**Evidence to remember.** In the reported aggregate ablation, removing QAR raises cost from **5.02 → 11.10** while F1 falls **0.482 → 0.309**.

**Open question.** Do the learned policies transfer beyond conversational memory-QA to agents acting through tools and environments?

</details>

### [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](papers/2026/2608.04746.md)
`Write, Update & Consolidation` · `episodic` `structured` `timeline` · **★★★★☆** · 2026-08-05

**AI take:** The clean abstraction is **per-memory future utility**: a durable preference and an expiring appointment should not share one global recency function.

[Paper](https://arxiv.org/abs/2608.04746) · [Research note](papers/2026/2608.04746.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Similarity retrieval ignores time; global recency assumes every memory ages in the same way.

**Core mechanism.** Store What-Where-When context plus perishability and a utility horizon per memory; combine semantic relevance, contextual fit, and time-dependent utility during retrieval.

**Memory loop.** `write structured episode → estimate local utility horizon → retrieve with semantic + temporal utility → revise / decay`

**Compared with.** Mem0, dense embedding retrieval, and global recency / temporal-prompt baselines.

**Evidence to remember.** On EventQA-64k, the highlighted setting reports **+2.66 F1 over Mem0** and **+3.09 over Qwen3-Embedding-4B**; removing decay degrades the controlled metric by roughly **5.7×**.

**Open question.** Does per-memory utility still help when conflict resolution, provenance, and fact consolidation matter as much as temporal expiry?

</details>

### [SkillJack: Persistent Skill Backdoors in Self-Evolving Agents](papers/2026/2608.03509.md)
`Evaluation & Analysis` · `procedural` `structured` · **★★★★☆** · 2026-08-04

**AI take:** The important failure is not merely another poisoned record. Experience can be **transformed into a descendant skill**, become less inspectable, and survive deletion of its source. That makes provenance and revocation a lineage property.

[Paper](https://arxiv.org/abs/2608.03509) · [Code](https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/SkillJack) · [Research note](papers/2026/2608.03509.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Self-evolving agents turn experience into reusable skills, so defending only the source memory record misses security failures created by the transformation itself.

**Core mechanism.** Poison experience, let the unmodified experience-to-skill pipeline extract a skill, then measure sanitization whitewashing, cross-layer promotion, and persistence after source deletion.

**Attack loop.** `poisoned experience → skill extraction → separate skill artifact → later routing → behavior proxy`

**Compared with.** Retrieval-time memory poisoning and direct-context injection, where the malicious source record remains the artifact that must be surfaced.

**Evidence to remember.** On SkillX, an LLM judge flags **98.5%** of poisoned trajectories but only **11.4%** of derived skills; **80.0%** of matched skill-mediated triggers persist after source deletion. The important caveat is a **20.0% clean-task trigger rate** and that most downstream ASR is a routing-level proxy.

**Open question.** Can a practical agent preserve provenance and transitive revocation across arbitrary experience→summary→skill→policy transformations without making self-evolution unusably expensive?

</details>

### [MAFIA: Memory Attacks via Fully Indirect Access for LLM Agents](papers/2026/2608.03844.md)
`Evaluation & Analysis` · `semantic` `text` · **★★★★☆** · 2026-08-04

**AI take:** Persistent memory turns prompt injection into a **state-integrity problem**: malicious content can be planted through ordinary interactions and influence a later benign-looking query after the original context is gone.

[Paper](https://arxiv.org/abs/2608.03844) · [Code](https://github.com/JiamingChen1234/MAFIA) · [Research note](papers/2026/2608.03844.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A malicious payload can enter memory now, persist across sessions, and be retrieved into an apparently normal future interaction.

**Core mechanism.** Black-box probes estimate where malicious memory should land in retrieval space; factual-looking cloaks aim to pass write-time auditing while preserving later retrieval and behavioral influence.

**Attack loop.** `probe retriever → craft cloak → write normally → persist → retrieve on future query`

**Compared with.** Ordinary prompt injection and query-only memory attacks such as MINJA.

**Evidence to remember.** MAFIA reports attack-success rates up to **90.7%**; the strongest tested write-time audit catches at most **7.4%** of crafted attacks in the highlighted setting.

**Open question.** How much of the attack survives typed, provenance-constrained, graph, or hierarchical memory architectures?

</details>

### [LeanMem: Simple and Efficient Long-Term Memory for LLM Agents](papers/2026/2608.03463.md)
`Representation & Organization` · `episodic` `semantic` `structured` `timeline` · **★★★★☆** · 2026-08-04

**AI take:** The contribution is not “three stores.” It is **heterogeneous lifecycle semantics**: stable profile facts, evolving events, and source-grounded records should not share one write/update/read contract.

[Paper](https://arxiv.org/abs/2608.03463) · [Research note](papers/2026/2608.03463.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Long-term histories mix facts with different temporal dynamics and fidelity requirements; one universal summary/vector store either wastes context or destroys needed detail.

**Core mechanism.** Filter low-value dialogue, route retained evidence into profile/event/record memory, evolve only temporal event memory, and plan retrieval using memory-type and token budgets.

**Memory loop.** `filter → classify evidence type → route to typed stores → selectively evolve → compose query-specific evidence`

**Compared with.** SimpleMem, LightMem, MemoryOS, and A-MEM-style systems.

**Evidence to remember.** On LoCoMo and LongMemEval-S, reported gains over the strongest memory baseline reach up to **5.54** and **15.07 points** depending on backbone; heterogeneous storage is the largest reported ablation contributor.

**Open question.** How brittle is routing when evidence changes type, conflicts, or drifts over months of interaction?

</details>

### [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory](papers/2026/2608.02508.md)
`Memory Learning & Evolution` · `episodic` `procedural` `structured` · **★★★★☆** · 2026-08-03

**AI take:** RoMeRL's important claim is about **what gets a learned utility**, not just how to train it: a growing evidence pool need not create a growing feedback-bearing state. The caveat is equally important—it reduces exposure to bad credit assignment; it does not solve causal attribution.

[Paper](https://arxiv.org/abs/2608.02508) · [Code](https://github.com/YOUNG-fnxm/RoMeRL) · [Research note](papers/2026/2608.02508.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Trajectory-indexed memory RL adds a new utility variable for every experience while bundle-level outcome rewards can reinforce irrelevant co-retrieved memories—the Memory-Reward Trap.

**Core mechanism.** Keep four persistent semantic coordinates per task: success/failure × consolidated/adaptive. Replace their trajectory contents over time while retaining coordinate-level utility state.

**Control loop.** `trajectory → semantic coordinate → bounded active state → similarity + utility retrieval → outcome reward → coordinate update`

**Compared with.** MemRL-style trajectory-indexed utility learning, plus MemP/RAG/Mem0 under matched interaction budgets.

**Evidence to remember.** Macro success is **0.862 vs 0.830** for MemRL; on OS, Cold-Q drops to **9.0% vs 44.9%**, feedback density rises **4.96 → 29.93**, memory shrinks **45K → 7K**, and LLM calls fall **570K → 450K**.

**Open question.** Is four-coordinate semantic state a transferable abstraction, or mainly a strong regularizer for reusable tasks with binary outcomes?

</details>

### [When Memory Becomes Authority: Benchmarking Authorization Collapse in Agent Memory](papers/2026/2608.01679.md)
`Evaluation & Analysis` · `semantic` `structured` · **★★★★☆** · 2026-08-03

**AI take:** The paper attacks a foundational assumption: a memory can preserve **what was said** while erasing **who was authorized to say it**, making a semantically faithful summary behaviorally unsafe.

[Paper](https://arxiv.org/abs/2608.01679) · [Research note](papers/2026/2608.01679.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Consolidation optimizes semantic retention, but acting agents also need source authority and provenance constraints to survive compression.

**Core mechanism.** Construct paired histories with identical claims/tasks but different source authority, test whether consolidation preserves that distinction, then persist an authority label as a mitigation.

**Behavior loop.** `role-labeled history → consolidate → read claim + authority → choose downstream action`

**Compared with.** The implicit baseline assumption that semantically faithful memory is automatically behaviorally faithful.

**Evidence to remember.** Authority collapse appears in **48/49** tested configurations; collapsed memories produce a mean **50.3% unauthorized-action rate**. Persisting authority labels reduces the mitigation setting from **16.9% → 0.0%** unauthorized actions with benign-task success essentially unchanged.

**Open question.** How should real memory represent delegation, revocation, conflicting authority, and organizational hierarchy over long horizons?

</details>

### [V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory](papers/2026/2608.01543.md)
`Retrieval & Access` · `episodic` `multimodal` `timeline` · **★★★★☆** · 2026-08-02

**AI take:** The headline is multimodal retrieval, but the decisive result is **structural**: same-round binding supplies almost all of the major ablation gain. The generated query anchor is secondary. This is stronger evidence for a richer access interface than for another universal embedding trick.

[Paper](https://arxiv.org/abs/2608.01543) · [Code](https://github.com/Dingyi-Kang/V-Mem) · [Research note](papers/2026/2608.01543.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Multimodal memory has both a modality gap and a similarity–relevance gap: the nearest text/image item may not be the evidence that answers the query.

**Core mechanism.** Preserve chronological rounds with separate text/image lanes, route by query and target modality, cross modalities through shared-round identity, optionally generate a query-side anchor, and include neighboring rounds.

**Memory loop.** `append raw round → modality-specific indexes + round binding → route → lane retrieval → structural cross-modal bridge → answer context`

**Compared with.** Omni-SimpleMem, M2A, and A-Mem under matched answer backbones/encoders.

**Evidence to remember.** On Mem-Gallery, vanilla retrieval is **0.680**, +routing **0.689**, +shared-round matching **0.818**, and +generated anchors **0.825**. With gpt-4o-mini the full system reports **0.825 vs 0.561** for the strongest baseline.

**Open question.** Does the structural advantage survive multimodal agents that act through tools/environments, where modality needs are less obvious than in history QA?

</details>

## ⭐ Design Anchors

These are **design points, not a ranking**.

| Work | Why it is a useful design point |
|---|---|
| **[LeanMem](papers/2026/2608.03463.md)** | Heterogeneous evidence types with different lifecycle semantics. |
| **[V-Mem](papers/2026/2608.01543.md)** | Modality-routed, structure-aware access rather than one universal similarity operation. |
| **[Activity Frames](papers/2026/2608.05784.md)** | Deterministic, auditable memory compilation. |
| **[MemoryCPT](papers/2026/2608.04843.md)** | Learned construction + read-time compression under an explicit cost × quality objective. |
| **[RoMeRL](papers/2026/2608.02508.md)** | Reduced-order semantic utility state for runtime memory learning. |
| **[Scrub Jay Memory](papers/2026/2608.04746.md)** | Per-memory future utility as a retention / forgetting abstraction. |
| **[AuthMem-Bench](papers/2026/2608.01679.md)** | Authority/provenance preservation as a memory correctness invariant. |
| **[SkillJack](papers/2026/2608.03509.md)** | Provenance and revocation across experience→skill transformation. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

A useful current stack is:

`construction → representation → access → lifecycle policy → cost / utility → provenance / trust`

**Activity Frames / LeanMem** ask what state should be compiled or typed before retrieval. **V-Mem** asks which read operators exploit that structure. **MemoryCPT / RoMeRL / Scrub Jay** ask what memory decisions deserve optimization and feedback. **AuthMem-Bench / SkillJack** ask which correctness invariants must survive state transformations.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

| Research problem | Current argument |
|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | **Anchors:** LeanMem, Activity Frames. **Strongest signal:** evidence with different temporal/fidelity semantics should not share one lifecycle contract. **Unresolved:** are typed stores intrinsically better or just benefiting from extra routing/preprocessing? **Next evidence:** matched flat-vs-typed ablations over months-long conflicting histories. |
| **[Retrieval & Access](categories/retrieval-access.md)** | **Anchor:** V-Mem. **Strongest signal:** structural relations can dominate cross-modal similarity. **Unresolved:** which access operators generalize beyond modality heuristics? **Next evidence:** acting-agent tests that vary access operators while holding memory content/controller fixed. |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | **Anchor:** Scrub Jay Memory. **Strongest signal:** retention is becoming an explicit per-memory utility decision. **Unresolved:** can forgetting save cost without deleting provenance/conflict history? **Next evidence:** end-to-end lifecycle evaluation with update, conflict, provenance, and cost. |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | **Anchors:** MemoryCPT, RoMeRL. **Strongest signal:** memory policy is learnable, but its feedback-bearing state must be carefully bounded. **Unresolved:** causal credit and transfer. **Next evidence:** cross-domain policy freeze/transfer plus explicit marginal-memory attribution tests. |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | **Anchors:** AuthMem-Bench, SkillJack; MAFIA is complementary. **Strongest signal:** correctness includes authority, persistent-state integrity, and descendant lineage. **Unresolved:** how to preserve transitive provenance/revocation cheaply. **Next evidence:** consequential multi-session tool-use benchmarks with auditable artifact lineage. |

<details>
<summary><strong>Scope, ratings, and what is intentionally excluded</strong></summary>

A work belongs here when memory **persists or manages information across interaction or reasoning steps and materially affects an agent's future behavior**. Generic RAG, KV-cache optimization, or long-context work is excluded unless persistent agent memory is central.

**Relevance and importance are separate.** Relevance asks whether the paper belongs in the radar; importance asks whether it changes a design point or is worth prioritizing. ★★★★★ is field-shaping; ★★★★☆ notable; ★★★☆☆ useful; ★★☆☆☆ peripheral; ★☆☆☆☆ archival.

Numeric results are surfaced only when they materially change interpretation. The full research notes carry richer evidence, caveats, and provenance.

</details>

---

**Agent Memory Radar is a living bibliography, but the primary reading interface is the research map — not the daily stream.**
