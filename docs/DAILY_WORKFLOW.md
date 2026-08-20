# Daily Agent Memory Adapter

This file adapts [Radar Agent Protocol v2](RADAR_AGENT_PROTOCOL.md) to Agent Memory Radar. The shared protocol governs role separation, private candidate states, canonical timestamps, atomic publication, bilingual projection, period boundaries, retries, and silent no-change completion. This adapter governs Agent Memory scope, lifecycle evidence, notes, visuals, and map consequences.

## Repository role

Agent Memory Radar is the Research Radar family's method-and-system surface for persistent agent state. Agent Benchmark Radar owns the horizontal evaluation genealogy; route evaluation intent to `Agent-Benchmark-Radar#benchmark-memory` rather than duplicating that genealogy here.

The Daily Agent is the normal and only repository writer. Research roles may return evidence and judgments, but only the orchestrator mutates canonical records, reader projections, digests, or GitHub state.

## Source lanes

Freeze and report each lane independently:

- primary paper sources and proceedings for long-term, episodic, semantic, procedural, multimodal, personalized, and structured agent memory;
- official paper/project repositories and verified protocol or version releases;
- adjacent retrieval, tool-use, personalization, continual-learning, and long-context work that may cross the inclusion boundary;
- independent replication, negative evidence, stronger baselines, cost studies, and safety/governance corrections;
- bounded historical backfill for lifecycle predecessors repeatedly cited by accepted frontier work.

Search beyond the literal phrase `agent memory`, including experience reuse, skill libraries, interaction state, user-state modeling, trajectory storage, consolidation, forgetting, memory-guided action, and stateful raw-log search. Prefer primary sources. Product or vendor material may identify a lead but cannot alone support a paper claim.

## Identity before scope

Resolve arXiv, DOI, venue, repository, renamed/versioned paper, and protocol-release identities before deciding relevance. Never merge on title similarity alone. A material version correction is an event attached to the original identity, not a second paper.

Only after identity resolution apply `CURATION.md`: information must persist or be explicitly managed across interaction/reasoning steps and materially change later agent behavior. Generic fixed RAG, generic long-context/KV-cache work, and unrelated continual learning remain out of scope unless persistent agent state is central.

## Full-text evidence and skeptical audit

Abstract-only judgment cannot reach `ACCEPTED`. From full text or equivalent primary protocol evidence, record:

1. the research question and smallest real delta;
2. the affected lifecycle boundary;
3. the closest lifecycle-matched control;
4. decisive evidence and its source location;
5. the strongest alternative explanation, negative result, or missing evidence;
6. offline and online lifecycle costs;
7. the resulting `map_delta` and why it meets—or does not meet—the map gate.

The Skeptical Reviewer challenges novelty, identity, baseline strength, causal attribution, evidence budget, model/task matching, costs, and external validity. It never invents facts. A blocked full text, unresolved identity, or missing decisive control moves the private candidate to `BLOCKED` or `DEFERRED`; no public pending record is created.

## Memory lifecycle record

For every accepted work, preserve the relevant fields across:

`source experience → write/event boundary → representation/organization → state localization → access/selection/admission → consumer-state reconstruction/reuse → update/consolidation/forgetting → governance/provenance → lifecycle cost`

Retrieval is not automatically reuse. If evidence is selected but must be reconstructed, rebound, transformed into a skill, or admitted under authority constraints, record that as a separate stage. Attribute a gain only to the smallest stage isolated by the comparison.

The closest control must match the claimed lifecycle boundary. Structure claims need a competent raw-record or online-search interface; writer claims need the same executor and feedback budget; reconstruction claims need matched retrieved evidence and synthesis budget; governance claims need matched artifacts and executor conditions. When several stages change together, state system-level evidence.

## Canonical-first update

For accepted work, update in this order:

1. `data/papers/<id>.json` with identity, provenance, classification, analysis, and time/map fields;
2. `papers/YYYY/<id>.md` and its Chinese counterpart when needed for the evidence audit;
3. category, research-line, anchor, and Library relationships;
4. `README.md` and `README.en.md` Timeline and rolling period projections;
5. closed-period digest if a boundary is due;
6. validation and one atomic commit.

## No public operational run logs

Never create a committed operational or daily-run file. Private scouting, candidate, lane, retry, dissent, and validation traces belong only under ignored `.radar-private/runs/<run_id>.json` or in ephemeral Agent memory. Public provenance is canonical data, the complete bilingual Timeline and rolling-period projection, any due closed digest, the gated Field Map, and one atomic Git commit. `runs/README.md` is static policy only.

New v2 records distinguish:

- `published_at`: earliest public version of the work;
- `first_seen_at`: first observation by this Radar's discovery process;
- `radar_published_at`: first accepted public publication in this Radar.

Untouched records with no v2 fields remain implicit legacy. The fixed eight Timeline compatibility records are the only explicit legacy migration: they preserve `published` exactly as `published_at`, keep `first_seen_at` and `radar_published_at` null, and use `legacy_unknown` plus `early_signal`. Every post-cutover acceptance is a complete native-v2 record with strict UTC timestamps ordered `published_at <= first_seen_at <= radar_published_at`. Never infer unknown acceptance times from arXiv identifiers, venue dates, commit dates, or scheduler runs, and never bulk-fill legacy timestamps.

