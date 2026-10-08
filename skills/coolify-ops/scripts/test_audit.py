import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import audit


class AuditTests(unittest.TestCase):
    def client(self, ssh=None):
        return audit.Client("https://coolify.example.test", "private-token", ssh)

    def test_url_and_ssh_boundaries(self):
        for url in ("http://remote.test", "https://u:p@host", "https://host/path",
                    'https://host"', 'https://host\\evil', "https://host:wrong",
                    "https://host:99999", "https://host\n", "https://host?x=1"):
            with self.subTest(url=url), self.assertRaises(audit.AuditError):
                audit.validate_url(url)
        self.assertEqual(audit.validate_url("http://127.0.0.1:8000/"), "http://127.0.0.1:8000")
        for alias in ("-oProxyCommand=x", "host;id", "user@host", "$(id)"):
            with self.assertRaises(audit.AuditError):
                self.client(alias)

    def test_env_is_literal_and_private_when_secret_present(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "private.env"
            file.write_text("COOLIFY_API_TOKEN='$(touch /never)'\nURL=https://host\n")
            file.chmod(0o644)
            with self.assertRaises(audit.AuditError):
                audit.read_env(file)
            file.chmod(0o600)
            self.assertEqual(audit.read_env(file)["COOLIFY_API_TOKEN"], "$(touch /never)")
            file.write_text("URL=https://host\n")
            file.chmod(0o644)
            self.assertEqual(audit.read_env(file)["URL"], "https://host")

    @patch("audit.subprocess.run")
    def test_curl_safe_transport(self, run):
        run.return_value = subprocess.CompletedProcess([], 0, b'[]\n200')
        self.assertEqual(self.client().get("servers"), [])
        args, kwargs = run.call_args
        self.assertNotIn("private-token", " ".join(args[0]))
        self.assertEqual(args[0], ["curl", "--disable", "--config", "-"])
        config = kwargs["input"].decode()
        self.assertIn("max-redirs = 0", config)
        self.assertNotIn("location", config)
        self.assertNotIn("insecure", config)
        self.assertIn("max-filesize", config)
        self.assertEqual(kwargs["stderr"], subprocess.DEVNULL)
        self.client("my-coolify").get("servers")
        args, kwargs = run.call_args
        self.assertEqual(args[0][-1], "curl --disable --config -")
        self.assertIn("http://127.0.0.1:8000/api/v1/servers", kwargs["input"].decode())

    @patch("audit.subprocess.run")
    def test_transport_errors_never_include_response_secrets(self, run):
        for output in (b'private-token\n403', b'private-token\n302', b'private-token\n200',
                       b'x' * (audit.LIMIT + 10)):
            run.return_value = subprocess.CompletedProcess([], 0, output)
            with self.assertRaises(audit.AuditError) as error:
                self.client().get("servers")
            self.assertNotIn("private-token", str(error.exception))
        run.side_effect = subprocess.TimeoutExpired("private-token", 25)
        with self.assertRaises(audit.AuditError):
            self.client().get("servers")

    def inventory(self, route):
        if route == "notifications/telegram":
            return {"telegram_enabled": True, "telegram_token": "secret", "telegram_chat_id": "personal-id"}
        if route.endswith("/sentinel"):
            return {"is_sentinel_enabled": None, "is_metrics_enabled": True, "secret": "hidden"}
        if route == "servers":
            return {"data": {"items": [{"uuid": "abcdefgh12345678abcdefgh", "name": "server"}]}}
        if route == "applications":
            return [{"uuid": "app1", "name": "App *x* private-token " + "A" * 30,
                     "status": "running", "environment_variables": "hidden", "password": "hidden"}]
        return []

    def test_allowlist_and_unknown_flag(self):
        client = self.client()
        client.get = self.inventory
        report, code = audit.audit(client)
        self.assertEqual(code, 0)
        for secret in ("private-token", "personal-id", "hidden", "A" * 30):
            self.assertNotIn(secret, report)
        self.assertIn("abcdefgh12345678abcdefgh", report)
        self.assertIn("Sentinel: não verificável", report)
        self.assertIn("running", report)
        self.assertIn("coleta real pendente", report)

    def test_filter_not_found_and_forbidden_inventory(self):
        client = self.client()
        def get(route):
            if route == "services":
                raise audit.AuditError("HTTP 403; não verificável")
            return self.inventory(route)
        client.get = get
        report, code = audit.audit(client, "absent")
        self.assertEqual(code, 2)
        self.assertIn("ausência não comprovada", report)
        self.assertIn("HTTP 403", report)
        self.assertNotIn("running", report)

    def test_read_scoped_telegram_credentials_are_unknown(self):
        client = self.client()
        for token in (None, "", "omitted"):
            def get(route):
                if route == "notifications/telegram":
                    result = {"telegram_enabled": True}
                    if token != "omitted":
                        result["telegram_token"] = token
                    return result
                return self.inventory(route)
            client.get = get
            report, code = audit.audit(client)
            self.assertEqual(code, 0)
            self.assertIn("token: não verificável", report)
            self.assertNotIn("token: ausente", report)

    def test_identifier_visible_but_actual_token_hidden(self):
        self.assertEqual(audit.clean("abcdefgh12345678abcdefgh", "private-token", True),
                         "abcdefgh12345678abcdefgh")
        self.assertNotIn("private-token", audit.clean("private-token", "private-token", True))

    def test_malformed_lists(self):
        self.assertEqual(audit.clean({"password": "secret"}, "token"), "não verificável")
        self.assertEqual(audit.clean(["secret"], "token"), "não verificável")
        for payload in (None, {}, {"data": [None]}, {"data": "secret"}, ["secret"]):
            with self.assertRaises(audit.AuditError):
                audit.records(payload)
        client = self.client()
        client.get = lambda route: {}
        report, code = audit.audit(client)
        self.assertEqual(code, 2)
        self.assertIn("formato", report)

    def test_missing_credentials(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(audit.main(["--url", "https://host"]), 2)


if __name__ == "__main__":
    unittest.main()
