# Task 1 Report: Apply the v2 family contract to Agent Memory Radar

Date: 2026-08-20

Branch: `agent/time-first-radar-v2`

Base: `67b48a22d89eae9468f54228594cbedfc073e3d6`

Requested source: Agent Benchmark Radar `5017ea419da0dab632819ad07eeac4d3ce7be638`

## Result

Agent Memory Radar now implements the family v2 time-first contract: eight legacy current records are bilingual Timeline disclosures, exact 7-day and 30-day migration syntheses precede the durable lifecycle map, the shared agent protocol/validator/tests are installed, the Memory-specific Daily Agent adapter and policies distinguish all three timestamps, and CI plus local validators enforce the contract without a fixed item cap.

The existing research identities, publication dates, claims, deep notes, Library routes, category/digest surfaces, and visual validation remain intact. No `radar_published_at` values were invented or bulk-filled.

## TDD evidence

### Baseline observation

Before the shared tests existed, the repository had no `tests/` directory, so the untouched baseline command was not importable:

```text
$ python -m unittest discover -s tests -v
ImportError: Start directory is not importable: 'tests'
```

No implementation code was changed before installing the shared family validator/tests.

### RED

After copying `scripts/timefirst_contract.py` and `tests/test_timefirst_contract.py` from Benchmark `5017ea4` byte-for-byte, the repository README assertion failed for the expected missing v2 structure while all ten generic fixtures passed:

```text
$ python -m unittest discover -s tests -v
test_contract_does_not_impose_a_fixed_latest_cap (test_timefirst_contract.TimeFirstContractTest.test_contract_does_not_impose_a_fixed_latest_cap) ... ok
test_empty_labeled_field_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_empty_labeled_field_is_rejected) ... ok
test_evidence_and_caveat_scope_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_evidence_and_caveat_scope_drift_is_rejected) ... ok
test_language_identity_or_date_order_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_language_identity_or_date_order_drift_is_rejected) ... ok
test_missing_evidence_or_caveat_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_missing_evidence_or_caveat_is_rejected) ... ok
test_period_window_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_period_window_drift_is_rejected) ... ok
test_primary_and_local_link_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_primary_and_local_link_drift_is_rejected) ... ok
test_repository_readmes_satisfy_contract (test_timefirst_contract.TimeFirstContractTest.test_repository_readmes_satisfy_contract) ... FAIL
test_title_area_and_delta_semantic_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_title_area_and_delta_semantic_drift_is_rejected) ... ok
test_visible_evidence_and_caveat_must_carry_contract_witness (test_timefirst_contract.TimeFirstContractTest.test_visible_evidence_and_caveat_must_carry_contract_witness) ... ok
test_whitespace_only_link_target_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_whitespace_only_link_target_is_rejected) ... ok

======================================================================
FAIL: test_repository_readmes_satisfy_contract (test_timefirst_contract.TimeFirstContractTest.test_repository_readmes_satisfy_contract)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests/test_timefirst_contract.py", line 116, in test_repository_readmes_satisfy_contract
    self.assertEqual([], errors)
AssertionError: Lists differ: [] != ['Chinese: missing stable anchor timeline' ...]

First violations:
- Chinese: missing stable anchor timeline
- Chinese: missing stable anchor frontier
- Chinese: missing stable anchor periods
- Chinese: missing stable anchor last-7-days
- Chinese: missing stable anchor last-30-days
- Chinese: missing stable anchor evolution
- English: the same six missing v2 anchors

----------------------------------------------------------------------
Ran 11 tests in 0.008s

FAILED (failures=1)
```

This was the intended failure: the generic validator itself worked, and only the repository projection lacked the v2 contract.

### GREEN

After the README and validator changes:

