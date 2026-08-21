import json
from pathlib import Path
import re
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading


TIMELINE_SUMMARY_RE = re.compile(
    r'<a id="entry-(?P<identity>[a-z0-9-]+)"></a>\s*'
    r'<details><summary><strong>(?P<title>[^<\n]+)</strong> · '
    r'(?P<area>[^<\n]+?)\s*'
    r'<!-- timefirst:area=(?P<area_key>[a-z0-9._-]+) --> — '
    r'(?P<delta>[^<\n]+?)\s*'
    r'<!-- timefirst:delta=(?P<delta_key>[a-z0-9._-]+) --></summary>'
)
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
EXPECTED_TIMELINE_TITLES = {
    "2608-19197": "2026-08-21 · SPADE",
    "2608-18704": "2026-08-21 · MemFuse",
    "2608-18719": "2026-08-21 · Competence, Not Accuracy",
    "2608-18852": "2026-08-21 · SkillGate",
    "2608-19013": "2026-08-21 · Harness Continual Learning",
    "2608-17911": "2026-08-18 · CABLE",
    "2608-17756": "2026-08-18 · D²ACCI",
    "2608-17587": "2026-08-18 · WER",
    "2608-17588": "2026-08-18 · TRUSS",
    "2608-17534": "2026-08-18 · ArborMem",
    "2608-16168": "2026-08-17 · QUMem",
    "2608-16114": "2026-08-17 · HyperSkill",
    "2608-12888": "2026-08-13 · ReFind",
}


def timeline_summaries(text: str) -> list[dict[str, str]]:
    start = text.index('<a id="timeline"></a>')
    end = text.index('<a id="periods"></a>', start)
    return [match.groupdict() for match in TIMELINE_SUMMARY_RE.finditer(text[start:end])]


class MemoryReadingContractTest(unittest.TestCase):
    def test_chinese_timeline_scan_layer_is_localized_and_semantically_bound(self):
        zh = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        zh_summaries = timeline_summaries(zh)
        en_summaries = timeline_summaries(en)
        records = [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted((ROOT / "data" / "papers").glob("*.json"))
        ]

        self.assertEqual(len(EXPECTED_TIMELINE_TITLES), len(zh_summaries))
        self.assertEqual(len(EXPECTED_TIMELINE_TITLES), len(en_summaries))
        semantic_fields = ("identity", "title", "area_key", "delta_key")
        self.assertEqual(
            [tuple(item[field] for field in semantic_fields) for item in en_summaries],
            [tuple(item[field] for field in semantic_fields) for item in zh_summaries],
        )
        for zh_item, en_item in zip(zh_summaries, en_summaries, strict=True):
            with self.subTest(identity=zh_item["identity"]):
                self.assertEqual(
                    EXPECTED_TIMELINE_TITLES[zh_item["identity"]], zh_item["title"]
                )
                for field, minimum_cjk in (("area", 2), ("delta", 8)):
                    value = zh_item[field].strip()
                    self.assertIsNotNone(CJK_RE.match(value), (field, value))
                    self.assertGreaterEqual(
                        len(CJK_RE.findall(value)), minimum_cjk, (field, value)
                    )
                    self.assertNotEqual(value, en_item[field].strip())

        self.assertEqual([], validate_reading.validate_pair(zh, en))
        self.assertEqual(
            [], validate_reading.validate_memory_projection(zh, en, records)
        )

    def test_repository_entries_have_corresponding_bilingual_deep_notes(self):
        errors = validate_reading.validate_memory_note_links(
            (ROOT / "README.md").read_text(encoding="utf-8"),
            (ROOT / "README.en.md").read_text(encoding="utf-8"),
        )
        self.assertEqual([], errors)

    def test_removing_both_deep_note_links_is_rejected(self):
        zh = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        links = (
            " · [中文深读](papers/2026/2608.17911.zh.md)"
            " · [英文深读](papers/2026/2608.17911.md)"
        )
        zh = zh.replace(links, "", 1)
        en = en.replace(links, "", 1)
        errors = validate_reading.validate_memory_note_links(zh, en)
        self.assertTrue(
            any(
                "2608-17911" in error and "deep-note" in error.lower()
                for error in errors
            )
        )

    def test_mismatched_deep_note_identity_is_rejected(self):
        zh = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        for old, new in (
            ("2608.17911.zh.md", "2608.17756.zh.md"),
            ("2608.17911.md", "2608.17756.md"),
        ):
            zh = zh.replace(old, new, 1)
            en = en.replace(old, new, 1)
        errors = validate_reading.validate_memory_note_links(zh, en)
        self.assertTrue(
            any(
                "2608-17911" in error and "correspond" in error.lower()
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
