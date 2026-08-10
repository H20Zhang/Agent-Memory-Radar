# Curation Protocol

Agent Memory Radar is maintained by a scheduled AI curator. The repository itself does not run a scheduled paper crawler.

## Daily process

The curator should use multiple independent subtasks/agents rather than one monolithic pass:

1. **Discovery** — search a broad overlapping recent window across arXiv and other high-signal scholarly sources; optimize for recall.
2. **Relevance + taxonomy** — independently decide whether each candidate satisfies the inclusion rule and assign the primary research-problem category plus orthogonal tags.
3. **Research interpretation** — for accepted papers, read enough of the full paper to support claims about method, comparisons, evidence, and limitations. Abstract-only analysis is insufficient for these fields.
4. **QC / adversarial review** — challenge inclusion, deduplicate versions, verify links, separate relevance from importance, and reject unsupported AI claims.

## Inclusion boundary

Include work when memory persists or manages information across interaction/reasoning steps and materially affects a language or multimodal agent's future behavior.

Do not include generic RAG, generic long-context modeling, KV-cache optimization, or unrelated continual learning unless agent memory is a central mechanism.

## Importance scale

- **5 — field-shaping:** likely changes an important design point, benchmark, or research direction.
- **4 — notable:** clear technical or empirical delta researchers in agent memory should know.
- **3 — useful:** solid relevant work, but primarily incremental or application-specific.
- **2 — peripheral:** relevant but weak novelty/evidence or narrow scope.
- **1 — archival:** technically in scope but little reason to prioritize reading.

A high relevance score must not imply a high importance score.

## Evidence discipline

Every research note should distinguish author claims from the curator's interpretation. `Compared to What`, `Evidence`, `Why It Matters`, and `Limitations` should be based on the paper body and verified external sources when needed. Unknowns should remain unknown rather than being filled by plausible text.

## Update policy

Canonical records live under `data/papers/`. The README and category pages are researcher-facing views derived from them. Preserve provenance, avoid duplicate arXiv versions, and only attach code/project URLs that were actually verified.
