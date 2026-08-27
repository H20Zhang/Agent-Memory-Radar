#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

from timefirst_contract import strip_html_comments, validate_pair

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "README.md"
EN = ROOT / "README.en.md"
LIB_ZH = ROOT / "library" / "README.md"
LIB_EN = ROOT / "library" / "README.en.md"
RECORDS = ROOT / "data" / "papers"
PUBLIC_OPERATIONAL_RUN_PATHS = (ROOT / "runs" / "daily",)

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
ENTRY_ANCHOR_RE = re.compile(r'<a\s+id=["\']entry-([^"\']+)["\']\s*></a>', re.I)
MEMORY_NOTE_RE = re.compile(
    r"\[[^\]]+\]\(papers/\d{4}/(?P<identity>\d{4}\.\d+)"
    r"(?P<chinese>\.zh)?\.md\)"
)
SUMMARY_IDENTITY_RE = re.compile(
    r"<details>\s*<summary>\s*<strong>(?P<date>\d{4}-\d{2}(?:-\d{2})?)\s*·\s*"
    r"(?P<title>[^<\n]+?)</strong>\s*·",
    re.I | re.S,
)
VISIBLE_MAP_RE = re.compile(
    r"\*\*(?:Map|地图)(?:[.。:：])?\*\*.*?"
    r"`(none|early_signal|reinforces|revises|splits|retires)`",
    re.I | re.S,
)
VISIBLE_LINKS_FIELD_RE = re.compile(
    r"\*\*(?:Links|链接)(?:[.。:：])?\*\*\s*(?P<links>.*?)(?=</details>|$)",
    re.I | re.S,
)
PERIOD_RANGE_RE = re.compile(
    r"(?P<start>\d{4}-\d{2}-\d{2})\s*[—–]\s*(?P<end>\d{4}-\d{2}-\d{2})"
)
DIRECTION_COMMENT_RE = re.compile(
    r"<!--\s*timefirst:direction\s+(?P<attributes>.*?)\s*-->", re.I
)
DIRECTION_ATTRIBUTE_RE = re.compile(r'(?P<name>[a-z_]+)="(?P<value>[^"]*)"', re.I)
DIRECTION_STATE_PATTERN = (
    r"new_signal|reinforced|revised|splits|retires|no_material_change"
)
DIRECTION_STATE_LABEL_RE = re.compile(
    rf"\*\*`(?P<value>{DIRECTION_STATE_PATTERN})`",
    re.I,
)
DIRECTION_STATE_VALUE_RE = re.compile(
    rf"\*\*`(?P<value>{DIRECTION_STATE_PATTERN})`\s*·",
    re.I,
)
DIRECTION_HEADING_RE = re.compile(
    rf"^\s*-\s+\*\*`(?P<state>{DIRECTION_STATE_PATTERN})`"
    r"\s*·\s*(?P<heading>.*?)\*\*",
    re.I | re.M,
)
PERIOD_SUPPORT_RE = re.compile(r"\[[^\]]+\]\(#entry-([^)]+)\)", re.I)
VISIBLE_DIRECTION_LABELS = {
    "README.md": {
        "state": DIRECTION_STATE_LABEL_RE,
        "supports": re.compile(r"支撑"),
        "confidence": re.compile(r"置信度"),
        "timing basis": re.compile(r"时间依据"),
        "synthesis": re.compile(r"精确合成时间"),
        "implication": re.compile(r"研究设计含义"),
        "prior": re.compile(r"先验地图证据"),
    },
    "README.en.md": {
        "state": DIRECTION_STATE_LABEL_RE,
        "supports": re.compile(r"\bSupports\b", re.I),
        "confidence": re.compile(r"\bconfidence\b", re.I),
        "timing basis": re.compile(r"\btiming basis\b", re.I),
        "synthesis": re.compile(r"\bExact synthesis time\b", re.I),
        "implication": re.compile(r"\bResearch-design implication\b", re.I),
        "prior": re.compile(r"\bprior map evidence\b", re.I),
    },
}
VISIBLE_DIRECTION_VALUES = {
    "README.md": {
        "state": DIRECTION_STATE_VALUE_RE,
        "supports": re.compile(r"支撑\s*：\s*(?P<value>[^\n；]*?)；"),
        "confidence": re.compile(
            r"置信度\s*：\s*\*\*(?P<value>[^*\n]+)\*\*"
        ),
        "timing basis": re.compile(r"时间依据\s*：\s*`(?P<value>[^`\n]+)`"),
        "synthesis": re.compile(r"精确合成时间\s*：\s*`(?P<value>[^`\n]+)`"),
        "implication": re.compile(
            r"研究设计含义\s*（(?P<value>[^）\n]+)）\s*："
        ),
        "prior": re.compile(r"先验地图证据\s*：\s*(?P<value>[^\n。；]+)[。；]"),
    },
    "README.en.md": {
        "state": DIRECTION_STATE_VALUE_RE,
        "supports": re.compile(r"\bSupports\s*:\s*(?P<value>[^\n;]*?);", re.I),
        "confidence": re.compile(
            r"\bconfidence\s*:\s*\*\*(?P<value>[^*\n]+)\*\*", re.I
        ),
        "timing basis": re.compile(
            r"\btiming basis\s*:\s*`(?P<value>[^`\n]+)`", re.I
        ),
        "synthesis": re.compile(
            r"\bExact synthesis time\s*:\s*`(?P<value>[^`\n]+)`", re.I
        ),
        "implication": re.compile(
            r"\bResearch-design implication\s*\((?P<value>[^)\n]+)\)\s*:",
            re.I,
        ),
        "prior": re.compile(
            r"\bprior map evidence\s*:\s*(?P<value>[^\n.;]+)[.;]", re.I
        ),
    },
}
VISIBLE_PRIOR_MAP_VALUE_RE = re.compile(r"\[[^\]]+\]\(#field-map\)", re.I)
TREND_CLAIM_RE = re.compile(r"(?<![a-z])trend(?![a-z])|趋势", re.I)
DEEP_NOTE_TARGET_RE = re.compile(
    r"^papers/(?P<year>\d{4})/(?P<identity>\d{4}\.\d+)"
    r"(?P<chinese>\.zh)?\.md$",
    re.I,
)
STRICT_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
PUBLISHED_RE = re.compile(r"^\d{4}-\d{2}(?:-\d{2})?$")
STABLE_TOKEN_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
V2_FIELDS = (
    "published_at",
    "first_seen_at",
    "radar_published_at",
    "time_provenance",
    "map_delta",
)
MAP_DELTAS = frozenset(
    ("none", "early_signal", "reinforces", "revises", "splits", "retires")
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
V2_CUTOVER = datetime(2026, 8, 20, tzinfo=timezone.utc)
DIRECTION_ATTRIBUTES = (
    "key",
    "state",
    "supports",
    "confidence",
    "implication",
    "timing",
    "synthesized",
    "prior",
)
DIRECTION_STATES = frozenset(DIRECTION_STATE_PATTERN.split("|"))
CONFIDENCE_VALUES = frozenset(("low", "medium", "high"))
SYNTHESIS_TIMESTAMP = "2026-08-27T00:34:29Z"
EXPECTED_PERIOD_WINDOWS = {
    "last-7-days": (date(2026, 8, 21), date(2026, 8, 27)),
    "last-30-days": (date(2026, 7, 29), date(2026, 8, 27)),
}
FAMILY_ROUTES = {
    "Agent Benchmark": "https://github.com/H20Zhang/Agent-Benchmark-Radar",
    "Agentic RAG": "https://github.com/H20Zhang/Agentic-RAG-Radar",
    "Data Agent": "https://github.com/H20Zhang/Data-Agent-Radar",
    "Agent Memory evaluation": "https://github.com/H20Zhang/Agent-Benchmark-Radar#benchmark-memory",
}
MEMORY_ALIASES = ("latest-papers", "changes", "whats-changing", "research-map")


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def local_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target = raw.strip().strip("<>")
        parsed = urlsplit(target)
        if not target or target.startswith("#") or parsed.scheme or parsed.netloc:
            continue
        rel = unquote(parsed.path)
        if not rel:
            continue
        resolved = (path.parent / rel).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(errors, f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            fail(errors, f"{path.relative_to(ROOT)}: broken local link: {target}")


def family_routes(text: str, name: str, errors: list[str]) -> None:
    targets = {
        raw.strip().strip("<>")
        for raw in LINK_RE.findall(strip_html_comments(text))
    }
    for label, target in FAMILY_ROUTES.items():
        if target not in targets:
            fail(errors, f"{name}: missing canonical {label} family route")


def _anchor_matches(text: str, anchor: str) -> list[re.Match[str]]:
    return list(
        re.finditer(rf'<a\s+id=["\']{re.escape(anchor)}["\']\s*></a>', text, re.I)
    )


def validate_memory_aliases(zh: str, en: str) -> list[str]:
    """Return Memory-only visible compatibility-alias cardinality violations."""

    errors: list[str] = []
    for language, raw_text in (("README.md", zh), ("README.en.md", en)):
        visible_text = strip_html_comments(raw_text)
        for alias in MEMORY_ALIASES:
            matches = _anchor_matches(visible_text, alias)
            if not matches:
                errors.append(f"{language}: missing Memory compatibility alias {alias}")
            elif len(matches) > 1:
                errors.append(f"{language}: duplicate Memory compatibility alias {alias}")
    return errors


def validate_memory_note_links(zh: str, en: str) -> list[str]:
    """Return Memory-specific Timeline deep-note contract violations."""

    errors: list[str] = []
    for language, text in (("README.md", zh), ("README.en.md", en)):
        timeline_start = text.find('<a id="timeline"></a>')
        periods_start = text.find('<a id="periods"></a>')
        if timeline_start < 0 or periods_start <= timeline_start:
            continue
        timeline = text[timeline_start:periods_start]
        anchors = list(ENTRY_ANCHOR_RE.finditer(timeline))
        for index, anchor in enumerate(anchors):
            end = anchors[index + 1].start() if index + 1 < len(anchors) else len(timeline)
            chunk = timeline[anchor.end():end]
            identity = anchor.group(1)
            english_ids: set[str] = set()
            chinese_ids: set[str] = set()
            for match in MEMORY_NOTE_RE.finditer(chunk):
                note_identity = match.group("identity").replace(".", "-", 1)
                target = chinese_ids if match.group("chinese") else english_ids
                target.add(note_identity)

            if identity not in english_ids or identity not in chinese_ids:
                if english_ids or chinese_ids:
                    errors.append(
                        f"{language}: entry identity {identity} deep-note links do not "
                        "correspond to the entry identity"
                    )
                else:
                    errors.append(
                        f"{language}: entry identity {identity} needs corresponding "
                        "Chinese and English deep-note links"
                    )
    return errors


def validate_no_public_run_files(paths: tuple[Path, ...]) -> list[str]:
    """Reject every file or symlink below a configured public run path."""

    errors: list[str] = []
    for root in paths:
        if not root.exists() and not root.is_symlink():
            continue
        candidates = (root,) if root.is_file() or root.is_symlink() else root.rglob("*")
        for path in sorted(candidates):
            if path.is_file() or path.is_symlink():
                errors.append(
                    "public operational run file is forbidden; preserve accepted provenance "
                    f"in canonical projections and git, and private state in .radar-private/: {path}"
                )
    return errors


def validate_record_time_contract(record: dict[str, object]) -> list[str]:
    """Validate one implicit-legacy, explicit-legacy, or native-v2 record."""

    errors: list[str] = []
    identity = str(record.get("id", "<missing-id>"))
    direction_keys_present = "direction_keys" in record
    if direction_keys_present and _canonical_direction_keys(
        record.get("direction_keys")
    ) is None:
        errors.append(
            f"canonical record {identity}: direction_keys must be a non-empty list "
            "of unique lowercase stable tokens"
        )
    present = {field for field in V2_FIELDS if field in record}
    if not present:
        if direction_keys_present:
            errors.append(
                f"canonical record {identity}: direction_keys requires the complete "
                "native_v2 time contract"
            )
        return errors

    missing = [field for field in V2_FIELDS if field not in record]
    if missing:
        for field in missing:
            errors.append(
                f"canonical record {identity}: any v2 field requires complete field {field}"
            )
        return errors

    map_delta = record.get("map_delta")
    if map_delta not in MAP_DELTAS:
        errors.append(
            f"canonical record {identity}: map_delta must be one of "
            f"{', '.join(sorted(MAP_DELTAS))}"
        )

    provenance = record.get("time_provenance")
    if provenance == "legacy_unknown":
        if direction_keys_present:
            errors.append(
                f"canonical record {identity}: direction_keys is native-v2 support "
                "metadata and is forbidden on explicit legacy records"
            )
        published = record.get("published")
        published_at = record.get("published_at")
        if not _honest_published_value(published):
            errors.append(
                f"canonical record {identity}: explicit legacy published must retain "
                "honest YYYY-MM or YYYY-MM-DD precision"
            )
        if published_at != published:
            errors.append(
                f"canonical record {identity}: explicit legacy published_at must equal "
                "published precision exactly"
            )
        if record.get("first_seen_at") is not None:
            errors.append(
                f"canonical record {identity}: legacy_unknown requires first_seen_at=null; "
                "do not fabricate discovery time"
            )
        if record.get("radar_published_at") is not None:
            errors.append(
                f"canonical record {identity}: legacy_unknown requires radar_published_at=null; "
                "do not fabricate Radar acceptance time"
            )
        return errors

    if provenance != "native_v2":
        errors.append(
            f"canonical record {identity}: complete v2 time fields require "
            "time_provenance=native_v2 or legacy_unknown"
        )
        return errors

    parsed: dict[str, datetime] = {}
    for field in ("published_at", "first_seen_at", "radar_published_at"):
        value = _strict_utc(record.get(field))
        if value is None:
            errors.append(
                f"canonical record {identity}: native_v2 {field} must be a strict UTC "
                "timestamp YYYY-MM-DDTHH:MM:SSZ"
            )
        else:
            parsed[field] = value
    if len(parsed) == 3 and not (
        parsed["published_at"]
        <= parsed["first_seen_at"]
        <= parsed["radar_published_at"]
    ):
        errors.append(
            f"canonical record {identity}: native_v2 requires "
            "published_at <= first_seen_at <= radar_published_at"
        )
    radar_time = parsed.get("radar_published_at")
    if radar_time is not None and radar_time < V2_CUTOVER:
        errors.append(
            f"canonical record {identity}: native_v2 radar_published_at cannot predate "
            f"the {V2_CUTOVER.strftime('%Y-%m-%dT%H:%M:%SZ')} cutover"
        )
    return errors


def validate_memory_registry(records: list[dict[str, object]]) -> list[str]:
    """Validate registry-wide time semantics and the bounded legacy migration."""

    errors: list[str] = []
    record_by_id: dict[str, dict[str, object]] = {}
    for record in records:
        identity = str(record.get("id", "<missing-id>"))
        if identity in record_by_id:
            errors.append(f"canonical registry contains duplicate id {identity}")
        record_by_id[identity] = record
        errors.extend(validate_record_time_contract(record))

    compatibility = set(LEGACY_TIMELINE_COMPATIBILITY_IDS)
    for identity in LEGACY_TIMELINE_COMPATIBILITY_IDS:
        record = record_by_id.get(identity)
        if record is None:
            errors.append(
                f"canonical registry is missing explicit legacy compatibility id {identity}"
            )
            continue
        if record.get("time_provenance") != "legacy_unknown":
            errors.append(
                f"canonical record {identity}: Timeline compatibility migration requires "
                "time_provenance=legacy_unknown"
            )
        if record.get("map_delta") != "early_signal":
            errors.append(
                f"canonical record {identity}: Timeline compatibility migration requires "
                "map_delta=early_signal"
            )

    for identity, record in record_by_id.items():
        if (
            identity not in compatibility
            and record.get("time_provenance") == "legacy_unknown"
        ):
            errors.append(
                f"canonical record {identity}: explicit legacy migration is outside the "
                "fixed Timeline compatibility set"
            )
    return errors


def _strict_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or STRICT_UTC_RE.fullmatch(value) is None:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        return None


def _honest_published_value(value: object) -> bool:
    if not isinstance(value, str) or PUBLISHED_RE.fullmatch(value) is None:
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d" if len(value) == 10 else "%Y-%m")
    except ValueError:
        return False
    return True


def _canonical_direction_keys(value: object) -> tuple[str, ...] | None:
    if not isinstance(value, list) or not value:
        return None
    if any(
        not isinstance(key, str) or STABLE_TOKEN_RE.fullmatch(key) is None
        for key in value
    ):
        return None
    keys = tuple(value)
    if len(keys) != len(set(keys)):
        return None
    return keys


def _section(text: str, anchor: str, next_anchor: str) -> str | None:
    start_marker = f'<a id="{anchor}"></a>'
    end_marker = f'<a id="{next_anchor}"></a>'
    start = text.find(start_marker)
    end = text.find(end_marker, start + len(start_marker)) if start >= 0 else -1
    if start < 0 or end <= start:
        return None
    return text[start:end]


def _period_window(section: str) -> tuple[date, date] | None:
    matches = list(PERIOD_RANGE_RE.finditer(strip_html_comments(section)))
    if len(matches) != 1:
        return None
    match = matches[0]
    try:
        return date.fromisoformat(match.group("start")), date.fromisoformat(
            match.group("end")
        )
    except ValueError:
        return None


def _record_anchor(identity: str) -> str:
    return identity.replace(".", "-")


def _timeline_chunks(text: str) -> tuple[list[str], dict[str, str]]:
    section = _section(text, "timeline", "periods")
    if section is None:
        return [], {}
    matches = list(ENTRY_ANCHOR_RE.finditer(section))
    identities = [match.group(1) for match in matches]
    chunks: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        chunks.setdefault(match.group(1), section[match.end() : end])
    return identities, chunks


def _expected_timeline_anchors(
    records: list[dict[str, object]],
    window: tuple[date, date],
    synthesis_cutoff: datetime,
) -> list[str]:
    start, end = window
    native: list[tuple[datetime, str]] = []
    for record in records:
        if record.get("time_provenance") != "native_v2":
            continue
        radar_time = _strict_utc(record.get("radar_published_at"))
        if (
            radar_time is not None
            and start <= radar_time.date() <= end
            and radar_time <= synthesis_cutoff
        ):
            native.append((radar_time, str(record.get("id"))))
    native.sort(key=lambda item: (-item[0].timestamp(), item[1]))
    return [_record_anchor(identity) for _, identity in native] + [
        _record_anchor(identity) for identity in LEGACY_TIMELINE_COMPATIBILITY_IDS
    ]


def _entry_link_targets(chunk: str) -> list[str]:
    visible_chunk = strip_html_comments(chunk)
    links_field = VISIBLE_LINKS_FIELD_RE.search(visible_chunk)
    if links_field is None:
        return []
    return [
        raw.strip().strip("<>")
        for raw in LINK_RE.findall(links_field.group("links"))
    ]


def _validate_timeline_language(
    language: str,
    text: str,
    records: list[dict[str, object]],
    expected: list[str],
    synthesis_cutoff: datetime,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    record_by_anchor: dict[str, dict[str, object]] = {}
    for record in records:
        anchor = _record_anchor(str(record.get("id")))
        if anchor in record_by_anchor:
            errors.append(
                f"{language}: canonical identities collide at Timeline anchor {anchor}"
            )
        record_by_anchor[anchor] = record

    identities, chunks = _timeline_chunks(text)
    if not identities:
        errors.append(f"{language}: cannot locate a populated Timeline section")
        return identities, errors

    seen: set[str] = set()
    for identity in identities:
        if identity in seen:
            errors.append(f"{language}: duplicate Timeline identity {identity}")
        seen.add(identity)
    for identity in expected:
        if identity not in identities:
            errors.append(f"{language}: canonical identity {identity} is missing from Timeline")
    for identity in identities:
        if identity not in expected:
            record = record_by_anchor.get(identity)
            radar_time = (
                _strict_utc(record.get("radar_published_at"))
                if record is not None and record.get("time_provenance") == "native_v2"
                else None
            )
            if radar_time is not None and radar_time > synthesis_cutoff:
                errors.append(
                    f"{language}: Timeline identity {identity} is after public synthesis "
                    f"cutoff {synthesis_cutoff.strftime('%Y-%m-%dT%H:%M:%SZ')}"
                )
            else:
                errors.append(f"{language}: unexpected Timeline identity {identity}")
    if identities != expected:
        errors.append(
            f"{language}: Timeline violates full Radar timestamp order or fixed legacy order"
        )

    for identity in identities:
        record = record_by_anchor.get(identity)
        if record is None:
            continue
        chunk = chunks.get(identity, "")
        visible_chunk = strip_html_comments(chunk)
        canonical_identity = str(record.get("id"))
        summary = SUMMARY_IDENTITY_RE.search(visible_chunk)
        if summary is None:
            errors.append(f"{language}: Timeline identity {identity} has no parseable summary")
        else:
            if record.get("time_provenance") == "native_v2":
                radar_time = _strict_utc(record.get("radar_published_at"))
                expected_date = radar_time.date().isoformat() if radar_time else None
            else:
                expected_date = record.get("published_at")
            if summary.group("date") != expected_date:
                errors.append(
                    f"{language}: Timeline identity {identity} displayed date does not match "
                    "its canonical time basis"
                )

        map_match = VISIBLE_MAP_RE.search(visible_chunk)
        visible_map = map_match.group(1).lower() if map_match else None
        if visible_map != record.get("map_delta"):
            errors.append(
                f"{language}: Timeline identity {identity} visible map token does not match "
                "canonical map_delta"
            )

        targets = _entry_link_targets(visible_chunk)
        primary = record.get("paper_url")
        if not isinstance(primary, str) or targets.count(primary) != 1:
            errors.append(
                f"{language}: Timeline identity {identity} must link its canonical primary "
                "paper exactly once"
            )

        published = record.get("published_at", record.get("published"))
        year = str(published)[:4]
        expected_english = f"papers/{year}/{canonical_identity}.md"
        expected_chinese = f"papers/{year}/{canonical_identity}.zh.md"
        if targets.count(expected_english) != 1 or targets.count(expected_chinese) != 1:
            errors.append(
                f"{language}: Timeline identity {identity} needs exactly one corresponding "
                "Chinese and English deep-note link"
            )
        for target in targets:
            note = DEEP_NOTE_TARGET_RE.fullmatch(target)
            if note is not None and note.group("identity") != canonical_identity:
                errors.append(
                    f"{language}: Timeline identity {identity} has a deep-note link for "
                    f"canonical identity {note.group('identity')}"
                )
    return identities, errors


def _stable_token_is_visible(token: str, visible: str) -> bool:
    phrase = re.sub(r"[-_.]+", " ", token.lower()).strip()
    normalized = re.sub(r"\s+", " ", visible.lower())
    if not phrase:
        return False
    pattern = r"(?<![a-z0-9])" + r"\s+".join(
        re.escape(part) for part in phrase.split()
    ) + r"(?![a-z0-9])"
    return re.search(pattern, normalized) is not None


def _normalized_stable_phrase(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[-_.]+", " ", value.lower())).strip()


def _direction_item_blocks(section: str) -> list[tuple[int, str]]:
    """Return complete visible direction blocks bounded by the next direction."""

    lines = section.splitlines()
    starts: list[int] = []
    for index, line in enumerate(lines):
        visible_line = strip_html_comments(line)
        if DIRECTION_HEADING_RE.search(visible_line) is not None:
            starts.append(index)
    return [
        (
            start + 1,
            "\n".join(
                lines[
                    start : starts[index + 1]
                    if index + 1 < len(starts)
                    else len(lines)
                ]
            ),
        )
        for index, start in enumerate(starts)
    ]


def _parse_direction_items(
    language: str,
    anchor: str,
    section: str,
    window: tuple[date, date],
    records: list[dict[str, object]],
    errors: list[str],
) -> list[tuple[str, str, tuple[str, ...], str, str, str, str, str]]:
    record_by_id = {str(record.get("id")): record for record in records}
    record_by_anchor = {
        _record_anchor(str(record.get("id"))): str(record.get("id"))
        for record in records
    }
    items: list[tuple[str, str, tuple[str, ...], str, str, str, str, str]] = []
    seen_keys: set[str] = set()
    label_patterns = VISIBLE_DIRECTION_LABELS[language]
    value_patterns = VISIBLE_DIRECTION_VALUES[language]
    for line_number, raw_block in _direction_item_blocks(section):
        location = f"{language}: {anchor} direction at line {line_number}"
        visible_block = strip_html_comments(raw_block)
        label_matches = {
            name: list(pattern.finditer(visible_block))
            for name, pattern in label_patterns.items()
        }
        visible_values: dict[str, str] = {}
        for name, matches in label_matches.items():
            if len(matches) != 1:
                errors.append(f"{location} requires exactly one visible {name} field")
                continue
            value_match = value_patterns[name].match(visible_block, matches[0].start())
            if value_match is None or not value_match.group("value").strip():
                errors.append(
                    f"{location} requires exactly one visible {name} field with valid structure"
                )
                continue
            visible_values[name] = value_match.group("value").strip()

        comments = list(DIRECTION_COMMENT_RE.finditer(raw_block))
        if len(comments) != 1:
            errors.append(f"{location} requires exactly one stable direction metadata block")
            continue

        attributes: dict[str, list[str]] = {name: [] for name in DIRECTION_ATTRIBUTES}
        for match in DIRECTION_ATTRIBUTE_RE.finditer(comments[0].group("attributes")):
            name = match.group("name").lower()
            if name in attributes:
                attributes[name].append(match.group("value"))
        complete = True
        for name, values in attributes.items():
            if len(values) != 1 or not values[0]:
                errors.append(f"{location} requires exactly one non-empty {name} value")
                complete = False
        if not complete:
            continue

        values = {name: found[0] for name, found in attributes.items()}
        key = values["key"]
        state = values["state"]
        timing = values["timing"]
        synthesized = values["synthesized"]
        synthesized_time = _strict_utc(synthesized)
        prior = values["prior"]
        for name in ("key", "confidence", "implication", "prior"):
            if STABLE_TOKEN_RE.fullmatch(values[name]) is None:
                errors.append(
                    f"{location} {name} must be a lowercase stable token, not free-form prose"
                )

        support_value = values["supports"]
        supports = (
            ()
            if support_value == "none"
            else tuple(part.strip() for part in support_value.split(",") if part.strip())
        )
        if state not in DIRECTION_STATES:
            errors.append(f"{location} has invalid direction state {state}")
        visible_state = visible_values.get("state")
        if visible_state is None or visible_state.lower() != state:
            errors.append(f"{location} visible state and stable direction state drift")
        visible_heading = DIRECTION_HEADING_RE.search(visible_block)
        if (
            visible_heading is None
            or visible_heading.group("state").lower() != state
            or not _stable_token_is_visible(key, visible_heading.group("heading"))
        ):
            errors.append(f"{location} direction key lacks a bounded heading witness")
        if values["confidence"] not in CONFIDENCE_VALUES:
            errors.append(f"{location} confidence must be low, medium, or high")
        visible_confidence = visible_values.get("confidence")
        if (
            visible_confidence is None
            or visible_confidence.lower() != values["confidence"]
        ):
            errors.append(f"{location} visible confidence and stable metadata drift")
        if timing != "radar_published_at":
            errors.append(f"{location} timing basis must be radar_published_at")
        visible_timing = visible_values.get("timing basis")
        if visible_timing != timing:
            errors.append(f"{location} visible timing basis and stable metadata drift")
        if synthesized_time is None or synthesized != SYNTHESIS_TIMESTAMP:
            errors.append(
                f"{location} synthesized must be the exact UTC synthesis timestamp "
                f"{SYNTHESIS_TIMESTAMP}"
            )
        visible_synthesis = visible_values.get("synthesis")
        if visible_synthesis != synthesized:
            errors.append(f"{location} exact visible synthesis timestamp drift")
        visible_implication = visible_values.get("implication")
        if (
            visible_implication is None
            or _normalized_stable_phrase(visible_implication)
            != _normalized_stable_phrase(values["implication"])
        ):
            errors.append(f"{location} implication lacks its labeled visible witness")

        if len(supports) != len(set(supports)):
            errors.append(f"{location} contains duplicate support identities")
        visible_support_field = visible_values.get("supports")
        visible_support_anchors = (
            tuple(PERIOD_SUPPORT_RE.findall(visible_support_field))
            if visible_support_field is not None
            else ()
        )
        visible_supports: list[str] = []
        for visible_anchor in visible_support_anchors:
            canonical = record_by_anchor.get(visible_anchor)
            if canonical is None:
                errors.append(
                    f"{location} visible support anchor {visible_anchor} has no canonical record"
                )
                visible_supports.append(f"<unknown:{visible_anchor}>")
            else:
                visible_supports.append(canonical)
        if tuple(visible_supports) != supports:
            errors.append(f"{location} visible support order and stable metadata drift")
        if not supports and visible_support_field != "**none**":
            errors.append(f"{location} zero support must be exactly **none**")
        if supports and visible_support_field is not None:
            remainder = PERIOD_SUPPORT_RE.sub("", visible_support_field)
            if re.sub(r"[\s·]+", "", remainder):
                errors.append(
                    f"{location} visible support field must contain only canonical support links"
                )
        if key in seen_keys:
            errors.append(f"{location} repeats stable direction key {key}")
        seen_keys.add(key)

        for identity in supports:
            record = record_by_id.get(identity)
            if record is None:
                errors.append(f"{location} support identity {identity} has no canonical record")
                continue
            if record.get("time_provenance") != "native_v2":
                errors.append(
                    f"{location} support identity {identity} must be a native_v2 Radar "
                    "acceptance; legacy context is not support"
                )
                continue
            direction_keys = _canonical_direction_keys(record.get("direction_keys"))
            if direction_keys is None or key not in direction_keys:
                errors.append(
                    f"{location} support identity {identity} direction_keys must include "
                    f"{key}"
                )
            radar_time = _strict_utc(record.get("radar_published_at"))
            if radar_time is None:
                errors.append(
                    f"{location} support identity {identity} has no valid radar_published_at"
                )
                continue
            if not window[0] <= radar_time.date() <= window[1]:
                errors.append(
                    f"{location} support identity {identity} falls outside "
                    f"{window[0].isoformat()}—{window[1].isoformat()} by radar_published_at"
                )
            if synthesized_time is not None and radar_time > synthesized_time:
                errors.append(
                    f"{location} support identity {identity} is accepted after direction "
                    f"synthesized={synthesized}"
                )

        if len(set(supports)) == 1 and TREND_CLAIM_RE.search(visible_block) is not None:
            errors.append(
                f"{location} one-paper direction cannot make a trend/趋势 claim"
            )

        if state == "no_material_change":
            if supports:
                errors.append(f"{location} no_material_change requires zero canonical support")
            if prior != "none":
                errors.append(f"{location} no_material_change requires prior=none")
        if state == "new_signal":
            if len(set(supports)) != 1:
                errors.append(f"{location} labeled new_signal requires exactly one support identity")
            elif record_by_id.get(supports[0], {}).get("map_delta") != "early_signal":
                errors.append(
                    f"{location} labeled new_signal requires its one record to have "
                    "map_delta=early_signal"
                )
            if prior != "none":
                errors.append(f"{location} new_signal requires prior=none")
        if state == "reinforced" and len(set(supports)) < 2:
            errors.append(
                f"{location} labeled reinforced requires at least two distinct support identities"
            )
        if state in {"revised", "splits", "retires"} and not supports:
            errors.append(f"{location} labeled {state} requires canonical support")
        if state in {"splits", "retires"} and supports:
            has_matching_map_evidence = any(
                record_by_id.get(identity, {}).get("time_provenance") == "native_v2"
                and record_by_id.get(identity, {}).get("map_delta") == state
                for identity in supports
            )
            if not has_matching_map_evidence:
                errors.append(
                    f"{location} labeled {state} requires at least one native support "
                    f"with map_delta={state}"
                )

        visible_prior = visible_values.get("prior")
        if visible_prior == "`none`":
            visible_prior_token = "none"
        elif (
            visible_prior is not None
            and VISIBLE_PRIOR_MAP_VALUE_RE.fullmatch(visible_prior) is not None
        ):
            visible_prior_token = "field-map"
        else:
            visible_prior_token = None
        if visible_prior_token != prior:
            errors.append(f"{location} visible prior-map evidence and metadata drift")
        if state in {"reinforced", "revised", "splits", "retires"}:
            if prior != "field-map" or visible_prior_token != "field-map":
                errors.append(
                    f"{location} durable direction requires independent prior Field Map "
                    "evidence via prior=field-map and a visible #field-map link"
                )

        items.append(
            (
                key,
                state,
                supports,
                values["confidence"],
                values["implication"],
                timing,
                synthesized,
                prior,
            )
        )
    if not items:
        errors.append(f"{language}: {anchor} has no parseable direction metadata")
    return items


def validate_memory_projection(
    zh: str,
    en: str,
    records: list[dict[str, object]],
) -> list[str]:
    """Validate Memory-only canonical Timeline and rolling-period projections."""

    errors: list[str] = []
    observed_windows: dict[str, dict[str, tuple[date, date]]] = {}
    directions: dict[
        str,
        dict[
            str,
            list[tuple[str, str, tuple[str, ...], str, str, str, str, str]],
        ],
    ] = {}

    for language, text in (("README.md", zh), ("README.en.md", en)):
        language_windows: dict[str, tuple[date, date]] = {}
        language_directions: dict[
            str, list[tuple[str, str, tuple[str, ...], str, str, str, str, str]]
        ] = {}
        for anchor, next_anchor in (
            ("last-7-days", "last-30-days"),
            ("last-30-days", "field-map"),
        ):
            section = _section(text, anchor, next_anchor)
            if section is None:
                errors.append(f"{language}: cannot locate {anchor} period section")
                continue
            window = _period_window(section)
            if window is None:
                errors.append(
                    f"{language}: {anchor} must contain exactly one visible date range "
                    "with valid inclusive dates"
                )
            else:
                language_windows[anchor] = window
                expected_window = EXPECTED_PERIOD_WINDOWS[anchor]
                if window != expected_window:
                    errors.append(
                        f"{language}: {anchor} must use current expected window "
                        f"{expected_window[0].isoformat()}—{expected_window[1].isoformat()}"
                    )
            language_directions[anchor] = _parse_direction_items(
                language,
                anchor,
                section,
                EXPECTED_PERIOD_WINDOWS[anchor],
                records,
                errors,
            )
        observed_windows[language] = language_windows
        directions[language] = language_directions

    for anchor in ("last-7-days", "last-30-days"):
        zh_window = observed_windows.get("README.md", {}).get(anchor)
        en_window = observed_windows.get("README.en.md", {}).get(anchor)
        if zh_window is not None and en_window is not None and zh_window != en_window:
            errors.append(f"Chinese/English {anchor} window drift")

    synthesis_cutoff = _strict_utc(SYNTHESIS_TIMESTAMP)
    if synthesis_cutoff is None:
        errors.append("Memory projection has an invalid public synthesis cutoff")
        return errors
    expected = _expected_timeline_anchors(
        records, EXPECTED_PERIOD_WINDOWS["last-30-days"], synthesis_cutoff
    )
    actual: dict[str, list[str]] = {}
    for language, text in (("README.md", zh), ("README.en.md", en)):
        identities, language_errors = _validate_timeline_language(
            language, text, records, expected, synthesis_cutoff
        )
        actual[language] = identities
        errors.extend(language_errors)
    if actual.get("README.md") != actual.get("README.en.md"):
        errors.append("Chinese/English Timeline identity or order drift")

    for anchor in ("last-7-days", "last-30-days"):
        if directions.get("README.md", {}).get(anchor) != directions.get(
            "README.en.md", {}
        ).get(anchor):
            errors.append(f"Chinese/English {anchor} direction parity drift")
    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for p in [ZH, EN, LIB_ZH, LIB_EN, ROOT / "docs" / "RADAR_AGENT_PROTOCOL.md", ROOT / "docs" / "EDITORIAL_STANDARD.md", ROOT / "docs" / "DAILY_WORKFLOW.md"]:
        if not p.exists():
            fail(errors, f"missing reader contract: {p.relative_to(ROOT)}")

    if errors:
        for e in errors:
            print("ERROR", e)
        return 1

    errors.extend(validate_no_public_run_files(PUBLIC_OPERATIONAL_RUN_PATHS))

    records: list[dict[str, object]] = []
    for path in sorted(RECORDS.glob("*.json")):
        try:
            records.append(json.loads(path.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"{path.relative_to(ROOT)}: invalid canonical JSON: {exc}")
    errors.extend(validate_memory_registry(records))

    zh = ZH.read_text(encoding="utf-8")
    en = EN.read_text(encoding="utf-8")

    if "README.en.md" not in zh or "README.md" not in en:
        fail(errors, "README language switch is incomplete")

    errors.extend(validate_pair(zh, en))
    errors.extend(validate_memory_aliases(zh, en))
    errors.extend(validate_memory_note_links(zh, en))
    errors.extend(validate_memory_projection(zh, en, records))

    for name, text in [("README.md", zh), ("README.en.md", en)]:
        family_routes(text, name, errors)

    forbidden = ["scheduler prompt", "upload blocker", "renderer failure", "backfill queue"]
    for name, text in [("README.md", zh), ("README.en.md", en)]:
        lower = text.lower()
        for phrase in forbidden:
            if phrase in lower:
                fail(errors, f"{name}: maintenance internals leaked: {phrase}")

    repeated_patterns = [
        r"真正重要的不是",
        r"关键不在于.*而在于",
        r"值得注意的是",
        r"the important (?:thing|delta) is not",
        r"this matters because",
    ]
    combined = zh + "\n" + en
    for pat in repeated_patterns:
        n = len(re.findall(pat, combined, flags=re.IGNORECASE))
        if n >= 3:
            warnings.append(f"repeated editorial skeleton {pat!r}: {n} occurrences")

    for p in [ZH, EN, LIB_ZH, LIB_EN]:
        local_links(p, errors)

    for w in warnings:
        print("WARN", w)
    if errors:
        for e in errors:
            print("ERROR", e)
        print(f"Reading-surface validation failed with {len(errors)} error(s).")
        return 1

    print("Validated Chinese-first bilingual progressive reading surfaces.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
