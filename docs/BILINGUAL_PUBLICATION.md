# Chinese-First Bilingual Publication Contract

Agent Memory Radar is bilingual, with Simplified Chinese as the default reader experience.

## Public file convention

- `README.md` — default Simplified Chinese landing page.
- `README.en.md` — complete English counterpart.
- Reader-facing Research Library/category pages, high-value paper notes, and public weekly/monthly/yearly synthesis should have both Chinese and English forms.
- Canonical JSON, schemas, maintenance docs, scheduler prompts, validation output, and `runs/*` remain single-source unless localization adds reader value.

## One judgment, two editorial projections

Chinese and English must derive from the same semantic research record: paper identity, importance, research delta, closest comparison, decisive evidence, caveat, field-map consequence, taxonomy, and links.

Chinese is the primary editorial surface. English must preserve the same information depth rather than becoming a shortened translation. Neither language may introduce a factual or causal claim absent from the shared research judgment.

Material changes must update both public language variants in one maintenance transaction. Drift on high-visibility facts or interpretation is a correctness failure.

## Terminology

Keep paper titles, benchmark/dataset names, model names, metrics, APIs, system names, and standard research acronyms in their canonical English form when that improves precision and literature search. Add a Chinese gloss only when it improves comprehension; do not repeat bilingual terminology mechanically after it is established.

## Editorial quality

Chinese should use natural technical Chinese rather than translated English syntax. Prefer direct sentences, concrete operations, and explicit comparison/evidence. Warn on repeated empty transitions and recurring templates such as `真正重要的是……`, `关键不在于……而在于……`, `值得注意的是……` when they become house style.

English follows the same Research Radar Editor standard: concrete verbs/nouns, comparison before praise, explicit attribution boundaries, and no repetitive LLM sentence skeletons.
