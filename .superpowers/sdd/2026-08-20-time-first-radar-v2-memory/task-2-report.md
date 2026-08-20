# Task 2 Report: Harden the Agent Memory Radar family contract

Date: `2026-08-20`

Branch: `agent/time-first-radar-v2`

Base: `46b23b91a220f6dfb4abc46f0f6a0f1ff6830adf`

Approved references:

- Agent Benchmark Radar `893827a`
- Agentic RAG Radar `c8b1441`
- `task-2-brief.md` plus the controller ruling

## Result

Agent Memory Radar now enforces the approved v2 public-state and time-first contract while preserving its lifecycle Field Map, all eight Timeline research judgments, canonical publication dates, paired deep notes, visuals, and prior compactions.

The repository has no public operational run logs. The fixed eight Timeline records are the only explicit legacy migration; every other pre-v2 record remains field-absent implicit legacy. Native-v2 records must use complete, ordered, strict UTC timestamps at or after cutover. The bilingual Timeline is a reverse projection of canonical state, and the current 7-day and 30-day sections are exact structured `no_material_change` judgments based only on `radar_published_at`.

No Radar acceptance timestamp was invented.

## TDD evidence

### Baseline

Before Task 2 mutations, the existing repository suites and validators were green:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
Ran 20 tests
OK

$ python scripts/validate_canonical.py
Validated 41 canonical Agent Memory records.

$ python scripts/validate_reading.py
Validated Chinese-first bilingual progressive reading surfaces.

$ python scripts/validate.py
Validated 41 canonical paper records and reader-facing repository contracts.
```

### Shared common-core parser RED → GREEN

The Benchmark `893827a` regression tests were added first. The old parser failed comment masking and exact period-range cardinality:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest tests/test_timefirst_contract.py -v
Ran 23 tests
FAILED (failures=9)
```

After applying the approved common parser:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest tests/test_timefirst_contract.py -v
Ran 23 tests
OK
```

The final parser and its tests are byte-identical to Benchmark `893827a`, including comment stripping, offset-preserving field-label masking, exactly one visible range per period, inclusive cardinality, and a shared synthesis endpoint.

### Public-run absence RED → GREEN

API and behavior were introduced test-first. Before the guard, file, path-as-file, broken-symlink, ignore-policy, repository, and guidance checks failed:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest tests/test_run_log_contract.py -v
Ran 7 tests
FAILED (failures=11)
```

An explicit integration RED also proved that `validate_reading.py` did not yet invoke the guard:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest \
  tests.test_run_log_contract.NoPublicRunLogContractTest.test_reading_validator_runs_the_absence_guard -v
FAIL: expected 1, got 0
```

After implementing and wiring the guard, deleting the nine tracked daily logs, adding static policy, and aligning authoritative guidance:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest tests/test_run_log_contract.py -v
Ran 7 tests
OK
```

### Canonical time contract RED → GREEN

Time-combination tests were added before implementation for partial v2 records, invalid legacy/native combinations, UTC precision, event order, cutover, map values, exactly-eight migration, schema nullability, and all validator entry points:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest tests/test_memory_v2_contract.py -v
Ran 14 tests
FAILED (failures=12)
```

After implementing the registry contract, migrating only the fixed identities, tightening the schema, and wiring canonical/reading/full validators:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest -v
Ran 14 tests
OK
```

### Reverse Timeline and period contracts RED → GREEN

The projection API was first required by a failing existence test, then exposed as an empty seam. Behavior tests against that empty seam captured missing/duplicate/unexpected Timeline identities; same-day full-timestamp order; displayed date, map, primary-paper and paired-note drift; comment laundering; exact ranges; bilingual metadata parity; confidence/implication/timing/synthesis witnesses; Radar-window support; one-paper, trend and prior-map gates; and zero-support `no_material_change`:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest tests.test_memory_v2_contract.MemoryProjectionContractTest -v
Ran 9 tests
FAILED (failures=23)
```

After implementing the Memory adapter:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest tests.test_memory_v2_contract.MemoryProjectionContractTest -v
Ran 12 tests
OK
```

The integration test then demonstrated a missing `main()` call:

```text
$ python -m unittest \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_reading_validator_enforces_memory_projection -v
FAIL: expected 1, got 0
```

