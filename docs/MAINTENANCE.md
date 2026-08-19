# Maintainer Guide

This page collects repository-maintenance details that are intentionally kept out of the audience-facing README.

## Source of truth

- `data/papers/*.json` — canonical structured paper records.
- `papers/YYYY/*.md` — researcher-facing notes grounded in the full paper.
- `categories/*.md` — living arguments by research problem.
- `papers/anchors.md` — bounded durable design points.
- `digests/weekly/`, `digests/monthly/`, `digests/yearly/` — research compactions at decreasing temporal resolution.
- `assets/visuals/` — published researcher-facing WebP explainers and synthesis maps.
- `runs/daily/` — compact archival provenance for each maintenance run.

## Maintenance contracts

- [`../CURATION.md`](../CURATION.md) — inclusion, role separation, evidence, publication, and QC rules.
- [`../COMPACTION.md`](../COMPACTION.md) — weekly/monthly/yearly synthesis and correction rules.
- [`../VISUAL_POLICY.md`](../VISUAL_POLICY.md) — GPT Image grounding and visual-QA protocol.
- [`../assets/README.md`](../assets/README.md) — binary visual publication contract.
- [`../taxonomy.yaml`](../taxonomy.yaml) — controlled primary research problems and orthogonal tags.
- [`../data/paper.schema.json`](../data/paper.schema.json) — canonical record schema.
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — public paper/correction contribution path.

## Editorial separation

The root `README.md` is a public research landing page. It should let a researcher answer, in order:

1. What are the newest papers worth inspecting?
2. What changed in the field recently?
3. What is the shortest reading path for the design question I care about?
4. How is the current design space organized?
5. What evidence standard and scope does this radar use?

Operational details — scheduling, prompt text, file-generation mechanics, upload paths, schema internals, and backfill queues — belong here or in the contracts above, not in README.

## Update flow

For an accepted paper:

1. verify canonical identity and primary sources;
2. update/create `data/papers/<id>.json`;
3. update/create `papers/YYYY/<id>.md`;
4. update the relevant category argument;
5. update README Latest Papers if the work is within the current bounded window;
6. change Reading Paths / Key Anchors only when the design map materially changes;
7. propagate corrections into due weekly/monthly/yearly compactions;
8. handle required visual publication according to the visual contract;
9. write one compact daily provenance log;
10. run repository validation before finishing.

## README contract

Keep the sibling-radar structure:

`Latest Papers → What’s Changing → Reading Paths → Research Map → How to Read → Scope/About/Contributing`

Inside **Research Map**, place **Key Anchors** before **Research Problems**. Avoid adding another top-level section for information already represented by these surfaces.

Latest Papers should stay at roughly 8–10 entries. Anchors should stay around 5–8 and should change slowly.

## Validation

`python scripts/validate.py` checks the contracts that can be verified locally and deterministically, including:

- schema and taxonomy consistency;
- duplicate/file-ID mismatches;
- paper-note existence;
- repository-relative Markdown links;
- generated visual path/embed consistency;
- documented blockers for important papers without a generated visual;
- README section order and bounded latest-paper/anchor counts.

External URLs are not treated as a CI hard dependency because transient network failures should not break repository validation. Verify important external paper/code/project links during curation instead.

## Visual publication

Do not stage binary fragments or use paper-ID-specific assembly workflows as a long-term publication mechanism. The canonical path is the Git data flow documented in [`../assets/README.md`](../assets/README.md), with the binary and its Markdown/JSON references committed together.

A `generated` state is only valid after reading back `main` and verifying the exact asset and references.

## Licensing

Research content and canonical data use **CC BY 4.0**. Maintenance code uses **MIT**. See [`../LICENSE.md`](../LICENSE.md).