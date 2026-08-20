#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import yaml

from validate_reading import validate_memory_registry

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "data" / "paper.schema.json"
RECORDS = ROOT / "data" / "papers"

CATEGORY_PAGES = {
    "representation_organization": "categories/representation-organization.md",
    "retrieval_access": "categories/retrieval-access.md",
    "write_update_consolidation": "categories/write-update-consolidation.md",
    "memory_learning_evolution": "categories/memory-learning-evolution.md",
    "evaluation_analysis": "categories/evaluation-analysis.md",
}


def main() -> int:
    errors: list[str] = []
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    taxonomy = yaml.safe_load((ROOT / "taxonomy.yaml").read_text(encoding="utf-8"))
    valid_categories = {x["id"] for x in taxonomy["primary_categories"]}
    valid_tags = {v for values in taxonomy.get("tag_axes", {}).values() for v in values}

    seen: set[str] = set()
    records: list[dict[str, object]] = []
    paths = sorted(RECORDS.glob("*.json"))
    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        records.append(record)

        for exc in sorted(validator.iter_errors(record), key=lambda e: list(e.path)):
            where = ".".join(str(x) for x in exc.path) or "<root>"
            errors.append(f"{path.relative_to(ROOT)}:{where}: {exc.message}")

        rid = record.get("id")
        if not isinstance(rid, str):
            continue
        if rid in seen: errors.append(f"duplicate id: {rid}")
        seen.add(rid)
        if path.stem != rid: errors.append(f"{path.relative_to(ROOT)}: filename/id mismatch")

        category = record.get("primary_category")
        if category not in valid_categories:
            errors.append(f"{rid}: unknown primary_category={category}")
        elif not (ROOT / CATEGORY_PAGES[str(category)]).exists():
            errors.append(f"{rid}: missing category page")

        tags = record.get("tags", [])
        unknown = sorted(set(tags) - valid_tags) if isinstance(tags, list) else []
        if unknown: errors.append(f"{rid}: unknown taxonomy tags {unknown}")

        year = str(record.get("published", ""))[:4]
        note = ROOT / "papers" / year / f"{rid}.md"
        if not note.exists():
            errors.append(f"{rid}: missing paper note {note.relative_to(ROOT)}")
            note_text = ""
        else:
            note_text = note.read_text(encoding="utf-8")

        visual = record.get("visual_explainer")
        if isinstance(visual, dict):
            status = visual.get("status")
            blocker = visual.get("blocker")
            importance = record.get("importance", 0)
            if isinstance(importance, (int, float)) and importance >= 4 and status != "generated":
                if not isinstance(blocker, str) or not blocker.strip():
                    errors.append(f"{rid}: importance>=4 needs generated visual or blocker")
            if status == "generated":
                rel = visual.get("path")
                if not isinstance(rel, str) or not rel:
                    errors.append(f"{rid}: generated visual missing path")
                else:
                    asset = ROOT / rel
                    if asset.suffix.lower() != ".webp": errors.append(f"{rid}: final visual must be WebP")
                    if not asset.exists(): errors.append(f"{rid}: missing visual asset {rel}")
                    if note_text and asset.name not in note_text: errors.append(f"{rid}: paper note does not embed {asset.name}")

    errors.extend(validate_memory_registry(records))

    if errors:
        for e in errors: print("ERROR", e)
        print(f"Canonical validation failed with {len(errors)} error(s).")
        return 1
    print(f"Validated {len(paths)} canonical Agent Memory records.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
