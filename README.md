# 🧠 Agent Memory Radar

**A living research map of memory for AI agents — updated daily, explained for researchers.**

Agent Memory Radar tracks new work on how agents **store, organize, retrieve, update, learn from, and reason over persistent memory**. The goal is not to maximize paper count: it is to help you quickly answer **what is new, compared to what, and why it matters**.

**Last updated:** 2026-08-10

## 🧭 Start Here: Research Compactions

If you do not want to scan individual papers, start with the compactions. They synthesize papers into changes in the research landscape rather than concatenating summaries.

- **[Weekly · 2026-W32](digests/weekly/2026-W32.md)** — early-August work points toward heterogeneous memory lifecycles, explicit memory policies, and persistent-state trust boundaries.
- **[Monthly · 2026-08 (rolling)](digests/monthly/2026-08.md)** — a rolling map of where the agent-memory design space is moving this month.
- **[Browse all compactions](digests/README.md)**

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

## ⭐ Papers Worth Reading

Not every on-topic paper deserves equal attention. **Importance is scored separately from relevance.** Current highlights:

- **MemoryCPT** — end-to-end cost/performance optimization across memory construction and query-time use.
- **LeanMem** — heterogeneous memory types with different lifecycle semantics.
- **Scrub Jay Memory** — per-memory temporal utility as an explicit forgetting abstraction.
- **AuthMem-Bench + MAFIA** — complementary evidence that provenance, authority, and state integrity become first-class problems once memory persists.

## 🗂 Browse by Research Problem

- [Representation & Organization](categories/representation-organization.md) — how memory is represented and structured.
- [Retrieval & Access](categories/retrieval-access.md) — how agents locate, query, and navigate memory.
- [Write, Update & Consolidation](categories/write-update-consolidation.md) — what gets written, merged, corrected, compressed, or forgotten.
- [Memory Learning & Evolution](categories/memory-learning-evolution.md) — learned memory policies, experience accumulation, and self-evolving agents.
- [Evaluation & Analysis](categories/evaluation-analysis.md) — benchmarks, empirical studies, security, and failure analysis.

## 🔍 What Counts as Agent Memory?

We include work where memory **persists or manages information across interaction or reasoning steps and materially affects an agent's future behavior**.

Generic RAG, KV-cache optimization, and long-context work are not included unless persistent agent memory is a central mechanism. Discovery is intentionally broad; inclusion is semantic rather than keyword-based.

## 📝 What You Get for Each Paper

Each paper has a researcher-facing note designed for fast technical triage:

- **TL;DR, problem, and core idea**
- **Memory design:** write, organize, read, update / forget
- **Compared to what:** closest design points and the actual delta
- **Evidence:** benchmarks, gains, and useful ablations
- **Why it matters, limitations, and confidence**

Important or mechanism-heavy papers also receive a visual explainer when it adds information rather than decoration.

## About This Radar

This is a living bibliography: new papers are added continuously, while weekly and monthly compactions turn the stream into a more stable research map. The taxonomy is organized around **which part of the memory system a paper changes**; orthogonal tags capture memory type, substrate, and application.

For implementation details, curation rules, schemas, and provenance, see [`CURATION.md`](CURATION.md), [`VISUAL_POLICY.md`](VISUAL_POLICY.md), [`taxonomy.yaml`](taxonomy.yaml), and the [`data/`](data/) directory.
