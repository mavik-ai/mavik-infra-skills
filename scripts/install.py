#!/usr/bin/env python3
"""Instala as skills locais sem executar seus helpers."""

import argparse
import os
from pathlib import Path
import shutil
import sys
import tempfile
from uuid import uuid4


VERSION = "1.2.0"
SOURCE_ROOT = Path(__file__).resolve().parent.parent
SKILLS = ("coolify-ops", "cloudflare-ops", "auditoria-pos-deploy-coolify")
REQUIRED = ("README.md", "SKILL.md", "agents/openai.yaml")


class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, f"Erro nos argumentos: {message}\n")


def validate_skill(path):
    if path.is_symlink():
        raise ValueError(f"Destino/source de skill é um symlink: {path}. Revise manualmente.")
    if not path.is_dir():
        raise ValueError(f"Pasta de skill inválida: {path}")
    for name in REQUIRED:
        if not (path / name).is_file():
            raise ValueError(f"Arquivo obrigatório ausente: {path / name}")


def install(target, update=False):
    if not (SOURCE_ROOT / "README.md").is_file():
        raise ValueError(f"README do pacote ausente: {SOURCE_ROOT / 'README.md'}")
    targets = ("codex", "claude") if target == "both" else (target,)
    home = Path.home()
    roots = {"codex": Path(os.environ.get("CODEX_HOME", home / ".codex")), "claude": home / ".claude"}
    entries = []
    for name in SKILLS:
        source = SOURCE_ROOT / "skills" / name
        validate_skill(source)
        for tool in targets:
            destination = roots[tool] / "skills" / name
            exists = destination.exists() or destination.is_symlink()
            if exists:
                validate_skill(destination)
            entries.append((source, tool, destination, exists))
    existing = [str(dest) for _, _, dest, exists in entries if exists]
    if existing and not update:
        raise ValueError("Instalações existentes; nada foi alterado. Revise e use --update: " + ", ".join(existing))

    private = home / ".mavik-infra-skills"
    private.mkdir(mode=0o700, parents=True, exist_ok=True)
    backup_root = private / "backups" / uuid4().hex
    installed, backups = [], []
    with tempfile.TemporaryDirectory(prefix="install-", dir=private) as temporary:
        staging = Path(temporary)
        for source, tool, destination, exists in entries:
            shutil.copytree(source, staging / tool / destination.name)
        # Confira novamente após preparar todas as cópias, antes de alterar destinos.
        for _, _, destination, exists in entries:
            current = destination.exists() or destination.is_symlink()
            if current != exists:
                raise ValueError(f"Destino mudou durante a preparação: {destination}. Tente novamente.")
            if current:
                validate_skill(destination)
        try:
            for _, tool, destination, exists in entries:
                destination.parent.mkdir(parents=True, exist_ok=True)
                if exists:
                    backup = backup_root / tool / destination.name
                    backup_root.parent.mkdir(mode=0o700, exist_ok=True)
                    backup_root.mkdir(mode=0o700, exist_ok=True)
                    backup.parent.mkdir(mode=0o700, exist_ok=True)
                    os.replace(destination, backup)
                    backups.append((destination, backup))
                os.replace(staging / tool / destination.name, destination)
                installed.append(destination)
        except OSError as error:
            rollback_errors = []
            for destination in reversed(installed):
                try:
                    shutil.rmtree(destination)
                except OSError as rollback_error:
                    rollback_errors.append(str(rollback_error))
            for destination, backup in reversed(backups):
                try:
                    os.replace(backup, destination)
                except OSError as rollback_error:
                    rollback_errors.append(f"Backup recuperável em {backup}: {rollback_error}")
            if rollback_errors:
                raise OSError(f"Instalação falhou: {error}. Rollback incompleto: {'; '.join(rollback_errors)}") from error
            raise OSError(f"Instalação falhou; destinos restaurados: {error}") from error
    return installed, [backup for _, backup in backups]


def main(argv=None):
    parser = Parser(description=f"Instalador local MAVIK Infra Skills {VERSION} (Python 3.10+).")
    parser.add_argument("--target", required=True, choices=("codex", "claude", "both"))
    parser.add_argument("--update", action="store_true", help="Atualiza instalações existentes com backup recuperável.")
    args = parser.parse_args(argv)
    try:
        if sys.version_info < (3, 10):
            raise ValueError("Python 3.10 ou superior é obrigatório.")
        installed, backups = install(args.target, args.update)
    except (OSError, ValueError, shutil.Error) as error:
        print(f"Erro: {error}", file=sys.stderr)
        return 2
    print(f"MAVIK Infra Skills {VERSION}")
    for path in installed:
        print(f"Instalada: {path}")
    for path in backups:
        print(f"Backup recuperável: {path}")
    print("Abra uma nova sessão do Codex/Claude Code para carregar as skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