```text
$ python -m unittest discover -s tests -v
test_contract_does_not_impose_a_fixed_latest_cap (test_timefirst_contract.TimeFirstContractTest.test_contract_does_not_impose_a_fixed_latest_cap) ... ok
test_empty_labeled_field_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_empty_labeled_field_is_rejected) ... ok
test_evidence_and_caveat_scope_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_evidence_and_caveat_scope_drift_is_rejected) ... ok
test_language_identity_or_date_order_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_language_identity_or_date_order_drift_is_rejected) ... ok
test_missing_evidence_or_caveat_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_missing_evidence_or_caveat_is_rejected) ... ok
test_period_window_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_period_window_drift_is_rejected) ... ok
test_primary_and_local_link_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_primary_and_local_link_drift_is_rejected) ... ok
test_repository_readmes_satisfy_contract (test_timefirst_contract.TimeFirstContractTest.test_repository_readmes_satisfy_contract) ... ok
test_title_area_and_delta_semantic_drift_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_title_area_and_delta_semantic_drift_is_rejected) ... ok
test_visible_evidence_and_caveat_must_carry_contract_witness (test_timefirst_contract.TimeFirstContractTest.test_visible_evidence_and_caveat_must_carry_contract_witness) ... ok
test_whitespace_only_link_target_is_rejected (test_timefirst_contract.TimeFirstContractTest.test_whitespace_only_link_target_is_rejected) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.009s

OK
```

## Full validation

The runtime-owned Python did not expose `jsonschema` and its default user site was read-only. I installed the unchanged `requirements.txt` into the temporary validation-only target `/tmp/agent-memory-radar-deps`; no dependency or repository file was changed. CI continues to install `requirements.txt` normally.

Fresh final command:

```bash
export PYTHONPATH=/tmp/agent-memory-radar-deps
export PYTHONDONTWRITEBYTECODE=1
python -m unittest discover -s tests -v
python scripts/validate_canonical.py
python scripts/validate_reading.py
python scripts/validate.py
```

Full result after the unit-test lines shown above:

```text
----------------------------------------------------------------------
Ran 11 tests in 0.009s

OK
Validated 41 canonical Agent Memory records.
Validated Chinese-first bilingual progressive reading surfaces.
Validated 41 canonical paper records and reader-facing repository contracts.
```

All four commands exited 0 with no warnings.

## Files changed

- `.github/workflows/validate.yml` — runs unit tests before canonical/reading validation and includes the repository validator.
- `README.md`, `README.en.md` — v2 Timeline, legacy-time disclosure, period synthesis, compatibility aliases, evaluation route, preserved map/paths/Library.
- `docs/RADAR_AGENT_PROTOCOL.md` — exact shared v2 protocol from Benchmark `5017ea4`.
- `docs/DAILY_WORKFLOW.md` — Memory discovery/evidence/lifecycle/closest-control/map/period/bilingual adapter.
- `CURATION.md`, `COMPACTION.md` — Daily Agent ownership, private candidates, three-time semantics, rolling versus closed periods, non-recursive evidence.
- `data/paper.schema.json` — optional `published_at`, `first_seen_at`, `radar_published_at`, `time_provenance`, and `map_delta` fields; no legacy records changed.
- `scripts/timefirst_contract.py`, `tests/test_timefirst_contract.py` — exact shared validator and strengthened semantic-invariant tests from Benchmark `5017ea4`.
- `scripts/validate_reading.py` — calls `validate_pair`, keeps family/local-link/compatibility checks, and removes the 6–8 bound.
- `scripts/validate.py` — recognizes non-empty `entry-*` Timeline disclosures without an item cap, while retaining note-navigation, category, visual, schema, and link checks.
- `docs/superpowers/plans/2026-08-20-time-first-radar-v2-memory.md` — in-scope implementation plan, completed checkboxes; reserved example URLs replace validator-visible placeholder links.
- `papers/2026/2608.16303.zh.md`, `categories/zh/write-update-consolidation.md` — corrected the pre-existing stale LycheeMemory link from nonexistent `2608.09424.md` to canonical `2608.12990.md` so full link validation remains strict and pristine.
- `.superpowers/sdd/2026-08-20-time-first-radar-v2-memory/task-1-report.md` — this report.

## Shared-artifact verification

`cmp` confirmed all three copied sources are byte-for-byte identical to Benchmark `5017ea4`:

```text
protocol: exact
validator: exact
tests: exact
```

SHA-256:

```text
0dbe84148ff0775b3c622426e63ce8ee7c40565dbabf147e99ef7fb7d527b6ee  docs/RADAR_AGENT_PROTOCOL.md
baf0479fafb30c91aff2da19b8609fcd88f3dd44e4f487445f2d22b26e95b0a3  scripts/timefirst_contract.py
4ccf0f14e43302ce10e32473ee7df40949f8788fd72b960e1a47918ba422570d  tests/test_timefirst_contract.py
```

