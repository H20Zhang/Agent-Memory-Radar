# Design Anchors

These papers are **design points**, not a ranking. Use them to orient yourself in the current agent-memory design space.

| Paper | Design point | Research card |
|---|---|---|
| **LeanMem** | heterogeneous lifecycle semantics | [2608.03463](2026/2608.03463.md) |
| **MemoryCPT** | learned end-to-end cost × quality memory policy | [2608.04843](2026/2608.04843.md) |
| **Scrub Jay Memory** | per-memory temporal utility / forgetting | [2608.04746](2026/2608.04746.md) |
| **Activity Frames** | deterministic, auditable memory compilation | [2608.05784](2026/2608.05784.md) |
| **AuthMem-Bench** | authority/provenance as memory correctness | [2608.01679](2026/2608.01679.md) |
| **MAFIA** | persistent-memory state-integrity threat | [2608.03844](2026/2608.03844.md) |

## How to read them

A useful order is **Activity Frames / LeanMem → MemoryCPT / Scrub Jay Memory → AuthMem-Bench / MAFIA**.

- Activity Frames asks how much memory construction should be deterministic and auditable.
- LeanMem asks which evidence types should get distinct representation and lifecycle semantics.
- MemoryCPT asks which write/read decisions should be learned under an explicit systems objective.
- Scrub Jay Memory makes retention/forgetting depend on per-memory future utility.
- AuthMem-Bench and MAFIA expand correctness from relevance to authority, provenance, and persistent-state integrity.

Together they suggest a broader stack:

`construction → representation → lifecycle policy → access → cost / utility → trust`

## Caveat

The radar is young and these anchors reflect current coverage, not a settled canon. Anchors should change when stronger design points appear or when later evidence weakens the current interpretation.
