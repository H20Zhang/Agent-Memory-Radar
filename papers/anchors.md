# Design Anchors

These papers are **design points**, not a ranking. Use them to orient yourself in the current agent-memory design space.

| Paper | Design point | Research card |
|---|---|---|
| **LeanMem** | heterogeneous lifecycle semantics | [2608.03463](2026/2608.03463.md) |
| **V-Mem** | modality-routed / structure-aware access | [2608.01543](2026/2608.01543.md) |
| **Activity Frames** | deterministic, auditable memory compilation | [2608.05784](2026/2608.05784.md) |
| **MemoryCPT** | learned end-to-end cost × quality memory policy | [2608.04843](2026/2608.04843.md) |
| **RoMeRL** | reduced-order utility state for runtime memory learning | [2608.02508](2026/2608.02508.md) |
| **Scrub Jay Memory** | per-memory temporal utility / forgetting | [2608.04746](2026/2608.04746.md) |
| **AuthMem-Bench** | authority/provenance as memory correctness | [2608.01679](2026/2608.01679.md) |
| **SkillJack** | provenance/revocation across experience→skill transformation | [2608.03509](2026/2608.03509.md) |

## How to read them

A useful order is **Activity Frames / LeanMem → V-Mem → MemoryCPT / RoMeRL / Scrub Jay → AuthMem-Bench / SkillJack**.

- **Activity Frames + LeanMem** ask what should be deterministically compiled, typed, or given distinct lifecycle semantics before retrieval begins.
- **V-Mem** asks what access operators become necessary once evidence is multimodal and structural relations can beat direct similarity.
- **MemoryCPT, RoMeRL, and Scrub Jay** make memory control itself the optimization target: cost-aware transformation, bounded feedback-bearing state, and future-utility-aware retention.
- **AuthMem-Bench + SkillJack** expand correctness beyond relevance: authority must survive consolidation, while provenance and revocation must survive transformation into derived skills.

Together they suggest a broader stack:

`construction → representation → access → lifecycle policy → cost / utility → provenance / trust`

## Caveat

The radar is young and these anchors reflect current coverage, not a settled canon. **MAFIA** remains an important security paper but is omitted here to keep the anchor set bounded; SkillJack currently supplies a more distinct lifecycle boundary while AuthMem-Bench supplies the authority boundary. Anchors should change when stronger design points appear or when later evidence weakens the current interpretation.