## Self-review

- The exact eight current identities remain in descending honest paper-date order: CABLE, D²ACCI, WER, TRUSS, ArborMem, QUMem, HyperSkill, ReFind.
- Each language has eight `entry-*` identities, eight disclosures, and exactly one Question/Evidence/Caveat/Map/Links field set per identity.
- All 14 family/generic/compatibility anchors occur exactly once in each README: `timeline`, `latest`, `latest-papers`, `frontier`, `periods`, `changes`, `whats-changing`, `last-7-days`, `last-30-days`, `evolution`, `field-map`, `research-map`, `reading-paths`, `library`.
- The 7-day and 30-day windows match across languages. Both README sections explicitly disclose that this migration snapshot uses displayed paper publication dates because legacy Radar acceptance times are unavailable.
- No fixed Timeline cap remains in validators or policies. The generic 11-entry fixture passes.
- No public Timeline candidate state (`BLOCKED`, `DEFERRED`, `ABSTRACT_ONLY`) appears.
- Every current identity has both English and Chinese deep notes; primary/local README links resolve. Canonical validation also rechecked all 41 records and their generated visual assets/embeds without loosening visual rules.
- The evaluation route is `Agent-Benchmark-Radar#benchmark-memory`; category, digest, Library, `latest-papers`, `changes`, and `research-map` compatibility routes remain reachable.
- Existing quantitative evidence was reused from the prior cards/notes; no new research metric or Radar timestamp was invented.
- `git diff --check` is clean.

## Concerns

- No content or validation blocker remains.
- The two period sections are deliberately a disclosed migration snapshot over legacy paper publication dates, not a claim about historical Radar acceptance. Native v2 records must switch to the three canonical timestamps.
- Local validation needs the temporary dependency target only because this managed runtime's default Python lacks `jsonschema`; repository CI installs the existing requirements normally.

## Fix round 1: review corrections

Date: 2026-08-20

Base: `bf02a4adcc6892fa6f2f686c7e3da253f5d8bf29`

### Scope and superseded statements

Controller review required the shared parser to become repository-neutral before the Benchmark backport. This section supersedes two statements above:

- `scripts/timefirst_contract.py` and `tests/test_timefirst_contract.py` now intentionally diverge from Benchmark `5017ea4`; `docs/RADAR_AGENT_PROTOCOL.md` remains unchanged.
- Memory exposes the 12 task-specified stable aliases. Artificial `frontier` and `evolution` anchors are removed; the common parser uses `field-map` as the 30-day boundary.

No Timeline identity, displayed legacy date, period claim, canonical record, visual, or deep note changed.

### TDD RED 1: common-core review findings

Tests were changed first to remove Benchmark aliases from the neutral fixture and cover missing/duplicate common anchors, distinctive witnesses, and bounded witness matching. A Memory test also required a dedicated deep-note contract API.

```text
$ python -m unittest tests/test_timefirst_contract.py tests/test_validate_reading.py -v
test_contract_does_not_impose_a_fixed_latest_cap ... FAIL
test_domain_pair_without_benchmark_aliases_is_valid ... FAIL
test_duplicate_common_anchor_is_rejected ... FAIL
test_witness_must_match_a_bounded_visible_phrase ... FAIL
test_witness_requires_a_distinctive_phrase (evidence) ... FAIL
test_witness_requires_a_distinctive_phrase (caveat) ... FAIL
test_memory_validator_exposes_deep_note_contract ... FAIL

Ran 17 tests in 0.011s
FAILED (failures=7)
```

Observed causes matched the review exactly:

```text
domain fixture: missing stable anchor frontier/evolution
duplicate timeline anchor: no duplicate error
numeric/generic witness: no distinctive-witness error
substring-only witness: no bounded-match error
Memory note contract: API absent
```

### TDD GREEN 1 and repository witness RED

After removing Benchmark-only anchors, using `field-map` as the period boundary, rejecting duplicate common anchors, requiring at least three witness terms with two lexical terms, and enforcing bounded phrase matches, every neutral fixture passed. The repository assertion then failed on the intentionally still-weak current witnesses:

