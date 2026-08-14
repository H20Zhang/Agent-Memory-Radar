# Representation & Organization

How agent memory is represented, structured, and organized.

## Current argument

Representation matters when it exposes a downstream operation or validity relation that a flat store cannot. **PGMem is useful counter-discipline:** persona-level nodes carry most of its gain; graph expansion becomes more important mainly at longer context, so “graph memory” itself is not the result.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-10 | [Muscle Memory](../papers/2026/2608.08995.md) | `procedural` `structured` `personalization` | ★★★☆☆ | Early signal: stable recurring intent may be compiled into executable specialists rather than retrieved as text. |
| 2026-08-06 | [Activity Frames](../papers/2026/2608.05784.md) | `episodic` `structured` `timeline` | ★★★☆☆ | Deterministic compilation is a credible alternative to LLM-based construction for high-volume personal activity memory. |
| 2026-08-04 | [LeanMem](../papers/2026/2608.03463.md) | `episodic` `semantic` `structured` | ★★★★☆ | Heterogeneous lifecycle semantics: profile, evolving event, and source-grounded evidence should not share one storage contract. |
| 2026-08-03 | [PGMem](../papers/2026/2608.01708.md) | `episodic` `semantic` `graph` `personalization` | ★★★☆☆ | Evidence-grounded persona representation is load-bearing; graph expansion adds more at 128k than on shorter settings. |

**Biggest unresolved question:** which representation distinctions remain useful after access/controller budget is matched, rather than merely giving the system more preprocessing or tokens?

**Next decisive evidence:** factorial flat-vs-typed/graph experiments that keep the retriever, controller, context budget, and answer model fixed while measuring the exact relation each representation exposes.
