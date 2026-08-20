# Task 3 Report: canonical protocol sync and Chinese scan layer

Date: `2026-08-20`

Branch: `agent/time-first-radar-v2`

Base: `e8680afa8f21de51b78fe48cf4109cf6e97395e2`

Approved protocol reference: Agent Benchmark Radar `cf98235d95fe2027b32d4cc05642902dbef37d89`

## Result

Agent Memory Radar now carries the canonical family protocol byte-for-byte, applies the exact public synthesis cutoff consistently in Memory guidance, and binds every future rolling-period support to its direction through canonical `direction_keys`.

The eight Chinese Timeline folds now expose Chinese-first area/problem labels and Chinese-first one-sentence deltas while retaining canonical paper titles, technical terms, dates, entry identities, hidden semantic keys, evidence/caveat scope, map tokens, links, notes, visuals, and the unchanged English projection.

No current canonical record was changed. No `direction_keys` or Radar timestamp was fabricated for the current zero-support rolling periods.

## TDD evidence

### Baseline

The assigned base was clean and the pre-Task-3 suite was green:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s tests -v
Ran 77 tests in 0.225s
OK
```

### Stable support-to-direction binding RED

Tests were added first for malformed direction keys, the implicit/explicit legacy boundary, JSON Schema structure, a mismatched reinforcement, and a valid same-direction reinforcement:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest -v \
  tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest.test_native_direction_keys_are_unique_stable_tokens_when_declared \
  tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest.test_direction_keys_require_native_v2_and_forbid_explicit_legacy \
  tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest.test_schema_encodes_optional_native_direction_keys \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_reinforced_supports_must_share_the_declared_direction_key \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_same_direction_reinforcement_with_two_bound_supports_can_pass
Ran 5 tests in 0.009s
FAILED (failures=7)
```

The old adapter ignored invalid and legacy `direction_keys`, the schema did not declare the field, and the mismatched support passed. The already-valid same-direction synthetic case passed, isolating the missing binding check.

### Stable support-to-direction binding GREEN

The minimal implementation added a domain-stable `direction_keys` parser, complete-native/legacy guards, exact support-key membership, and the corresponding schema dependency/shape:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest -v \
  tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest.test_native_direction_keys_are_unique_stable_tokens_when_declared \
  tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest.test_direction_keys_require_native_v2_and_forbid_explicit_legacy \
  tests.test_memory_v2_contract.CanonicalMemoryTimeContractTest.test_schema_encodes_optional_native_direction_keys \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_reinforced_supports_must_share_the_declared_direction_key \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_same_direction_reinforcement_with_two_bound_supports_can_pass
Ran 5 tests in 0.011s
OK
```

`direction_keys` is optional for a native-v2 record not used as support. When present it is a non-empty list of unique lowercase stable tokens, requires the complete native-v2 time bundle, and is forbidden on explicit or implicit legacy. A support cited under direction key `K` must include exact `K`.

### Chinese scan layer RED

A bounded Timeline-summary parser was added to compare the eight folds by entry identity, canonical date/title, area key, and delta key. It also requires both the Chinese area and delta to begin with CJK, contain meaningful CJK content, and differ from their English counterparts:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest -v \
  tests.test_validate_reading.MemoryReadingContractTest.test_chinese_timeline_scan_layer_is_localized_and_semantically_bound
Ran 1 test in 0.007s
FAILED (failures=8)
```

All eight subtests failed on the copied English area label, proving the regression was present on every Chinese fold.

### Chinese scan layer GREEN

Only the visible Chinese area/delta text was localized; paired semantic keys and the English page were left unchanged:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest -v \
  tests.test_validate_reading.MemoryReadingContractTest.test_chinese_timeline_scan_layer_is_localized_and_semantically_bound
Ran 1 test in 0.010s
OK
```

## Canonical protocol and guidance

`docs/RADAR_AGENT_PROTOCOL.md` is byte-identical to the approved Benchmark commit:

```text
$ cmp -s docs/RADAR_AGENT_PROTOCOL.md \
  <(git -C ../Agent-Benchmark-Radar show cf98235:docs/RADAR_AGENT_PROTOCOL.md)
$ sha256sum docs/RADAR_AGENT_PROTOCOL.md
30e1f3271edb8f8f1ae504597b0ec60dc9666c824e632c37f493945e58d485ac  docs/RADAR_AGENT_PROTOCOL.md
$ git -C ../Agent-Benchmark-Radar show \
  cf98235:docs/RADAR_AGENT_PROTOCOL.md | sha256sum