```text
$ python -m unittest tests/test_timefirst_contract.py -v
15 neutral fixture tests ... ok
test_repository_readmes_satisfy_contract ... FAIL

First violation:
Chinese: entry identity 2608-17911 evidence semantic contract needs a distinctive visible-text witness with at least three terms

Ran 16 tests in 0.013s
FAILED (failures=1)
```

All 16 current evidence/caveat witnesses were then replaced with distinctive load-bearing phrases visible in both languages. The focused common suite became GREEN:

```text
$ python -m unittest tests/test_timefirst_contract.py -v
Ran 16 tests in 0.013s
OK
```

### TDD RED/GREEN 2: Memory deep-note correspondence

The initial API-existence test failed, then passed after the smallest callable contract was added:

```text
$ python -m unittest tests.test_validate_reading.MemoryReadingContractTest.test_memory_validator_exposes_deep_note_contract -v
FAIL: callable(validate_memory_note_links) was false

$ python -m unittest tests.test_validate_reading.MemoryReadingContractTest.test_memory_validator_exposes_deep_note_contract -v
Ran 1 test in 0.000s
OK
```

Behavior tests were then added against the real repository pair. The empty implementation failed removal and misrouting as expected:

```text
$ python -m unittest tests/test_validate_reading.py -v
test_memory_validator_exposes_deep_note_contract ... ok
test_mismatched_deep_note_identity_is_rejected ... FAIL
test_removing_both_deep_note_links_is_rejected ... FAIL
test_repository_entries_have_corresponding_bilingual_deep_notes ... ok

Ran 4 tests in 0.001s
FAILED (failures=2)
```

After implementing per-entry Chinese/English note-ID correspondence and wiring it into `validate_reading.py`:

```text
$ python -m unittest tests/test_validate_reading.py -v
test_memory_validator_exposes_deep_note_contract ... ok
test_mismatched_deep_note_identity_is_rejected ... ok
test_removing_both_deep_note_links_is_rejected ... ok
test_repository_entries_have_corresponding_bilingual_deep_notes ... ok

Ran 4 tests in 0.001s
OK
```

### Focused GREEN

```text
$ python -m unittest tests/test_timefirst_contract.py tests/test_validate_reading.py -v
Ran 19 tests in 0.013s
OK

$ python scripts/validate_reading.py
Validated Chinese-first bilingual progressive reading surfaces.
```

### Full validation

```bash
export PYTHONPATH=/tmp/agent-memory-radar-deps
export PYTHONDONTWRITEBYTECODE=1
python -m unittest discover -s tests -v
python scripts/validate_canonical.py
python scripts/validate_reading.py
python scripts/validate.py
```

```text
Ran 19 tests in 0.015s
OK
Validated 41 canonical Agent Memory records.
Validated Chinese-first bilingual progressive reading surfaces.
Validated 41 canonical paper records and reader-facing repository contracts.
```

All four commands exited 0 with no warnings.

### Fix files

- `scripts/timefirst_contract.py` — common anchors only, duplicate rejection, `field-map` period boundary, distinctive bounded witnesses.
- `tests/test_timefirst_contract.py` — neutral domain fixture and regression coverage for every common-core review finding.
- `scripts/validate_reading.py` — Memory alias cardinality and per-entry bilingual deep-note identity validation.
- `tests/test_validate_reading.py` — repository note-link presence, removal, and correspondence tests.
- `README.md`, `README.en.md` — artificial aliases removed; 16 weak witnesses replaced with bilingual visible load-bearing phrases without changing research claims.

### Fix-round self-review

- Both READMEs contain each of the 12 Memory aliases exactly once, eight unchanged Timeline identities, and no `frontier` or `evolution` anchor.
- The common parser requires only repository-neutral anchors, rejects duplicate common anchors, and terminates the 30-day section at `field-map`.
- Every Timeline entry in each language exposes English and Chinese deep notes whose note identity matches its `entry-*` identity.
- Every evidence/caveat contract uses a bounded distinctive phrase that is visible in both languages; numeric-only and two-term generic witnesses are rejected.
- Timeline items, legacy dates, period claims, canonical data, visuals, and deep-note files are unchanged.
- `git diff --check` is clean.

