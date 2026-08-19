# Research Compactions

[Home](../README.md) · [What’s Changing](../README.md#whats-changing) · [Reading Paths](../README.md#reading-paths) · [Research Map](../README.md#research-map)

Compactions answer a different question from paper notes: **what changed in the field, how strong is the evidence, and what should a researcher update in their mental model?**

## Current synthesis

| Horizon | Report | Research takeaway |
|---|---|---|
| **Weekly** | [2026-W33 — Memory architecture decomposes into stage-specific controls](weekly/2026-W33.md) | Archive, access, consumer state/reuse, evolution, and lifecycle cost need matched controls rather than one architecture-level score. |
| **Weekly** | [2026-W32 — Structure only matters when control can use it](weekly/2026-W32.md) | Added structure should be credited only when a downstream controller/operator actually exploits it. |
| **Monthly** | [2026-08 — rolling through Aug 19](monthly/2026-08.md) | August separates raw vs structured access, memory admission, consumer-state reconstruction, evolvable read policy, write granularity, lifecycle economics, and provenance/governance. |
| **Yearly** | [2026 — rolling, incomplete](yearly/2026.md) | Current evidence supports a multi-stage memory-state interface, but coverage begins in August with one July backfill and is not a full-year reconstruction. |

## Time hierarchy

- **Recent ~31 days → weekly:** preserve local changes while comparisons are fresh.
- **Recent 3 calendar months → monthly:** rebuild the design-space map and record which weekly claims persist or weaken.
- **Covered years → yearly:** retain only durable shifts, field-shaping evidence, corrections, and open problems.

Older lower-resolution artifacts remain in the repository for provenance even after they age out of primary navigation.

## Reading a compaction

A useful compaction is not a list of paper summaries. It should tell you:

1. **Old assumption → new evidence → updated claim.**
2. **Which papers are actually load-bearing, and compared with what.**
3. **Where papers disagree or attribution remains confounded.**
4. **What next experiment would most decisively change the current view.**

See [`../COMPACTION.md`](../COMPACTION.md) for the full synthesis contract. Raw daily provenance lives under [`../runs/daily/`](../runs/daily/) and is intentionally not a primary reading surface.