After wiring it, the test passed. The newly strict validator then rejected the old publication-date-derived rolling prose with 18 metadata errors:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate_reading.py
ERROR README.md: last-7-days direction ... requires exactly one stable direction metadata block
...
ERROR README.en.md: last-30-days has no parseable direction metadata
Reading-surface validation failed with 18 error(s).
```

Rewriting both language projections to the canonical empty Radar-acceptance windows produced GREEN:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate_reading.py
Validated Chinese-first bilingual progressive reading surfaces.
```

A final focused RED proved that an HTML-comment-hidden family route still counted as navigation; stripping comments in the Memory route adapter made that test GREEN.

### Field-scoped witness hardening RED → GREEN

Staged self-review added adversarial tests that left a correct token elsewhere on the line while corrupting its labeled field. The first run proved that generic line-wide matching could launder four bindings:

```text
$ python -m unittest \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_period_metadata_and_visible_bindings_are_complete_and_bilingual -v
FAILED (failures=4)
```

Direction keys are now scoped to the bold heading, and implication, timing, and synthesis witnesses are scoped to their labeled visible fields. Two more RED runs proved that support or prior links elsewhere on the line, primary/deep-note links outside the Links field, and a visible `none` contradiction could still launder the intended field:

```text
support/prior laundering: FAILED (failures=2)
primary/deep-note field laundering: FAILED (failures=2)
support-none contradiction: FAILED (failures=1)
```

The minimal fixes scope support, prior, primary, and deep-note extraction to their labeled fields and reject contradictory visible support. All focused tests then passed.

## Final validation

Fresh final commands:

```bash
export PYTHONPATH=/tmp/agent-memory-radar-deps
export PYTHONDONTWRITEBYTECODE=1
python -m unittest discover -s tests -v
python scripts/validate_canonical.py
python scripts/validate_reading.py
python scripts/validate.py
```

Final output:

```text
Ran 60 tests in 0.168s
OK
Validated 41 canonical Agent Memory records.
Validated Chinese-first bilingual progressive reading surfaces.
Validated 41 canonical paper records and reader-facing repository contracts.
```

`scripts/validate.py` includes the repository-relative link audit. Additional mechanical checks passed:

```text
parser-exact
tests-exact
public-run-absence-ok
private-state-ignore-ok
benchmark-memory-route-ok
exact-witness-wording-ok
python-compile-ok
git diff --check: clean
```

Shared SHA-256 values:

```text
f1649a6b081ad889e0779dc494a6221bb2701a190f4ec5b2c35d32f7e76ed5e7  scripts/timefirst_contract.py
102718fc5ce3d86072056e6cf5bc43653e85144e976362f588ea0bae9bda4af1  tests/test_timefirst_contract.py
```

## Files changed

- `.gitignore` — ignores Python bytecode and `.radar-private/` state.
- `runs/README.md` — static no-public-run policy.
- `runs/daily/2026/08/{10,12,13,14,16,17,18,19,20}.md` — removed; history remains recoverable from Git.
- `tests/test_run_log_contract.py` — absence, path-as-file, symlink, ignore, integration, repository, and guidance checks.
- `scripts/timefirst_contract.py`, `tests/test_timefirst_contract.py` — exact Benchmark `893827a` common artifacts.
- `data/paper.schema.json` — non-null explicit provenance/map/published-time schema surface.
- `data/papers/2608.{17911,17756,17587,17588,17534,16168,16114,12888}.json` — the only explicit legacy migration.
- `scripts/validate_reading.py` — run absence, time registry, hyphen/dotted Timeline adapter, canonical reverse binding, paired notes, exact period metadata and support gates.
- `scripts/validate_canonical.py`, `scripts/validate.py` — registry-time enforcement at all public validator entry points.
- `tests/test_memory_v2_contract.py` — canonical, Timeline, rolling-period, visible-binding, support-gate, comment-laundering, and integration coverage.
- `README.md`, `README.en.md` — exact current windows and structured `no_material_change` Radar-acceptance judgments with visible bilingual metadata.
- `docs/RADAR_AGENT_PROTOCOL.md`, `docs/DAILY_WORKFLOW.md`, `docs/MAINTENANCE.md`, `docs/BILINGUAL_PUBLICATION.md`, `CURATION.md`, `COMPACTION.md`, `digests/README.md`, and the paper-note reading-interface design — aligned public-state, time, projection, and no-public-run guidance.
- `.superpowers/sdd/2026-08-20-time-first-radar-v2-memory/task-2-report.md` — this report.

