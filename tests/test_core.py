from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


class CoreTests(unittest.TestCase):
    def test_section_parser(self):
        module = load("build_index", "Operator Team OS/3. Skills/memory-read/scripts/build_index.py")
        self.assertEqual(
            module.sections("# A\nalpha\n## B\nbeta"),
            [("A", "alpha"), ("B", "beta")],
        )

    def test_query_scoring_prefers_heading(self):
        module = load("query", "Operator Team OS/3. Skills/memory-read/scripts/query.py")
        heading = {"heading": "Current priorities", "path": "x.md", "text": "other"}
        body = {"heading": "Other", "path": "x.md", "text": "current priorities"}
        self.assertGreater(module.score(heading, ["priorities"]), module.score(body, ["priorities"]))

    def test_index_exclusions_are_case_insensitive(self):
        module = load("build_index_exclusions", "Operator Team OS/3. Skills/memory-read/scripts/build_index.py")
        self.assertTrue(module.excluded(Path("docs/z_Archive/old.md")))
        self.assertTrue(module.excluded(Path("node_modules/readme.md")))

    def test_session_log_helpers(self):
        module = load("session_log", "Operator Team OS/3. Skills/memory-manage/scripts/append_session_log.py")
        self.assertEqual(module.clean("a\n  b"), "a b")
        self.assertIn("## Decisions", module.bullets("Decisions", ["Use one source"]))

    def test_manifest_and_doctor(self):
        subprocess.run(
            [sys.executable, "Operator Team OS/3. Skills/workspace-doctor/scripts/generate_manifest.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        manifest = json.loads((ROOT / "Operator Team OS/MANIFEST.json").read_text())
        self.assertEqual(manifest["os_version"], (ROOT / "Operator Team OS/VERSION").read_text().strip())
        result = subprocess.run(
            [sys.executable, "Operator Team OS/3. Skills/workspace-doctor/scripts/operator_doctor.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
