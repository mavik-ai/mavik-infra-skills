#!/usr/bin/env python3
"""Read-only Coolify inventory. No operational guarantee is inferred from flags."""
import argparse
import ipaddress
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
from urllib.parse import urlsplit

LIMIT = 1024 * 1024
ID = re.compile(r"[A-Za-z0-9_-]{1,64}\Z")
ALIAS = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}\Z")
ENDPOINTS = ("servers", "projects", "applications", "services", "databases",
             "s3-storages", "notifications/telegram")
SECRET_KEY = re.compile(r"TOKEN|SECRET|PASSWORD|KEY|CREDENTIAL", re.I)


class AuditError(Exception):
    pass


def read_env(path):
    """Parse literal assignments; never expand or execute shell expressions."""
    file = Path(path)
    if file.stat().st_size > LIMIT:
        raise AuditError("arquivo env excede o limite")
    values = {}
    for line in file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:]
        key, sep, value = line.partition("=")
        if not sep or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            raise AuditError("env possui atribuição inválida")
        value = value.strip()
        if value[:1] in ("'", '"'):
            if len(value) < 2 or value[-1] != value[0]:
                raise AuditError("env possui aspas inválidas")
            value = value[1:-1]
        values[key] = value
    if any(value and SECRET_KEY.search(key) for key, value in values.items()):
        if stat.S_IMODE(file.stat().st_mode) & 0o077:
            raise AuditError("env com segredo exige modo privado (600 ou mais restrito)")
    return values


def validate_url(url):
    parsed = urlsplit(url)
    if (not parsed.hostname or parsed.username is not None or parsed.password is not None
            or parsed.query or parsed.fragment or parsed.path not in ("", "/")
            or any(ord(char) < 33 or char in '\\"' for char in url)):
        raise AuditError("URL deve ser origem explícita sem credenciais, caminho ou parâmetros")
    try:
        parsed.port
    except ValueError:
        raise AuditError("porta inválida") from None
    try:
        loopback = parsed.hostname == "localhost" or ipaddress.ip_address(parsed.hostname).is_loopback
    except ValueError:
        loopback = parsed.hostname == "localhost"
    if parsed.netloc.endswith(":"):
        raise AuditError("porta inválida")
    if parsed.scheme != "https" and not (parsed.scheme == "http" and loopback):
        raise AuditError("HTTPS obrigatório; HTTP permitido somente em loopback")
    return url.rstrip("/")


class Client:
    def __init__(self, url, token, ssh=None):
        self.url = validate_url(url)
        if not token or any(ord(c) < 32 or ord(c) == 127 for c in token):
            raise AuditError("COOLIFY_API_TOKEN ausente ou inválido")
        if ssh and not ALIAS.fullmatch(ssh):
            raise AuditError("alias SSH inválido")
        self.token, self.ssh = token, ssh

    def get(self, route):
        # Routes originate only from fixed endpoints and validated resource IDs.
        base = "http://127.0.0.1:8000" if self.ssh else self.url
        bearer = self.token.replace("\\", "\\\\").replace('"', '\\"')
        config = (f'url = "{base}/api/v1/{route}"\n'
                  f'header = "Authorization: Bearer {bearer}"\n'
                  'request = "GET"\nconnect-timeout = 10\nmax-time = 20\n'
                  f'max-filesize = {LIMIT}\nmax-redirs = 0\n'
                  'silent\nwrite-out = "\\n%{http_code}"\n')
        command = (["ssh", "-T", "-o", "BatchMode=yes", "-o", "ConnectTimeout=10",
                    self.ssh, "curl --disable --config -"] if self.ssh else
                   ["curl", "--disable", "--config", "-"])
        try:
            result = subprocess.run(command, input=config.encode(), stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL, timeout=25, check=False)
        except (OSError, subprocess.TimeoutExpired):
            raise AuditError("transporte indisponível ou timeout") from None
        if result.returncode:
            raise AuditError("falha de transporte (detalhes privados omitidos)")
        if len(result.stdout) > LIMIT + 8:
            raise AuditError("resposta excede o limite")
        body, _, code = result.stdout.rpartition(b"\n")
        if code != b"200":
            status = code.decode() if re.fullmatch(rb"[0-9]{3}", code) else "desconhecido"
            raise AuditError(f"HTTP {status}; não verificável")
        try:
            return json.loads(body)
        except (ValueError, UnicodeError, RecursionError):
            raise AuditError("resposta JSON inválida") from None


def records(payload):
    if isinstance(payload, list) and all(isinstance(item, dict) for item in payload):
        return payload
    if isinstance(payload, dict):
        for key in ("data", "items", "resources"):
            if key in payload:
                return records(payload[key])
    raise AuditError("formato de lista não reconhecido")


def clean(value, token, identifier=False):
    if not isinstance(value, (str, int, float, bool)):
        return "não verificável"
    text = str(value).replace(token, "[redigido]")
    if not identifier:
        text = re.sub(r"[A-Za-z0-9_./+=:-]{24,}", "[redigido]", text)
    text = re.sub(r"[\x00-\x1f\x7f]", " ", text)[:120]
    return re.sub(r"([\\`*_{}\[\]()<>#!|])", r"\\\1", text)


