# 🧠 Agent Memory Radar

**A living research map of memory for AI agents — updated daily, distilled for researchers.**

Agent Memory Radar tracks how AI agents **store, organize, retrieve, update, learn from, and reason over persistent experience**. It is designed to answer three questions quickly:

> **What changed? Compared to what? Why does it matter?**

Rather than maximizing paper count, the radar separates *relevance* from *importance*, explains the actual technical delta of each paper, and periodically compacts the stream into weekly, monthly, and yearly research maps.

**Last updated:** 2026-08-10

## 🧭 Current Research Signals

Early-August work suggests three shifts worth watching:

- **Flat memory → heterogeneous memory lifecycles.** Different kinds of memory increasingly get different write, update, and read semantics rather than sharing one universal interface.
- **Fixed heuristics → learned or utility-aware memory policies.** Memory construction, compression, retrieval, and forgetting are beginning to be treated as adaptive decisions rather than fixed knobs.
- **Retrieval quality → persistent-state correctness.** Once memory survives across sessions, provenance, authorization, poisoning, and state integrity become part of the memory problem itself.

These are **early signals, not settled trends**. The compactions track whether they strengthen, weaken, or fragment as new evidence arrives.

## 🗺 Research Compactions

Start here if you care more about the **research landscape** than the daily paper stream. The time scale gets coarser as the horizon grows: weekly reports capture local shifts; monthly reports track design-space movement; yearly reports preserve the durable map.

### Weekly · last 1 month

- **[2026-W32 · Aug 3–9](digests/weekly/2026-W32.md)** — early-August work shifts from “better retrieval” toward heterogeneous lifecycles, explicit memory policies, and persistent-state trust boundaries.

### Monthly · last 1 quarter

- **[2026-08 · rolling](digests/monthly/2026-08.md)** — month-to-date map of which themes are strengthening, which assumptions are being challenged, and what evidence would change the current interpretation.

### Yearly · all available years

- **[2026 · rolling](digests/yearly/2026.md)** — current yearly research map. **Coverage begins Aug 2026**, so it is explicitly not presented as a full-year reconstruction yet.

**[Browse the full compaction archive →](digests/README.md)**

## 🧭 Choose a Reading Path

You do not need to read the papers chronologically.

| If you care about… | Start with | Question to keep in mind |
|---|---|---|
| **Memory systems & representation** | [LeanMem](papers/2026/2608.03463.md) → [Activity Frames](papers/2026/2608.05784.md) | Should different evidence types have different storage and lifecycle semantics? |
| **Adaptive memory policies** | [MemoryCPT](papers/2026/2608.04843.md) → [Scrub Jay Memory](papers/2026/2608.04746.md) | Which memory decisions should be learned instead of fixed heuristics? |
| **Safety, provenance & correctness** | [AuthMem-Bench](papers/2026/2608.01679.md) → [MAFIA](papers/2026/2608.03844.md) | What new failure modes appear once state persists across sessions? |

## ⭐ Papers Worth Reading

Not every on-topic paper deserves equal attention. Current highlights:

| Paper | Why it is worth reading |
|---|---|
| **[MemoryCPT](papers/2026/2608.04843.md)** | Treats memory construction and query-time compression as a joint **cost × quality optimization** problem rather than optimizing retrieval alone. |
| **[LeanMem](papers/2026/2608.03463.md)** | Makes a strong case that profile, event, and source-grounded evidence should have **different lifecycle semantics**. |
| **[Scrub Jay Memory](papers/2026/2608.04746.md)** | Reframes forgetting around **per-memory future utility** instead of one universal recency rule. |
| **[AuthMem-Bench](papers/2026/2608.01679.md)** | Shows that memory can preserve a claim while losing **who had authority to make it**. |
| **[MAFIA](papers/2026/2608.03844.md)** | Demonstrates that persistent memory turns prompt injection into a **cross-session state-integrity** problem. |

## 🔥 Latest Papers

The list stays compact by default. **Expand a paper to understand it without leaving the README; open the full analysis when you want the complete technical note.**

<details>
<summary><strong>★★★☆☆ Activity Frames — Deterministic Screen-Activity Compilation for Agent Memory and Replay</strong> · 2026-08-06</summary>

**Why read it.** It challenges a common assumption: high-volume personal memory does not necessarily need an LLM in the construction path.