## Self-review

- The Timeline still contains exactly CABLE, D²ACCI, WER, TRUSS, ArborMem, QUMem, HyperSkill, and ReFind in the required fixed legacy order.
- Each migrated record retains its exact existing `published` value as `published_at`; legacy `first_seen` remains untouched; both new discovery/Radar timestamps are null; provenance is `legacy_unknown`; map delta is `early_signal`.
- The other 33 records have no v2 fields and remain implicit legacy.
- No `radar_published_at` value exists in the current canonical registry, so both rolling windows correctly expose one `no_material_change` direction with zero support.
- Legacy names remain visible only as historical lifecycle context, never as entry-anchor supports.
- The adapter maps dotted canonical IDs to hyphenated entry anchors without changing public anchors, validates full native timestamp order before the legacy set, and checks canonical dates, map tokens, primary papers, and exactly one Chinese plus English note link per entry.
- Visible direction prose binds the key, state, support order, confidence enum, implication witness, timing basis, prior-map evidence, and exact `2026-08-20T00:00:00Z` synthesis time in both languages.
- A one-paper direction is limited to `new_signal` with `early_signal`; `reinforced` needs two in-window native supports; durable states require a visible `#field-map` prior; legacy and out-of-window records fail support validation.
- HTML comments cannot rescue routes, Timeline links/map tokens, period supports, ranges, or semantic field witnesses.
- The lifecycle Field Map, paper claims, metrics, notes, visual assets, categories, Library, and historical digest claims were preserved.
- The exact evaluation route remains `#benchmark-memory`.

## Concerns

- No implementation blocker remains.
- The expected rolling windows and exact synthesis timestamp are deliberately version-bound to the `2026-08-20` contract. A future material Radar publication must advance them transactionally with both README projections and validator constants.
- The managed runtime requires the existing validation dependencies through `/tmp/agent-memory-radar-deps`; repository CI installs the unchanged `requirements.txt` normally.

---

## Review fix round 1

Review base: `f57e644cfa7c706ce5fb1b6687ef94330a4ff238`

Approved common-core reference: Agent Benchmark Radar `ea41c69c5c3f01f4256c7f7e8ec828d210e5d54b`

### Result

The review findings are fixed without changing either README, any canonical record, any deep note, any visual, any lifecycle Field Map material, or any historical claim. No Radar timestamp was added or invented.

- The common parser and common tests are byte-identical to Benchmark `ea41c69`, including comment-masked stable anchors and structural aliases.
- Native Timeline projection and rolling support now both stop at the public synthesis instant, not merely its calendar day. A `2026-08-20T01:00:00Z` acceptance cannot appear in or support a direction synthesized at `2026-08-20T00:00:00Z`.
- Period judgments are parsed as complete, bounded direction blocks. Each block requires exactly one visible, language-specific state, support, confidence, timing-basis, synthesis, implication, and prior field. Label cardinality is counted independently from value syntax, so a malformed primary label cannot be rescued by a valid labeled aside.
- Zero support is exactly `**none**`; nonempty support fields contain only ordered canonical entry links. One-paper trend claims are rejected across the complete block, including indented continuations and attached paragraphs, while the next period and Field Map stay outside the block.
- Stable machine metadata stays comment-only and is compared pairwise with the visible fields.
- JSON Schema now encodes the v2 fields as all-or-none through both `dependentRequired` and `oneOf`, while field-absent implicit legacy records remain valid.
- Memory compatibility aliases and family routes are evaluated only on comment-stripped visible Markdown.

### RED evidence

#### Comment-masked common anchors

The two Benchmark regression tests were copied first. The prior common parser accepted hidden-only anchors and counted hidden decoys as duplicates:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest \
  tests.test_timefirst_contract.TimeFirstContractTest.test_html_commented_common_anchor_does_not_satisfy_required_anchor \
  tests.test_timefirst_contract.TimeFirstContractTest.test_hidden_anchor_decoy_does_not_duplicate_legitimate_visible_anchor -v
Ran 2 tests
FAILED (failures=16)
```

#### Exact synthesis cutoff

The `01:00` native Timeline/support probes were added and the previously valid same-day ordering fixture was corrected to use records accepted exactly at the `00:00` synthesis instant. Before implementation, both late-acceptance probes returned no errors:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_native_timeline_rejects_acceptance_after_public_synthesis_cutoff \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_support_at_0100_cannot_backdate_a_0000_direction_synthesis \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_native_timeline_uses_full_timestamp_then_identity_order_before_legacy \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_period_support_is_visible_native_in_window_and_state_gated -v
Ran 4 tests
FAILED (failures=2)
```

