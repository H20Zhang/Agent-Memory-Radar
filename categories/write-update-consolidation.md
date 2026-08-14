# Write, Update & Consolidation

How memory is extracted, written, compressed, merged, corrected, forgotten, or consolidated.

## Current argument

The evidence now supports a stricter rule than “compress intelligently”: **a write/update transform must preserve the low-volume fields that later decisions depend on, and richer structure must beat a matched simple policy**.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-12 | [The Sleeping Agent](../papers/2026/2608.11775.md) | `semantic` `text` `timeline` | ★★★☆☆ | Generic gist preserved entities/events but erased temporal anchors; explicit temporal protection raised preservation 3.05%→62.39% and recovered temporal QA. |
| 2026-08-06 | [MERIT / Causal Episodic Memory](../papers/2026/2608.05906.md) | `episodic` `structured` | ★★★☆☆ | Cross-query repair memory helps, but polarity/type structure is not reliably better than untyped dynamic retrieval. |
| 2026-08-05 | [Scrub Jay Memory](../papers/2026/2608.04746.md) | `episodic` `structured` `timeline` | ★★★★☆ | Treat forgetting as per-memory future utility rather than one global recency heuristic. |

**Biggest unresolved question:** can a lifecycle policy discover what must be preserved—time, authority, provenance, identifiers, constraints—without hand-specifying every semantic field?

**Next decisive evidence:** longitudinal conflict/update benchmarks with matched append-only retrieval, field-level preservation diagnostics, provenance, and explicit lifecycle cost.
