# Representation & Organization

[Research Map](../README.md#research-map) · [All research problems](README.md) · [Reading Paths](../README.md#reading-paths)

How agent memory is represented, structured, and transformed for the current consumer.

## Current argument

Representation now has **two audiences**: the persistent store and the acting consumer. **QCR** shows that a provenance-rich full trajectory can be the right archival record but the wrong actor-facing representation even when retrieval is fixed. **QUMem** adds a personalized-state version of the same boundary: typed historical evidence is not itself the final memory object; a query-time reconstruction stage must infer which facts, preference trajectory, and transferable principles are currently applicable. Structure remains justified only when a downstream operation can exploit it.

| Date | Paper | Tags | Importance | Research take |
|---|---|---|---:|---|
| 2026-08-17 | [QUMem](../papers/2026/2608.16168.md) | `semantic` `structured` `timeline` `personalization` | 4/5 | The biggest ablation effect comes after storage/retrieval: query-conditioned user-state reconstruction turns distributed historical evidence into currently applicable state. |
| 2026-08-13 | [Beyond Retrieval / QCR](../papers/2026/2608.12847.md) | `procedural` `text` `web-agent` | 4/5 | Same selected trajectory, different delivery: target-bound workflow/rebinding support beats raw trace by 10.7pp while halving online tokens. |
| 2026-08-10 | [Muscle Memory](../papers/2026/2608.08995.md) | `procedural` `structured` `personalization` | 3/5 | Early signal: stable recurring intent may be compiled into executable specialists rather than retrieved as text. |
| 2026-08-06 | [Activity Frames](../papers/2026/2608.05784.md) | `episodic` `structured` `timeline` | 3/5 | Deterministic compilation is a credible alternative to LLM-based construction for high-volume personal activity memory. |
| 2026-08-04 | [LeanMem](../papers/2026/2608.03463.md) | `episodic` `semantic` `structured` | 4/5 | Heterogeneous lifecycle semantics: profile, evolving event, and source-grounded evidence should not share one storage contract. |
| 2026-08-03 | [PGMem](../papers/2026/2608.01708.md) | `episodic` `semantic` `graph` `personalization` | 3/5 | Persona representation is load-bearing; graph expansion matters more mainly at longer context. |

**Biggest unresolved question:** when should the system preserve full-fidelity archival state but synthesize a smaller task-conditioned consumer state, and how can it do so without introducing hallucinated preferences/procedures or silently dropping provenance?

**Next decisive evidence:** hold the retrieved source records fixed and compare raw evidence, source-only summaries, target-conditioned support, and inferred user-state representations under preference drift, conflicting memories, binding shift, safety constraints, and matched synthesis cost.

**Continue:** [Retrieval & Access →](retrieval-access.md)