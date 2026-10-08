# MAVIK · Coolify Ops

Skill para Codex e Claude Code: auditoria pós-deploy e operação assistida de segurança, backup, recuperação, saúde e alertas em projetos Docker/Coolify.

**Versão 1.0.0 · Licença MIT · Idioma PT-BR.** Projeto independente, sem afiliação oficial ao Coolify.

## O que entrega

- Checklist proporcional: site estático, API, SaaS, banco, arquivos, filas e integrações.
- Inventário somente leitura pela API, opcionalmente por SSH autorizado.
- Orientação operacional de backup externo, restauração, hardening, Sentinel, Telegram e e-mail.
- Relatório com evidências, riscos e próxima ação. Configuração habilitada não significa funcionamento comprovado.

Não instala um daemon, receptor webhook, monitor 24 horas, proteção DDoS ou mecanismo de correção automática. O helper não modifica o Coolify nem envia mensagens. Correções são executadas pelo agente somente dentro da autorização do operador.

## Instalação

Requisitos: Python 3.10+, curl; SSH opcional. Acesso à instância Coolify e token com permissões de leitura suficientes. Sem dependências Python externas.

Este diretório é a skill instalável. Copie-o inteiro para `~/.codex/skills/coolify-ops` ou `~/.claude/skills/coolify-ops`; consulte o README do pacote para instalação por subpasta. Preserve instalação existente antes de substituir. Reinicie a sessão para atualizar a descoberta de skills.

```bash
cp -R skills/coolify-ops ~/.codex/skills/coolify-ops
```

Para instalação reproduzível, use a tag do pacote. Somente esta subpasta forma a skill; não instale a raiz do monorepo como uma skill.

## Uso pelo agente

> Use $coolify-ops para auditar este projeto no Coolify. Identifique a instância e o recurso autorizados, apresente evidências e pendências antes de corrigir.

O agente lê o checklist e usa ferramentas disponíveis (API/SSH/interface). Ele não adquire acesso automaticamente nem herda permissão para publicar, excluir dados, contratar serviços ou enviar mensagens.

## Helper e credenciais

```bash
chmod 600 /caminho/privado/coolify.env
python3 scripts/audit.py --url https://coolify.example.com --env-file /caminho/privado/coolify.env
python3 scripts/audit.py --url https://coolify.example.com --resource UUID --ssh servidor-autorizado
```

O arquivo privado contém `COOLIFY_API_TOKEN=<token>`; alternativamente, use a variável no secret store do runner. Nunca versione o arquivo nem coloque o valor do token em argumentos. O parser lê atribuições literais, não executa shell e não expande variáveis.

`--url` é obrigatório e deve ser uma origem confiável HTTPS (HTTP só em loopback). `--resource` filtra aplicações/serviços/bancos por UUID ou nome exato; servidores, projetos e destinos S3 continuam no relatório. `--ssh` consulta a API interna em `127.0.0.1:8000` pelo alias configurado; confira porta, identidade do host e acesso antes de usar. Não desative a verificação de host.

Código **0**: inventário coletado. Código **2**: falha ou coleta degradada. Nenhum código aprova segurança ou prova restauração/entrega de alertas. O relatório pode conter nomes e IDs de infraestrutura: armazene-o privadamente.

## Documentação

- [Fluxo e autorização](SKILL.md)
- [Checklist de projeto](references/post-deploy.md)
- [Pipeline, webhook e monitoramento](references/hooks.md)
- [Backup, alertas, e-mail e defesa](references/operations.md)
- [Segurança e reporte de falhas](SECURITY.md)
- [Contribuição e validação](CONTRIBUTING.md)
- [Histórico](CHANGELOG.md)

## Compatibilidade e validação

Inventário foi exercitado em Coolify 4.4.2; APIs variam por versão e permissões. Consulte rotas/documentação da versão antes de mutações. Testes locais usam respostas simuladas e não acessam servidor real:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Não há garantia de compatibilidade universal ou auditoria de segurança independente. Não inclua tokens, dumps, IPs privados de clientes ou evidências operacionais em issues.
