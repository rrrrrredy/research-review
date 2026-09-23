"""Regression checks for complete source provenance."""
import contextlib
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

REPOSITORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY / "scripts"))
import check_skill


class SourceManifestTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="research-review-test-")
        self.addCleanup(temporary.cleanup)
        self.package = Path(temporary.name) / "research-review"
        shutil.copytree(
            REPOSITORY, self.package,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "tests")
        )
        self.manifest_path = self.package / "UPSTREAM.json"
        self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        self.root_patch = patch.object(check_skill, "ROOT", self.package)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def check(self):
        with contextlib.redirect_stdout(io.StringIO()):
            check_skill.main()

    def expect_rejected_manifest(self):
        self.manifest_path.write_text(
            json.dumps(self.manifest, indent=2) + "\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "each bundled method exactly once"):
            self.check()

    def test_intact_package_passes(self):
        self.check()

    def test_omitted_method_is_rejected(self):
        self.manifest["files"].pop()
        self.expect_rejected_manifest()

    def test_empty_manifest_is_rejected(self):
        self.manifest["files"] = []
        self.expect_rejected_manifest()

    def test_duplicate_entry_is_rejected(self):
        self.manifest["files"].append(dict(self.manifest["files"][0]))
        self.expect_rejected_manifest()


if __name__ == "__main__":
    unittest.main()
