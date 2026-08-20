# Agent Memory Radar Time-First v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Agent Memory Radar a compact time-first, inline-expandable research surface driven end-to-end by its Daily Scheduled Agent.

**Architecture:** Reuse the family protocol and parser from Agent Benchmark Radar verbatim, then keep Memory-specific lifecycle judgment in the local workflow. Convert the eight current cards into compact Timeline disclosures, move direction synthesis ahead of the stable lifecycle map, and preserve all deep notes and Library routes.

**Tech Stack:** Markdown, Python 3.12, `unittest`, JSON Schema, GitHub Actions.

**Spec:** `https://github.com/H20Zhang/Agent-Benchmark-Radar/blob/main/docs/superpowers/specs/2026-08-20-agent-maintained-time-first-radar-v2-design.md`

## Global Constraints

- The Daily Scheduled Agent is the only writer; candidates and failures remain internal.
- Public order is `Latest Timeline → 7-day / 30-day synthesis → Field Map → Reading Paths → Library`.
- Timeline has no fixed count cap and every current item is an inline `<details>` summary with Question, Evidence, Caveat, Map, and Links.
- Do not fabricate `radar_published_at`; current legacy cards retain honest paper-date order under one migration notice.
- Memory claims identify the lifecycle boundary and closest lifecycle-matched control; retrieval is not automatically reuse.
- A record may be `early_signal`; a durable map change requires historical comparison and independent support.
- Chinese/English identities, dates/order, evidence scope, map status, and links remain paired.
- Preserve all canonical records, notes, visuals, categories, compactions, and benchmark genealogy boundary.

---

### Task 1: Apply the v2 family contract to Agent Memory Radar

**Files:**
- Create: `docs/RADAR_AGENT_PROTOCOL.md`
- Modify: `docs/DAILY_WORKFLOW.md`
- Modify: `CURATION.md`
- Modify: `COMPACTION.md`
- Modify: `data/paper.schema.json`
- Modify: `README.md`
- Modify: `README.en.md`
- Create: `scripts/timefirst_contract.py`
- Create: `tests/test_timefirst_contract.py`
- Modify: `scripts/validate_reading.py`
- Modify: `scripts/validate.py`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes verbatim: `docs/RADAR_AGENT_PROTOCOL.md`, `scripts/timefirst_contract.py`, and the generic fixture tests from the merged Benchmark v2 implementation.
- Adds stable aliases: `timeline`, `latest`, `latest-papers`, `periods`, `changes`, `whats-changing`, `last-7-days`, `last-30-days`, `field-map`, `research-map`, `reading-paths`, `library`.
- Routes evaluation intent to `Agent-Benchmark-Radar#benchmark-memory`.

- [x] **Step 1: Copy the generic validator/tests and verify RED against the existing README**

Copy the merged Benchmark `scripts/timefirst_contract.py` and its generic fixture tests without semantic changes. Add this repository assertion to `tests/test_timefirst_contract.py`:

```python
def test_repository_readmes_satisfy_contract(self):
    errors = validate_pair(
        (ROOT / "README.md").read_text(encoding="utf-8"),
        (ROOT / "README.en.md").read_text(encoding="utf-8"),
    )
    self.assertEqual([], errors)
```

Run: `python -m unittest discover -s tests -v`

Expected: the generic fixtures pass, while the repository assertion fails because Timeline/period anchors and compact disclosure entries do not yet exist.

- [x] **Step 2: Convert both current Latest sections into Timeline disclosures**

Co-locate `<a id="timeline"></a><a id="latest"></a><a id="latest-papers"></a>` before the first H2. Keep all eight current identities and paper publication dates in descending order. Convert each card into:

```markdown
<a id="entry-2608-17911"></a>
<details>
<summary><strong>2026-08-18 · CABLE</strong> · Retrieval & Access — one-sentence research delta</summary>

**问题。** ... closest lifecycle-matched control ...

**证据。** ... decisive evidence ...

**限制。** ... strongest alternative / missing cost ...

**地图。** `early_signal` — ... lifecycle boundary ...

**链接。** [Paper](https://paper.example) · [中文深读](https://zh-note.example) · [English note](https://en-note.example)

</details>
```