#### Scoped complete direction blocks, schema, and visible aliases

Tests were added before implementation for all seven visible fields in both languages, multiline continuation fields, wrong-language labels, exact `none`, continuation/attached-paragraph trends, section boundaries, schema all-or-none behavior, and hidden alias cardinality:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest -v \
  tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest.test_schema_encodes_v2_fields_as_all_or_none_while_allowing_implicit_legacy \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_memory_aliases_are_visible_comment_stripped_and_cardinality_bound \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_period_direction_blocks_require_exactly_one_of_each_visible_field \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_period_direction_fields_may_live_on_continuation_lines \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_period_direction_requires_its_language_specific_visible_labels \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_zero_support_visible_field_is_exact_not_an_aside_prefix \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_one_paper_signal_rejects_trend_in_continuations_and_attached_paragraphs \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_next_period_and_field_map_prose_are_outside_direction_blocks
Ran 8 tests
FAILED (failures=34, errors=1)
```

An adversarial self-review then exposed a subtler first-complete-match path: a malformed primary label followed by a valid labeled aside still passed for every structured field tested. The dedicated CN/EN probe was RED in all 12 cases:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest -v \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_malformed_primary_fields_cannot_be_laundered_by_valid_labeled_asides
Ran 1 test
FAILED (failures=12)
```

### GREEN evidence

The common suite after the exact Benchmark backport:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest tests/test_timefirst_contract.py -v
Ran 25 tests
OK
```

The exact synthesis-cutoff set after Timeline/support cutoff enforcement:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_native_timeline_rejects_acceptance_after_public_synthesis_cutoff \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_support_at_0100_cannot_backdate_a_0000_direction_synthesis \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_native_timeline_uses_full_timestamp_then_identity_order_before_legacy \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_period_support_is_visible_native_in_window_and_state_gated -v
Ran 4 tests
OK
```

The eight initial review probes after the block parser, schema, and alias changes:

```text
Ran 8 tests
OK
```

The malformed-primary/labeled-aside probe after separating label cardinality from value parsing:

```text
Ran 1 test
OK
```

Schema enforcement initially made two validator-integration fixtures fail before their intended assertion because their temporary registries lived outside the repository root:

```text
Ran 62 tests
FAILED (errors=2)
```

Moving only those test fixtures under the repository root preserved the production validators and restored the intended entry-point assertions:

```text
Ran 2 tests
OK
```

