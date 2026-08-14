# Retrieval & Access

How an agent locates, queries, navigates, or reasons over stored memory.

## Current argument

The read interface is splitting into **three distinct decisions**: *which evidence structure to consult*, *whether that evidence is admissible*, and *how controller state should condition access*. Similarity is becoming one primitive inside a broader access policy.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-11 | [MAP-Graph](../papers/2026/2608.10509.md) | `semantic` `graph` `general-agent` | ★★★★☆ | Separates semantic relevance from hard read eligibility, recursive provenance trust, and action-risk gating. |
| 2026-08-10 | [MESA](../papers/2026/2608.10108.md) | `episodic` `structured` `general-agent` | ★★★★☆ | The right policy is often several memory structures but not all: 65.1% with 2.8 views / 11.0k tokens vs 63.7% reading all five / 18.7k. |
| 2026-08-07 | [PMCoder](../papers/2026/2608.06811.md) | `episodic` `structured` `coding` | ★★★★☆ | Planner phase conditions retrieval and memory statistics can trigger replanning; the controller↔memory interaction is the key result. |
| 2026-08-02 | [V-Mem](../papers/2026/2608.01543.md) | `episodic` `multimodal` `timeline` | ★★★★☆ | Modality routing plus same-round binding exposes relations that one cross-modal similarity space misses. |

**Biggest unresolved question:** can one access policy jointly choose structure, respect provenance/admissibility, and condition on evolving controller state without becoming a brittle hand-built router?

**Next decisive evidence:** freeze the stored evidence and base model, then compare access policies on consequential acting-agent tasks while measuring answer/action quality, evidence cost, and read-boundary correctness.