Use `Question/Evidence/Caveat/Map/Links` in English. Reuse and tighten the existing card text; do not invent new quantitative claims. Keep deep-note and visual links. Add one section-level legacy notice that these current records use paper publication dates because reliable Radar acceptance timestamps were not historically stored.

- [x] **Step 3: Turn the current change table into explicit period synthesis**

Co-locate `<a id="periods"></a><a id="changes"></a><a id="whats-changing"></a>` after Timeline. Add:

- `last-7-days`, window `2026-08-14—2026-08-20`, covering the new lifecycle evidence in the seven-day window;
- `last-30-days`, window `2026-07-22—2026-08-20`, preserving the strongest current three direction judgments.

Each direction states `new_signal|reinforced|revised|no_material_change`, supporting paper identities, confidence, and research-design implication. Preserve links to existing weekly/monthly/yearly compactions. Put `<a id="field-map"></a><a id="research-map"></a>` before the lifecycle map, followed by Reading Paths and Library. Change the top navigation to Timeline → periods → Field Map → paths → Library. Route the evaluation link to `Agent-Benchmark-Radar#benchmark-memory`.

- [x] **Step 4: Install the shared protocol and Memory adapter**

Copy the merged Benchmark `docs/RADAR_AGENT_PROTOCOL.md` verbatim. Rewrite `docs/DAILY_WORKFLOW.md` as the Memory adapter: discovery lanes, identity-before-scope, full-text evidence, skeptical audit, lifecycle fields, closest matched control, Timeline projection, period boundaries, map gate, bilingual atomicity, validation, and silent no-change exit. Preserve useful existing note/visual rules.

Update `CURATION.md` and `COMPACTION.md` to make the Daily Agent the normal editor, keep candidates private, distinguish `published_at/first_seen_at/radar_published_at`, make rolling versus closed periods explicit, and forbid recursive summary evidence.

Extend `data/paper.schema.json` with optional cutover fields:

```json
"published_at": {"type": ["string", "null"]},
"first_seen_at": {"type": ["string", "null"]},
"radar_published_at": {"type": ["string", "null"]},
"time_provenance": {"enum": ["native_v2", "legacy_unknown", null]},
"map_delta": {"enum": ["none", "early_signal", "reinforces", "revises", "splits", "retires", null]}
```

Do not bulk-fill legacy timestamps.

- [x] **Step 5: Wire validation, remove caps, and verify GREEN**

Make `scripts/validate_reading.py` call `validate_pair`, retain canonical/link/family checks, and delete its `6–8` bound. In `scripts/validate.py`, replace the legacy `8–10` Latest-card bound with structural recognition of any non-empty Timeline; update parsing for `entry-*` disclosures while retaining note navigation checks. Do not loosen unrelated visual/category validation.

Update `.github/workflows/validate.yml` to run unit tests before canonical and reading validators. Run with the shared environment Python:

```bash
python -m unittest discover -s tests -v
python scripts/validate_canonical.py
python scripts/validate_reading.py
python scripts/validate.py
```

Expected: all tests and all three validators exit 0 with pristine output.

- [x] **Step 6: Self-review and commit**

Check every current identity remains reachable; each item has one disclosure and five semantic fields; current dates are honest; no fixed Timeline cap or public pending state remains; period windows match across languages; deep-note/visual links resolve; category/digest compatibility anchors remain.

Commit:

```bash
git add docs/superpowers/plans/2026-08-20-time-first-radar-v2-memory.md docs/RADAR_AGENT_PROTOCOL.md docs/DAILY_WORKFLOW.md CURATION.md COMPACTION.md data/paper.schema.json README.md README.en.md scripts/timefirst_contract.py tests/test_timefirst_contract.py scripts/validate_reading.py scripts/validate.py .github/workflows/validate.yml
git commit -m "Add agent-maintained time-first memory radar"
```
