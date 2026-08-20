# Maintainer Guide

This page keeps repository-maintenance details out of the public reader surfaces.

## Source of truth

- `data/papers/*.json` — canonical structured records.
- `papers/YYYY/*.md` — evidence-layer research notes; historical English notes are progressively receiving Chinese counterparts by reader value.
- `categories/*.md` — living arguments by research problem.
- `library/` — long-lived navigation by problem/research line/year.
- `papers/anchors.md` — durable design points.
- `digests/` — temporal synthesis.
- `assets/visuals/` — researcher-facing explainers.
- `runs/README.md` — static no-public-run policy; private workflow state lives only under ignored `.radar-private/` or in ephemeral Agent memory.

## Reader architecture

Public responsibilities are deliberately separated:

- root README — **judgment/router layer**;
- Research Library — **historical retrieval layer**;
- category pages — **argument layer**;
- paper notes — **evidence layer**;
- digests — **temporal synthesis layer**.

Do not repeat one paragraph across these surfaces.

The default reader flow is:

`Latest Papers → What’s Changing → Field Map → Reading Paths → Research Library`

README should let a reader scan quickly and deepen in place. High-value papers may expose a 60–90 second fold, but the fold is a causal compression rather than copied note prose.

## Chinese-first bilingual publication

`README.md` is Simplified Chinese default and `README.en.md` is the complete English counterpart. Research Library and current high-value public narrative are bilingual.

Chinese and English are two editorial projections of one research judgment. A material correction to paper identity, importance, research delta, decisive evidence, caveat, or field relationship updates both high-visibility language variants in the same maintenance transaction.

Migration priority is current Latest/Reading Path papers → anchors/category arguments → older high-importance notes. Do not churn the entire archive for cosmetic parity.

## Paper-note reasoning contract

High-visibility notes should resolve:

`Research delta → Problem → Mechanism → Closest comparison → Decisive evidence → What remains unproven → Field-map consequence → Related reading`

For Agent Memory, add lifecycle projection only when useful: `write / organize / access / consumer state / update-forget / governance`.

The structure is stable; sentence templates are not. Apply `EDITORIAL_STANDARD.md` and review adjacent notes together for repeated AI-house-style phrasing.

## Update flow

For accepted work:

1. verify identity and primary sources;
2. update canonical JSON;
3. create/update the evidence note;
4. update category/research-line relationship only if the field argument changes;
5. update README only if the work deserves current high-visibility placement;
6. update Reading Paths/anchors only when the conceptual map changes;
7. propagate meaningful corrections into compactions;
8. handle visuals under the existing visual contract;
9. update bilingual high-visibility reader surfaces atomically;
10. validate and preserve the accepted projection in one atomic commit.

## No public operational run logs

Do not commit daily-run, candidate, lane, retry, or validation inventories. Canonical records, the bilingual Timeline, rolling periods, due closed digests, gated maps, and Git history are public provenance. Private operational traces belong only under ignored `.radar-private/runs/<run_id>.json` or in ephemeral Agent memory; [`../runs/README.md`](../runs/README.md) is static policy only.

## Validation

CI separates canonical and reader contracts:

```bash
python scripts/validate_canonical.py
python scripts/validate_reading.py
```

`validate_canonical.py` checks schema/taxonomy, record identity, paper-note existence, and visual publication invariants.

`validate_reading.py` checks Chinese/English README and Library pairing, progressive-depth order, canonical Timeline completeness/order/bindings, stable anchors, rolling-window metadata and support gates, public-run absence, local links, and obvious repeated editorial skeletons.

`scripts/validate.py` remains the full repository, schema, visual, category, and relative-link audit and is run after the focused canonical and reading validators.

## Research Library

Weekly/monthly/yearly files are not the historical index. A durable/high-importance paper should remain reachable through at least one non-temporal route: research problem, research line, anchor, or controlled tag.

## Visual publication

A visual is research compression, not decoration. Follow `VISUAL_POLICY.md` and `assets/README.md`; do not expose render/upload/scheduler status in reader-facing pages.

## Scheduler

The recurring automation should be a thin pointer to `DAILY_WORKFLOW.md`. Stable editorial, bilingual, visual, compaction, and validation rules belong in the repository, not in a giant task prompt.
