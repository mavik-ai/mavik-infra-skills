"""Regressões do instalador, sempre com home e fontes temporárias."""

from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("installer", Path(__file__).with_name("install.py"))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.home = self.root / "home"
        self.home.mkdir()
        self.source = self.root / "package"
        self.source.mkdir()
        (self.source / "README.md").write_text("package", encoding="utf-8")
        for name in installer.SKILLS:
            skill = self.source / "skills" / name
            for required in installer.REQUIRED:
                file = skill / required
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text("new", encoding="utf-8")
            (skill / "helper.py").write_text("raise RuntimeError('must not execute')", encoding="utf-8")
        self.addCleanup(patch.stopall)
        environment = dict(os.environ)
        environment.pop("CODEX_HOME", None)
        patch.dict(os.environ, environment, clear=True).start()
        patch.object(installer, "SOURCE_ROOT", self.source).start()
        patch.object(installer.Path, "home", return_value=self.home).start()

    def run_cli(self, *arguments):
        output, error = io.StringIO(), io.StringIO()
        with redirect_stdout(output), redirect_stderr(error):
            result = installer.main(list(arguments))
        return result, output.getvalue(), error.getvalue()

    def destination(self, target="codex", name=None):
        return self.home / f".{target}" / "skills" / (name or installer.SKILLS[0])

    def test_both_installs_six_complete_folders(self):
        code, output, error = self.run_cli("--target", "both")
        self.assertEqual(code, 0, error)
        self.assertIn("1.2.0", output)
        self.assertIn("nova sessão", output)
        self.assertEqual(output.count("Instalada:"), 6)
        for target in ("codex", "claude"):
            for name in installer.SKILLS:
                for file in (*installer.REQUIRED, "helper.py"):
                    self.assertEqual((self.destination(target, name) / file).read_text(), "raise RuntimeError('must not execute')" if file == "helper.py" else "new")

    def test_existing_aborts_all_without_overwriting(self):
        installer.install("claude")
        original = self.destination("claude") / "SKILL.md"
        original.write_text("old")
        code, _, error = self.run_cli("--target", "both")
        self.assertEqual(code, 2)
        self.assertIn("--update", error)
        self.assertEqual(original.read_text(), "old")
        self.assertFalse((self.home / ".codex").exists())

    def test_update_preserves_old_installation_in_backup(self):
        installer.install("codex")
        (self.destination() / "SKILL.md").write_text("old")
        (self.destination() / "local.txt").write_text("preserve")
        paths, backups = installer.install("both", update=True)
        self.assertEqual(len(paths), 6)
        self.assertEqual(len(backups), 3)
        self.assertEqual((backups[0] / "SKILL.md").read_text(), "old")
        self.assertEqual((backups[0] / "local.txt").read_text(), "preserve")
        self.assertTrue(backups[0].is_relative_to(self.home / ".mavik-infra-skills" / "backups"))
        self.assertEqual((self.destination() / "SKILL.md").read_text(), "new")

    def test_symlink_refused_even_with_update(self):
        self.destination().parent.mkdir(parents=True)
        self.destination().symlink_to(self.source / "skills" / installer.SKILLS[0], target_is_directory=True)
        code, _, error = self.run_cli("--target", "both", "--update")
        self.assertEqual(code, 2)
        self.assertIn("Revise manualmente", error)
        self.assertTrue(self.destination().is_symlink())
        self.assertFalse((self.home / ".claude").exists())

    def test_install_failure_rolls_back_old_and_new_destinations(self):
        installer.install("codex")
        for name in installer.SKILLS:
            (self.destination(name=name) / "SKILL.md").write_text("old")
        replace = os.replace
        def fail_one(source, destination):
            if Path(destination) == self.destination("claude", installer.SKILLS[1]) and "install-" in str(source):
                raise OSError("injected failure")
            return replace(source, destination)
        with patch.object(installer.os, "replace", side_effect=fail_one):
            code, _, error = self.run_cli("--target", "both", "--update")
        self.assertEqual(code, 2)
        self.assertIn("destinos restaurados", error)
        self.assertNotIn("Traceback", error)
        for name in installer.SKILLS:
            self.assertEqual((self.destination(name=name) / "SKILL.md").read_text(), "old")
            self.assertFalse(self.destination("claude", name).exists())

    def test_incomplete_source_aborts_before_any_install(self):
        (self.source / "skills" / installer.SKILLS[-1] / "agents/openai.yaml").unlink()
        code, _, error = self.run_cli("--target", "both")
        self.assertEqual(code, 2)
        self.assertIn("Arquivo obrigatório ausente", error)
        self.assertFalse((self.home / ".codex").exists())

    def test_codex_home_is_respected(self):
        custom = self.root / "custom-codex"
        with patch.dict(os.environ, {"CODEX_HOME": str(custom)}):
            paths, _ = installer.install("codex")
        self.assertEqual(len(paths), 3)
        self.assertTrue(all(path.is_relative_to(custom / "skills") for path in paths))
        self.assertFalse((self.home / ".codex").exists())

    def test_staging_failure_keeps_existing_installations(self):
        installer.install("codex")
        original = self.destination() / "SKILL.md"
        original.write_text("old")
        with patch.object(installer.shutil, "copytree", side_effect=OSError("copy failure")):
            code, _, error = self.run_cli("--target", "both", "--update")
        self.assertEqual(code, 2)
        self.assertIn("copy failure", error)
        self.assertEqual(original.read_text(), "old")
        self.assertFalse((self.home / ".claude").exists())

    def test_failed_rollback_reports_recoverable_backup(self):
        installer.install("codex")
        (self.destination() / "SKILL.md").write_text("old")
        replace = os.replace
        def fail_install_and_restore(source, destination):
            if Path(destination) == self.destination():
                raise OSError("destination unavailable")
            return replace(source, destination)
        with patch.object(installer.os, "replace", side_effect=fail_install_and_restore):
            code, _, error = self.run_cli("--target", "codex", "--update")
        self.assertEqual(code, 2)
        self.assertIn("Rollback incompleto", error)
        self.assertIn("Backup recuperável", error)
        backups = list((self.home / ".mavik-infra-skills" / "backups").glob("*/codex/*/SKILL.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), "old")

    def test_target_is_required(self):
        error = io.StringIO()
        with redirect_stderr(error), self.assertRaises(SystemExit) as raised:
            installer.main([])
        self.assertEqual(raised.exception.code, 2)
        self.assertIn("Erro nos argumentos", error.getvalue())


if __name__ == "__main__":
    unittest.main()
