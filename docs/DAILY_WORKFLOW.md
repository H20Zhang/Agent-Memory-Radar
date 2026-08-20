# Daily Research-Maintenance Workflow

This is the authoritative orchestration contract for Agent Memory Radar. The recurring scheduler should stay short and point here.

## Transaction

One run is one idempotent transaction:

`preflight → discover → independent judgment → canonical update → evidence note → relationship update → derive Chinese/English reader surfaces → editorial review → validate → log → notify only if material`

An empty discovery day is successful when the repository remains correct.

## 1. Preflight

Read `CURATION.md`, `COMPACTION.md`, `VISUAL_POLICY.md`, `docs/MAINTENANCE.md`, `docs/EDITORIAL_STANDARD.md`, the current README pair, Research Library pair, taxonomy/schema, recent run log, and relevant paper/category pages.

Repair deterministic drift before adding work. Never let a maintenance run re-expand README into a paper dump.

## 2. Discovery and judgment

Use overlapping recent windows and independent roles when supported:

- discovery optimizes recall;
- taxonomy/inclusion decides semantic relevance;
- research analyst reads the full paper for important work;
- skeptical reviewer challenges novelty, attribution, baseline strength, cost, and alternative explanations;
- editor decides which reader surfaces actually deserve an update.

Keep relevance separate from importance. A relevant paper does not automatically enter Latest Papers, Reading Paths, or Field Map.

## 3. Canonical-first update

For accepted work:

`data/papers record → evidence note → category/research-line relationship → reader projections`

The canonical record is factual state. Reader prose is derived judgment.

## 4. Research Explainer Standard

High-visibility notes must resolve:

`Research delta → Problem → Mechanism → Closest comparison → Decisive evidence → What remains unproven → Field-map consequence → Related reading`

Use the Agent Memory lifecycle lens only when it clarifies a changed boundary.

## 5. Bilingual publication

Chinese is primary.

- `README.md` is Chinese default; `README.en.md` is the complete English counterpart.
- Research Library and current high-value public narrative should have both languages.
- Material interpretation changes update both languages in the same transaction.
- Do not translate paper titles, dataset names, metrics, model names, or established technical terms mechanically.
- English is rewritten naturally from the same semantic judgment; it is not a shorter translation.

During migration, prioritize bilingual backfill in this order: current Latest/Reading Path papers → anchors/current category arguments → older high-importance work. Do not churn the archive for cosmetic parity.

## 6. README projection

README order is:

`Latest Papers → What’s Changing → Field Map → Reading Paths → Research Library → How to Use / Scope / About`

Keep roughly 6–8 high-signal Latest entries. Importance >=4/5 or field-map-changing work may receive a 60–90 second fold. A fold is a causal compression, not copied paper-note prose.

Field Map changes only when a design boundary changes. Reading Paths change only when a better conceptual route becomes available.

## 7. Historical discoverability

Weekly/monthly/yearly digests are time views, not the archive index. Every durable/high-importance work should be reachable through at least one non-temporal route: research problem, research line, anchor, or controlled tag.

## 8. Editorial review

Apply `docs/EDITORIAL_STANDARD.md` after research judgment is stable. Check especially for repeated sentence skeletons across recent notes and Chinese machine-translation patterns. Pattern density is the target; do not word-police isolated vocabulary.

## 9. Visuals and compaction

Follow the existing visual and compaction contracts. Update them only when they add research value. Do not expose generation status or scheduler mechanics on public pages.

## 10. Validation and log

Validate schema/taxonomy/links/visual consistency plus the reader contracts:

- Chinese default + English counterpart exist and cross-link;
- same Latest identities/importance/primary links across languages;
- section order and Latest bounds are preserved;
- historical high-value work remains discoverable outside weekly digests;
- no operational internals leak to public surfaces;
- bilingual high-visibility facts do not drift.

Write one compact provenance log under `runs/daily/YYYY/MM/DD.md`.

## Notification gate

Notify only for a newly accepted important paper, a field-level correction/reclassification, a meaningful synthesis/visual repair, or an exact blocker requiring attention. Otherwise complete silently.
