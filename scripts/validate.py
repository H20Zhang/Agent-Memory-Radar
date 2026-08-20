#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import jsonschema
import yaml

from validate_reading import validate_memory_registry

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "data" / "paper.schema.json"
PAPERS_DIR = ROOT / "data" / "papers"
README = ROOT / "README.md"

README_SECTIONS = [
    "## Latest Timeline",
    "## 7 天 / 30 天",
    "## 领域地图",
    "## 阅读路径",
    "## Research Library",
    "## 如何使用",
    "## Scope / About / Contributing",
]

LATEST_NOTE_HEADINGS = [
    "## Problem",
    "## Mechanism",
    "## Compared with",
    "## Decisive evidence",
    "## Main caveat",
    "## Memory lifecycle",
    "## Why it matters",
    "## Related reading",
]

CATEGORY_PAGES = {
    "representation_organization": "categories/representation-organization.md",
    "retrieval_access": "categories/retrieval-access.md",
    "write_update_consolidation": "categories/write-update-consolidation.md",
    "memory_learning_evolution": "categories/memory-learning-evolution.md",
    "evaluation_analysis": "categories/evaluation-analysis.md",
}

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
ENTRY_ANCHOR_RE = re.compile(r'<a id="entry-([^"\n]+)"></a>')
TIMELINE_NOTE_RE = re.compile(
    r"\[[^\]]+\]\((papers/\d{4}/[\d.]+\.md)\)"
)


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def check_repo_relative_links(errors: list[str]) -> None:
    roots = [
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "LICENSE.md",
        ROOT / "CURATION.md",
        ROOT / "COMPACTION.md",
        ROOT / "VISUAL_POLICY.md",
        ROOT / "assets" / "README.md",
        ROOT / "papers" / "anchors.md",
        ROOT / "digests" / "README.md",
        ROOT / "categories" / "README.md",
    ]
    roots.extend(sorted((ROOT / "docs").glob("**/*.md")) if (ROOT / "docs").exists() else [])
    roots.extend(sorted((ROOT / "categories").glob("*.md")) if (ROOT / "categories").exists() else [])
    roots.extend(sorted((ROOT / "digests").glob("**/*.md")) if (ROOT / "digests").exists() else [])
    roots.extend(sorted((ROOT / "papers").glob("**/*.md")) if (ROOT / "papers").exists() else [])

    seen: set[Path] = set()
    for doc in roots:
        if doc in seen or not doc.exists():
            continue
        seen.add(doc)
        text = doc.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith("#"):
                continue
            parsed = urlsplit(target)
            if parsed.scheme in {"http", "https", "mailto"} or parsed.netloc:
                continue
            rel = unquote(parsed.path)
            if not rel:
                continue
            resolved = (doc.parent / rel).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                error(errors, f"{doc.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                error(errors, f"{doc.relative_to(ROOT)}: broken relative link: {target}")


def validate_latest_note_style(errors: list[str], timeline: str) -> None:
    note_paths = TIMELINE_NOTE_RE.findall(timeline)
    for relative in note_paths:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "> **Research delta.**" not in text:
            error(errors, f"{relative}: latest paper note is missing one-line Research delta")
        if "[← Latest Papers]" not in text or "[Research Map]" not in text:
            error(errors, f"{relative}: latest paper note needs compact return navigation")
        for heading in LATEST_NOTE_HEADINGS:
            if heading not in text:
                error(errors, f"{relative}: missing researcher-facing section {heading!r}")
        if "AI confidence" in text:
            error(errors, f"{relative}: use neutral 'Confidence' rather than 'AI confidence'")
        if "## Visual status" in text:
            error(errors, f"{relative}: maintenance-only visual status should not be on the researcher-facing note")


def validate_readme(errors: list[str]) -> None:
    if not README.exists():
        error(errors, "README.md is missing")
        return

    text = README.read_text(encoding="utf-8")
    positions: list[int] = []
    for heading in README_SECTIONS:
        pos = text.find(heading)
        if pos < 0:
            error(errors, f"README.md: missing required section {heading!r}")
        positions.append(pos)

    valid_positions = [p for p in positions if p >= 0]
    if len(valid_positions) == len(positions) and valid_positions != sorted(valid_positions):
        error(errors, "README.md: reader-facing sections are out of canonical order")

    timeline_start = text.find('<a id="timeline"></a>')
    timeline_end = text.find('<a id="periods"></a>')
    if 0 <= timeline_start < timeline_end:
        timeline = text[timeline_start:timeline_end]
        identities = ENTRY_ANCHOR_RE.findall(timeline)
        if not identities:
            error(errors, "README.md: Timeline must contain at least one entry disclosure")
        details_count = len(re.findall(r"<details(?:\s|>)", timeline, flags=re.IGNORECASE))
        if details_count != len(identities):
            error(
                errors,
                "README.md: every Timeline identity must have exactly one details disclosure",
            )
        if "**AI take:**" in timeline:
            error(errors, "README.md: use 'Research take' rather than 'AI take' on the public research surface")
        validate_latest_note_style(errors, timeline)
    else:
        error(errors, "README.md: Timeline must precede the periods section")

    field_start = text.find('<a id="field-map"></a>')
    field_end = text.find('<a id="reading-paths"></a>')
    if 0 <= field_start < field_end:
        field_map = text[field_start:field_end]
        boundary_count = len(
            re.findall(r"^\| \*\*[^|]+\*\* \|", field_map, flags=re.MULTILINE)
        )
        if boundary_count < 5:
            error(errors, "README.md: Field Map must retain the lifecycle boundary map")
    else:
        error(errors, "README.md: Field Map must precede Reading Paths")

    if "dashboard" in text.lower() and "not a dashboard" not in text.lower():
        error(errors, "README.md: public surface should not present itself as a dashboard")


def validate_category_style(errors: list[str]) -> None:
    for relative in CATEGORY_PAGES.values():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "| AI take |" in text:
            error(errors, f"{relative}: use 'Research take' rather than 'AI take'")
        if "**Biggest unresolved question:**" not in text:
            error(errors, f"{relative}: missing biggest unresolved question")
        if "**Next decisive evidence:**" not in text:
            error(errors, f"{relative}: missing next decisive evidence")


def main() -> int:
    errors: list[str] = []

    required_files = [
        ROOT / "CONTRIBUTING.md",
        ROOT / "CITATION.cff",
        ROOT / "LICENSE.md",
        ROOT / "LICENSE-CONTENT.md",
        ROOT / "LICENSE-CODE",
        ROOT / "COMPACTION.md",
        ROOT / "docs" / "MAINTENANCE.md",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "suggest-paper.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "correction.yml",
    ]
    for path in required_files:
        if not path.exists():
            error(errors, f"missing repository contract: {path.relative_to(ROOT)}")

    legacy_visual_workflow = ROOT / ".github" / "workflows" / "assemble-visuals.yml"
    if legacy_visual_workflow.exists():
        error(errors, "legacy paper-ID-specific assemble-visuals workflow should be removed")

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    taxonomy = yaml.safe_load((ROOT / "taxonomy.yaml").read_text(encoding="utf-8"))
    valid_categories = {item["id"] for item in taxonomy["primary_categories"]}
    valid_tags = {
        value
        for values in taxonomy.get("tag_axes", {}).values()
        for value in values
    }

    seen_ids: set[str] = set()
    records: list[dict[str, object]] = []
    paths = sorted(PAPERS_DIR.glob("*.json")) if PAPERS_DIR.exists() else []

    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            error(errors, f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        records.append(record)

        record_errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
        for exc in record_errors:
            where = ".".join(str(part) for part in exc.path) or "<root>"
            error(errors, f"{path.relative_to(ROOT)}:{where}: {exc.message}")
        if record_errors:
            continue

        record_id = record["id"]
        if record_id in seen_ids:
            error(errors, f"{path.relative_to(ROOT)}: duplicate id {record_id}")
        seen_ids.add(record_id)

        if path.stem != record_id:
            error(errors, f"{path.relative_to(ROOT)}: filename does not match id={record_id}")

        category = record["primary_category"]
        if category not in valid_categories:
            error(errors, f"{path.relative_to(ROOT)}: unknown primary_category={category}")
        elif not (ROOT / CATEGORY_PAGES[category]).exists():
            error(errors, f"{path.relative_to(ROOT)}: missing category page {CATEGORY_PAGES[category]}")

        unknown_tags = sorted(set(record["tags"]) - valid_tags)
        if unknown_tags:
            error(errors, f"{path.relative_to(ROOT)}: unknown taxonomy tags {unknown_tags}")

        year = str(record["published"])[:4]
        note = ROOT / "papers" / year / f"{record_id}.md"
        if not note.exists():
            error(errors, f"{path.relative_to(ROOT)}: missing researcher note papers/{year}/{record_id}.md")
            note_text = ""
        else:
            note_text = note.read_text(encoding="utf-8")

        visual = record["visual_explainer"]
        status = visual["status"]
        blocker = visual.get("blocker")
        importance = record["importance"]

        if importance >= 4 and status != "generated" and not (isinstance(blocker, str) and blocker.strip()):
            error(errors, f"{path.relative_to(ROOT)}: importance>=4 requires generated visual or documented blocker")

        if status == "generated":
            visual_path = visual.get("path")
            if not isinstance(visual_path, str) or not visual_path.strip():
                error(errors, f"{path.relative_to(ROOT)}: generated visual has null/empty path")
            else:
                asset = ROOT / visual_path
                if asset.suffix.lower() != ".webp":
                    error(errors, f"{path.relative_to(ROOT)}: generated visual must be WebP: {visual_path}")
                if not asset.exists():
                    error(errors, f"{path.relative_to(ROOT)}: generated visual asset missing: {visual_path}")
                if note_text and asset.name not in note_text:
                    error(errors, f"{path.relative_to(ROOT)}: paper note does not embed generated visual {asset.name}")

    for item in validate_memory_registry(records):
        error(errors, item)

    validate_readme(errors)
    validate_category_style(errors)
    check_repo_relative_links(errors)

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for item in errors:
            print(f"ERROR {item}")
        return 1

    print(f"Validated {len(paths)} canonical paper records and reader-facing repository contracts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