Native-v2 records used as rolling-period supports also declare `direction_keys`, a non-empty list of unique lowercase stable tokens. A support cited by a direction block with key `K` must carry that exact `K`; records count as same-direction reinforcement only when every cited support carries the block key. `direction_keys` by itself requires the complete native-v2 time bundle. Native-v2 records not used as supports may omit it, and legacy records never carry it, so this adapter does not trigger a bulk migration.

## Notes and visuals

A high-visibility note resolves `Research delta → Problem → Mechanism → Closest comparison → Decisive evidence → Main caveat → Memory lifecycle → Why it matters → Related reading`. Preserve paper titles, model/dataset names, metrics, uncertainty, and source locations; do not turn author claims into verified facts.

Follow `VISUAL_POLICY.md` and `assets/README.md`. A visual must add explanatory value, be grounded in the full paper, pass grounding and visual QA, exist as the required WebP, be embedded in the note, and match canonical metadata before its status becomes `generated`. Visual-generation failures and upload blockers stay private.

## Timeline projection

Public order is `Latest Timeline → 7-day / 30-day synthesis → Field Map → Reading Paths → Library`. Timeline contains every accepted native-v2 record whose `radar_published_at` falls in the current 30-day window and is no later than the exact public synthesis cutoff shared by Timeline and both rolling periods, sorted by its full timestamp, followed by the fixed eight compatibility records in their preserved legacy order. It has no fixed item cap. A compatibility entry with unknown Radar acceptance time retains its honest paper publication date under the section-level migration notice.

Each `entry-*` disclosure has one closed summary containing displayed date, identity, lifecycle/problem label, and one-sentence delta. Its open body contains Question, Evidence, Caveat, Map, and Links. Preserve the paper, both local deep-note routes, and any published visual route. The Chinese and English versions carry one identity, date/order, evidence scope, caveat scope, map token, and link set.

Keep the public entry surfaces index-like. Open with one compact Radar Family sibling line and one layer-time navigation line: `30 sec Timeline → 3 min 7/30-day changes → 5 min Field Map → 15 min Reading Paths → Browse all`. These labels describe the depth of each route; they do not belong in individual fold summaries. Do not add repeated `Research delta` or `Takeaway` labels around the required Timeline fields, and do not paraphrase every row of a table in adjacent prose.

## Period boundaries and synthesis

Rolling 7-day and 30-day sections state exactly one visible inclusive window and the exact UTC synthesis timestamp shared with the Timeline cutoff. Native membership and support use only `radar_published_at` values no later than that same cutoff; legacy records may provide Field Map context but never native window support. Re-read canonical records and deep notes in each window; do not summarize weekly prose to produce a monthly claim.

Every direction is labeled `new_signal`, `reinforced`, `revised`, `splits`, `retires`, or `no_material_change`. Stable metadata and visible prose bind its key, state, ordered canonical supports, `low` / `medium` / `high` confidence, implication witness, `radar_published_at` basis, exact synthesis timestamp, and prior-map evidence; Chinese and English metadata must match semantically. Every native support under direction key `K` must include `K` in canonical `direction_keys`. One bound native support permits only `new_signal` with `map_delta=early_signal`; `reinforced` needs at least two distinct in-window native supports bound to the exact block key. `reinforced` and `revised` cite independent prior Field Map evidence. `splits` and `retires` each require at least one bound, in-window native support with the matching `map_delta`, plus independent prior Field Map evidence. `no_material_change` has zero support and `prior=none`.

On the first successful run after an ISO week closes, write the missing immutable digest for that complete week. On the first successful run of a new month, write the missing immutable digest for the previous calendar month. The Daily Agent owns both boundary checks; retries use idempotent period identities.

## Field Map gate

Assign exactly one `map_delta`: `none`, `early_signal`, `reinforces`, `revises`, `splits`, or `retires`.

- `early_signal` may change Timeline and period synthesis but not a durable Field Map node.
- `reinforces` names at least two independent accepted identities supporting the same lifecycle direction.
- `revises`, `splits`, and `retires` record the previous map claim, new evidence, strongest alternative, and smallest reversible edit.

Shared vocabulary, temporal proximity, or one notable paper is not historical comparison. Preserve the current map when the gate is not met.

## Bilingual atomicity

Chinese is the default public surface and English is a complete counterpart. Material changes to identity, dates, lifecycle boundary, closest control, decisive evidence, caveat, map status, links, period windows, reading routes, or Library relationships update both languages in the same transaction. English should be natural prose from the same judgment, not a shortened translation.

## Validation and publication

Run from the repository root:

```bash
python -m unittest discover -s tests -v
python scripts/validate_canonical.py
python scripts/validate_reading.py
python scripts/validate.py
```

All commands must exit zero without warnings or errors. Inspect the diff for duplicate identities, invented time precision, public candidate states, fixed Timeline caps, unpaired links, broken notes/visuals, category drift, recursive period evidence, evaluation-genealogy duplication, and claims that outrun the closest matched control.

Before publishing, recheck the frozen repository head. If it moved, abort, re-read affected canonical state, re-render, and retry without force-pushing. A material run produces one commit containing canonical state, both languages, derived surfaces, and due digests, without a public run log.

If no candidate survives the evidence and skeptical-audit gates and no correction, period boundary, or deterministic repair is due, validate and exit without a content commit or notification.
