# Representation & Organization

How agent memory is represented, structured, and organized.

## Current argument

Representation now has **two audiences**: the persistent store and the acting consumer. QCR supplies the clearest new evidence that a provenance-rich full trajectory can be the right archival record but the wrong actor-facing representation; target-conditioned reuse can outperform direct trace injection even when retrieval is held fixed. Structure remains justified only when a downstream operation can exploit it.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-13 | [Beyond Retrieval / QCR](../papers/2026/2608.12847.md) | `procedural` `text` `web-agent` | ★★★★☆ | Same selected trajectory, different delivery: target-bound workflow/rebinding support beats raw trace by 10.7pp while halving online tokens. |
| 2026-08-10 | [Muscle Memory](../papers/2026/2608.08995.md) | `procedural` `structured` `personalization` | ★★★☆☆ | Early signal: stable recurring intent may be compiled into executable specialists rather than retrieved as text. |
| 2026-08-06 | [Activity Frames](../papers/2026/2608.05784.md) | `episodic` `structured` `timeline` | ★★★☆☆ | Deterministic compilation is a credible alternative to LLM-based construction for high-volume personal activity memory. |
| 2026-08-04 | [LeanMem](../papers/2026/2608.03463.md) | `episodic` `semantic` `structured` | ★★★★☆ | Heterogeneous lifecycle semantics: profile, evolving event, and source-grounded evidence should not share one storage contract. |
| 2026-08-03 | [PGMem](../papers/2026/2608.01708.md) | `episodic` `semantic` `graph` `personalization` | ★★★☆☆ | Persona representation is load-bearing; graph expansion matters more mainly at longer context. |

**Biggest unresolved question:** when should the system preserve full-fidelity archival state but synthesize a smaller target-bound consumer view, and how can it do so without introducing hallucinated procedure or losing provenance?

**Next decisive evidence:** hold the retrieved source record fixed and compare raw, source-summary, target-conditioned, and executable representations under binding shift, multi-memory composition, safety constraints, and matched synthesis cost.
