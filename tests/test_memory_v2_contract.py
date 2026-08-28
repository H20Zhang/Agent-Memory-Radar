from copy import deepcopy
from contextlib import redirect_stdout
import io
import json
import jsonschema
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading
import validate_canonical
import validate as validate_repository


V2_FIELDS = (
    "published_at",
    "first_seen_at",
    "radar_published_at",
    "time_provenance",
    "map_delta",
)
LEGACY_TIMELINE_COMPATIBILITY_IDS = (
    "2608.17911",
    "2608.17756",
    "2608.17587",
    "2608.17588",
    "2608.17534",
    "2608.16168",
    "2608.16114",
    "2608.12888",
)


def repository_records() -> list[dict[str, object]]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((ROOT / "data" / "papers").glob("*.json"))
    ]


def native_record(
    identity: str = "native",
    radar_published_at: str = "2026-08-22T01:18:00Z",
    *,
    map_delta: str = "early_signal",
    direction_keys: tuple[str, ...] = ("memory-radar-acceptance-time",),
) -> dict[str, object]:
    return {
        "id": identity,
        "title": identity.upper(),
        "published": "2026-08-01",
        "published_at": "2026-08-01T00:00:00Z",
        "first_seen_at": "2026-08-22T01:18:00Z",
        "radar_published_at": radar_published_at,
        "time_provenance": "native_v2",
        "map_delta": map_delta,
        "direction_keys": list(direction_keys),
        "paper_url": f"https://example.com/{identity}",
    }


def repository_readmes() -> tuple[str, str]:
    return (
        (ROOT / "README.md").read_text(encoding="utf-8"),
        (ROOT / "README.en.md").read_text(encoding="utf-8"),
    )


def entry_anchor(identity: str) -> str:
    return identity.replace(".", "-")


def direction_line(
    language: str,
    *,
    key: str = "memory-radar-acceptance-time",
    state: str = "no_material_change",
    supports: tuple[str, ...] = (),
    confidence: str = "high",
    implication: str = "require-native-v2-times-for-period-claims",
    timing: str = "radar_published_at",
    synthesized: str = "2026-08-28T00:53:00Z",
    prior: str = "none",
    visible_supports: tuple[str, ...] | None = None,
) -> str:
    support_value = ",".join(supports) if supports else "none"
    visible = supports if visible_supports is None else visible_supports
    support_links = " · ".join(
        f"[{identity}](#entry-{entry_anchor(identity)})" for identity in visible
    )
    if not support_links:
        support_links = "**none**"
    prior_visible = "`none`" if prior == "none" else f"[Field Map](#{prior})"
    heading_witness = (
        "Memory Radar acceptance time"
        if key == "memory-radar-acceptance-time"
        else key.replace("-", " ")
    )
    metadata = (
        f'<!-- timefirst:direction key="{key}" '
        f'state="{state}" supports="{support_value}" confidence="{confidence}" '
        f'implication="{implication}" timing="{timing}" synthesized="{synthesized}" '
        f'prior="{prior}" -->'
    )
    if language == "zh":
        return (
            f"- **`{state}` · {heading_witness} 当前判断。** "
            f"支撑：{support_links}；置信度：**{confidence}**；时间依据：`{timing}`；"
            f"先验地图证据：{prior_visible}。研究设计含义（require native v2 times for period claims）："
            f"仅原生接受时间可以支持窗口判断。精确合成时间：`{synthesized}`。 {metadata}"
        )
    return (
        f"- **`{state}` · {heading_witness} current judgment.** "
        f"Supports: {support_links}; confidence: **{confidence}**; timing basis: `{timing}`; "
        f"prior map evidence: {prior_visible}. Research-design implication "
        f"(require native v2 times for period claims): only native acceptance times support "
        f"the window. Exact synthesis time: `{synthesized}`. {metadata}"
    )


def multiline_direction_line(language: str) -> str:
    """Move all labeled visible fields onto a continuation line."""

    line = direction_line(language)
    metadata_start = line.index("<!-- timefirst:direction")
    metadata = line[metadata_start:]
    visible = line[:metadata_start].rstrip()
    heading_end = visible.index("** ", 3) + 2
    return f"{visible[:heading_end]} {metadata}\n  {visible[heading_end:].strip()}"


def replace_period_section(
    text: str,
    anchor: str,
    next_anchor: str,
    heading: str,
    line: str,
) -> str:
    start_marker = f'<a id="{anchor}"></a>'
    end_marker = f'<a id="{next_anchor}"></a>'
    start = text.index(start_marker)
    end = text.index(end_marker, start + len(start_marker))
    replacement = f"{start_marker}\n{heading}\n\n{line}\n\n"
    return text[:start] + replacement + text[end:]


def projection_readme(
    text: str,
    language: str,
    *,
    seven_line: str | None = None,
    thirty_line: str | None = None,
) -> str:
    if language == "zh":
        seven_heading = "### 过去 7 天：2026-08-22—2026-08-28"
        thirty_heading = "### 过去 30 天：2026-07-30—2026-08-28"
    else:
        seven_heading = "### Last 7 days: 2026-08-22—2026-08-28"
        thirty_heading = "### Last 30 days: 2026-07-30—2026-08-28"
    text = replace_period_section(
        text,
        "last-7-days",
        "last-30-days",
        seven_heading,
        seven_line or direction_line(language),
    )
    return replace_period_section(
        text,
        "last-30-days",
        "field-map",
        thirty_heading,
        thirty_line or direction_line(language),
    )


def valid_projection_pair() -> tuple[str, str]:
    zh, en = repository_readmes()
    return projection_readme(zh, "zh"), projection_readme(en, "en")


def timeline_entry(record: dict[str, object], language: str) -> str:
    identity = str(record["id"])
    anchor = entry_anchor(identity)
    label_map = "地图" if language == "zh" else "Map"
    label_links = "链接" if language == "zh" else "Links"
    return (
        f'<a id="entry-{anchor}"></a>\n'
        f'<details><summary><strong>{str(record["radar_published_at"])[:10]} · '
        f'{record["title"]}</strong> · Native</summary>\n\n'
        f'**{label_map}.** `{record["map_delta"]}` — Native projection.\n\n'
        f'**{label_links}.** [Paper]({record["paper_url"]}) · '
        f'[中文深读](papers/2026/{identity}.zh.md) · '
        f'[English note](papers/2026/{identity}.md)\n\n</details>\n\n'
    )


def prepend_timeline_entries(
    text: str,
    records: list[dict[str, object]],
    language: str,
) -> str:
    marker = '<a id="entry-2608-17911"></a>'
    insertion = "".join(timeline_entry(record, language) for record in records)
    return text.replace(marker, insertion + marker, 1)


