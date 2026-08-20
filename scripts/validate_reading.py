#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "README.md"
EN = ROOT / "README.en.md"
LIB_ZH = ROOT / "library" / "README.md"
LIB_EN = ROOT / "library" / "README.en.md"

CARD_RE = re.compile(r"^### \[[^\]]+\]\((papers/\d{4}/[^)]+\.md)\)", re.MULTILINE)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


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


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for p in [ZH, EN, LIB_ZH, LIB_EN, ROOT / "docs" / "EDITORIAL_STANDARD.md", ROOT / "docs" / "DAILY_WORKFLOW.md"]:
        if not p.exists():
            fail(errors, f"missing reader contract: {p.relative_to(ROOT)}")

    if errors:
        for e in errors:
            print("ERROR", e)
        return 1

    zh = ZH.read_text(encoding="utf-8")
    en = EN.read_text(encoding="utf-8")

    if "README.en.md" not in zh or "README.md" not in en:
        fail(errors, "README language switch is incomplete")

    for anchor in ["latest", "changes", "field-map", "reading-paths", "library"]:
        if f'<a id="{anchor}"></a>' not in zh:
            fail(errors, f"README.md missing stable anchor {anchor}")
        if f'<a id="{anchor}"></a>' not in en:
            fail(errors, f"README.en.md missing stable anchor {anchor}")

    order = ["latest", "changes", "field-map", "reading-paths", "library"]
    for name, text in [("README.md", zh), ("README.en.md", en)]:
        pos = [text.find(f'<a id="{a}"></a>') for a in order]
        if pos != sorted(pos) or any(p < 0 for p in pos):
            fail(errors, f"{name}: progressive-depth section order drift")

    zh_cards = CARD_RE.findall(zh)
    en_cards = CARD_RE.findall(en)
    if not 6 <= len(zh_cards) <= 8:
        fail(errors, f"README.md: expected 6–8 Latest papers, found {len(zh_cards)}")
    if zh_cards != en_cards:
        fail(errors, "Chinese/English Latest paper identities or order drifted")

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
