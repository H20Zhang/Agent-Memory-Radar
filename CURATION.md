# Curation Protocol

Agent Memory Radar is maintained by a scheduled AI curator. The repository itself does not run a scheduled paper crawler. Curated updates are written directly to `main`; GitHub Actions is only the consistency guardrail.

## Public surface policy

`README.md` is the **reader-facing landing page**, not the maintainer manual. Its job is to behave like a compact living survey: orient a first-time reader, expose the newest evidence without becoming a feed, and connect short-term papers to a more durable research map.

### README information architecture

Keep the public information architecture aligned with `H20Zhang/Agentic-RAG-Radar` so the two research radars feel like one product family. The default order is:

1. **Latest Papers** — newest accepted work with a visible AI take and a collapsible 60-second explanation. The newest evidence should be the first substantive section.
2. **Start Here** — 2–4 short reading paths plus an optional “if you only read three papers” foldout.
3. **Design Anchors** — durable design points, explicitly not a best-paper ranking.
4. **Browse by Research Problem** — taxonomy table plus foldouts stating current anchors, strongest signal, biggest unresolved question, and next decisive evidence.
5. **Research Compactions** — recent-month weekly, recent-quarter monthly, and all yearly reports. Compactions remain high-signal but should not displace new papers from the first screenful.
6. **Reader guidance / scope / contributing** — compact explanation of how to read the radar, what is in scope, how ratings work, and how to contribute corrections.

The first screenful may include one concise **current field thesis** and a light star/cross-radar call to action. Do not turn the README into a marketing page or keyword list: discoverability text should naturally describe the research value and use domain terms such as agent memory, LLM agents, long-term memory, procedural memory, benchmarks, and research compactions only when they genuinely fit.

Do not add a separate “current signals” or “papers worth reading” section when the same information is already expressed more coherently through Latest Papers, Start Here, Design Anchors, or compactions. Prefer fewer stronger surfaces over duplicated summaries.

### Research Compactions on README

The archive deliberately becomes coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

Each visible compaction entry should contain a short **thesis paragraph**, not just a filename. Weekly entries may include a suggested reading order. Monthly entries should state how the reader's mental model of the field should change. Yearly entries should emphasize durable shifts and be explicit when coverage is rolling or incomplete.

README should show every weekly compaction from roughly the last 31 days, every monthly compaction from the last 3 calendar months, and all yearly compactions. Older weekly/monthly reports stay in `digests/README.md` but age out of the homepage.

### Latest-paper presentation

Use **progressive disclosure**, but keep the most useful judgment visible before the fold:

- visible by default: paper title, category/tags, importance, date, a 1–2 sentence **AI take**, and paper/code/research-note links;
- inside `<details><summary><strong>Understand this paper in 60 seconds</strong></summary>`: **Problem**, **Core mechanism**, a compact memory/data/control loop when useful, **Compared with**, **Evidence to remember**, and **Open question**.

The 60-second foldout should let a researcher understand the paper's real delta without leaving README, but it must not duplicate the full research note. Prefer one decisive result/ablation over a table of metrics. The “Open question” should reveal the main assumption that could change the importance judgment.

Keep roughly **8–10 latest papers** on README. Older work remains discoverable through category pages, anchors, paper pages, and compactions.

### Start Here and Design Anchors

Maintain roughly **3 short reading paths** that reflect the current design space, not a static topic list. Each path should say what the reader is supposed to learn, not merely provide links.

Maintain roughly **5–8 Design Anchors** in README and `papers/anchors.md`. Anchors are design points, not rankings. They should span distinct abstractions or control boundaries and may be replaced when stronger papers supersede them.

### Browse by Research Problem

Maintain `categories/README.md` as the compact overview. On README, each primary category should have a concise foldout with:

- **Current anchors**;
- **Strongest signal**;
- **Biggest unresolved question**;
- **Next decisive evidence**.

Category views are living research arguments, not append-only paper lists. If no paper clears the radar's threshold for a category, say so; absence can expose an important research gap.

### What never belongs on README

Do **not** expose scheduler behavior, subagent roles, schemas, validation internals, storage layout, prompt mechanics, binary-upload details, or operational provenance. Those belong in `CURATION.md`, `VISUAL_POLICY.md`, `assets/README.md`, schemas, and run logs.

A useful final test is: **does this help a visitor understand agent-memory research, compare design points, decide what to read next, or discover an adjacent radar?** If not, it probably does not belong in README.

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

## Yearly compaction

On the first daily run after a calendar year closes, synthesize that year's finalized monthly compactions plus canonical paper records into `digests/yearly/YYYY.md`.

The yearly file should be the most compressed and durable research map. It should identify:

- design-space shifts that persisted beyond a few weeks or one benchmark cycle;
- the strongest / field-shaping papers and benchmarks of the year;
- themes that strengthened, weakened, fragmented, or disappeared;
- durable trade-offs and research gaps;
- where earlier weekly/monthly interpretations were wrong or needed revision;
- concrete evidence that would falsify the final yearly thesis.

A rolling current-year file may exist, but its **coverage window must be explicit**. Never present a mid-year or partially backfilled view as a full-year reconstruction.

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

Canonical records live under `data/papers/`. Per-paper notes live under `papers/`. Weekly/monthly/yearly compactions are the high-level browsing layer. `papers/anchors.md`, `categories/README.md`, README, and category pages are derived researcher-facing views. Preserve provenance, avoid duplicate arXiv versions, and only attach code/project URLs that were actually verified.