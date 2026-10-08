# MAVIK · Cloudflare Ops

Skill independente de auditoria e operação assistida da Cloudflare. Versão inicial 1.0.0, PT-BR, MIT. Não é produto oficial Cloudflare.

## Uso

Instale esta pasta em `~/.codex/skills/cloudflare-ops` ou `~/.claude/skills/cloudflare-ops` e reinicie a sessão. Use `$cloudflare-ops audite a configuração Cloudflare deste projeto`.

Requer agente com acesso autorizado a API/painel/documentação; CLI/MCP são opcionais. Não inclui cliente API nem scripts. Credenciais privadas de leitura primeiro; alterações exigem autorização correspondente. Nenhum domínio/IP padrão.

## Conteúdo

- SKILL.md: descoberta, evidências, permissões e integração com origem.
- references/security.md: DNS, TLS, origem, Access, WAF e abuso.
- references/performance.md: cache, privacidade, streaming e medições.
- references/operations.md: ferramentas, backup R2, monitor e rollout.
- agents/openai.yaml: descoberta e apresentação no Codex.

Pode operar sem coolify-ops; quando a origem for Coolify, a revisão conjunta cobre responsabilidades distintas. Não configura monitoramento contínuo, backup, proteção ou custos automaticamente. Documentação foi consultada em 08/10/2026; revalidar recursos/preços conforme plano e versão antes de executar.
