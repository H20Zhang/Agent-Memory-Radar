# 🧠 Agent Memory Radar

**A living research map of memory for AI agents.**  
Track new papers, understand what actually changed, and see how the field is moving — with skeptical AI research notes, visual explainers, and weekly/monthly/yearly synthesis.

**Last updated:** 2026-08-11 · [Research compactions](#-research-compactions) · [Latest papers](#-latest-papers) · [Browse by research problem](categories/README.md)

## 🧭 Research Compactions

If you only have a few minutes, **start here**. The archive deliberately becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

### Recent Month · Weekly

Weekly compactions preserve local research movement while it is still useful to inspect week by week.

**[2026-W32 · Memory becomes a state-management problem](digests/weekly/2026-W32.md)**  
Early-August memory work looks less like “better retrieval” and more like **stateful system design**: heterogeneous memory lifecycles, learned cost/quality policies, per-memory forgetting, and persistent-state trust boundaries. The main tension is whether richer memory structure and policy actually justify their complexity once cost, provenance, and matched baselines are considered.

**Suggested reading:** LeanMem → MemoryCPT → Scrub Jay Memory → AuthMem-Bench → MAFIA.  
[Read the full weekly synthesis →](digests/weekly/2026-W32.md)

> As new weeks arrive, this section keeps the meaningful weekly compactions from roughly the latest month. Older weekly reports remain in the repository but stop competing for homepage attention once monthly synthesis covers them.

### Recent Quarter · Monthly

Monthly compactions answer a slower question: **how should your mental model of agent memory change?**

**[2026-08 · Rolling research map](digests/monthly/2026-08.md)**  
Agent memory is beginning to look less like “RAG over conversation history” and more like a **queryable, mutable, policy-controlled state system**:

`representation → write/update policy → access → forgetting/compression → provenance & safety`

The current August map has three provisional clusters: **heterogeneous memory lifecycles**, **learned / utility-aware memory control**, and **persistent-state correctness**. The unresolved issue is whether these abstractions generalize beyond conversational memory-QA to long-lived, tool-using agents.

[Explore the rolling August research map →](digests/monthly/2026-08.md)

> This section keeps monthly maps from roughly the latest quarter. Older monthly reports remain available, while the durable public history is compressed again at yearly granularity.

### All Years · Yearly

Yearly compactions are the durable archive: **what survived the year, what weakened, which design points mattered, and what questions carried forward?**

**[2026 · Rolling year-to-date map](digests/yearly/2026.md)**  
Within current coverage, the strongest signal is a move from **retrieval-centric memory** toward explicit state-management decisions over representation, lifecycle policy, cost, provenance, and security.

This report is deliberately labeled rolling: radar coverage currently begins in August 2026, so it is not presented as a full-year reconstruction.

[Explore the 2026 year-to-date map →](digests/yearly/2026.md) · [Browse all compactions →](digests/README.md)

<details>
<summary><strong>How the time hierarchy works</strong></summary>

**Weekly** keeps local changes and disagreements while they are fresh. **Monthly** compresses several weeks into design-space movement. **Yearly** re-evaluates the period and preserves only durable shifts, defining design points, weakening ideas, evidence standards, and open problems entering the next year.

Lower-level reports are retained for provenance; they simply age out of the primary reading surface. Higher-level reports are also **re-grounded from canonical paper records**, not produced by recursively summarizing lower-level prose.

</details>

## 🚀 Start Here

Different papers matter depending on what you want to understand. These are deliberately short reading paths rather than exhaustive lists.

| If you want to understand… | Read in this order | What you should learn |
|---|---|---|
| **Why agent memory is more than a flat vector store** | [LeanMem](papers/2026/2608.03463.md) → [Activity Frames](papers/2026/2608.05784.md) → [Scrub Jay Memory](papers/2026/2608.04746.md) | How representation, construction, and lifecycle semantics become first-class design choices. |
| **How memory becomes an adaptive policy / optimizer** | [MemoryCPT](papers/2026/2608.04843.md) → [Scrub Jay Memory](papers/2026/2608.04746.md) → [LeanMem](papers/2026/2608.03463.md) | Which write, compression, retention, and forgetting decisions should be learned or utility-aware rather than fixed heuristics. |
| **Why persistent state changes safety and correctness** | [AuthMem-Bench](papers/2026/2608.01679.md) → [MAFIA](papers/2026/2608.03844.md) → [August map](digests/monthly/2026-08.md) | Why semantic correctness is insufficient once memory carries authority, provenance, and attack persistence across sessions. |

<details>
<summary><strong>If you only read three papers</strong></summary>

**LeanMem** gives the cleanest current systems abstraction: heterogeneous evidence should not share one universal memory lifecycle.

**MemoryCPT** adds the policy layer: memory construction and query-time compression can be optimized jointly under an explicit cost × quality objective.

**AuthMem-Bench** attacks a deeper assumption: a semantically faithful memory can still be behaviorally wrong if consolidation erases who had authority to make a claim.

Together they motivate the current radar thesis: **agent memory is becoming a typed, policy-controlled state system whose correctness includes utility, cost, provenance, and safety.**

</details>

## 🔥 Latest Papers

### [Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay](papers/2026/2608.05784.md)
`Representation & Organization` · `episodic` `structured` `timeline` · **★★★☆☆** · 2026-08-06

**AI take:** The interesting result is not another retriever. It is that high-volume personal activity can be **compiled deterministically before retrieval**, preserving evidence pointers and auditability while avoiding an LLM in the memory-construction path.

[Paper](https://arxiv.org/abs/2608.05784) · [Code](https://github.com/nossa-y/activity-frames) · [Research note](papers/2026/2608.05784.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Raw desktop activity is too verbose for an agent to consume directly; LLM summaries are compact but can be lossy, expensive, and difficult to audit.

**Core mechanism.** Deterministically compile passive screen events into typed chronological **Activity Frames** containing application/site, time, input volume, measured observations, and evidence pointers.

**Memory loop.** `capture events → compile frames → preserve evidence/gaps → retrieve/replay frames`

**Compared with.** Raw activity rows and LLM-generated activity summaries — not primarily another vector retriever.

**Evidence to remember.** Across eight evaluated days, the strongest reported setting reaches **98.4% QA accuracy**, versus **82.1–91.1%** for raw rows and **66.1–80.4%** for LLM summaries; compilation is reported at **68 ms**.

**Open question.** Does deterministic compilation remain effective across months, multiple devices, changing applications, and multiple users?

</details>

### [MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off](papers/2026/2608.04843.md)
`Memory Learning & Evolution` · `episodic` `semantic` `structured` · **★★★★☆** · 2026-08-05

**AI take:** MemoryCPT turns memory from a fixed retrieval pipeline into an **end-to-end systems optimization problem**: both write-time construction and query-time compression become trainable under an explicit answer-quality / inference-cost objective.

[Paper](https://arxiv.org/abs/2608.04843) · [Research note](papers/2026/2608.04843.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Multi-stage memory systems repeatedly invoke LLMs for construction, retrieval, and summarization, but quality and cost are usually optimized only indirectly.

**Core mechanism.** **QAD** learns episodic/semantic construction operations; **QAR** combines dense+sparse retrieval with GRPO-trained query-aware compression before a frozen answer model.

**Memory loop.** `history → learned construction → episodic/semantic stores → fused retrieval → learned compression → answer`

**Compared with.** Training-free modular systems such as LightMem/MemoryOS, learned memory-policy approaches such as Memory-R1, and explicitly cost-aware baselines such as BudgetMem.

**Evidence to remember.** In the reported aggregate ablation, removing QAR raises cost from **5.02 → 11.10** while F1 falls from **0.482 → 0.309**; removing QAD also reduces answer quality.

**Open question.** Do learned construction/compression policies transfer beyond conversational memory-QA to tool-using or environment-acting agents?

</details>

### [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](papers/2026/2608.04746.md)
`Write, Update & Consolidation` · `episodic` `timeline` · **★★★★☆** · 2026-08-05

**AI take:** The clean abstraction is **per-memory future utility**: a durable preference and an expiring appointment should not share one global recency function.

[Paper](https://arxiv.org/abs/2608.04746) · [Research note](papers/2026/2608.04746.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Similarity retrieval ignores time; global recency heuristics still assume every memory ages in the same way.

**Core mechanism.** Store What-Where-When context plus **perishability** and a **utility horizon** per memory, then combine semantic relevance, contextual fit, and time-dependent utility during retrieval.

**Memory loop.** `write structured episode → estimate local utility horizon → retrieve with semantic + temporal utility → retroactively revise / decay`

**Compared with.** Mem0, dense embedding retrieval, and global-recency / temporal-prompt baselines.

**Evidence to remember.** On EventQA-64k, the highlighted setting reports **+2.66 F1 over Mem0** and **+3.09 over Qwen3-Embedding-4B**; removing decay degrades the key controlled metric by roughly **5.7×**.

**Open question.** Does utility-aware forgetting still help when conflict resolution, fact consolidation, and long-term provenance become equally important?

</details>

### [MAFIA: Memory Attacks via Fully Indirect Access for LLM Agents](papers/2026/2608.03844.md)
`Evaluation & Analysis` · `semantic` `text` · **★★★★☆** · 2026-08-04

**AI take:** Persistent memory turns prompt injection into a **state-integrity problem**: malicious content can be planted through ordinary interactions and influence a later benign-looking query after the original attack context is gone.

[Paper](https://arxiv.org/abs/2608.03844) · [Code](https://github.com/JiamingChen1234/MAFIA) · [Research note](papers/2026/2608.03844.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** A memory payload can be written now, persist across sessions, and later be retrieved into an apparently normal interaction.

**Core mechanism.** Use black-box probes to infer where malicious memory should land in retrieval space, then construct factual-looking **cloaks** that evade write-time auditing while preserving later retrieval and behavioral influence.

**Attack loop.** `probe retriever → craft cloak → write via normal interaction → persist → trigger later query`

**Compared with.** Ordinary prompt injection and query-only memory attacks such as MINJA.

**Evidence to remember.** MAFIA reports attack-success rates up to **90.7%**; in a highlighted setting, the strongest tested write-time audit detects at most **7.4%** of crafted attacks.

**Open question.** How much of this attack surface survives graph, hierarchical, typed, or provenance-constrained memory stores?

</details>

### [LeanMem: Simple and Efficient Long-Term Memory for LLM Agents](papers/2026/2608.03463.md)
`Representation & Organization` · `episodic` `semantic` `structured` `timeline` · **★★★★☆** · 2026-08-04

**AI take:** The real contribution is not “three stores.” It is **heterogeneous lifecycle semantics**: stable profile facts, evolving events, and source-grounded records should not share one write/update/read contract.

[Paper](https://arxiv.org/abs/2608.03463) · [Research note](papers/2026/2608.03463.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Long-term histories mix stable profile facts, evolving events, and source-grounded evidence; one universal summary/vector store either wastes context or destroys needed detail.

**Core mechanism.** Filter low-value dialogue, route retained evidence into **profile / event / record** memory, evolve only temporal event memory, and plan retrieval using memory-type and token budgets.

**Memory loop.** `filter history → classify evidence type → route to typed stores → selectively evolve → compose query-specific evidence`

**Compared with.** SimpleMem, LightMem, MemoryOS, and A-MEM: the main delta is not a more elaborate universal store but **different lifecycle contracts for different evidence types**.

**Evidence to remember.** On LoCoMo and LongMemEval-S, reported gains over the strongest memory baseline reach up to **5.54** and **15.07 points**, depending on backbone; removing heterogeneous storage causes the largest ablation drop.

**Open question.** How brittle is routing when information type is ambiguous, changes over time, or conflicts across months of interaction?

</details>

### [When Memory Becomes Authority: Benchmarking Authorization Collapse in Agent Memory](papers/2026/2608.01679.md)
`Evaluation & Analysis` · `semantic` `structured` · **★★★★☆** · 2026-08-03

**AI take:** The paper attacks a foundational assumption: a memory can preserve **what was said** while erasing **who was authorized to say it**, making a semantically faithful summary behaviorally unsafe.

[Paper](https://arxiv.org/abs/2608.01679) · [Research note](papers/2026/2608.01679.md)

<details>
<summary><strong>Understand this paper in 60 seconds</strong></summary>

**Problem.** Memory consolidation optimizes semantic retention, but tool-using agents also need to preserve source authority and provenance constraints.

**Core mechanism.** Construct paired histories with identical claims/tasks but different **source authority**, test whether consolidators preserve that distinction, then persist an authority label as a source-first mitigation.

**Behavioral loop.** `role-labeled history → consolidate memory → read memory + authority → choose downstream action`

**Compared with.** The deeper baseline assumption that **semantically faithful memory is automatically behaviorally faithful**.

**Evidence to remember.** Authority collapse appears in **48/49** tested consolidator/backbone configurations; collapsed memories produce a mean **50.3% unauthorized-action rate**. The source-first mitigation reports **16.9% → 0.0%** unauthorized actions with benign-task success essentially unchanged.

**Open question.** How should real agents represent revocation, delegation, conflicting authority, and organizational hierarchy over long time spans?

</details>

## ⭐ Design Anchors

Use these to orient yourself in the design space rather than as a “best papers” ranking.

| Work | Why it is a useful design point |
|---|---|
| **[LeanMem](papers/2026/2608.03463.md)** | Heterogeneous evidence types with different lifecycle semantics. |
| **[MemoryCPT](papers/2026/2608.04843.md)** | Learned construction + query-time compression under an explicit cost × quality objective. |
| **[Scrub Jay Memory](papers/2026/2608.04746.md)** | Per-memory temporal utility as a forgetting / retention abstraction. |
| **[Activity Frames](papers/2026/2608.05784.md)** | Deterministic compilation as an alternative to model-driven memory construction. |
| **[AuthMem-Bench](papers/2026/2608.01679.md)** | Authority/provenance preservation as a memory correctness invariant. |
| **[MAFIA](papers/2026/2608.03844.md)** | Persistent-memory poisoning as a cross-session state-integrity threat. |

<details>
<summary><strong>How these anchors fit together</strong></summary>

One useful way to read the current design space is by asking where control enters the memory lifecycle:

1. **Activity Frames** — memory **construction** can sometimes be deterministic and auditable rather than model-driven.
2. **LeanMem** — memory **representation and lifecycle** can be typed rather than flat.
3. **MemoryCPT** — construction and read-time compression can become **learned policies** under a systems objective.
4. **Scrub Jay Memory** — retention/forgetting can depend on **per-memory future utility** rather than one global heuristic.
5. **AuthMem-Bench + MAFIA** — memory **correctness** extends beyond relevance to provenance, authority, and persistent-state integrity.

The current frontier is therefore not one new memory store. It is the co-design of **representation × lifecycle policy × access × cost × trust**.

[See the full anchor notes →](papers/anchors.md)

</details>

## 🗂 Browse by Research Problem

Rather than grouping papers primarily by application, the radar asks **which part of the memory lifecycle is changing?** Open a research problem for the current design points, strongest signal, and next decisive question.

| Research problem | Question |
|---|---|
| **[Representation & Organization](categories/representation-organization.md)** | What memory forms should exist, and which evidence types deserve different structure/lifecycle semantics? |
| **[Retrieval & Access](categories/retrieval-access.md)** | How should an agent locate, query, navigate, and combine stored memory once representation is no longer flat? |
| **[Write, Update & Consolidation](categories/write-update-consolidation.md)** | What should be written, merged, revised, compressed, retained, or forgotten over time? |
| **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** | Which memory decisions should be learned rather than hand-designed, and what objective should train them? |
| **[Evaluation & Analysis](categories/evaluation-analysis.md)** | What does “correct memory” mean once cost, provenance, authority, security, and downstream behavior matter? |

<details>
<summary><strong>Representation & Organization — one store, or typed memory?</strong></summary>

**Current anchors.** [LeanMem](papers/2026/2608.03463.md) and [Activity Frames](papers/2026/2608.05784.md).

**Strongest signal.** The clearest current cluster pushes against one universal memory representation: profile facts, evolving events, source-grounded records, and high-volume activity traces appear to benefit from different construction and lifecycle semantics.

**Biggest unresolved question.** Is heterogeneous memory intrinsically better, or are gains mostly from extra routing logic, preprocessing, and representation-specific prompts?

**Next decisive evidence.** Same-model, matched-budget ablations comparing one strong flat store against typed stores over months-long histories with drift, conflict, and multimodal evidence.

[Explore this research problem →](categories/representation-organization.md)

</details>

<details>
<summary><strong>Retrieval & Access — what is the right interface to persistent memory?</strong></summary>

**Current anchor.** No paper in the current seed set clears the radar's precision threshold as a primary Retrieval & Access contribution.

**Strongest signal.** This absence is itself useful: recent work is changing representation, lifecycle policy, and safety faster than it is changing the read interface. Yet richer memory types will eventually require richer access semantics than one semantic top-k call.

**Biggest unresolved question.** Should typed memories expose query operators, temporal filters, aggregation, graph traversal, hierarchy navigation, or a learned router — and which of these actually matter under matched budgets?

**Next decisive evidence.** Interface/action-set ablations that keep the same memory content and controller while varying only the access operations.

[Explore this research problem →](categories/retrieval-access.md)

</details>

<details>
<summary><strong>Write, Update & Consolidation — what deserves to survive?</strong></summary>

**Current anchor.** [Scrub Jay Memory](papers/2026/2608.04746.md), with LeanMem and Activity Frames providing adjacent signals around typed update semantics and deterministic construction.

**Strongest signal.** Retention is moving from a side effect of storage toward an explicit lifecycle decision: utility horizon, selective evolution, consolidation, and evidence-preserving compilation are all candidate control points.

**Biggest unresolved question.** Can aggressive compression/forgetting improve efficiency without deleting the provenance, conflict history, or authority metadata needed later?

**Next decisive evidence.** End-to-end lifecycle evaluations that jointly stress write, update, forgetting, provenance, retrieval, and cost rather than scoring each stage independently.

[Explore this research problem →](categories/write-update-consolidation.md)

</details>

<details>
<summary><strong>Memory Learning & Evolution — which memory decisions should be learned?</strong></summary>

**Current anchor.** [MemoryCPT](papers/2026/2608.04843.md), with Scrub Jay Memory as an adjacent utility-aware design point.

**Strongest signal.** Memory construction and query-time compression are becoming optimization targets rather than fixed modules. The key question is shifting from “which retriever?” to “which lifecycle decisions should adapt to expected downstream utility and cost?”

**Biggest unresolved question.** Do learned memory policies generalize across domains, models, and changing memory distributions, or merely overfit benchmark-specific QA economics?

**Next decisive evidence.** Cross-domain transfer, policy-freeze experiments, and long-horizon adaptation under changing user/task distributions with matched inference budgets.

[Explore this research problem →](categories/memory-learning-evolution.md)

</details>

<details>
<summary><strong>Evaluation & Analysis — when is remembered state actually correct?</strong></summary>

**Current anchors.** [AuthMem-Bench](papers/2026/2608.01679.md) and [MAFIA](papers/2026/2608.03844.md).

**Strongest signal.** Semantic relevance is an incomplete notion of correctness. Persistent state can be useful yet wrong because provenance, authority, or integrity was lost or poisoned.

**Biggest unresolved question.** How should benchmarks jointly measure answer utility, lifecycle cost, temporal consistency, provenance, authority, and security without collapsing them into one opaque score?

**Next decisive evidence.** A realistic end-to-end benchmark where memory influences consequential tool actions across many sessions and where write/update/forget/retrieve decisions can be independently audited.

[Explore this research problem →](categories/evaluation-analysis.md)

</details>

<details>
<summary><strong>Scope, ratings, and what is intentionally excluded</strong></summary>

A work belongs here when memory **persists or manages information across interaction or reasoning steps and materially affects an agent's future behavior**. Generic RAG, KV-cache optimization, or long-context work is not included unless persistent agent memory is a central mechanism.

Ratings represent **importance, not relevance**: ★★★★★ field-shaping; ★★★★☆ notable; ★★★☆☆ useful. A paper can be highly relevant to agent memory without being high priority to read.

Numeric results are surfaced only when they materially change the interpretation; full paper pages carry the richer evidence, caveats, and provenance.

</details>

---

**Agent Memory Radar is a living bibliography, but the primary reading interface is the research map — not the daily stream.**
