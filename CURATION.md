# Curation Protocol

Agent Memory Radar is maintained as a **reader-facing living survey backed by auditable structured records**. The Daily Agent defined by [`docs/RADAR_AGENT_PROTOCOL.md`](docs/RADAR_AGENT_PROTOCOL.md) and [`docs/DAILY_WORKFLOW.md`](docs/DAILY_WORKFLOW.md) is the normal editor and only writer. Research roles may return evidence, but only the orchestrator mutates repository or GitHub state. Candidates, blocked evidence, and scheduler state remain private until the evidence and skeptical-audit gates are complete.

## Public surface policy

`README.md` is the landing page for researchers, not a maintainer manual. Keep its structure aligned with the sibling [Agentic RAG Radar](https://github.com/H20Zhang/Agentic-RAG-Radar) while preserving agent-memory-specific research questions.

### README information architecture

Default order:

1. **Latest Timeline** — every native-v2 acceptance in the current 30-day Radar window whose `radar_published_at` is no later than the exact public synthesis cutoff shared with both rolling periods, ordered by full timestamp, followed by the fixed eight legacy compatibility entries; no fixed item cap.
2. **7-day / 30-day synthesis** — exact rolling windows and direction-level changes before the durable map.
3. **Field Map** — durable lifecycle/problem structure, changed only through the map gate.
4. **Reading Paths** — about three short question-led paths.
5. **Research Library** — complete history and alternate routes by problem, line, and year.
6. **How to Use / Scope / About / Contributing** — compact reading-depth, scope, evidence, citation/reuse, and contribution guidance.

The first screenful may include one concise current-field thesis and a light star/cross-radar call to action. Optimize discoverability naturally around terms such as agent memory, LLM agents, long-term memory, procedural memory, benchmarks, and memory systems; never turn the page into a keyword list.

Do not expose scheduling, subagent internals, schema mechanics, binary-upload details, prompt text, backfill queues, or operational provenance on README.

### Timeline presentation

Use one `<details>` disclosure per accepted identity:

- closed summary: `displayed date · identity · lifecycle/problem label — one-sentence research delta`;
- open body: **Question**, including the closest lifecycle-matched control; **Evidence**; **Caveat**; **Map** with `map_delta`; and verified **Links** to the primary source and local deep notes.

Timeline has no fixed count cap: show every native-v2 record whose `radar_published_at` falls in the current 30-day window and is no later than the shared exact public synthesis cutoff, then the fixed eight compatibility identities in their preserved order. Those explicit legacy records retain their honest paper publication dates under the section-level migration notice. Do not infer or fabricate `radar_published_at`, and do not silently add or remove compatibility identities.

### Period synthesis / compactions

The rolling 7-day and 30-day sections state exactly one visible inclusive window and the exact UTC synthesis timestamp shared with the Timeline cutoff. Native membership and support use only `radar_published_at` values no later than that same cutoff; legacy records may provide historical Field Map context but never rolling support. Every direction binds visible prose to stable bilingual metadata for its key, state, ordered canonical supports, confidence enum, implication witness, Radar timing basis, synthesis timestamp, and prior-map evidence. Every cited native support under direction key `K` must carry `K` in its canonical `direction_keys`. One bound native record permits only an `early_signal`-backed `new_signal`; `reinforced` requires two distinct in-window native records bound to the exact block key. `splits` and `retires` each require at least one bound in-window native support whose `map_delta` matches the state. Durable directions cite independent prior Field Map evidence; `no_material_change` has zero support and `prior=none`.

Closed-period digests deliberately become coarser with time:

`recent month → weekly` · `recent quarter → monthly` · `all years → yearly`

Show every available weekly compaction from roughly the last 31 days, monthly maps from the last 3 calendar months, and all sufficiently covered yearly maps. Each entry must state a research conclusion, not merely link a file. Rolling windows are mutable projections; closed ISO weeks and calendar months are immutable period identities. Open months/years must be labeled rolling or incomplete.

### Reading Paths and Research Map

Maintain about **3 reading paths**. Each path should teach a tension or design boundary, not act as a topic dump.

Maintain about **5–8 durable anchors** in README and `papers/anchors.md`. Anchors are design points, not rankings or a recency leaderboard.

For each research problem on README and its category page, maintain:

- Current anchors / current evidence;
- Strongest signal;
- Biggest unresolved question;
- Next decisive evidence.

Category pages are living arguments rather than append-only paper lists.

## Inclusion boundary

Include work when **information persists or is explicitly managed across interaction/reasoning steps and materially changes a language or multimodal agent’s future behavior**.

Typical in-scope changes affect one or more of:

- write / event boundaries / extraction;
- persistent representation and organization;
- retrieval, navigation, evidence completion, selection, or admission;
- consumer-facing reconstruction/rebinding/reuse;
- update, consolidation, conflict repair, forgetting, or revocation;
- learned/evolved memory state or policy;
- evaluation of lifecycle cost, authority, provenance, safety, or marginal behavioral effect.

Do not include generic fixed RAG, generic long-context modeling, KV-cache optimization, or unrelated continual learning unless persistent agent memory is central to the research contribution.

## Daily Agent research process

Use independent roles when the execution environment supports them. Their judgments should be formed separately before synthesis, and they never publish directly.

1. **Discovery Agent** — broad overlapping recent discovery; optimize recall and search beyond the literal phrase `agent memory`.
2. **Relevance / Taxonomy Agent** — decide semantic inclusion and assign one primary research problem plus orthogonal tags.
3. **Research Analyst** — read the full paper deeply enough to identify the mechanism, memory lifecycle, comparison, evidence, limitations, and provenance.
4. **Skeptical Reviewer** — challenge novelty, closest comparison, causal attribution, importance, resource matching, unsupported claims, duplicate versions, and link quality.
5. **Visual Editor / Visual QA Reviewer** — only for required visuals; ground briefs in the full paper and reject generic or fabricated images.
6. **Research Editor** — return a publication recommendation only after seeing disagreements and corrections from the independent roles; the Daily Agent orchestrator remains the writer.

Relevant papers that are not sufficiently reviewed remain private deferred/backfill candidates rather than being silently rejected or exposed as public pending entries.

## Canonical paper contract

For every accepted paper:

1. maintain `data/papers/<id>.json` as the canonical structured record;
2. maintain `papers/YYYY/<id>.md` as the researcher-facing note;
3. preserve Problem, Core Idea, Memory Design (`write / organize / read / update-forget`), Compared to What, Evidence, Why It Matters, Limitations/Questions, and confidence;
4. keep relevance separate from importance;
5. preserve provenance and add code/project links only when verified;
6. propagate a material correction upward to category pages, anchors, README, and affected compactions.

For records accepted at or after the v2 cutover, distinguish `published_at` (earliest public version), `first_seen_at` (first Radar observation), and `radar_published_at` (first accepted Radar publication), and assign `time_provenance` plus `map_delta`. Native timestamps are strict UTC and preserve event order. A native-v2 record cited as rolling-period support also declares a non-empty, unique stable-token `direction_keys` list containing the exact key of every direction it supports; unsupported native records may omit it. Existing field-absent `published` / `first_seen` records remain implicit legacy. Only the fixed eight Timeline compatibility identities are explicit `legacy_unknown` records with honest `published_at` precision and null discovery/Radar times; neither kind of legacy record carries `direction_keys`, so do not expand that migration or fabricate a bulk timestamp fill.

### Researcher-facing paper-note interface

High-visibility notes—at minimum papers currently exposed in README Latest Papers—should read like compact mini reviews rather than archival summaries. Use this order:

1. compact navigation back to Latest Papers, Research Map, and the primary category;
2. metadata line: canonical paper link, date, importance, confidence, tags, plus verified code/project links when present;
3. one-line **Research delta** stating the smallest claim that makes the paper worth reading;
4. **Problem**;
5. **Mechanism**, including a concise data/control-flow expression when useful;
6. **Compared with**, centered on the closest causal control rather than a long baseline inventory;
7. **Decisive evidence**, keeping only the result/ablation set needed to support the interpretation;
8. **Main caveat**, containing the strongest alternative explanation and concrete open questions;
9. **Memory lifecycle** table for write / organize / read / update-forget;
10. **Why it matters** as the field-level implication;
11. **Related reading** with 2–3 links and one sentence explaining the relationship.

Do not put visual-generation failures, scheduler state, upload blockers, or other maintenance-only status on researcher-facing paper notes. Accepted facts remain in canonical JSON; private workflow state remains only under ignored `.radar-private/` or in ephemeral Agent memory. Older archival notes may be backfilled gradually; do not rewrite them merely for cosmetic uniformity.

## Evidence discipline

The default causal lens is stage-specific:

`archive/representation → access program → evidence completion/selection/admission → consumer-facing state/reuse → update feedback/governance → lifecycle cost/provenance`

For every strong claim ask:

- **What actually changed?**
- **Compared with what?** Prefer the simplest matched alternative, not a weak straw baseline.
- **Which stage caused the gain?** Do not credit the whole architecture when several stages changed together.
- **What would falsify the interpretation?** Preserve negative results and stronger alternative explanations.

Unknowns remain unknown rather than being filled with plausible text.

## Importance scale

`relevance ∈ [0,1]` measures topical fit. `importance ∈ {1,...,5}` measures expected research significance.

- **5 — field-shaping:** changes an important abstraction, benchmark, or dominant research direction with unusually strong evidence.
- **4 — notable:** clear reusable technical/empirical delta researchers in agent memory should know.
- **3 — useful:** meaningful contribution but narrower delta, weaker attribution, or limited external validity.
- **2 — peripheral:** relevant but weak novelty/evidence or narrow scope.
- **1 — archival:** technically in scope but little reason to prioritize reading.

Recency and relevance do not imply importance.

## Visuals

Follow [`VISUAL_POLICY.md`](VISUAL_POLICY.md) and [`assets/README.md`](assets/README.md). A generated status is a publication claim: it is valid only when the exact WebP exists on `main`, the paper page embeds it, the image passed grounding/visual QA, and canonical metadata matches the published path.

## Compaction

Follow [`COMPACTION.md`](COMPACTION.md). Rolling periods and weekly/monthly/yearly reports are synthesis layers, not repeated paper summaries. Re-read canonical records and deep notes for load-bearing claims: weekly prose may be used as an index but must never be recursively summarized into monthly evidence. A one-paper observation must be labeled an early signal.

## Validation and final QC

Before completing a maintenance run, run the unit, canonical, reading, and repository validators. Check schema/taxonomy consistency, duplicate IDs/versions, paper-note existence, relative links, visual paths/embeds, important-paper visual blockers, Timeline structure and order without a fixed cap, researcher-facing paper-note structure, bilingual semantic parity, exact period windows, and due closed compactions.

## No public operational run logs

The repository publishes no Daily Agent operational log. Accepted provenance is the canonical record, complete bilingual Timeline, rolling periods, due closed digest, gated map update, and atomic Git commit. Private scouting, candidate, lane, retry, dissent, and validation traces belong only under ignored `.radar-private/runs/<run_id>.json` or in ephemeral Agent memory; [`runs/README.md`](runs/README.md) is static policy only.

## Licensing and contributions

Research notes, category maps, compactions, canonical paper data, and original radar visuals are licensed under **CC BY 4.0**. Maintenance code is licensed under **MIT**. See [`LICENSE.md`](LICENSE.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).
