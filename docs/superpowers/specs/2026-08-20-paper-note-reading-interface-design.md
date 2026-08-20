# Paper Note Reading Interface Design

## Goal

Make researcher-facing paper notes read like compact mini reviews rather than archival summaries. The note should let a researcher identify the paper's real delta, closest comparison, decisive evidence, main caveat, and lifecycle position before committing to a full read.

## Reading order

Every high-visibility paper note should use this hierarchy:

1. compact navigation back to Latest Papers, Research Map, and the paper's category;
2. metadata line: paper, date, category, importance, confidence, tags;
3. one-line **Research delta**;
4. **Problem**;
5. **Mechanism** with a compact data/control-flow expression when useful;
6. **Compared with** focused on the closest causal control rather than a long baseline list;
7. **Decisive evidence** containing the smallest result/ablation set needed to support the interpretation;
8. **Main caveat** with the strongest alternative explanation plus open questions;
9. **Memory lifecycle** table (`write / organize / read / update-forget`);
10. **Why it matters** as a field-level implication;
11. **Related reading** with 2–3 papers and one sentence explaining the relationship.

## Presentation principles

- Prefer `Research delta`, `Research take`, and explicit comparisons over model-persona language such as `AI take`.
- Keep visual/maintenance status, generation failures, scheduler details, and operational provenance out of researcher-facing notes; accepted facts remain in canonical JSON, while private workflow traces stay only under ignored `.radar-private/` or in ephemeral Agent memory. No public operational run logs are created; `runs/README.md` is static policy only.
- Avoid restating the abstract. Mechanism and evidence should expose the paper's control boundary.
- A note is allowed to be shorter than before if repeated architecture prose is recoverable from the paper and canonical record.
- Exact numbers remain only when already verified from the full paper.

## Rollout

First normalize the papers currently exposed in README Latest Papers. Future accepted papers should follow the same structure; older notes can be backfilled opportunistically rather than rewritten merely for uniformity.

## Validation

Repository validation should require this structure for paper notes currently exposed in README Latest Papers, while leaving older archival notes backward-compatible during gradual backfill.
