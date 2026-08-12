import json
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "data" / "paper.schema.json").read_text())
TAXONOMY = yaml.safe_load((ROOT / "taxonomy.yaml").read_text())
VALID_CATEGORIES = {x["id"] for x in TAXONOMY["primary_categories"]}

errors = []
for path in sorted((ROOT / "data" / "papers").glob("*.json")) if (ROOT / "data" / "papers").exists() else []:
    record = json.loads(path.read_text())
    try:
        jsonschema.validate(record, SCHEMA)
    except jsonschema.ValidationError as exc:
        errors.append(f"{path}: schema validation failed: {exc.message}")
        continue
    if record["primary_category"] not in VALID_CATEGORIES:
        errors.append(f"{path}: unknown primary_category={record['primary_category']}")
    print(f"validated {path.name}")

if errors:
    raise SystemExit("\n".join(errors))

print("repository validation passed")