30e1f3271edb8f8f1ae504597b0ec60dc9666c824e632c37f493945e58d485ac  -
```

Memory-specific authoritative guidance now states that native Timeline membership and rolling membership/support use `radar_published_at` no later than the exact synthesis cutoff shared across Timeline and both periods. It also names `direction_keys` as the canonical Memory adapter field and requires exact block-key membership for each cited support.

## Final validation

Fresh full suite:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s tests -v
Ran 83 tests in 0.226s
OK
```

Fresh repository validators:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate_canonical.py
Validated 41 canonical Agent Memory records.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate_reading.py
Validated Chinese-first bilingual progressive reading surfaces.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate.py
Validated 41 canonical paper records and reader-facing repository contracts.
```

`scripts/validate.py` includes the repository-relative link audit. Additional preservation, guidance, and mechanical checks passed:

```text
protocol-byte-identical-cf98235
preserved-english-canonical-notes-visuals-compactions
current-zero-support-records-unmodified-no-direction-keys
guidance-audit-diff-check-python-compile-ok
```

These checks used:

```bash
git diff --quiet e8680af -- README.en.md data/papers papers assets digests library categories
! rg -n '"direction_keys"' data/papers
rg -n "synthesis cutoff|same cutoff|same exact cutoff|same shared cutoff|that cutoff" \
  docs/DAILY_WORKFLOW.md CURATION.md COMPACTION.md docs/BILINGUAL_PUBLICATION.md
rg -n "direction_keys" docs/DAILY_WORKFLOW.md CURATION.md \
  docs/BILINGUAL_PUBLICATION.md data/paper.schema.json scripts/validate_reading.py
git diff --check
PYTHONDONTWRITEBYTECODE=1 python -m compileall -q scripts tests
```

## Files changed

- `docs/RADAR_AGENT_PROTOCOL.md` — exact canonical `cf98235` protocol.
- `docs/DAILY_WORKFLOW.md` — Memory cutoff and `direction_keys` adapter contract.
- `CURATION.md`, `COMPACTION.md`, `docs/BILINGUAL_PUBLICATION.md` — aligned authoritative cutoff and support-binding guidance.
- `data/paper.schema.json` — optional native-v2 `direction_keys`, stable-token uniqueness, full-time dependency, and legacy exclusion.
- `scripts/validate_reading.py` — canonical direction-key parsing and exact support-to-direction validation.
- `tests/test_memory_v2_contract.py` — invalid/legacy/schema probes plus same-direction positive and mismatch negative coverage.
- `README.md` — Chinese-first area and delta text for the eight collapsed Timeline folds.
- `tests/test_validate_reading.py` — bounded CJK scan-layer and semantic/title parity regression.
- `.superpowers/sdd/2026-08-20-time-first-radar-v2-memory/task-3-report.md` — this report.

`README.en.md`, all canonical paper records, deep notes, visuals, digests, Library routes, and category pages are unchanged.

## Self-review

- The shared protocol contains no Memory-specific wording and matches Benchmark `cf98235` at the byte level.
- Native Timeline inclusion and native period support are both bounded by the same exact public synthesis timestamp in code and every guidance surface that defines membership.
- A future support record cannot use an empty, duplicate, free-form, scalar, or mismatched direction key. The schema and repository validator both reject invalid combinations.
- Two synthetic native records carrying one exact direction key can pass the reinforced gate; swapping one record to a different key fails with the support identity and required key in the error.
- Current `supports=none` period judgments remain untouched. No production record carries `direction_keys`, and no canonical data file changed.
- All eight Chinese summaries preserve the exact date/title and paired `timefirst:area` / `timefirst:delta` keys. The bounded test confirms identity/order/key parity and meaningful CJK in both visible scan-layer fields.
- Technical identifiers such as `aggregate score`, `paired evidence`, `skill-writer policy`, `shadow-execution certification`, `trajectory`, `query-conditioned`, `structural access package`, `stateful iterative search`, and `BM25` remain searchable in the Chinese-first summaries.
- The English page, Question/Evidence/Caveat/Map/Links bodies, local notes, primary links, images, lifecycle Field Map, and historical compactions were not modified.
- Full canonical, reading, repository-relative-link, schema, public-run absence, common-parser, and bilingual projection tests pass.

## Concerns

- No implementation blocker remains.
- The rolling windows and exact synthesis timestamp remain deliberately version-bound to `2026-08-20T00:00:00Z`. A future material acceptance must advance the timestamp, windows, both public projections, and validator constants atomically.
- A future native record becomes period support only when its `direction_keys` contains the exact visible direction block key; native records that are not cited as support may continue to omit the field.
- Local validation uses the existing dependency environment at `/tmp/agent-memory-radar-deps`; repository CI installs the unchanged requirements normally.

---

## Review fix round 1: split and retirement direction states

Review base: `f0e15226b531690265cb5413fc5d4e3d9f139d9f`

### Result

The Memory period adapter now implements every state named by the binding family protocol. `splits` and `retires` are parsed as first-class visible/stable direction states, participate in Chinese/English parity, and pass only with defensible durable-map evidence.

For either state, the block must cite at least one canonical native-v2 support that is in-window, accepted no later than the exact synthesis cutoff, bound to the block's exact `direction_keys` key, and accompanied by independent visible prior Field Map evidence. At least one cited native support must carry the matching event judgment (`map_delta=splits` or `map_delta=retires`).

The current README remains the same zero-support `no_material_change` projection. No canonical record, timestamp, public claim, note, visual, link, map, or compaction changed.

### RED evidence

The focused fixtures were added before the parser/gates. Both positive states were unparseable, all ten required negative probes lacked their intended gate errors, and the bilingual mismatch could not reach parity comparison:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest -v \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_split_and_retirement_directions_with_bound_map_evidence_can_pass \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_split_and_retirement_direction_gates_reject_invalid_evidence \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_split_retirement_state_drift_is_rejected_as_bilingual_parity
Ran 3 tests in 0.032s
FAILED (failures=13)
```

