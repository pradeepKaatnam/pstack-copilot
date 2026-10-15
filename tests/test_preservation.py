import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import verify

spec = importlib.util.spec_from_file_location("installer", SCRIPTS / "install-project.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class PreservationTests(unittest.TestCase):
    def test_tree_identity_includes_hidden_files_modes_and_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".hidden").write_bytes(b"original\0binary")
            (root / "sub").mkdir()
            script = root / "sub/run"
            script.write_text("#!/bin/sh\nexit 0\n")
            script.chmod(0o755)
            (root / "sub/path").write_text("A filename must not be mistaken for tree metadata.\n")
            (root / "link").symlink_to("sub/run")
            entries = []
            for name in (".hidden", "sub/run", "link", "sub/path"):
                path = root / name
                data = verify.contents(path)
                entries.append({"path": name, "mode": verify.mode(path),
                                "git_blob": verify.git_hash("blob", data)})
            subprocess.run(["git", "-C", str(root), "add", "."], check=True)
            expected = subprocess.check_output(["git", "-C", str(root), "write-tree"]).decode().strip()
            self.assertEqual(verify.tree_hash(entries), expected)
            entries[1]["mode"] = "100644"
            self.assertNotEqual(verify.tree_hash(entries), expected)
            self.assertNotEqual(verify.tree_hash(entries[:-1]), expected)

    def test_passages_preserve_exact_original_and_line_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / "source", Path(directory) / "target"
            a.write_text("prefix\nTask(readonly=true)\nsuffix\n")
            b.write_text("prefix\nUse a sequential review pass.\nsuffix\n")
            result = verify.changes(a, b)
            self.assertEqual(result[0]["source_start"], 2)
            self.assertEqual(result[0]["source_end"], 2)
            self.assertEqual(result[0]["original"], "Task(readonly=true)\n")

    def test_unsafe_mapping_paths_are_rejected(self):
        for path in ("../elsewhere", "/tmp/elsewhere", "copilot/../../elsewhere"):
            with self.assertRaises(ValueError):
                verify.safe_path(path)

    def test_passages_do_not_normalize_original_line_endings(self):
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "a", Path(directory) / "b"
            source.write_bytes(b"old\r\nlast line")
            target.write_bytes(b"replacement\nlast line")
            self.assertEqual(verify.changes(source, target)[0]["original"], "old\r\n")

    def test_package_checks_exclude_only_designated_runtime_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)
            runtime = package / "skills/poteto-mode/scripts"
            generated = runtime / "node_modules/.bin"
            generated.mkdir(parents=True)
            (generated / "bun").symlink_to("/nonexistent-dependency-binary")
            (generated.parent / "README.md").write_text("[Third party](missing.md)")
            (runtime / "tool.ts").write_text("export {}")
            other = package / "skills/other/node_modules"
            other.mkdir(parents=True)
            (other / "README.md").write_text("Not an allowed generated directory.")
            paths = set(verify.package_paths(package))
            self.assertIn(runtime / "tool.ts", paths)
            self.assertIn(other / "README.md", paths)
            self.assertNotIn(generated / "bun", paths)
            self.assertNotIn(generated.parent / "README.md", set(verify.package_paths(package, "*.md")))


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        root = Path(self.temporary.name)
        self.source = root / "copilot/skills"
        skill = self.source / "example"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: example\ndescription: Example\n---\n")
        (skill / "script.sh").write_text("#!/bin/sh\nexit 0\n")
        (skill / "script.sh").chmod(0o755)
        (self.source.parent / "plugin.json").write_text('{"version":"test"}')
        (self.source.parent / "LICENSE").write_text("MIT License\nCopyright example\n")
        self.project = root / "project"
        self.project.mkdir()
        self.patcher = patch.object(installer, "SOURCE", self.source)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_install_update_and_resource_modes(self):
        installer.install(self.project)
        script = self.project / ".github/skills/example/script.sh"
        self.assertEqual(verify.mode(script), "100755")
        (self.source / "example/SKILL.md").write_text("new\n")
        installer.install(self.project, update=True)
        self.assertEqual((script.parent / "SKILL.md").read_text(), "new\n")
        state = json.loads((self.project / ".github/pstack-installed.json").read_text())
        self.assertEqual(state["files"]["example/SKILL.md"], hashlib.sha256(b"new\n").hexdigest())
        self.assertEqual((self.project / ".github/pstack-LICENSE").read_text(), "MIT License\nCopyright example\n")

    def test_refuses_modified_snapshot(self):
        installer.install(self.project)
        skill = self.project / ".github/skills/example/SKILL.md"
        skill.write_text("company guidance\n")
        with self.assertRaisesRegex(ValueError, "Locally modified"):
            installer.install(self.project, update=True)
        self.assertEqual(skill.read_text(), "company guidance\n")

    def test_refuses_existing_unmanaged_skill(self):
        skill = self.project / ".github/skills/example"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("existing")
        with self.assertRaisesRegex(ValueError, "Unmanaged"):
            installer.install(self.project)

    def test_refuses_symlinked_discovery(self):
        outside = self.project.parent / "outside"
        outside.mkdir()
        (self.project / ".github").symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "symlink"):
            installer.install(self.project)
        self.assertEqual(list(outside.iterdir()), [])

    def test_refuses_tampered_state_path(self):
        installer.install(self.project)
        state = self.project / ".github/pstack-installed.json"
        record = json.loads(state.read_text())
        record["files"] = {"../../../outside": "anything"}
        state.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, "Invalid"):
            installer.install(self.project, update=True)

    def test_runtime_dependencies_are_not_snapshots_or_update_conflicts(self):
        (self.source / "example").rename(self.source / "poteto-mode")
        source_modules = self.source / "poteto-mode/scripts/node_modules/dependency"
        source_modules.mkdir(parents=True)
        (source_modules / "index.js").write_text("source dependency")
        installer.install(self.project)
        destination = self.project / ".github/skills/poteto-mode"
        self.assertFalse((destination / "scripts/node_modules").exists())
        installed_modules = destination / "scripts/node_modules/dependency"
        installed_modules.mkdir(parents=True)
        (installed_modules / "index.js").write_text("installed dependency")
        installer.install(self.project, update=True)
        self.assertEqual((installed_modules / "index.js").read_text(), "installed dependency")
        (destination / "scripts/unmanaged.js").write_text("local addition")
        with self.assertRaisesRegex(ValueError, "Unmanaged"):
            installer.install(self.project, update=True)


if __name__ == "__main__":
    unittest.main()