- **Problem:** raw desktop activity is too verbose, while LLM summaries can be lossy, expensive, and hard to audit.
- **Core idea:** deterministically compile screen events into typed, chronological **Activity Frames** with application/site, time, input volume, and evidence pointers.
- **Compared to what:** the meaningful baseline is **raw activity rows or LLM-generated activity summaries**, not another vector retriever.
- **Evidence:** across eight evaluated days, the strongest reported setting reaches **98.4% QA accuracy**, versus **82.1–91.1%** for raw rows and **66.1–80.4%** for LLM summaries; compilation is reported at **68 ms**.
- **Caveat:** the study is single-user and single-machine; the architecture is more convincing than the current breadth of evidence.

`Representation & Organization` · `episodic` `structured` `timeline`

[Paper](https://arxiv.org/abs/2608.05784) · [Code](https://github.com/nossa-y/activity-frames) · **[Full AI Analysis →](papers/2026/2608.05784.md)**

</details>

<details>
<summary><strong>★★★★☆ MemoryCPT — An End-to-End Agent Memory Framework for Cost-Performance Trade-off</strong> · 2026-08-05</summary>

**Why read it.** It turns memory from a retrieval component into an **end-to-end systems optimization problem**.

- **Problem:** multi-stage memory pipelines repeatedly call LLMs for construction, retrieval, and summarization, but usually optimize quality and cost only indirectly.
- **Core idea:** learn both offline construction (**QAD**) and online query-aware compression (**QAR**), with a reward that explicitly balances answer quality against context/inference cost.
- **Compared to what:** unlike training-free modular systems such as LightMem/MemoryOS, learned policy approaches such as Memory-R1, or cost-aware BudgetMem, MemoryCPT makes **both write-time construction and read-time compression trainable parts of one pipeline**.
- **Evidence:** on LoCoMo / LongMemEval, removing QAR reportedly raises cost from **5.02 → 11.10** while F1 falls from **0.482 → 0.309**; removing QAD also hurts answer quality.
- **Caveat:** evidence is concentrated on conversational memory QA; transfer to tool-using and environment-acting agents remains unclear.

`Memory Learning & Evolution` · `episodic` `semantic` `structured`

[Paper](https://arxiv.org/abs/2608.04843) · **[Full AI Analysis →](papers/2026/2608.04843.md)**

</details>

<details>
<summary><strong>★★★★☆ Scrub Jay Memory — Caching for the Future</strong> · 2026-08-05</summary>

**Why read it.** It gives forgetting a cleaner abstraction: **estimate each memory's future utility**, rather than apply one global recency rule.

- **Problem:** similarity retrieval ignores time, while global recency heuristics still treat all memories as if they age the same way.
- **Core idea:** attach What-Where-When context, **perishability**, and a **utility horizon** to each episodic memory; combine semantic relevance with time-dependent utility at retrieval time.
- **Compared to what:** compared with Mem0, dense retrieval, and global-recency baselines, the key delta is that **time affects each memory differently**.
- **Evidence:** on EventQA-64k, the highlighted setting reports **+2.66 F1 over Mem0** and **+3.09 over Qwen3-Embedding-4B**; removing decay worsens the key controlled diagnostic by roughly **5.7×**.
- **Caveat:** the gains are strongest on temporal/perishable facts; flat retrieval remains stronger in some conflict and consolidation settings.

`Write, Update & Consolidation` · `episodic` `timeline`

[Paper](https://arxiv.org/abs/2608.04746) · **[Full AI Analysis →](papers/2026/2608.04746.md)**

</details>

<details>
<summary><strong>★★★★☆ MAFIA — Memory Attacks via Fully Indirect Access for LLM Agents</strong> · 2026-08-04</summary>

**Why read it.** It shows why persistent memory is qualitatively different from one-turn prompt injection: the attack becomes part of future agent state.

- **Problem:** malicious input can be written now, retrieved later under a benign-looking query, and influence the agent after the original interaction has disappeared from context.
- **Core idea:** infer where malicious content should land in retrieval space using black-box probes, then wrap payloads in factual-looking **cloaks** that evade write-time audits while maximizing future retrieval.
- **Compared to what:** the right comparison is not ordinary prompt injection; MAFIA extends **query-only memory attacks** such as MINJA into persistent-state poisoning.
- **Evidence:** the paper reports attack-success rates up to **90.7%**; in a highlighted setting, the strongest tested write-time audit detects at most **7.4%** of crafted attacks.
- **Caveat:** the evaluation mainly targets similarity/RAG-style memories, leaving graph, hierarchical, and strongly typed stores underexplored.

`Evaluation & Analysis` · `semantic` `text`

[Paper](https://arxiv.org/abs/2608.03844) · [Code](https://github.com/JiamingChen1234/MAFIA) · **[Full AI Analysis →](papers/2026/2608.03844.md)**

</details>

<details>
<summary><strong>★★★★☆ LeanMem — Simple and Efficient Long-Term Memory for LLM Agents</strong> · 2026-08-04</summary>

**Why read it.** Its strongest claim is architectural: **heterogeneous evidence should have heterogeneous memory lifecycles**.

- **Problem:** long-term histories mix stable profile facts, evolving events, and source-grounded evidence; one universal summary/vector store either wastes context or destroys needed detail.
- **Core idea:** route retained evidence into **profile / event / record** memory, evolve only the temporal event store, and plan retrieval with memory-type and token budgets.
- **Compared to what:** versus SimpleMem, LightMem, MemoryOS, and A-MEM, the main delta is not a more elaborate universal store but **different write/update/read semantics for different evidence types**.
- **Evidence:** on LoCoMo and LongMemEval-S, the paper reports gains over the strongest memory baseline of up to **5.54** and **15.07 points**, depending on backbone; removing heterogeneous storage causes the largest ablation drop.
- **Caveat:** routing relies on correctly identifying information type and temporal dynamics, and the evaluation remains dialogue-memory QA rather than consequential agent action.

`Representation & Organization` · `episodic` `semantic` `structured` `timeline`

[Paper](https://arxiv.org/abs/2608.03463) · **[Full AI Analysis →](papers/2026/2608.03463.md)**

</details>

<details>
<summary><strong>★★★★☆ AuthMem-Bench — When Memory Becomes Authority</strong> · 2026-08-03</summary>

**Why read it.** It exposes an invariant most memory benchmarks miss: preserving the statement is not enough if consolidation loses **who was authorized to make it**.

- **Problem:** semantic compression can preserve *what was said* while silently deleting provenance and authorization constraints that determine how an agent should act.
- **Core idea:** construct paired histories with identical claims/tasks but different **source authority**, then measure whether memory consolidation preserves the behavioral distinction.
- **Compared to what:** the deeper baseline assumption being challenged is that a **semantically faithful summary is necessarily a behaviorally faithful memory**.
- **Evidence:** authority collapse appears in **48/49** tested consolidator/backbone configurations; collapsed memories produce a mean **50.3% unauthorized-action rate**. A source-first mitigation reports **16.9% → 0.0%** unauthorized actions while benign-task success stays essentially unchanged.
- **Caveat:** the benchmark is controlled and synthetic, with one consolidation-to-action cycle; delegation, revocation, and realistic organizational authority remain open.

`Evaluation & Analysis` · `semantic` `structured`

[Paper](https://arxiv.org/abs/2608.01679) · **[Full AI Analysis →](papers/2026/2608.01679.md)**

</details>

## 🗂 Browse by Research Problem

The primary taxonomy asks **which part of the memory system a paper changes**:

- **[Representation & Organization](categories/representation-organization.md)** — how memory is represented, structured, and materialized.
- **[Retrieval & Access](categories/retrieval-access.md)** — how agents locate, query, navigate, and reason over memory.
- **[Write, Update & Consolidation](categories/write-update-consolidation.md)** — what gets written, merged, corrected, compressed, or forgotten.
- **[Memory Learning & Evolution](categories/memory-learning-evolution.md)** — learned memory policies, accumulated experience, procedural memory, and self-evolving agents.
- **[Evaluation & Analysis](categories/evaluation-analysis.md)** — benchmarks, empirical studies, security, reliability, and failure analysis.

## 🔍 Scope

A work belongs here when memory **persists or manages information across interaction or reasoning steps and materially affects an agent's future behavior**.

Generic RAG, KV-cache optimization, or long-context work is not included unless persistent agent memory is a central mechanism. The boundary is deliberately semantic rather than keyword-based.

<details>
<summary><strong>How to interpret the ratings and notes</strong></summary>

- **★★★★★ Field-shaping** — likely changes an important design point, benchmark, or research direction.
- **★★★★☆ Notable** — clear technical or empirical delta that agent-memory researchers should know.
- **★★★☆☆ Useful** — solid relevant work, but currently more incremental, narrow, or weakly validated.
- The rating is **importance, not relevance**. A paper can be highly relevant to agent memory without being high priority to read.
- Numeric results in the README are included only when they materially help understand the paper; the full page carries the richer evidence and caveats.

</details>

## 📖 What Each Paper Page Gives You

Each accepted paper is turned into a researcher-facing technical note with **TL;DR → problem → core mechanism → memory design → compared-to-what → evidence → why-it-matters → limitations**. Important or mechanism-heavy papers also receive a visual explainer when a figure genuinely reduces reading effort.

---

**Agent Memory Radar is a living bibliography, but the primary reading interface is the research map — not the daily stream.**
