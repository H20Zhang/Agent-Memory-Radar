# Design Anchors

[← Agent Memory Radar](../README.md) · [Research Map](../README.md#-research-map) · [What’s changing](../README.md#-whats-changing)

These papers are **design points, not a ranking**. The set is intentionally bounded and changes only when a new paper exposes a distinct control boundary.

| Paper | Design point | Research card |
|---|---|---|
| **LeanMem** | heterogeneous lifecycle contracts for different evidence types | [2608.03463](2026/2608.03463.md) |
| **V-Mem** | structural same-round access across modalities | [2608.01543](2026/2608.01543.md) |
| **ReFind** | raw archival record + stateful query-time search as the semantic-structure control | [2608.12888](2026/2608.12888.md) |
| **QCR** | target-conditioned post-retrieval reuse / rebinding | [2608.12847](2026/2608.12847.md) |
| **PMCoder** | bidirectional controller↔memory coupling | [2608.06811](2026/2608.06811.md) |
| **RoMeRL** | reduced-order feedback-bearing utility state | [2608.02508](2026/2608.02508.md) |
| **AuthMem-Bench** | authority/provenance as memory correctness | [2608.01679](2026/2608.01679.md) |
| **SkillJack** | provenance/revocation across experience→skill transformation | [2608.03509](2026/2608.03509.md) |

## How the anchors fit together

A useful reading order is **LeanMem / ReFind → V-Mem → QCR / PMCoder → RoMeRL → AuthMem-Bench / SkillJack**.

The sequence encodes the current research map:

`what state exists → whether to pre-structure it → how to access it → how selected evidence is adapted to the current decision → how control state learns → whether authority/provenance survive lifecycle transforms`

**ReFind** and **QCR** are the newer additions. ReFind raises the baseline for representation claims: generated semantic structure should beat a competent raw-record search interface, not one-shot top-k. QCR adds a different boundary after retrieval: even the correct long trajectory can be the wrong actor-facing representation when source bindings are stale.

## Rotated-out but still important

**MemoryCPT** remains the strongest current end-to-end learned cost×quality pipeline, and **Scrub Jay Memory** remains a clean per-memory temporal-utility design. They are rotated out only to keep the anchor set bounded as raw-record access and post-retrieval reuse become distinct design points; their research notes and category pages remain canonical.
