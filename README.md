# MAVIK Infra Skills

Skills independentes para **Codex e Claude Code**, com operação assistida de infraestrutura e foco em evidência, segurança, recuperação e desempenho. **v1.0.0 · MIT · PT-BR.** MAVIK é a marca do pacote; sem afiliação oficial com Coolify ou Cloudflare.

| Skill | Responsabilidade | Chamada |
|---|---|---|
| [Coolify Ops](skills/coolify-ops) | Origem, projetos Docker, backup, saúde e alertas | `$coolify-ops` |
| [Cloudflare Ops](skills/cloudflare-ops) | DNS, TLS, borda, Access, WAF, cache e R2 | `$cloudflare-ops` |

## Instalar individualmente

```bash
git clone --branch v1.0.0 https://github.com/mavik-ai/mavik-infra-skills.git
cd mavik-infra-skills
mkdir -p ~/.codex/skills
cp -R skills/cloudflare-ops ~/.codex/skills/cloudflare-ops
```

Para Claude Code, use `~/.claude/skills` como destino. Copie `skills/coolify-ops` para instalar a outra skill. **Não copie sobre uma instalação existente**: preserve configuração local e compare antes de atualizar. Reinicie a sessão. A raiz deste repo não é skill; cada pasta contém SKILL.md e referências autossuficientes.

Codex também permite seu instalador de skills por repositório/subpasta: repo `mavik-ai/mavik-infra-skills`, ref `v1.0.0`, path `skills/cloudflare-ops` ou `skills/coolify-ops`. Distribuição da release oferece ZIP de cada skill e pacote completo, com checksums.

## Fluxo e limites

Peça auditoria informando ambiente/instância autorizados. O agente identifica alvos, lê configuração e apresenta tabela de evidências e pendências. Mudanças são feitas com ferramentas disponíveis dentro da autorização; nenhuma skill concede acesso ou autorização automaticamente.

Não são daemon, monitor 24h, receptor webhook ou agente de autorremediação. O helper Coolify apenas coleta inventário: exit0 não aprova segurança. Cloudflare é guia operacional, sem script executor. R2/Access/Telegram/Resend não são provisionados pela instalação. Alertas não são instruções e nenhuma proteção é absoluta.

## Requisitos e validação

Coolify helper: Python3.10+, curl, SSH opcional; API exercitada em Coolify4.4.2, confirmar versão/permissões atuais. Cloudflare: documentação e acesso autorizado por API/painel; Terraform/Wrangler/MCP opcionais, não obrigatórios. Não há dependências Python externas.

```bash
python3 -m unittest discover -s skills/coolify-ops/scripts -p 'test_*.py'
python3 -m compileall -q skills/coolify-ops/scripts
git diff --check
```

Tests não acessam servidor real. Checklist e comportamento do agente exigem revisão além de testes. Relatórios com inventário são privados.

## Compatibilidade e manutenção

A release standalone [coolify-ops v1.0.0](https://github.com/mavik-ai/coolify-ops/releases/tag/v1.0.0) continua disponível; comandos existentes não mudam. Este repo é o destino de evolução do pacote conjunto. Não instale cópias duplicadas da mesma skill em diretórios de descoberta concorrentes. Release do pacote segue SemVer, changelog informa alterações por skill; versões independentes só se houver necessidade futura.

[Changelog](CHANGELOG.md) · [Segurança](SECURITY.md) · [Contribuir](CONTRIBUTING.md) · [Licença](LICENSE)