Representative old errors were:

```text
README.md: last-7-days has no parseable direction metadata
README.en.md: last-7-days has no parseable direction metadata
```

### GREEN evidence

The direction-state spelling is now defined once and shared by the label, visible-value, heading, and enum parsers. State gates extend the existing canonical/native/window/cutoff/key checks with nonempty support, prior-map, and matching-map requirements:

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest -v \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_split_and_retirement_directions_with_bound_map_evidence_can_pass \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_split_and_retirement_direction_gates_reject_invalid_evidence \
  tests.test_memory_v2_contract.MemoryProjectionContractTest.test_split_retirement_state_drift_is_rejected_as_bilingual_parity
Ran 3 tests in 0.033s
OK
```

The matrix covers both `splits` and `retires` for:

- positive bound native support with matching `map_delta` and visible `#field-map` prior;
- zero support;
- `prior=none`;
- mismatched `direction_keys`;
- support accepted after the exact synthesis cutoff;
- incompatible `map_delta`;
- Chinese/English split-versus-retirement parity drift.

### Final verification

```text
$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s tests -v
Ran 86 tests in 0.264s
OK

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate_canonical.py
Validated 41 canonical Agent Memory records.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate_reading.py
Validated Chinese-first bilingual progressive reading surfaces.

$ PYTHONPATH=/tmp/agent-memory-radar-deps PYTHONDONTWRITEBYTECODE=1 \
  python scripts/validate.py
Validated 41 canonical paper records and reader-facing repository contracts.
```

Additional checks passed:

```text
protocol-byte-identical-cf98235
README-and-canonical-research-surfaces-unchanged
current-zero-support-records-still-have-no-direction-keys
split-retire-guidance-audit-ok
link-preservation-diff-compile-ok
```

### Files changed in this fix

- `scripts/validate_reading.py` — shared direction-state spelling plus split/retirement support, prior, and matching-map gates.
- `tests/test_memory_v2_contract.py` — positive, rejection-matrix, and bilingual-parity fixtures.
- `docs/DAILY_WORKFLOW.md`, `CURATION.md` — explicit matching `map_delta`, exact key, cutoff, support, and prior-evidence rules.
- `.superpowers/sdd/2026-08-20-time-first-radar-v2-memory/task-3-report.md` — this appended fix evidence.

### Self-review and concerns

- Existing `new_signal`, `reinforced`, `revised`, and `no_material_change` branches are unchanged except that the existing `revised` nonempty-support check now shares the same expression with the two new durable states and retains its exact error wording.
- Generic support validation still owns canonical identity, native provenance, window membership, exact-key binding, and cutoff enforcement; the new state logic does not duplicate or weaken those gates.
- A split or retirement cannot be justified by an unrelated `early_signal`, `reinforces`, or `revises` record merely placed beneath matching prose. At least one bound native support must carry the exact state-level map event.
- Independent prior evidence remains exact `prior=field-map` plus one visible `#field-map` link; arbitrary non-none prose cannot satisfy it.
- The shared canonical protocol remains byte-identical to Benchmark `cf98235`.
- No implementation blocker remains. The version-bound synthesis timestamp concern from Task 3 is unchanged.
