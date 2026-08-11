# Curation Protocol

Agent Memory Radar is maintained by a scheduled AI curator. The repository itself does not run a scheduled paper crawler. Curated updates are written directly to `main`; GitHub Actions is only the consistency guardrail.

## Public surface policy

`README.md` is the **reader-facing landing page**, not the maintainer manual. Optimize it for a researcher who lands on the repository for the first time and wants to understand the field quickly.

The README should prioritize:

1. what Agent Memory Radar is and why it is useful;
2. the current high-level research signals;
3. weekly and monthly research compactions;
4. reading paths, papers worth reading, and the latest accepted work;
5. clear category and scope entry points.

Use **progressive disclosure** rather than choosing between a tiny README and an unreadably long one. For latest papers, prefer GitHub-native `<details><summary>...</summary>...</details>` blocks: the collapsed summary should expose title, importance, and date; the expanded body should let a reader understand the paper without leaving the README.

A good expanded paper card contains only high-signal fields:

- **Why read it** — the single reason this paper deserves attention;
- **Problem** — what existing memory abstraction fails;
- **Core idea** — the actual mechanism / design change;
- **Compared to what** — the closest baseline and the real delta;
- **Evidence** — only the strongest result or ablation that changes confidence;
- **Caveat** — the main reason not to over-generalize;
- links to paper, code/project when verified, and the full analysis.

Do not duplicate the whole paper page inside README. The purpose of the foldout is **technical triage**, not exhaustive documentation.

Keep the landing page bounded as the corpus grows:

- keep roughly **8–10 latest paper foldouts** on README, rather than accumulating every paper forever;
- keep roughly **3 reading paths** that reflect the current design space, not a static taxonomy dump;
- keep **2–4 current research signals**, rewritten as evidence changes rather than appended historically;
- keep a short **Papers Worth Reading** ranking; older work remains discoverable through category pages, paper pages, and compactions.

Do **not** expose routine implementation details in the README: scheduler behavior, subagent roles, schemas, validation internals, storage layout, prompt mechanics, or operational provenance. Those belong in `CURATION.md`, `VISUAL_POLICY.md`, `assets/README.md`, schemas, and run logs.

A useful test is: **does this sentence help a visitor understand agent-memory research or decide what to read?** If not, it probably does not belong in the README.

## Daily process

The curator should use multiple independent subtasks/agents rather than one monolithic pass:

1. **Discovery** — search a broad overlapping recent window across arXiv and other high-signal scholarly sources; optimize for recall.
2. **Relevance + taxonomy** — independently decide whether each candidate satisfies the inclusion rule and assign the primary research-problem category plus orthogonal tags.
3. **Research interpretation** — for accepted papers, read enough of the full paper to support claims about method, comparisons, evidence, and limitations. Abstract-only analysis is insufficient for these fields.
4. **QC / adversarial review** — challenge inclusion, deduplicate versions, verify links, separate relevance from importance, and reject unsupported AI claims.

Daily run logs are archival provenance and live under `runs/daily/YYYY/MM/DD.md`; they should not dominate the README.

## Weekly compaction

On the first daily run after an ISO week closes, synthesize the previous week's accepted papers into `digests/weekly/YYYY-Www.md`.

The weekly file is **not** a concatenation of paper summaries. It should identify the 2–4 meaningful changes in the design space, rank the papers worth reading, expose tensions between approaches, and state the strongest newly visible research gaps. Multiple independent subtasks should separately propose themes, challenge importance rankings, and check that each claimed trend is supported by more than superficial wording overlap.

## Monthly compaction

On the first daily run after a calendar month closes, synthesize that month's weekly compactions plus canonical paper records into `digests/monthly/YYYY-MM.md`.

The monthly file should answer: how did the research map move; which ideas persisted across multiple weeks; which themes weakened; what were the strongest papers; what unresolved trade-offs now matter; and what future evidence would falsify the current interpretation. A rolling month-to-date file may exist during the active month, but it must be explicitly marked rolling until finalized.

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

For compactions, do not infer a trend from a single paper unless it is explicitly labeled an early signal. Prefer cross-paper synthesis and preserve counter-evidence.

## Update policy

Canonical records live under `data/papers/`. Per-paper notes live under `papers/`. Weekly/monthly compactions are the high-level browsing layer. README and category pages are derived researcher-facing views. Preserve provenance, avoid duplicate arXiv versions, and only attach code/project URLs that were actually verified.
