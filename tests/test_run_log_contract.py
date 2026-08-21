from pathlib import Path
from contextlib import redirect_stdout
import io
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading


class NoPublicRunLogContractTest(unittest.TestCase):
    def test_public_digests_do_not_expose_candidate_or_visual_workflow_state(self):
        forbidden_markers = (
            "## Backfill queue",
            "remain deferred pending complete adversarial review",
            "## Visual status",
        )
        for path in sorted((ROOT / "digests").glob("**/*.md")):
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                for marker in forbidden_markers:
                    self.assertNotIn(marker, text)

    def test_repository_has_no_public_daily_run_files(self):
        errors = validate_reading.validate_no_public_run_files(
            validate_reading.PUBLIC_OPERATIONAL_RUN_PATHS
        )
        self.assertEqual([], errors)

    def test_any_file_under_public_run_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            public_path = Path(temporary_directory) / "daily"
            forbidden = public_path / "2026" / "08" / "21.md"
            forbidden.parent.mkdir(parents=True)
            forbidden.write_text("# Operational state\n", encoding="utf-8")
            errors = validate_reading.validate_no_public_run_files((public_path,))
        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_public_run_path_cannot_itself_be_a_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            forbidden = Path(temporary_directory) / "daily"
            forbidden.write_text("# Operational state\n", encoding="utf-8")
            errors = validate_reading.validate_no_public_run_files((forbidden,))
        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_broken_symlink_cannot_hide_a_public_run_artifact(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            public_path = Path(temporary_directory) / "daily"
            public_path.mkdir()
            forbidden = public_path / "latest.md"
            forbidden.symlink_to(public_path / "missing.md")
            errors = validate_reading.validate_no_public_run_files((public_path,))
        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_reading_validator_runs_the_absence_guard(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            forbidden = Path(temporary_directory) / "daily"
            forbidden.write_text("# Operational state\n", encoding="utf-8")
            original = validate_reading.PUBLIC_OPERATIONAL_RUN_PATHS
            validate_reading.PUBLIC_OPERATIONAL_RUN_PATHS = (forbidden,)
            try:
                with redirect_stdout(io.StringIO()):
                    result = validate_reading.main()
            finally:
                validate_reading.PUBLIC_OPERATIONAL_RUN_PATHS = original
        self.assertEqual(1, result)

    def test_private_run_state_directory_is_git_ignored(self):
        result = subprocess.run(
            ["git", "check-ignore", ".radar-private/runs/example.json"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)

    def test_static_policy_and_authoritative_guidance_share_boundary(self):
        documents = (
            ROOT / "runs" / "README.md",
            ROOT / "docs" / "RADAR_AGENT_PROTOCOL.md",
            ROOT / "docs" / "DAILY_WORKFLOW.md",
            ROOT / "docs" / "MAINTENANCE.md",
            ROOT / "docs" / "BILINGUAL_PUBLICATION.md",
            ROOT / "CURATION.md",
            ROOT / "COMPACTION.md",
        )
        stale_directions = (
            "L0-log",
            "one private run log",
            "and the run log",
            "and one run log",
            "one compact daily log",
            "Daily provenance belongs under",
            "`runs/*` remain single-source",
        )
        for path in documents:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(path.exists(), f"missing guidance: {path}")
                text = path.read_text(encoding="utf-8")
                self.assertIn("No public operational run logs", text)
                self.assertIn(".radar-private", text)
                for stale in stale_directions:
                    self.assertNotIn(stale, text)


if __name__ == "__main__":
    unittest.main()
