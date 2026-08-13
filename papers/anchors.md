# Design Anchors

These papers are **design points**, not a ranking. Use them to orient yourself in the current agent-memory design space.

| Paper | Design point | Research card |
|---|---|---|
| **LeanMem** | heterogeneous lifecycle semantics | [2608.03463](2026/2608.03463.md) |
| **V-Mem** | modality-routed / structure-aware access | [2608.01543](2026/2608.01543.md) |
| **PMCoder** | bidirectional controller↔memory coupling | [2608.06811](2026/2608.06811.md) |
| **MemoryCPT** | learned end-to-end cost × quality memory policy | [2608.04843](2026/2608.04843.md) |
| **RoMeRL** | reduced-order utility state for runtime memory learning | [2608.02508](2026/2608.02508.md) |
| **Scrub Jay Memory** | per-memory temporal utility / forgetting | [2608.04746](2026/2608.04746.md) |
| **AuthMem-Bench** | authority/provenance as memory correctness | [2608.01679](2026/2608.01679.md) |
| **SkillJack** | provenance/revocation across experience→skill transformation | [2608.03509](2026/2608.03509.md) |

## How to read them

A useful order is **LeanMem → V-Mem → PMCoder → MemoryCPT / RoMeRL / Scrub Jay → AuthMem-Bench / SkillJack**.

- **LeanMem** asks which evidence types deserve different lifecycle contracts before retrieval begins.
- **V-Mem** asks which access operator becomes necessary once a representation preserves cross-modal structural relations.
- **PMCoder** asks what changes when memory access is conditioned on controller state and memory can change that state in return.
- **MemoryCPT / RoMeRL / Scrub Jay** make memory control itself the optimization target: cost-aware transformation, bounded feedback-bearing state, and future-utility-aware retention.
- **AuthMem-Bench / SkillJack** expand correctness beyond relevance: authority must survive consolidation, while provenance/revocation must survive transformation into derived artifacts.

Together they suggest a broader stack:

`construction → representation → access → controller coupling → lifecycle policy → cost / utility → provenance / trust`

## Caveat

The radar is young and these anchors reflect current coverage, not a settled canon. **Agent Memory Distillation** is a strong new cross-model transfer result but is not yet an anchor because its teacher-assisted tool-use setting is narrower than the control boundaries above. **Activity Frames** remains a useful deterministic-compilation point but has been rotated out to keep the anchor set bounded.
