# Retrieval & Access

How an agent locates, queries, navigates, or reasons over stored memory.

## Current argument

The read-side question is becoming **what interface should expose evidence to this decision?** ReFind adds a crucial negative control: much of the gain attributed to semantic memory structure can disappear when a raw archive receives a competent, stateful search interface. MESA and MAP-Graph then show the complementary boundaries—choose the useful representation subset and enforce whether retrieved evidence is admissible.

| Date | Paper | Tags | Importance | AI take |
|---|---|---|---:|---|
| 2026-08-13 | [ReFind](../papers/2026/2608.12888.md) | `episodic` `text` `timeline` | ★★★★☆ | Raw chat + iterative lexical search + chat-native controls is a serious structured-memory baseline; interface quality can dominate representation complexity. |
| 2026-08-11 | [MAP-Graph](../papers/2026/2608.10509.md) | `semantic` `graph` `general-agent` | ★★★★☆ | Separates semantic relevance from hard read eligibility, recursive provenance trust, and action-risk gating. |
| 2026-08-10 | [MESA](../papers/2026/2608.10108.md) | `episodic` `structured` `general-agent` | ★★★★☆ | The right policy is often several memory structures but not all: 65.1% with 2.8 views / 11.0k tokens vs 63.7% reading all five / 18.7k. |
| 2026-08-07 | [PMCoder](../papers/2026/2608.06811.md) | `episodic` `structured` `coding` | ★★★★☆ | Planner phase conditions retrieval and memory statistics can trigger replanning; controller↔memory interaction is the key result. |
| 2026-08-02 | [V-Mem](../papers/2026/2608.01543.md) | `episodic` `multimodal` `timeline` | ★★★★☆ | Same-round identity is a structural access operator that bridges cross-modal evidence when similarity alone fails. |

**Biggest unresolved question:** after matching online compute, can learned/structured access policies consistently beat a raw-record agentic-search baseline across semantic abstraction, acting-agent tasks, and low-latency serving—not only precise refinding?

**Next decisive evidence:** freeze raw evidence and the base model, then factor representation preprocessing × access policy × online search budget on the same long-horizon acting tasks while measuring quality, latency/tokens, and provenance correctness.
