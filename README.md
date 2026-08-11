# 🧠 Agent Memory Radar

**A living research map of memory for AI agents — updated daily, distilled for researchers.**

Agent Memory Radar tracks how AI agents **store, organize, retrieve, update, learn from, and reason over persistent experience**. It is designed to answer three questions quickly:

> **What changed? Compared to what? Why does it matter?**

Rather than maximizing paper count, the radar separates *relevance* from *importance*, explains the actual technical delta of each paper, and periodically compacts the stream into weekly and monthly research maps.

**Last updated:** 2026-08-10

## 🧭 Current Research Signals

Early-August work suggests three shifts worth watching:

- **Flat memory → heterogeneous memory lifecycles.** Different kinds of memory increasingly get different write, update, and read semantics rather than sharing one universal interface.
- **Fixed heuristics → learned or utility-aware memory policies.** Memory construction, compression, retrieval, and forgetting are beginning to be treated as adaptive decisions rather than fixed knobs.
- **Retrieval quality → persistent-state correctness.** Once memory survives across sessions, provenance, authorization, poisoning, and state integrity become part of the memory problem itself.

These are **early signals, not settled trends**. The weekly and monthly compactions track whether they strengthen, weaken, or fragment as new evidence arrives.

## 🗺 Research Compactions

If you do not want to scan individual papers, start here. Compactions synthesize **changes in the design space**, not a concatenation of paper summaries.

- **[Weekly · 2026-W32](digests/weekly/2026-W32.md)** — how early-August work shifts from “better retrieval” toward heterogeneous lifecycles, explicit memory policies, and persistent-state trust boundaries.
- **[Monthly · 2026-08 (rolling)](digests/monthly/2026-08.md)** — a month-to-date map of which themes are strengthening, which assumptions are being challenged, and what evidence would change the current interpretation.
- **[Browse all compactions](digests/README.md)**

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

### [Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay](papers/2026/2608.05784.md)
`Representation & Organization` · `episodic` `structured` `timeline` · **★★★☆☆** · 2026-08-06

**AI take:** Some high-volume personal memory may be better **compiled deterministically before retrieval** than summarized by an LLM. Promising architecture; current evidence is single-user.

[Paper](https://arxiv.org/abs/2608.05784) · [Code](https://github.com/nossa-y/activity-frames) · [AI Analysis](papers/2026/2608.05784.md)

### [MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off](papers/2026/2608.04843.md)
`Memory Learning & Evolution` · `episodic` `semantic` `structured` · **★★★★☆** · 2026-08-05

**AI take:** Treat both memory construction and query-time compression as trainable components under an explicit **quality × cost** objective, instead of optimizing retrieval in isolation.

[Paper](https://arxiv.org/abs/2608.04843) · [AI Analysis](papers/2026/2608.04843.md)

### [Caching for the Future: Scrub Jay Episodic Memory Principles for Agent Memory Systems](papers/2026/2608.04746.md)
`Write, Update & Consolidation` · `episodic` `timeline` · **★★★★☆** · 2026-08-05

**AI take:** The useful abstraction is **per-memory future utility**: forgetting should depend on how a particular fact ages, not one universal recency function.

[Paper](https://arxiv.org/abs/2608.04746) · [AI Analysis](papers/2026/2608.04746.md)

### [MAFIA: Memory Attacks via Fully Indirect Access for LLM Agents](papers/2026/2608.03844.md)
`Evaluation & Analysis` · `semantic` `text` · **★★★★☆** · 2026-08-04

**AI take:** Persistent memory turns prompt injection into a **state-integrity** problem: malicious content can be written now and retrieved into a later benign-looking interaction.

[Paper](https://arxiv.org/abs/2608.03844) · [Code](https://github.com/JiamingChen1234/MAFIA) · [AI Analysis](papers/2026/2608.03844.md)

### [LeanMem: Simple and Efficient Long-Term Memory for LLM Agents](papers/2026/2608.03463.md)
`Representation & Organization` · `episodic` `semantic` `structured` · **★★★★☆** · 2026-08-04

**AI take:** The strongest idea is not another store but **heterogeneous lifecycle semantics**: profile, event, and source-grounded evidence should not share one write/update/read contract.

[Paper](https://arxiv.org/abs/2608.03463) · [AI Analysis](papers/2026/2608.03463.md)

### [When Memory Becomes Authority: Benchmarking Authorization Collapse in Agent Memory](papers/2026/2608.01679.md)
`Evaluation & Analysis` · `semantic` `structured` · **★★★★☆** · 2026-08-03

**AI take:** A memory can preserve the claim but lose **who had authority to make it**. For tool-using agents, provenance is part of memory semantics rather than optional metadata.

[Paper](https://arxiv.org/abs/2608.01679) · [AI Analysis](papers/2026/2608.01679.md)

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

## 📖 What Each Paper Page Gives You

Each accepted paper is turned into a researcher-facing technical note:

- **TL;DR, problem, and core idea**
- **Memory design:** write, organize, read, update / forget
- **Compared to what:** closest design points and the actual delta
- **Evidence:** benchmarks, gains, and useful ablations
- **Why it matters, limitations, and confidence**
- **Visual explainer** for important or mechanism-heavy papers when a figure genuinely reduces reading effort

---

**Agent Memory Radar is a living bibliography, but the primary reading interface is the research map — not the daily stream.**
