# 🧠 Agent Memory Radar

A daily-updated, GitHub-native research radar for **agent memory** papers, with a stable taxonomy and AI-generated research notes designed for researchers rather than generic summaries.

> **Maintenance model:** paper discovery, filtering, classification, full-paper interpretation, and repository updates are maintained by a scheduled ChatGPT task. GitHub Actions only validates repository consistency; it is not the daily crawler.

## 🔥 Latest Papers

_No accepted papers yet. The daily curator will populate this section._

## ⭐ Notable Recent Papers

_Importance is scored separately from relevance, so “on-topic” does not automatically mean “worth reading.”_

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

## Daily Curation

The scheduled curator uses an overlapping recent-paper window and multiple independent subtasks for:

1. broad discovery;
2. semantic relevance filtering + taxonomy assignment;
3. full-paper research interpretation;
4. adversarial quality control, deduplication, and claim checking.

The QC step explicitly challenges both inclusion and importance. Updates should preserve source provenance and only add code/project links when verified.

## Repository Status

This is an early living bibliography. The schema and taxonomy are intentionally kept small enough to stay stable as the collection grows.
