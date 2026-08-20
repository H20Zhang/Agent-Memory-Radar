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
- `runs/daily/` — maintenance provenance.

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
10. validate and write one compact daily log.

## Validation

CI separates canonical and reader contracts:

```bash
python scripts/validate_canonical.py
python scripts/validate_reading.py
```

`validate_canonical.py` checks schema/taxonomy, record identity, paper-note existence, and visual publication invariants.

`validate_reading.py` checks Chinese/English README and Library pairing, progressive-depth order, Latest identity parity, stable anchors, local links, and obvious repeated editorial skeletons.

The legacy `scripts/validate.py` remains only as migration history and should not be used as the authoritative public-layout validator after v1.

## Research Library

Weekly/monthly/yearly files are not the historical index. A durable/high-importance paper should remain reachable through at least one non-temporal route: research problem, research line, anchor, or controlled tag.

## Visual publication

A visual is research compression, not decoration. Follow `VISUAL_POLICY.md` and `assets/README.md`; do not expose render/upload/scheduler status in reader-facing pages.

## Scheduler

The recurring automation should be a thin pointer to `DAILY_WORKFLOW.md`. Stable editorial, bilingual, visual, compaction, and validation rules belong in the repository, not in a giant task prompt.
