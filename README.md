# 🧠 Agent Memory Radar

A daily-updated, GitHub-native research radar for **agent memory** papers, with a stable taxonomy and AI-generated research notes designed for researchers rather than generic summaries.

> **Maintenance model:** scheduled ChatGPT curation writes directly to `main`. Daily runs discover and curate papers; weekly and monthly compactions compress the stream into research-level takeaways. GitHub Actions only validates repository consistency.

**Last curated:** 2026-08-10 · [raw daily log](runs/daily/2026/08/10.md)

## 🧭 Research Compactions

- **[Weekly · 2026-W32](digests/weekly/2026-W32.md)** — early-August memory work shifts from “better retrieval” toward heterogeneous lifecycles, explicit memory policies, and persistent-state trust boundaries.
- **[Monthly · 2026-08 (rolling)](digests/monthly/2026-08.md)** — month-to-date research map; finalized after August closes.
- [How compaction works](digests/README.md)

Daily logs are archival provenance, not the primary reading interface.

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

## ⭐ Notable Recent Papers

The first seed run has no 5/5 paper. That is intentional: **relevance is not importance**, and a new preprint needs unusually strong conceptual or empirical evidence to be called field-shaping.

- **MemoryCPT** — learned end-to-end cost/performance optimization across the memory pipeline.
- **LeanMem** — heterogeneous memory representation and lifecycle semantics with strong ablation signal.
- **Scrub Jay Memory** — explicit temporal utility / perishability as a forgetting abstraction.
- **AuthMem-Bench + MAFIA** — two complementary warnings that persistent memory introduces provenance, authority, and state-integrity failure modes.

## 🗂 Browse by Research Problem

- [Representation & Organization](categories/representation-organization.md)
- [Retrieval & Access](categories/retrieval-access.md)
- [Write, Update & Consolidation](categories/write-update-consolidation.md)
- [Memory Learning & Evolution](categories/memory-learning-evolution.md)
- [Evaluation & Analysis](categories/evaluation-analysis.md)

## Inclusion Rule

A work is included when memory **persists or manages information across interaction/reasoning steps and materially affects a language or multimodal agent's future behavior**.

Generic RAG, KV-cache optimization, and long-context work are excluded unless agent memory is a central mechanism. The curator intentionally uses a broad discovery stage followed by semantic filtering, rather than relying on the phrase “agent memory.”

## Research Note for Each Paper

Each accepted paper gets a concise researcher-facing note covering:

- **TL;DR / Problem / Core Idea**
- **Memory Design:** write, organize, read, update/forget
- **Compared to What:** the closest prior design points and the actual delta
- **Evidence:** benchmarks, gains, and the strongest supporting ablations
- **Why It Matters / Limitations / AI Confidence**

Canonical structured records live in `data/papers/`; Markdown views are derived from those records.

## Taxonomy

Primary categories answer **which part of the memory system the paper changes**, rather than forcing every paper into a single cognitive-memory label. Orthogonal tags capture memory type, substrate, and application. See [`taxonomy.yaml`](taxonomy.yaml).

## Curation Cadence

The scheduled curator uses multiple independent subtasks for broad discovery, semantic filtering/taxonomy, full-paper interpretation, and adversarial QC. It writes clean, auditable updates directly to `main`.

On the first daily run after an ISO week closes, it creates or revises the previous week's **research compaction**. On the first daily run after a calendar month closes, it creates the previous month's **monthly research map**. Compaction must synthesize changes and trade-offs rather than concatenate paper summaries.

## Repository Status

This is an early living bibliography. The schema and taxonomy are intentionally kept small enough to stay stable as the collection grows.
