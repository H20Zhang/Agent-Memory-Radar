# Research Compaction Protocol

Agent Memory Radar treats curation as a **research-memory hierarchy**, not an append-only stream of paper summaries. Compaction should preserve disagreement, evidence status, and causal uncertainty while removing repeated detail.

## Levels

| Level | Persistent artifact | Purpose | What must not be lost |
|---|---|---|---|
| **L0 · Paper records** | `data/papers/*.json` + `papers/YYYY/*.md` | Canonical facts, provenance, classification, paper-level interpretation, visual publication state. | links, evidence, uncertainty, corrections |
| **L0-log · Daily runs** | `runs/daily/YYYY/MM/DD.md` | Compact history of accepted/deferred/corrected work. | decision history, edge cases, blockers |
| **L1 · Weekly** | `digests/weekly/YYYY-Www.md` | Identify local research deltas, disagreements, and reading priority. | negative results, competing explanations |
| **L2 · Monthly** | `digests/monthly/YYYY-MM.md` | Rebuild the field map and causal model. | weakening claims, open problems, reinterpreted anchors |
| **L3 · Yearly** | `digests/yearly/YYYY.md` | Preserve only durable shifts and evidence standards. | changes of mind, failed ideas, durable trade-offs |

## Public time hierarchy

The reader-facing archive deliberately loses temporal resolution as work ages:

- **Recent ~1 month → weekly.**
- **Recent ~1 quarter → monthly.**
- **All sufficiently covered years → yearly.**

Lower-level files remain in the repository even after they age out of primary navigation. Active months and years may be explicitly **rolling**; never imply complete historical coverage from partial backfill.

## Editorial principle

A compaction succeeds only if it answers questions a chronological list cannot:

> **So what changed? Compared with what? How strong is the evidence? What should a researcher do differently?**

The report should be shorter than its sources but harder to write. A paragraph per paper is not compaction.

## Weekly compaction

After an ISO week closes, synthesize the accepted papers from that week into one research argument. The report should contain:

1. **Week thesis** — one falsifiable statement about what changed.
2. **2–4 design-space changes** — supported by multiple papers; a one-paper observation must be labeled **early signal**.
3. **Representative / important papers** — each expressed as `delta → compared with → evidence → so what`.
4. **Tension / contradiction** — the strongest competing interpretation or negative result.
5. **Research gaps** — what remains unresolved after the week’s evidence.
6. **Evidence to watch next** — the experiment or external signal that would change the current conclusion.
7. **Reading order** — the smallest sequence that teaches the week’s change.

Adjacent papers may be used as context but must not be silently counted as part of the week.

## Monthly compaction

A monthly map operates one abstraction level higher. During an open month it may be **rolling**, but new evidence should rewrite the map rather than append another chronological paragraph.

Synthesize weekly compactions **plus canonical records** into:

- older/default assumptions → current movement;
- persistent vs weakening themes;
- strongest papers and negative controls;
- unresolved trade-offs and hidden assumptions;
- concrete falsification conditions;
- a minimal researcher reading path.

Weekly reports may be used as an index only. Re-ground load-bearing claims in canonical paper records/notes.

## Yearly compaction

A yearly report is not twelve monthly reports concatenated. It asks **what actually survived the year?**

A finalized report should preserve:

- the start→end change in the field map;
- durable design-space shifts;
- field-shaping papers and benchmarks;
- themes that strengthened, weakened, fragmented, or disappeared;
- durable trade-offs and open questions;
- corrections where an earlier weekly/monthly narrative failed;
- 2–4 concrete conditions that would falsify the final year thesis.

A rolling year file must state incomplete coverage prominently.

## Multi-role challenge before synthesis

When independent roles are supported:

| Role | Job | What it should challenge |
|---|---|---|
| **Clusterer / Field Mapper** | Group papers by actual memory-control delta and propose a field map. | keyword similarity, fashionable naming |
| **Evidence Auditor** | Compare baselines, evidence, ablations, calls/tokens/latency, and negative results. | causal over-attribution |
| **Trend Skeptic** | Construct the strongest alternative explanation. | several similarly framed papers being mistaken for a durable shift |
| **Research Editor** | Write only after seeing the independent analyses. | paper-by-paper concatenation |

Prefer **one important tension** over five weak trends.

## Factorized evaluation lens

Memory papers often change several variables simultaneously. Compactions should reason over:

`raw archive / source evidence × representation × write granularity × access program × selection/admission × consumer-state transform × update/evolution rule × provenance/governance × offline+online resources × base model × task distribution`

This is a causal checklist, not a taxonomy.

Three rules matter most:

1. **A strong raw-record interface is the baseline for structure claims.** Pre-built semantic structure should beat competent question-time search when representation is credited.
2. **Retrieval is not reuse.** Selected evidence may still need rebinding, reconstruction, or procedural transformation before the current actor can use it safely.
3. **Cost spans the entire lifecycle.** Construction, consolidation, embedding/indexing, retrieval, synthesis, maintenance, and reacquisition belong in the same systems accounting.

## Visual maps

Weekly/monthly/yearly visuals are research compression, not decorative collages. Follow [`VISUAL_POLICY.md`](VISUAL_POLICY.md). A synthesis visual must be grounded in the compaction’s verified claims and may be published only after visual QA and WebP publication on `main`.

## Retention and correction policy

- Keep every accepted canonical paper record and useful paper note.
- Keep daily logs as provenance, not primary browsing surfaces.
- Keep every weekly/monthly compaction after it ages out of homepage navigation.
- Keep one yearly report per sufficiently covered calendar year; the current year may remain rolling.
- Correct upward: if a paper’s evidence, importance, classification, or newly discovered baseline changes a higher-level conclusion, revise the affected compaction.
- Do not preserve an old narrative merely for consistency.

The goal is **lossy compression of repetition, not loss of disagreement, provenance, or uncertainty**.