def flag(value):
    return "habilitado" if value is True else "desabilitado" if value is False else "não verificável"


def audit(client, resource=None):
    lines = ["# Inventário Coolify somente leitura", "", "Inventário não comprova segurança ou operação."]
    failed, inventories = False, {}
    for route in ENDPOINTS:
        try:
            payload = client.get(route)
            if route == "notifications/telegram":
                if isinstance(payload, dict) and isinstance(payload.get("data"), dict):
                    payload = payload["data"]
                if not isinstance(payload, dict) or not any(k.startswith("telegram_") for k in payload):
                    raise AuditError("formato de notificações não reconhecido")
                enabled = payload.get("telegram_enabled")
                token_field = next((key for key in ("telegram_token", "telegram_bot_token") if key in payload), None)
                # Read-scoped API responses can hide credential values.
                presence = "presente" if token_field and isinstance(payload[token_field], str) and payload[token_field] else "não verificável"
                lines += ["", "## Telegram", f"- Canal: {flag(enabled)}; token: {presence}.",
                          "- Entrega de alerta: pendente de prova autorizada."]
                failed |= enabled is not True
            else:
                inventories[route] = records(payload)
                lines += ["", f"## {route}"]
                selected = [item for item in inventories[route] if not resource or route not in
                            ("applications", "services", "databases") or item.get("uuid") == resource or item.get("name") == resource]
                if not selected:
                    lines.append("- Nenhum recurso listado neste escopo; não significa auditoria aprovada.")
                for item in selected:
                    name = clean(item.get("name", "sem nome"), client.token)
                    uuid = item.get("uuid")
                    identifier = uuid if isinstance(uuid, str) and ID.fullmatch(uuid) else "não verificável"
                    state = clean(item.get("status", "não verificável"), client.token)
                    lines.append(f"- {name}; ID: {clean(identifier, client.token, True)}; estado: {state}.")
        except AuditError as error:
            failed = True
            lines += ["", f"## {route}", f"- Não verificável: {error}."]
    if resource:
        routes = ("applications", "services", "databases")
        found = any(item.get("uuid") == resource or item.get("name") == resource
                    for route in routes for item in inventories.get(route, []))
        if not found:
            failed = True
            lines += ["", "Recurso solicitado não localizado; ausência não comprovada se alguma consulta falhou."]
    for server in inventories.get("servers", []):
        uuid = server.get("uuid")
        if not isinstance(uuid, str) or not ID.fullmatch(uuid):
            failed = True
            lines += ["", "Sentinel: ID de servidor inválido; não verificável."]
            continue
        try:
            settings = client.get(f"servers/{uuid}/sentinel")
            if isinstance(settings, dict) and isinstance(settings.get("data"), dict):
                settings = settings["data"]
            if not isinstance(settings, dict) or not any(k in settings for k in ("is_sentinel_enabled", "is_metrics_enabled")):
                raise AuditError("formato Sentinel não reconhecido")
            lines += ["", f"## Sentinel ({clean(uuid, client.token, True)})",
                      f"- Sentinel: {flag(settings.get('is_sentinel_enabled'))}.",
                      f"- Métricas: {flag(settings.get('is_metrics_enabled'))}; coleta real pendente de prova."]
            failed |= (settings.get("is_metrics_enabled") is not True
                       or settings.get("is_sentinel_enabled") is False)
        except AuditError as error:
            failed = True
            lines += ["", f"Sentinel: não verificável: {error}."]
    lines += ["", "## Verificações manuais pendentes",
              "- Backup: agenda, execução, cópia externa e restauração isolada.",
              "- TLS público, restrições/rate limit da API e permissões do token.",
              "- Autenticação, 2FA, cadastro e entrega de emails.",
              "- Portas Docker, firewall IPv4/IPv6 e saúde/coleta real de métricas.",
              "- Entrega de alertas e monitor externo do host."]
    return "\n".join(lines), 2 if failed else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, help="origem confiável escolhida explicitamente")
    parser.add_argument("--env-file")
    parser.add_argument("--resource", help="nome ou UUID exato")
    parser.add_argument("--ssh", help="alias SSH explícito; API remota em loopback")
    args = parser.parse_args(argv)
    try:
        if args.resource is not None and (not args.resource or len(args.resource) > 120
                                         or any(ord(c) < 32 or ord(c) == 127 for c in args.resource)):
            raise AuditError("filtro de recurso inválido")
        values = read_env(args.env_file) if args.env_file else {}
        client = Client(args.url, os.environ.get("COOLIFY_API_TOKEN") or values.get("COOLIFY_API_TOKEN"), args.ssh)
        report, code = audit(client, args.resource)
        print(report)
        return code
    except (AuditError, OSError, UnicodeError):
        print("Coleta não verificável: confira URL, token, arquivo privado e acesso.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