class CanonicalMemoryTimeContractTest(unittest.TestCase):
    def test_untouched_legacy_record_remains_field_absent_compatible(self):
        record = {"id": "untouched", "published": "2024-08"}
        self.assertEqual([], validate_reading.validate_record_time_contract(record))

    def test_any_v2_field_requires_the_complete_contract(self):
        record = {"id": "partial", "published": "2026-08", "map_delta": "early_signal"}
        errors = validate_reading.validate_record_time_contract(record)
        for field in set(V2_FIELDS) - {"map_delta"}:
            self.assertTrue(any(field in error for error in errors), (field, errors))

    def test_native_v2_requires_strict_utc_timestamps(self):
        record = native_record()
        for field, value in (
            ("published_at", "2026-08-01T00:00:00+00:00"),
            ("first_seen_at", "2026-08-20T00:00Z"),
            ("radar_published_at", "2026-08-20 01:00:00Z"),
        ):
            with self.subTest(field=field):
                mutated = deepcopy(record)
                mutated[field] = value
                errors = validate_reading.validate_record_time_contract(mutated)
                self.assertTrue(any("strict UTC" in error for error in errors), errors)

    def test_native_v2_requires_event_order(self):
        record = native_record()
        record["published_at"] = "2026-08-22T00:00:00Z"
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(
            any("published_at <= first_seen_at <= radar_published_at" in error for error in errors),
            errors,
        )

    def test_native_direction_keys_are_unique_stable_tokens_when_declared(self):
        record = native_record()
        mutations = (
            ("not-a-list", "memory-radar-acceptance-time"),
            ("empty", []),
            (
                "duplicate",
                ["memory-radar-acceptance-time", "memory-radar-acceptance-time"],
            ),
            ("free-form", ["Memory Radar acceptance time"]),
        )
        for name, value in mutations:
            with self.subTest(name=name):
                mutated = deepcopy(record)
                mutated["direction_keys"] = value
                errors = validate_reading.validate_record_time_contract(mutated)
                self.assertTrue(
                    any("direction_keys" in error for error in errors), errors
                )

    def test_direction_keys_require_native_v2_and_forbid_explicit_legacy(self):
        implicit_legacy = {
            "id": "implicit-legacy",
            "published": "2024-08",
            "direction_keys": ["memory-radar-acceptance-time"],
        }
        errors = validate_reading.validate_record_time_contract(implicit_legacy)
        self.assertTrue(
            any("direction_keys" in error and "native_v2" in error for error in errors),
            errors,
        )

        explicit_legacy = {
            "id": "explicit-legacy",
            "published": "2026-08",
            "published_at": "2026-08",
            "first_seen_at": None,
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "early_signal",
            "direction_keys": ["memory-radar-acceptance-time"],
        }
        errors = validate_reading.validate_record_time_contract(explicit_legacy)
        self.assertTrue(
            any("direction_keys" in error and "forbidden" in error for error in errors),
            errors,
        )

    def test_native_v2_radar_time_cannot_predate_cutover(self):
        record = native_record(radar_published_at="2026-08-19T23:59:59Z")
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(any("cutover" in error.lower() for error in errors), errors)

    def test_explicit_legacy_forbids_fabricated_discovery_or_radar_time(self):
        record = {
            "id": "legacy",
            "published": "2026-08",
            "published_at": "2026-08",
            "first_seen_at": "2026-08-28T00:53:00Z",
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "early_signal",
        }
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(any("first_seen_at=null" in error for error in errors), errors)

        record["first_seen_at"] = None
        record["radar_published_at"] = "2026-08-20T01:00:00Z"
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(any("radar_published_at=null" in error for error in errors), errors)

    def test_explicit_legacy_preserves_honest_published_precision(self):
        month = {
            "id": "legacy",
            "published": "2026-08",
            "published_at": "2026-08",
            "first_seen_at": None,
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "early_signal",
        }
        self.assertEqual([], validate_reading.validate_record_time_contract(month))

        day = deepcopy(month)
        day.update(published="2026-08-17", published_at="2026-08-17")
        self.assertEqual([], validate_reading.validate_record_time_contract(day))

        fabricated = deepcopy(month)
        fabricated["published_at"] = "2026-08-01"
        errors = validate_reading.validate_record_time_contract(fabricated)
        self.assertTrue(any("published precision" in error for error in errors), errors)

    def test_invalid_map_delta_is_rejected_for_native_and_explicit_legacy(self):
        native = native_record(map_delta="trend")
        legacy = {
            "id": "legacy",
            "published": "2026-08",
            "published_at": "2026-08",
            "first_seen_at": None,
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "trend",
        }
        for record in (native, legacy):
            with self.subTest(provenance=record["time_provenance"]):
                errors = validate_reading.validate_record_time_contract(record)
                self.assertTrue(any("map_delta" in error for error in errors), errors)

    def test_schema_rejects_null_provenance_map_and_published_time(self):
        schema = json.loads(
            (ROOT / "data" / "paper.schema.json").read_text(encoding="utf-8")
        )
        self.assertNotIn(None, schema["properties"]["time_provenance"]["enum"])
        self.assertNotIn(None, schema["properties"]["map_delta"]["enum"])
        self.assertEqual("string", schema["properties"]["published_at"]["type"])

    def test_schema_encodes_v2_fields_as_all_or_none_while_allowing_implicit_legacy(self):
        schema = json.loads(
            (ROOT / "data" / "paper.schema.json").read_text(encoding="utf-8")
        )
        validator = jsonschema.Draft202012Validator(schema)
        self.assertIn("dependentRequired", schema)
        self.assertIn("oneOf", schema)

        untouched = next(
            record
            for record in repository_records()
            if not any(field in record for field in V2_FIELDS)
        )
        self.assertEqual([], list(validator.iter_errors(untouched)))

        field_values: dict[str, object] = {
            "published_at": untouched["published"],
            "first_seen_at": None,
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "early_signal",
        }
        for field, value in field_values.items():
            with self.subTest(field=field):
                partial = deepcopy(untouched)
                partial[field] = value
                self.assertTrue(list(validator.iter_errors(partial)))

        explicit_legacy = next(
            record
            for record in repository_records()
            if record.get("time_provenance") == "legacy_unknown"
        )
        self.assertEqual([], list(validator.iter_errors(explicit_legacy)))

    def test_schema_encodes_optional_native_direction_keys(self):
        schema = json.loads(
            (ROOT / "data" / "paper.schema.json").read_text(encoding="utf-8")
        )
        validator = jsonschema.Draft202012Validator(schema)
        self.assertIn("direction_keys", schema["properties"])
        self.assertIn("direction_keys", schema["dependentRequired"])

        explicit_legacy = next(
            record
            for record in repository_records()
            if record.get("time_provenance") == "legacy_unknown"
        )
        native = deepcopy(explicit_legacy)
        native.update(
            published_at="2026-08-18T00:00:00Z",
            first_seen_at="2026-08-28T00:53:00Z",
            radar_published_at="2026-08-28T00:53:00Z",
            time_provenance="native_v2",
            direction_keys=["memory-radar-acceptance-time"],
        )
        self.assertEqual([], list(validator.iter_errors(native)))

        for name, value in (
            ("not-a-list", "memory-radar-acceptance-time"),
            ("empty", []),
            (
                "duplicate",
                ["memory-radar-acceptance-time", "memory-radar-acceptance-time"],
            ),
            ("free-form", ["Memory Radar acceptance time"]),
        ):
            with self.subTest(name=name):
                invalid = deepcopy(native)
                invalid["direction_keys"] = value
                self.assertTrue(list(validator.iter_errors(invalid)))

        legacy_with_keys = deepcopy(explicit_legacy)
        legacy_with_keys["direction_keys"] = ["memory-radar-acceptance-time"]
        self.assertTrue(list(validator.iter_errors(legacy_with_keys)))

        implicit_legacy = deepcopy(explicit_legacy)
        for field in V2_FIELDS:
            implicit_legacy.pop(field)
        implicit_legacy["direction_keys"] = ["memory-radar-acceptance-time"]
        self.assertTrue(list(validator.iter_errors(implicit_legacy)))

    def test_only_fixed_timeline_records_are_explicitly_migrated(self):
        records = repository_records()
        migrated = {
            str(record["id"])
            for record in records
            if record.get("time_provenance") == "legacy_unknown"
        }
        self.assertEqual(set(LEGACY_TIMELINE_COMPATIBILITY_IDS), migrated)
        for record in records:
            if record["id"] in migrated:
                self.assertEqual(record["published"], record["published_at"])
                self.assertIsNone(record["first_seen_at"])
                self.assertIsNone(record["radar_published_at"])
                self.assertEqual("early_signal", record["map_delta"])
            elif record.get("time_provenance") != "native_v2":
                self.assertFalse(any(field in record for field in V2_FIELDS), record["id"])

    def test_explicit_legacy_outside_fixed_set_is_rejected(self):
        records = repository_records()
        extra = deepcopy(records[0])
        extra.update(
            id="outside-fixed-set",
            published_at=extra["published"],
            first_seen_at=None,
            radar_published_at=None,
            time_provenance="legacy_unknown",
            map_delta="early_signal",
        )
        errors = validate_reading.validate_memory_registry([*records, extra])
        self.assertTrue(any("outside-fixed-set" in error and "outside" in error for error in errors), errors)

    def test_reading_validator_loads_and_checks_the_canonical_registry(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            records = Path(temporary_directory)
            (records / "partial.json").write_text(
                json.dumps(
                    {"id": "partial", "published": "2026-08", "map_delta": "early_signal"}
                ),
                encoding="utf-8",
            )
            original = getattr(validate_reading, "RECORDS", None)
            validate_reading.RECORDS = records
            try:
                with redirect_stdout(io.StringIO()):
                    result = validate_reading.main()
            finally:
                if original is None:
                    delattr(validate_reading, "RECORDS")
                else:
                    validate_reading.RECORDS = original
        self.assertEqual(1, result)

    def test_canonical_validator_enforces_the_time_contract(self):
        record = next(
            item for item in repository_records() if item["id"] == "2608.17911"
        )
        for field in V2_FIELDS:
            if field != "map_delta":
                record.pop(field)

        with tempfile.TemporaryDirectory(dir=ROOT) as temporary_directory:
            records = Path(temporary_directory)
            (records / "2608.17911.json").write_text(
                json.dumps(record), encoding="utf-8"
            )
            original = validate_canonical.RECORDS
            validate_canonical.RECORDS = records
            try:
                with redirect_stdout(io.StringIO()):
                    result = validate_canonical.main()
            finally:
                validate_canonical.RECORDS = original
        self.assertEqual(1, result)

    def test_repository_validator_enforces_the_time_contract(self):
        record = next(
            item for item in repository_records() if item["id"] == "2608.17911"
        )
        for field in V2_FIELDS:
            if field != "map_delta":
                record.pop(field)

        with tempfile.TemporaryDirectory(dir=ROOT) as temporary_directory:
            records = Path(temporary_directory)
            (records / "2608.17911.json").write_text(
                json.dumps(record), encoding="utf-8"
            )
            original = validate_repository.PAPERS_DIR
            validate_repository.PAPERS_DIR = records
            try:
                with redirect_stdout(io.StringIO()):
                    result = validate_repository.main()
            finally:
                validate_repository.PAPERS_DIR = original
        self.assertEqual(1, result)


class MemoryProjectionContractTest(unittest.TestCase):
    def test_memory_projection_contract_is_exposed(self):
        self.assertTrue(callable(getattr(validate_reading, "validate_memory_projection", None)))

    def test_comment_hidden_family_route_does_not_count_as_visible_navigation(self):
        zh, _ = repository_readmes()
        route = validate_reading.FAMILY_ROUTES["Agent Benchmark"]
        mutated = zh.replace(
            f"[Agent Benchmark Radar]({route})",
            f"<!-- [Agent Benchmark Radar]({route}) -->",
            1,
        )
        errors: list[str] = []
        validate_reading.family_routes(mutated, "README.md", errors)
        self.assertTrue(any("Agent Benchmark" in error for error in errors), errors)

    def test_memory_aliases_are_visible_comment_stripped_and_cardinality_bound(self):
        zh, en = repository_readmes()
        self.assertEqual([], validate_reading.validate_memory_aliases(zh, en))
        for alias in ("latest-papers", "changes", "whats-changing", "research-map"):
            anchor = f'<a id="{alias}"></a>'
            with self.subTest(alias=alias, mutation="hidden-only"):
                hidden = zh.replace(anchor, f"<!-- {anchor} -->", 1)
                errors = validate_reading.validate_memory_aliases(hidden, en)
                self.assertTrue(
                    any(f"missing Memory compatibility alias {alias}" in error for error in errors),
                    errors,
                )
            with self.subTest(alias=alias, mutation="hidden-decoy"):
                decoy = zh.replace(anchor, f"<!-- {anchor} -->\n{anchor}", 1)
                self.assertEqual([], validate_reading.validate_memory_aliases(decoy, en))
            with self.subTest(alias=alias, mutation="visible-duplicate"):
                duplicate = zh.replace(anchor, anchor + anchor, 1)
                errors = validate_reading.validate_memory_aliases(duplicate, en)
                self.assertTrue(
                    any(f"duplicate Memory compatibility alias {alias}" in error for error in errors),
                    errors,
                )

    def test_reverse_timeline_rejects_missing_duplicate_and_unexpected_identities(self):
        zh, en = valid_projection_pair()
        records = repository_records()
        first = '<a id="entry-2608-17911"></a>'
        next_entry = '<a id="entry-2608-17756"></a>'
        first_start = zh.index(first)
        first_end = zh.index(next_entry, first_start)
        variants = {
            "missing": zh[:first_start] + zh[first_end:],
            "duplicate": zh.replace(first, first + "\n" + first, 1),
            "unexpected": zh.replace(first, '<a id="entry-not-canonical"></a>\n' + first, 1),
        }
        for name, mutated in variants.items():
            with self.subTest(name=name):
                errors = validate_reading.validate_memory_projection(mutated, en, records)
                self.assertTrue(any("Timeline" in error for error in errors), errors)

    def test_timeline_binds_date_map_primary_and_paired_deep_notes(self):
        zh, en = valid_projection_pair()
        records = repository_records()
        variants = {
            "date": zh.replace("2026-08-18 · CABLE", "2026-08-17 · CABLE", 1),
            "map": zh.replace("`early_signal`", "`reinforces`", 1),
            "primary": zh.replace(
                "https://arxiv.org/abs/2608.17911",
                "https://example.com/wrong-paper",
                1,
            ),
            "hidden-primary": zh.replace(
                "[论文](https://arxiv.org/abs/2608.17911)",
                "<!-- [论文](https://arxiv.org/abs/2608.17911) --> "
                "[论文](https://example.com/wrong-paper)",
                1,
            ),
            "primary-field-laundering": zh.replace(
                "[论文](https://arxiv.org/abs/2608.17911)",
                "[论文](https://example.com/wrong-paper)",
                1,
            ).replace(
                "**证据。**",
                "**证据。** [论文](https://arxiv.org/abs/2608.17911)",
                1,
            ),
            "hidden-map": zh.replace(
                "`early_signal`",
                "<!-- `early_signal` --> `reinforces`",
                1,
            ),
            "notes": zh.replace(
                "[中文深读](papers/2026/2608.17911.zh.md) · "
                "[英文深读](papers/2026/2608.17911.md)",
                "[中文深读](papers/2026/2608.17756.zh.md) · "
                "[英文深读](papers/2026/2608.17756.md)",
                1,
            ),
            "hidden-notes": zh.replace(
                "[中文深读](papers/2026/2608.17911.zh.md) · "
                "[英文深读](papers/2026/2608.17911.md)",
                "<!-- [中文深读](papers/2026/2608.17911.zh.md) · "
                "[英文深读](papers/2026/2608.17911.md) -->",
                1,
            ),
            "note-field-laundering": zh.replace(
                "[中文深读](papers/2026/2608.17911.zh.md) · "
                "[英文深读](papers/2026/2608.17911.md)",
                "[No local note](https://example.com/no-local-note)",
                1,
            ).replace(
                "**证据。**",
                "**证据。** [中文深读](papers/2026/2608.17911.zh.md) · "
                "[英文深读](papers/2026/2608.17911.md)",
                1,
            ),
        }
        expected_fragments = {
            "date": "displayed date",
            "map": "map token",
            "primary": "primary",
            "hidden-primary": "primary",
            "primary-field-laundering": "primary",
            "hidden-map": "map token",
            "notes": "deep-note",
            "hidden-notes": "deep-note",
            "note-field-laundering": "deep-note",
        }
        for name, mutated in variants.items():
            with self.subTest(name=name):
                errors = validate_reading.validate_memory_projection(mutated, en, records)
                self.assertTrue(
                    any(expected_fragments[name] in error for error in errors), errors
                )

    def test_native_timeline_uses_full_timestamp_then_identity_order_before_legacy(self):
        zh, en = valid_projection_pair()
        first = native_record("2608.90001")
        second = native_record("2608.90002")
        records = [*repository_records(), first, second]
        wrong_zh = prepend_timeline_entries(zh, [second, first], "zh")
        wrong_en = prepend_timeline_entries(en, [second, first], "en")
        errors = validate_reading.validate_memory_projection(wrong_zh, wrong_en, records)
        self.assertTrue(any("timestamp order" in error for error in errors), errors)

        correct_zh = prepend_timeline_entries(zh, [first, second], "zh")
        correct_en = prepend_timeline_entries(en, [first, second], "en")
        self.assertEqual(
            [], validate_reading.validate_memory_projection(correct_zh, correct_en, records)
        )

    def test_native_timeline_rejects_acceptance_after_public_synthesis_cutoff(self):
        zh, en = valid_projection_pair()
        late = native_record("2608.90001", "2026-08-28T01:00:00Z")
        records = [*repository_records(), late]
        zh = prepend_timeline_entries(zh, [late], "zh")
        en = prepend_timeline_entries(en, [late], "en")
        errors = validate_reading.validate_memory_projection(zh, en, records)
        self.assertTrue(any("Timeline" in error and "synthesis cutoff" in error for error in errors), errors)

    def test_support_at_0100_cannot_backdate_a_0000_direction_synthesis(self):
        zh, en = valid_projection_pair()
        late = native_record("2608.90001", "2026-08-28T01:00:00Z")
        records = [*repository_records(), late]
        zh = prepend_timeline_entries(zh, [late], "zh")
        en = prepend_timeline_entries(en, [late], "en")
        zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh", state="new_signal", supports=("2608.90001",)
            ),
        )
        en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en", state="new_signal", supports=("2608.90001",)
            ),
        )
        errors = validate_reading.validate_memory_projection(zh, en, records)
        self.assertTrue(
            any("support identity 2608.90001" in error and "synthesized" in error for error in errors),
            errors,
        )

    def test_periods_require_exact_windows_and_one_visible_range(self):
        zh, en = valid_projection_pair()
        records = repository_records()
        variants = {
            "wrong": zh.replace("2026-08-22—2026-08-28", "2026-08-13—2026-08-20", 1),
            "duplicate": zh.replace(
                direction_line("zh"),
                direction_line("zh") + " 2026-08-22—2026-08-28",
                1,
            ),
        }
        for name, mutated in variants.items():
            with self.subTest(name=name):
                errors = validate_reading.validate_memory_projection(mutated, en, records)
                self.assertTrue(any("window" in error or "range" in error for error in errors), errors)

    def test_period_metadata_and_visible_bindings_are_complete_and_bilingual(self):
        zh, en = valid_projection_pair()
        records = repository_records()
        mutations = {
            "confidence-enum": direction_line("zh", confidence="certain"),
            "key-visible": direction_line("zh").replace(
                "Memory Radar acceptance time", "unrelated visible direction", 1
            ),
            "key-laundering": direction_line("zh")
            .replace("Memory Radar acceptance time", "unrelated visible direction", 1)
            .replace(
                "仅原生接受时间可以支持窗口判断。",
                "仅原生接受时间可以支持窗口判断。旁注：Memory Radar acceptance time。",
                1,
            ),
            "implication-visible": direction_line("zh").replace(
                "require native v2 times for period claims",
                "unrelated visible implication",
                1,
            ),
            "implication-laundering": direction_line("zh")
            .replace(
                "（require native v2 times for period claims）",
                "（unrelated visible implication）",
                1,
            )
            .replace(
                "仅原生接受时间可以支持窗口判断。",
                "仅原生接受时间可以支持窗口判断。旁注：require native v2 times for period claims。",
                1,
            ),
            "timing": direction_line("zh", timing="published_at"),
            "timing-laundering": direction_line("zh")
            .replace("时间依据：`radar_published_at`", "时间依据：`missing`", 1)
            .replace(
                "仅原生接受时间可以支持窗口判断。",
                "仅原生接受时间可以支持窗口判断。旁注：`radar_published_at`。",
                1,
            ),
            "synthesis": direction_line("zh", synthesized="2026-08-20"),
            "synthesis-laundering": direction_line("zh")
            .replace(
                "精确合成时间：`2026-08-28T00:53:00Z`",
                "精确合成时间：`2026-08-20`",
                1,
            )
            .replace(
                "仅原生接受时间可以支持窗口判断。",
                "仅原生接受时间可以支持窗口判断。旁注：`2026-08-28T00:53:00Z`。",
                1,
            ),
            "prior-visible": direction_line("zh").replace(
                "先验地图证据：`none`", "先验地图证据：`missing`", 1
            ),
        }
        for name, line in mutations.items():
            with self.subTest(name=name):
                mutated = projection_readme(zh, "zh", seven_line=line)
                errors = validate_reading.validate_memory_projection(mutated, en, records)
                self.assertTrue(errors, name)

        drifted = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en", implication="use-a-different-research-design-gate"
            ),
        )
        errors = validate_reading.validate_memory_projection(zh, drifted, records)
        self.assertTrue(any("parity" in error for error in errors), errors)

    def test_period_direction_blocks_require_exactly_one_of_each_visible_field(self):
        base_zh, base_en = valid_projection_pair()
        records = repository_records()
        duplicates = {
            "zh": {
                "state": "旁注：**`no_material_change` · 矛盾状态。**",
                "supports": "旁注：支撑：**none**；",
                "confidence": "旁注：置信度：**high**；",
                "timing basis": "旁注：时间依据：`radar_published_at`；",
                "synthesis": "旁注：精确合成时间：`2026-08-28T00:53:00Z`。",
                "implication": (
                    "旁注：研究设计含义（require native v2 times for period claims）：重复。"
                ),
                "prior": "旁注：先验地图证据：`none`。",
            },
            "en": {
                "state": "Aside: **`no_material_change` · contradictory state.**",
                "supports": "Aside: Supports: **none**;",
                "confidence": "Aside: confidence: **high**;",
                "timing basis": "Aside: timing basis: `radar_published_at`;",
                "synthesis": "Aside: Exact synthesis time: `2026-08-28T00:53:00Z`.",
                "implication": (
                    "Aside: Research-design implication "
                    "(require native v2 times for period claims): duplicate."
                ),
                "prior": "Aside: prior map evidence: `none`.",
            },
        }
        for language, fields in duplicates.items():
            for field, duplicate in fields.items():
                with self.subTest(language=language, field=field):
                    line = f"{direction_line(language)} {duplicate}"
                    case_zh = (
                        projection_readme(base_zh, "zh", seven_line=line)
                        if language == "zh"
                        else base_zh
                    )
                    case_en = (
                        projection_readme(base_en, "en", seven_line=line)
                        if language == "en"
                        else base_en
                    )
                    errors = validate_reading.validate_memory_projection(
                        case_zh, case_en, records
                    )
                    self.assertTrue(
                        any(f"exactly one visible {field}" in error for error in errors),
                        errors,
                    )

    def test_period_direction_fields_may_live_on_continuation_lines(self):
        zh, en = valid_projection_pair()
        zh = projection_readme(
            zh, "zh", seven_line=multiline_direction_line("zh")
        )
        en = projection_readme(
            en, "en", seven_line=multiline_direction_line("en")
        )
        self.assertEqual(
            [], validate_reading.validate_memory_projection(zh, en, repository_records())
        )

    def test_direction_metadata_at_continuation_end_stays_in_visible_item_block(self):
        zh, en = valid_projection_pair()
        zh_line = direction_line("zh").replace(" 支撑：", "\n  支撑：", 1)
        en_line = direction_line("en").replace(" Supports:", "\n  Supports:", 1)
        zh = projection_readme(zh, "zh", seven_line=zh_line)
        en = projection_readme(en, "en", seven_line=en_line)

        self.assertEqual(
            [], validate_reading.validate_memory_projection(zh, en, repository_records())
        )

    def test_metadata_only_continuation_stays_in_visible_direction_item(self):
        zh, en = valid_projection_pair()
        lines: dict[str, str] = {}
        for language in ("zh", "en"):
            line = direction_line(language)
            metadata_start = line.index("<!-- timefirst:direction")
            lines[language] = (
                f"{line[:metadata_start].rstrip()}\n  {line[metadata_start:]}"
            )
        zh = projection_readme(zh, "zh", seven_line=lines["zh"])
        en = projection_readme(en, "en", seven_line=lines["en"])

        self.assertEqual(
            [], validate_reading.validate_memory_projection(zh, en, repository_records())
        )

    def test_true_duplicate_metadata_on_continuation_is_rejected(self):
        zh, en = valid_projection_pair()
        line = direction_line("zh")
        metadata = line[line.index("<!-- timefirst:direction") :]
        zh = projection_readme(zh, "zh", seven_line=f"{line}\n  {metadata}")

        errors = validate_reading.validate_memory_projection(
            zh, en, repository_records()
        )

        self.assertTrue(
            any(
                "README.md" in error
                and "last-7-days" in error
                and "exactly one stable direction metadata block" in error
                for error in errors
            ),
            errors,
        )

    def test_adjacent_visible_direction_items_remain_distinct_block_boundaries(self):
        zh, en = valid_projection_pair()
        lines: dict[str, str] = {}
        for language in ("zh", "en"):
            first = direction_line(language)
            second = direction_line(language).replace(
                "Memory Radar acceptance time",
                "Memory retrieval cutoff",
                1,
            ).replace(
                'key="memory-radar-acceptance-time"',
                'key="memory-retrieval-cutoff"',
                1,
            )
            metadata_start = second.index("<!-- timefirst:direction")
            second = (
                f"{second[:metadata_start].rstrip()}\n  {second[metadata_start:]}"
            )
            lines[language] = f"{first}\n{second}"
        zh = projection_readme(zh, "zh", seven_line=lines["zh"])
        en = projection_readme(en, "en", seven_line=lines["en"])

        self.assertEqual(
            [], validate_reading.validate_memory_projection(zh, en, repository_records())
        )

    def test_malformed_primary_fields_cannot_be_laundered_by_valid_labeled_asides(self):
        base_zh, base_en = valid_projection_pair()
        records = repository_records()
        mutations = {
            "zh": (
                (
                    "supports",
                    "支撑：**none**；",
                    "支撑缺少结构。旁注：支撑：**none**；",
                ),
                (
                    "confidence",
                    "置信度：**high**；",
                    "置信度缺少结构。旁注：置信度：**high**；",
                ),
                (
                    "timing basis",
                    "时间依据：`radar_published_at`；",
                    "时间依据缺少结构。旁注：时间依据：`radar_published_at`；",
                ),
                (
                    "prior",
                    "先验地图证据：`none`。",
                    "先验地图证据缺少结构。旁注：先验地图证据：`none`。",
                ),
                (
                    "implication",
                    "研究设计含义（require native v2 times for period claims）：",
                    "研究设计含义缺少结构。旁注：研究设计含义"
                    "（require native v2 times for period claims）：",
                ),
                (
                    "synthesis",
                    "精确合成时间：`2026-08-28T00:53:00Z`。",
                    "精确合成时间缺少结构。旁注：精确合成时间："
                    "`2026-08-28T00:53:00Z`。",
                ),
            ),
            "en": (
                (
                    "supports",
                    "Supports: **none**;",
                    "Supports lacks structure. Aside: Supports: **none**;",
                ),
                (
                    "confidence",
                    "confidence: **high**;",
                    "confidence lacks structure. Aside: confidence: **high**;",
                ),
                (
                    "timing basis",
                    "timing basis: `radar_published_at`;",
                    "timing basis lacks structure. Aside: timing basis: "
                    "`radar_published_at`;",
                ),
                (
                    "prior",
                    "prior map evidence: `none`.",
                    "prior map evidence lacks structure. Aside: prior map evidence: `none`.",
                ),
                (
                    "implication",
                    "Research-design implication "
                    "(require native v2 times for period claims):",
                    "Research-design implication lacks structure. Aside: "
                    "Research-design implication "
                    "(require native v2 times for period claims):",
                ),
                (
                    "synthesis",
                    "Exact synthesis time: `2026-08-28T00:53:00Z`.",
                    "Exact synthesis time lacks structure. Aside: Exact synthesis time: "
                    "`2026-08-28T00:53:00Z`.",
                ),
            ),
        }
        for language, cases in mutations.items():
            for field, old, new in cases:
                with self.subTest(language=language, field=field):
                    line = direction_line(language).replace(old, new, 1)
                    case_zh = (
                        projection_readme(base_zh, "zh", seven_line=line)
                        if language == "zh"
                        else base_zh
                    )
                    case_en = (
                        projection_readme(base_en, "en", seven_line=line)
                        if language == "en"
                        else base_en
                    )
                    errors = validate_reading.validate_memory_projection(
                        case_zh, case_en, records
                    )
                    self.assertTrue(
                        any(f"exactly one visible {field}" in error for error in errors),
                        errors,
                    )

    def test_period_direction_requires_its_language_specific_visible_labels(self):
        base_zh, base_en = valid_projection_pair()
        records = repository_records()
        mutations = {
            "zh": (
                ("支撑：", "Supports: ", "supports"),
                ("置信度：", "confidence: ", "confidence"),
                ("时间依据：", "timing basis: ", "timing basis"),
                ("先验地图证据：", "prior map evidence: ", "prior"),
                ("研究设计含义（", "Research-design implication (", "implication"),
                ("精确合成时间：", "Exact synthesis time: ", "synthesis"),
            ),
            "en": (
                ("Supports: ", "支撑：", "supports"),
                ("confidence: ", "置信度：", "confidence"),
                ("timing basis: ", "时间依据：", "timing basis"),
                ("prior map evidence: ", "先验地图证据：", "prior"),
                ("Research-design implication (", "研究设计含义（", "implication"),
                ("Exact synthesis time: ", "精确合成时间：", "synthesis"),
            ),
        }
        for language, cases in mutations.items():
            for old, new, field in cases:
                with self.subTest(language=language, field=field):
                    line = direction_line(language).replace(old, new, 1)
                    case_zh = (
                        projection_readme(base_zh, "zh", seven_line=line)
                        if language == "zh"
                        else base_zh
                    )
                    case_en = (
                        projection_readme(base_en, "en", seven_line=line)
                        if language == "en"
                        else base_en
                    )
                    errors = validate_reading.validate_memory_projection(
                        case_zh, case_en, records
                    )
                    self.assertTrue(
                        any(f"exactly one visible {field}" in error for error in errors),
                        errors,
                    )

    def test_zero_support_visible_field_is_exact_not_an_aside_prefix(self):
        base_zh, base_en = valid_projection_pair()
        records = repository_records()
        mutations = (
            ("zh", "支撑：**none**；", "支撑：**none**（旁注仍称有证据）；"),
            ("en", "Supports: **none**;", "Supports: **none** plus an aside claim;"),
        )
        for language, old, new in mutations:
            with self.subTest(language=language):
                line = direction_line(language).replace(old, new, 1)
                case_zh = (
                    projection_readme(base_zh, "zh", seven_line=line)
                    if language == "zh"
                    else base_zh
                )
                case_en = (
                    projection_readme(base_en, "en", seven_line=line)
                    if language == "en"
                    else base_en
                )
                errors = validate_reading.validate_memory_projection(
                    case_zh, case_en, records
                )
                self.assertTrue(
                    any("zero support must be exactly" in error for error in errors),
                    errors,
                )

    def test_one_paper_signal_rejects_trend_in_continuations_and_attached_paragraphs(self):
        base_zh, base_en = valid_projection_pair()
        native = native_record("2608.90001")
        records = [*repository_records(), native]
        base_zh = prepend_timeline_entries(base_zh, [native], "zh")
        base_en = prepend_timeline_entries(base_en, [native], "en")
        valid_lines = {
            language: direction_line(
                language, state="new_signal", supports=("2608.90001",)
            )
            for language in ("zh", "en")
        }
        mutations = (
            ("en", "\n  This indented continuation calls it a trend."),
            ("zh", "\n  这个缩进续行称其为趋势。"),
            ("en", "\n\nThis attached paragraph calls it a trend."),
            ("zh", "\n\n这个附着段落称其为趋势。"),
        )
        for language, addition in mutations:
            with self.subTest(language=language, addition=addition.strip()):
                zh_line = valid_lines["zh"] + (addition if language == "zh" else "")
                en_line = valid_lines["en"] + (addition if language == "en" else "")
                zh = projection_readme(base_zh, "zh", seven_line=zh_line)
                en = projection_readme(base_en, "en", seven_line=en_line)
                errors = validate_reading.validate_memory_projection(zh, en, records)
                self.assertTrue(
                    any("trend/趋势 claim" in error for error in errors), errors
                )

    def test_next_period_and_field_map_prose_are_outside_direction_blocks(self):
        zh, en = valid_projection_pair()
        native = native_record("2608.90001")
        records = [*repository_records(), native]
        zh = prepend_timeline_entries(zh, [native], "zh")
        en = prepend_timeline_entries(en, [native], "en")
        zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh", state="new_signal", supports=("2608.90001",)
            ),
        )
        en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en", state="new_signal", supports=("2608.90001",)
            ),
        )
        mutations = (
            (
                '<a id="last-30-days"></a>',
                '<a id="last-30-days"></a>\n下一个时间窗的趋势说明。',
                '<a id="last-30-days"></a>\nThe next period trend prose.',
            ),
            (
                '<a id="field-map"></a>',
                '<a id="field-map"></a>\n这是领域地图的趋势说明。',
                '<a id="field-map"></a>\nThis is Field Map trend prose.',
            ),
        )
        for marker, zh_replacement, en_replacement in mutations:
            with self.subTest(marker=marker):
                case_zh = zh.replace(marker, zh_replacement, 1)
                case_en = en.replace(marker, en_replacement, 1)
                self.assertEqual(
                    [],
                    validate_reading.validate_memory_projection(
                        case_zh, case_en, records
                    ),
                )

    def test_period_support_is_visible_native_in_window_and_state_gated(self):
        zh, en = valid_projection_pair()
        first = native_record("2608.90001")
        second = native_record("2608.90002", map_delta="reinforces")
        records = [*repository_records(), first, second]
        zh = prepend_timeline_entries(zh, [first, second], "zh")
        en = prepend_timeline_entries(en, [first, second], "en")

        cases = {
            "legacy-support": (
                direction_line("zh", state="new_signal", supports=("2608.17911",)),
                direction_line("en", state="new_signal", supports=("2608.17911",)),
                "native_v2",
            ),
            "hidden-support": (
                direction_line(
                    "zh", state="new_signal", supports=("2608.90001",), visible_supports=()
                ).replace(
                    "支撑：**none**",
                    "支撑：<!-- [2608.90001](#entry-2608-90001) -->**none**",
                    1,
                ),
                direction_line(
                    "en", state="new_signal", supports=("2608.90001",), visible_supports=()
                ).replace(
                    "Supports: **none**",
                    "Supports: <!-- [2608.90001](#entry-2608-90001) -->**none**",
                    1,
                ),
                "visible support",
            ),
            "support-laundering": (
                direction_line(
                    "zh", state="new_signal", supports=("2608.90001",), visible_supports=()
                ).replace(
                    "仅原生接受时间可以支持窗口判断。",
                    "仅原生接受时间可以支持窗口判断。旁注：[2608.90001](#entry-2608-90001)。",
                    1,
                ),
                direction_line(
                    "en", state="new_signal", supports=("2608.90001",), visible_supports=()
                ).replace(
                    "only native acceptance times support the window.",
                    "only native acceptance times support the window. Aside: "
                    "[2608.90001](#entry-2608-90001).",
                    1,
                ),
                "visible support",
            ),
            "support-none-contradiction": (
                direction_line(
                    "zh", state="new_signal", supports=("2608.90001",)
                ).replace("支撑：", "支撑：**none** · ", 1),
                direction_line(
                    "en", state="new_signal", supports=("2608.90001",)
                ).replace("Supports: ", "Supports: **none** · ", 1),
                "visible support",
            ),
            "one-reinforced": (
                direction_line(
                    "zh",
                    state="reinforced",
                    supports=("2608.90001",),
                    prior="prior-memory-claim",
                ),
                direction_line(
                    "en",
                    state="reinforced",
                    supports=("2608.90001",),
                    prior="prior-memory-claim",
                ),
                "at least two",
            ),
            "new-signal-map": (
                direction_line("zh", state="new_signal", supports=("2608.90002",)),
                direction_line("en", state="new_signal", supports=("2608.90002",)),
                "map_delta=early_signal",
            ),
            "durable-no-prior": (
                direction_line(
                    "zh",
                    state="reinforced",
                    supports=("2608.90002", "2608.90001"),
                ),
                direction_line(
                    "en",
                    state="reinforced",
                    supports=("2608.90002", "2608.90001"),
                ),
                "prior",
            ),
        }
        for name, (zh_line, en_line, fragment) in cases.items():
            with self.subTest(name=name):
                case_zh = projection_readme(zh, "zh", seven_line=zh_line)
                case_en = projection_readme(en, "en", seven_line=en_line)
                errors = validate_reading.validate_memory_projection(case_zh, case_en, records)
                self.assertTrue(any(fragment in error for error in errors), errors)

    def test_no_material_change_requires_zero_support_and_radar_basis(self):
        zh, en = valid_projection_pair()
        native = native_record("2608.90001")
        records = [*repository_records(), native]
        zh = prepend_timeline_entries(zh, [native], "zh")
        en = prepend_timeline_entries(en, [native], "en")
        bad_zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line("zh", supports=("2608.90001",)),
        )
        bad_en = projection_readme(
            en,
            "en",
            seven_line=direction_line("en", supports=("2608.90001",)),
        )
        errors = validate_reading.validate_memory_projection(bad_zh, bad_en, records)
        self.assertTrue(any("no_material_change" in error for error in errors), errors)

    def test_reinforced_supports_must_share_the_declared_direction_key(self):
        zh, en = valid_projection_pair()
        direction_key = "memory-shared-direction"
        first = native_record(
            "2608.90001",
            direction_keys=(direction_key,),
        )
        mismatch = native_record(
            "2608.90002",
            map_delta="reinforces",
            direction_keys=("memory-other-direction",),
        )
        records = [*repository_records(), first, mismatch]
        zh = prepend_timeline_entries(zh, [first, mismatch], "zh")
        en = prepend_timeline_entries(en, [first, mismatch], "en")
        zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh",
                key=direction_key,
                state="reinforced",
                supports=("2608.90001", "2608.90002"),
                prior="field-map",
            ),
        )
        en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en",
                key=direction_key,
                state="reinforced",
                supports=("2608.90001", "2608.90002"),
                prior="field-map",
            ),
        )

        errors = validate_reading.validate_memory_projection(zh, en, records)

        self.assertTrue(
            any(
                "2608.90002" in error
                and "direction_keys" in error
                and direction_key in error
                for error in errors
            ),
            errors,
        )

    def test_same_direction_reinforcement_with_two_bound_supports_can_pass(self):
        zh, en = valid_projection_pair()
        direction_key = "memory-shared-direction"
        first = native_record(
            "2608.90001",
            direction_keys=(direction_key,),
        )
        second = native_record(
            "2608.90002",
            map_delta="reinforces",
            direction_keys=(direction_key,),
        )
        records = [*repository_records(), first, second]
        zh = prepend_timeline_entries(zh, [first, second], "zh")
        en = prepend_timeline_entries(en, [first, second], "en")
        zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh",
                key=direction_key,
                state="reinforced",
                supports=("2608.90001", "2608.90002"),
                prior="field-map",
            ),
        )
        en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en",
                key=direction_key,
                state="reinforced",
                supports=("2608.90001", "2608.90002"),
                prior="field-map",
            ),
        )

        self.assertEqual(
            [], validate_reading.validate_memory_projection(zh, en, records)
        )

    def test_split_and_retirement_directions_with_bound_map_evidence_can_pass(self):
        for state in ("splits", "retires"):
            with self.subTest(state=state):
                key = f"memory-{state}-direction"
                record = native_record(
                    "2608.90001",
                    map_delta=state,
                    direction_keys=(key,),
                )
                records = [*repository_records(), record]
                zh, en = valid_projection_pair()
                zh = prepend_timeline_entries(zh, [record], "zh")
                en = prepend_timeline_entries(en, [record], "en")
                zh = projection_readme(
                    zh,
                    "zh",
                    seven_line=direction_line(
                        "zh",
                        key=key,
                        state=state,
                        supports=("2608.90001",),
                        prior="field-map",
                    ),
                )
                en = projection_readme(
                    en,
                    "en",
                    seven_line=direction_line(
                        "en",
                        key=key,
                        state=state,
                        supports=("2608.90001",),
                        prior="field-map",
                    ),
                )

                self.assertEqual(
                    [], validate_reading.validate_memory_projection(zh, en, records)
                )

    def test_split_and_retirement_direction_gates_reject_invalid_evidence(self):
        for state in ("splits", "retires"):
            key = f"memory-{state}-direction"
            identity = "2608.90001"

            def errors_for(
                record: dict[str, object] | None,
                *,
                supports: tuple[str, ...],
                prior: str = "field-map",
            ) -> list[str]:
                zh, en = valid_projection_pair()
                records = repository_records()
                if record is not None:
                    records.append(record)
                    zh = prepend_timeline_entries(zh, [record], "zh")
                    en = prepend_timeline_entries(en, [record], "en")
                zh = projection_readme(
                    zh,
                    "zh",
                    seven_line=direction_line(
                        "zh",
                        key=key,
                        state=state,
                        supports=supports,
                        prior=prior,
                    ),
                )
                en = projection_readme(
                    en,
                    "en",
                    seven_line=direction_line(
                        "en",
                        key=key,
                        state=state,
                        supports=supports,
                        prior=prior,
                    ),
                )
                return validate_reading.validate_memory_projection(zh, en, records)

            cases = {
                "zero-support": (
                    None,
                    (),
                    "field-map",
                    f"labeled {state} requires canonical support",
                ),
                "prior-none": (
                    native_record(
                        identity, map_delta=state, direction_keys=(key,)
                    ),
                    (identity,),
                    "none",
                    "durable direction requires independent prior Field Map evidence",
                ),
                "wrong-direction-key": (
                    native_record(
                        identity,
                        map_delta=state,
                        direction_keys=("memory-other-direction",),
                    ),
                    (identity,),
                    "field-map",
                    f"direction_keys must include {key}",
                ),
                "post-cutoff": (
                    native_record(
                        identity,
                        "2026-08-28T01:00:00Z",
                        map_delta=state,
                        direction_keys=(key,),
                    ),
                    (identity,),
                    "field-map",
                    "accepted after direction synthesized=2026-08-28T00:53:00Z",
                ),
                "incompatible-map-delta": (
                    native_record(
                        identity,
                        map_delta="early_signal",
                        direction_keys=(key,),
                    ),
                    (identity,),
                    "field-map",
                    f"requires at least one native support with map_delta={state}",
                ),
            }
            for name, (record, supports, prior, fragment) in cases.items():
                with self.subTest(state=state, case=name):
                    errors = errors_for(record, supports=supports, prior=prior)
                    self.assertTrue(
                        any(fragment in error for error in errors), errors
                    )

    def test_split_retirement_state_drift_is_rejected_as_bilingual_parity(self):
        split_key = "memory-splits-direction"
        retire_key = "memory-retires-direction"
        split = native_record(
            "2608.90001",
            map_delta="splits",
            direction_keys=(split_key,),
        )
        retire = native_record(
            "2608.90002",
            map_delta="retires",
            direction_keys=(retire_key,),
        )
        records = [*repository_records(), split, retire]
        zh, en = valid_projection_pair()
        zh = prepend_timeline_entries(zh, [split, retire], "zh")
        en = prepend_timeline_entries(en, [split, retire], "en")
        zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh",
                key=split_key,
                state="splits",
                supports=("2608.90001",),
                prior="field-map",
            ),
        )
        en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en",
                key=retire_key,
                state="retires",
                supports=("2608.90002",),
                prior="field-map",
            ),
        )

        errors = validate_reading.validate_memory_projection(zh, en, records)

        self.assertTrue(any("direction parity drift" in error for error in errors), errors)

    def test_one_paper_signal_and_two_paper_reinforcement_can_pass_the_gates(self):
        zh, en = valid_projection_pair()
        first = native_record("2608.90001")
        second = native_record("2608.90002", map_delta="reinforces")
        records = [*repository_records(), first, second]
        zh = prepend_timeline_entries(zh, [first, second], "zh")
        en = prepend_timeline_entries(en, [first, second], "en")

        new_signal_zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh", state="new_signal", supports=("2608.90001",)
            ),
        )
        new_signal_en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en", state="new_signal", supports=("2608.90001",)
            ),
        )
        self.assertEqual(
            [],
            validate_reading.validate_memory_projection(
                new_signal_zh, new_signal_en, records
            ),
        )

        reinforced_zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh",
                state="reinforced",
                supports=("2608.90002", "2608.90001"),
                prior="field-map",
            ),
        )
        reinforced_en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en",
                state="reinforced",
                supports=("2608.90002", "2608.90001"),
                prior="field-map",
            ),
        )
        self.assertEqual(
            [],
            validate_reading.validate_memory_projection(
                reinforced_zh, reinforced_en, records
            ),
        )

        laundered_zh = reinforced_zh.replace(
            "先验地图证据：[Field Map](#field-map)",
            "先验地图证据：`missing`",
            1,
        ).replace(
            "仅原生接受时间可以支持窗口判断。",
            "仅原生接受时间可以支持窗口判断。旁注：[Field Map](#field-map)。",
            1,
        )
        laundered_en = reinforced_en.replace(
            "prior map evidence: [Field Map](#field-map)",
            "prior map evidence: `missing`",
            1,
        ).replace(
            "only native acceptance times support the window.",
            "only native acceptance times support the window. Aside: [Field Map](#field-map).",
            1,
        )
        errors = validate_reading.validate_memory_projection(
            laundered_zh, laundered_en, records
        )
        self.assertTrue(any("prior" in error for error in errors), errors)

    def test_period_support_membership_uses_radar_acceptance_time_only(self):
        zh, en = valid_projection_pair()
        outside = native_record("2608.90001", "2026-08-14T23:59:59Z")
        outside["first_seen_at"] = "2026-08-14T23:59:59Z"
        records = [*repository_records(), outside]
        zh = projection_readme(
            zh,
            "zh",
            seven_line=direction_line(
                "zh", state="new_signal", supports=("2608.90001",)
            ),
        )
        en = projection_readme(
            en,
            "en",
            seven_line=direction_line(
                "en", state="new_signal", supports=("2608.90001",)
            ),
        )
        errors = validate_reading.validate_memory_projection(zh, en, records)
        self.assertTrue(
            any("falls outside" in error and "radar_published_at" in error for error in errors),
            errors,
        )

    def test_valid_projection_pair_passes(self):
        zh, en = valid_projection_pair()
        self.assertEqual(
            [], validate_reading.validate_memory_projection(zh, en, repository_records())
        )

    def test_reading_validator_enforces_memory_projection(self):
        with mock.patch.object(
            validate_reading,
            "validate_memory_projection",
            return_value=["sentinel projection error"],
        ):
            with redirect_stdout(io.StringIO()):
                result = validate_reading.main()
        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