### Fix-round concerns

- No blocker remains in Memory.
- The common parser/tests intentionally differ from Benchmark `5017ea4` under the controller ruling; the controller owns the Benchmark backport before family merge.

### Field-map boundary mutation check

The period-window test now covers both windows. Temporarily restoring the rejected `evolution` boundary produced the expected RED only for the 30-day subcase:

```text
$ python -m unittest tests.test_timefirst_contract.TimeFirstContractTest.test_period_window_drift_is_rejected -v
test_period_window_drift_is_rejected (expected='last-30-days') ... FAIL
Ran 1 test in 0.004s
FAILED (failures=1)
```

Restoring the neutral `field-map` boundary returned GREEN:

```text
$ python -m unittest tests.test_timefirst_contract.TimeFirstContractTest.test_period_window_drift_is_rejected -v
test_period_window_drift_is_rejected ... ok
Ran 1 test in 0.004s
OK
```

## Fix round 2: load-bearing witness definition

Date: 2026-08-20

Base: `31f82da6ec4f673acadb9cfcbf02092fb0df1b02`

### Review finding and contract

The round-1 three-token/two-lexical-token rule still accepted generic contract boilerplate such as `same-matched-evidence` when that exact phrase was visible. The domain-neutral common core now defines a distinctive witness as:

- at least three normalized hyphen-separated terms;
- at least two distinct lexical content terms after common comparison, contract-role, and result boilerplate is discounted; and
- an exact bounded visible-phrase match.

The discounted vocabulary is repository-neutral (`same`, `matched`, `evidence`, `result`, `control`, `score`, and related generic terms); it contains no Memory identity, method, benchmark, or current README phrase. Existing fixture witnesses were changed from generic `matched-control-output` / `unmatched-lifecycle-cost` to domain-specific fixture phrases so the positive case exercises the intended contract.

### TDD RED

The regression test was added first and run against the round-1 implementation:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_timefirst_contract.TimeFirstContractTest.test_generic_contract_boilerplate_is_not_a_distinctive_witness -v
test_generic_contract_boilerplate_is_not_a_distinctive_witness ... FAIL

AssertionError: False is not true

Ran 1 test in 0.003s
FAILED (failures=1)
```

This proved that visible `same matched evidence` with witness `same-matched-evidence` was incorrectly accepted.

### TDD GREEN

After the minimal common-core change:

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_timefirst_contract.TimeFirstContractTest.test_generic_contract_boilerplate_is_not_a_distinctive_witness -v
test_generic_contract_boilerplate_is_not_a_distinctive_witness ... ok

Ran 1 test in 0.003s
OK

$ PYTHONDONTWRITEBYTECODE=1 python -m unittest tests/test_timefirst_contract.py -v
Ran 17 tests in 0.014s
OK
```

### Full validation

```bash
export PYTHONPATH=/tmp/agent-memory-radar-deps
export PYTHONDONTWRITEBYTECODE=1
python -m unittest discover -s tests -v
python scripts/validate_canonical.py
python scripts/validate_reading.py
python scripts/validate.py
git diff --check
```

```text
Ran 20 tests in 0.014s
OK
Validated 41 canonical Agent Memory records.
Validated Chinese-first bilingual progressive reading surfaces.
Validated 41 canonical paper records and reader-facing repository contracts.
```

All commands exited 0 with no warnings; `git diff --check` produced no output.

### Files and self-review

- `scripts/timefirst_contract.py` — adds repository-neutral generic-boilerplate discounting and requires two distinct specific content terms.
- `tests/test_timefirst_contract.py` — adds the reported `same-matched-evidence` regression and strengthens positive fixture language.
- `.superpowers/sdd/2026-08-20-time-first-radar-v2-memory/task-1-report.md` — records this RED/GREEN cycle and validation evidence.
- Current Memory README witnesses pass unchanged; no Timeline item, timestamp, research claim, canonical datum, visual, note, alias, or period synthesis changed.

### Concerns

- The witness gate is intentionally a conservative lexical contract, not a semantic-language model. It closes generic contract-boilerplate bypasses while remaining deterministic and repository-neutral.
- The controller still owns backporting the corrected common parser/tests to Benchmark before family merge.
