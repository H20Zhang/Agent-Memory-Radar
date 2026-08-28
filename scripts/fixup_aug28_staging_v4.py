from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]

CATEGORY = {
    "2608.25329": ("Memory Learning & Evolution", "memory-learning-evolution.md"),
    "2608.25553": ("Evaluation & Analysis", "evaluation-analysis.md"),
    "2608.25570": ("Memory Learning & Evolution", "memory-learning-evolution.md"),
    "2608.25655": ("Representation & Organization", "representation-organization.md"),
    "2608.26005": ("Representation & Organization", "representation-organization.md"),
}

for identity, (category_label, category_file) in CATEGORY.items():
    note_path = ROOT / "papers" / "2026" / f"{identity}.md"
    record_path = ROOT / "data" / "papers" / f"{identity}.json"
    text = note_path.read_text(encoding="utf-8")
    record = json.loads(record_path.read_text(encoding="utf-8"))

    # Replace the ad-hoc link row with the repository's compact return navigation
    # plus canonical paper metadata.
    lines = text.splitlines()
    link_index = next(
        i for i, line in enumerate(lines)
        if line.startswith("[Paper](") and f"{identity}.zh.md" in line
    )
    nav = (
        f"[← Latest Papers](../../README.en.md#latest-papers) · "
        f"[Research Map](../../README.en.md#field-map) · "
        f"[{category_label}](../../categories/{category_file}) · "
        f"[中文]({identity}.zh.md)"
    )
    metadata = (
        f"**Paper:** [arXiv:{identity}]({record['paper_url']}) · "
        f"**Published:** {record['published']} · "
        f"**Importance:** {record['importance']}/5 · "
        f"**Confidence:** {str(record['confidence']).title()}"
    )
    lines[link_index:link_index + 1] = [nav, "", metadata]
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    # Research delta is a one-line reader hook, not a section.
    match = re.search(r"\n## Research delta\n\n(.+?)\n\n## Problem\n", text, flags=re.S)
    if not match:
        raise RuntimeError(f"{identity}: missing Research delta section")
    delta = " ".join(match.group(1).split())
    text = text[:match.start()] + f"\n> **Research delta.** {delta}\n\n## Problem\n" + text[match.end():]

    if "## Closest comparison" not in text:
        raise RuntimeError(f"{identity}: missing closest-comparison heading")
    text = text.replace("## Closest comparison", "## Compared with", 1)
    note_path.write_text(text, encoding="utf-8")

Path(__file__).unlink()
