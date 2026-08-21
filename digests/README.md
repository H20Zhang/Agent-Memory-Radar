# Research Compactions

[Home](../README.md) · [What’s Changing](../README.md#whats-changing) · [Reading Paths](../README.md#reading-paths) · [Research Map](../README.md#research-map)

Compactions answer a different question from paper notes: **what changed in the field, how strong is the evidence, and what should a researcher update in their mental model?**

## Current synthesis

| Horizon | Report | Research takeaway |
|---|---|---|
| **Weekly** | [2026-W33 — Memory architecture decomposes into stage-specific controls](weekly/2026-W33.md) | Archive, access, consumer state/reuse, evolution, and lifecycle cost need matched controls rather than one architecture-level score. |
| **Weekly** | [2026-W32 — Structure only matters when control can use it](weekly/2026-W32.md) | Added structure should be credited only when a downstream controller/operator actually exploits it. |
| **Monthly** | [2026-08 — rolling through Aug 21](monthly/2026-08.md) | August now adds **multi-source evidence completion, an oracle-local skill selector signal, judge-gate qualification, and guarded harness commits** without promoting any one-paper signal into the durable map. |
| **Yearly** | [2026 — rolling, incomplete](yearly/2026.md) | Current evidence supports a multi-stage memory-state interface, but coverage begins in August with limited backfill and is not a full-year reconstruction. |

## Time hierarchy

- **Recent ~31 days → weekly:** preserve local changes while comparisons are fresh.
- **Recent 3 calendar months → monthly:** rebuild the design-space map and record which weekly claims persist or weaken.
- **Covered years → yearly:** retain only durable shifts, field-shaping evidence, corrections, and open problems.

W34 is still open, so Aug 17–20 evidence is integrated into the rolling monthly map without pretending the week is closed.

## Reading a compaction

A useful compaction is not a list of paper summaries. It should tell you:

1. **Old assumption → new evidence → updated claim.**
2. **Which papers are actually load-bearing, and compared with what.**
3. **Where papers disagree or attribution remains confounded.**
4. **What next experiment would most decisively change the current view.**

See [`../COMPACTION.md`](../COMPACTION.md) for the full synthesis contract and [`../runs/README.md`](../runs/README.md) for the no-public-run policy. Accepted provenance lives in canonical projections, due closed digests, and atomic Git history; private workflow state is never a reader surface.
