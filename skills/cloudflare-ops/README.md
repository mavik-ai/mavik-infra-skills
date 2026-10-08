# MAVIK.AI · Cloudflare Ops

Skill independente de auditoria e operação assistida da Cloudflare. Parte do pacote v1.2.0, PT-BR, MIT. Não é produto oficial Cloudflare.

## O que ela resolve

O agente verifica primeiro se consegue acessar sua conta e o que tem permissão para fazer. Entende seu projeto e prepara DNS, HTTPS e proteção adequados ao plano; com autorização, aplica as mudanças e confere os resultados. Se o domínio ainda não usa Cloudflare, orienta a entrada e a troca de nameservers no registrador, preservando site e e-mail.

**Token R2 serve ao armazenamento.** Para DNS, TLS e WAF, é preciso acesso com as permissões desses serviços. A skill ensina o caminho certo, um passo por vez, sem pedir segredo na conversa. Recursos gratuitos são avaliados conforme o projeto; ligar todos pode quebrar APIs, pagamentos ou automações.

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

## Configuração guiada

> Use $cloudflare-ops para entender meu projeto, conferir a conexão e preparar a configuração de DNS, TLS e segurança compatível com meu plano. Se faltar acesso, ensine um passo por vez como criar e guardar o token correto. Apresente as mudanças e os testes antes de aplicar o que ainda não foi autorizado.

[Guia de acesso privado](references/acesso-privado.md) · [Configuração por projeto](references/configuracao-projeto.md) · [Atendimento passo a passo](references/conducao-guiada.md)

A skill pode orientar no Codex e Claude Code quando instalados e com as ferramentas necessárias. Claude em conversa web comum não adquire acesso ao computador por receber esse texto; conexão por outro ambiente depende de suporte próprio. Compatibilidade AgY não homologada. O guia não comprova que uma conta esteja configurada nem que um agente tenha acesso atual.