### Fresh full verification

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
Ran 73 tests in 0.208s
OK

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python scripts/validate_canonical.py
Validated 41 canonical Agent Memory records.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python scripts/validate_reading.py
Validated Chinese-first bilingual progressive reading surfaces.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python scripts/validate.py
Validated 41 canonical paper records and reader-facing repository contracts.
```

Mechanical audits also passed:

```text
common parser cmp to Benchmark ea41c69: exit 0
common tests cmp to Benchmark ea41c69: exit 0
public runs/daily tracked-file absence: exit 0
.radar-private ignore probe: exit 0
exact bilingual #benchmark-memory route count: exit 0
README/data/papers/notes/visuals/categories/library/digests preservation diff: exit 0
python compile: exit 0
git diff --check: exit 0
```

Current common-file hashes:

```text
c1a2e98ee0f4e08c4836387a313eb9d8b7ab60b69367b6a4097605b6831c4dae  scripts/timefirst_contract.py
f1a95c110710ed666f2070c21a592ad24fa69d1c3872c2167714f18fd0fdbc40  tests/test_timefirst_contract.py
```

### Files changed in review fix round 1

- `scripts/timefirst_contract.py`, `tests/test_timefirst_contract.py` — exact Benchmark `ea41c69` common artifacts.
- `scripts/validate_reading.py` — synthesis cutoff, bounded direction-block parser, exact visible-field cardinality/structure, one-paper trend scope, and comment-stripped Memory aliases.
- `data/paper.schema.json` — all-or-none v2 field combination in JSON Schema.
- `tests/test_memory_v2_contract.py` — exact cutoff, block completeness/cardinality, aside laundering, language labels, trend continuation/boundary, alias, and schema probes.
- `.superpowers/sdd/2026-08-20-time-first-radar-v2-memory/task-2-report.md` — this review-fix evidence.

### Fix self-review and concerns

- The common files were not locally customized; both byte comparisons target the binding reviewed Benchmark commit.
- The Timeline cutoff uses the exact public synthesis instant before selecting/sorting native identities. A late accepted record omitted from the public projection is not treated as missing; the same record becomes an explicit cutoff error if displayed or cited as support.
- Support window and synthesis checks are independent, so a late record can report both violations when applicable.
- Complete direction blocks begin at a visible direction heading or stable machine block, stop at the next direction, and are already bounded by the current period section. Trend prose in a continuation belongs to the direction; next-period and Field Map prose do not.
- Label count and value structure are distinct checks. Hidden comments, duplicate labels, malformed-primary plus valid-aside pairs, wrong-language labels, support prose outside the support field, and contradictory `none` all fail.
- All current production directions still parse identically and remain pairwise equal across Chinese and English.
- The schema accepts every current canonical record, including all 33 implicit legacy records and the fixed eight explicit legacy records.
- No implementation blocker remains. The version-bound synthesis timestamp/window concern from the original report remains unchanged.

---

## Review fix round 2

Review base: `e82302f46132ca4bac761acc4d336c697a1466ac`

### Result

Direction block discovery now uses visible direction list items as the only block boundaries. A stable metadata comment on the heading line, at the end of a natural continuation, or on its own continuation line belongs to the open visible item. Multiple metadata comments inside that item are therefore counted together and rejected, while the next visible direction list item still begins a separate block.

The fix changes no public projection, canonical data, research claim, note, visual, lifecycle map, timestamp, common parser, or common test.

### RED evidence

Four exact behavior probes were added before changing block discovery:

- the requested English reproduction `direction_line("en").replace(" Supports:", "\n  Supports:", 1)` plus its Chinese counterpart;
- a stable metadata comment moved to its own continuation line;
- a true second metadata comment on a continuation line;
- two adjacent visible direction items, with the second item's metadata on its own continuation line.

The old implementation treated every metadata-bearing continuation as a new block. Both valid multiline forms and the adjacent-item form were rejected, while the duplicate comment escaped the intended block-level cardinality error as an orphan item:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest -v \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_direction_metadata_at_continuation_end_stays_in_visible_item_block \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_metadata_only_continuation_stays_in_visible_direction_item \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_true_duplicate_metadata_on_continuation_is_rejected \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_adjacent_visible_direction_items_remain_distinct_block_boundaries
Ran 4 tests
FAILED (failures=4)
```

### GREEN evidence

The minimal production change removed metadata-comment lines from the block-start predicate. The same focused command then passed:

```text
Ran 4 tests in 0.011s
OK
```

Fresh complete verification:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
Ran 77 tests in 0.236s
OK

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python scripts/validate_canonical.py
Validated 41 canonical Agent Memory records.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python scripts/validate_reading.py
Validated Chinese-first bilingual progressive reading surfaces.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 python scripts/validate.py
Validated 41 canonical paper records and reader-facing repository contracts.
```

Mechanical audits:

```text
common parser/tests cmp to Benchmark ea41c69: exit 0
public-run absence/private-state ignore/#benchmark-memory route: exit 0
README/data/notes/visuals/maps/digests preservation diff: exit 0
python compile: exit 0
git diff --check: exit 0
```

### Files changed in review fix round 2

- `scripts/validate_reading.py` — visible direction headings are the only item boundaries.
- `tests/test_memory_v2_contract.py` — exact natural-continuation, metadata-only, duplicate-metadata, and adjacent-item regressions.
- `.superpowers/sdd/2026-08-20-time-first-radar-v2-memory/task-2-report.md` — this RED/GREEN and verification record.

### Fix self-review and concerns

- Heading-line metadata remains accepted by the existing repository pair and all prior projection tests.
- A metadata-only orphan without a visible direction list item does not create a parseable direction.
- A continuation cannot evade the exactly-one metadata rule: all comments before the next visible direction heading remain in the current block.
- Adjacent visible direction items remain separate even when the latter's metadata is on a continuation.
- Period and Field Map section boundaries remain enforced by `_section`; all prior continuation/trend boundary tests remain green.
- No blocker remains. The existing version-bound synthesis timestamp/window concern is unchanged.
