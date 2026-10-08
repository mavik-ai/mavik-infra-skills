---
name: coolify-ops
description: Auditar projetos Docker/Coolify após deploy e operar backup, segurança, saúde, Sentinel e alertas. Use ao publicar, revisar infraestrutura ou investigar incidentes em Coolify.
---

# Operação do Coolify

## Pós-deploy e cuidado dos projetos

Ao concluir deploy Coolify conduzido pelo agente, ou quando solicitado revisar um recurso, execute a auditoria antes de encerrar a entrega. Não transforme deploy saudável em aprovação de segurança. Leia [checklist pós-deploy](references/post-deploy.md); para integrar a chamada a pipeline ou monitoramento, leia [hook e alertas](references/hooks.md).

Reutilize token autorizado no env privado; peça apenas credencial ausente/inválida por arquivo privado ou pela interface do Coolify. Nunca solicite segredo na conversa. Se o usuário rotacionou token Telegram, não reutilize a cópia antiga nem substitua a configuração por ela. Valide a credencial atual no local em que foi salva.

Helper somente leitura:

```bash
python3 scripts/audit.py --url https://SEU-COOLIFY --env-file /caminho/privado/.env
```

Use caminho absoluto para o script da skill instalada. `--resource UUID` filtra aplicações/serviços/bancos; inventário de servidores, projetos e destinos S3 permanece visível; `--ssh ALIAS` consulta a API interna por SSH previamente validado quando necessário. O helper inventaria campos permitidos da API; os controles não observáveis exigem investigação adicional do checklist. Relatório parcial, sem recurso encontrado ou sem permissões nunca significa aprovação. Não imprime token, env, chaves, chat ID ou respostas brutas.

Monte tabela com status, evidência, motivo, responsável e ação. Priorize recuperação e exposição; informe impacto nos demais projetos do mesmo host. Acione Arquiteto, DevOps/SRE, DBA/Backend, QA ou Segurança somente para subtarefa delimitada; respeite limites de subagentes e rito do projeto. Auditoria é leitura; correções seguem autorização aplicável e são revalidadas depois. Não simule ataques, quedas ou exclusões para testar sem escopo aprovado.

## Identificar a instalação

Leia o inventário atual do projeto/servidor antes de usar IP, alias SSH, porta ou UUID. Use somente o inventário e o acesso autorizados para a instalação escolhida; nunca adote um alvo de exemplo como padrão.

Confirme versão, containers, equipe, usuário e recursos reais. Preserve os aplicativos existentes. Registre resultados na documentação operacional do projeto, sem segredos. Não considere backup do painel como backup dos bancos e volumes dos aplicativos.

Use credenciais já autorizadas em arquivo privado, sem imprimir valores ou executar `.env` como shell. Prefira túnel SSH para a API administrativa quando disponível. Tokens root podem devolver segredos: filtre respostas por campos necessários. Confira documentação oficial e rotas da versão instalada antes de escrever.

## Backup e recuperação

1. Capture dump consistente do banco interno usando ferramenta do engine e preserve a APP_KEY correspondente, source/.env, chaves SSH do Coolify e configurações próprias de proxy, rede e Compose. Evite copiar diretórios de banco em escrita como única cópia.
2. Guarde os arquivos em diretório privado (700, arquivos 600), fora do VPS, com checksum. O pacote contém credenciais e certificados: defina proteção/criptografia antes de enviá-lo a armazenamento externo. Não registre conteúdo no Git.
3. Configure agenda, fuso, retenção e alerta de ausência pelos recursos suportados. Confirme execução e arquivo; toggle enabled não comprova sucesso. Backup do banco não inclui automaticamente arquivos e volumes. Zero nos limites de retenção pode significar ilimitado.
4. Para S3/R2, identifique bucket, endpoint, região e credencial restrita autorizados. Descubra a rota `/s3-storages`; não suponha `/s3`. Validação do destino não prova upload de backup. Confirme escrita, leitura e objeto real. Não crie recursos com custo sem autorização.
5. Ensaie restore isolado, sem jobs/deploys/notificações e sem substituir dados ativos. Verifique tabelas e compatibilidade da APP_KEY; diferencie restore do banco de boot completo do painel em outra VPS.

Se a API de backups retornar erro, Use a interface Settings → Backup ou investigue a causa; não repita indefinidamente nem escreva diretamente no banco para contornar o erro. Se fizer dump manual, declare que ele não aparece nas execuções nativas.

## Sentinel e alertas

- Descubra o UUID do servidor. GET/PATCH `/servers/{uuid}/sentinel` permite configurar `is_metrics_enabled`, `sentinel_metrics_refresh_rate_seconds` e `sentinel_metrics_history_days`. Alteração pode reiniciar o Sentinel. Confirme saúde e novas amostras; configuração habilitada não comprova coleta. Retenção de 7 dias e intervalo de 30 segundos são ponto inicial ajustável.
- Para Telegram, use GET/PATCH `/notifications/telegram` da equipe correta. Selecione falhas de backup/deploy/tarefa/cleanup, limite de reinícios, disco, indisponibilidade/recuperação e mudanças de status conforme pedido. Métricas internas não implicam alertas de limiar CPU/RAM.
- Solicite token por arquivo privado local e chat de destino autorizado; nunca peça para colar token em conversa. Pode preparar eventos antes das credenciais, mantendo o canal desativado. Com credenciais, valide o bot e o chat, habilite o canal e confirme entrega de teste. Não presuma o primeiro chat de getUpdates como destino.
- Um monitor externo é necessário para detectar perda do próprio host; o Coolify indisponível não consegue emitir seus próprios alertas. Só configure serviço externo dentro da autorização existente.

## Segurança sem perder acesso

Verifique HTTPS, cadastro fechado, permissões de equipe/token, 2FA, SSH por chave e updates de segurança. Ativar 2FA exige autenticador e recuperação do dono. Não restrinja API por IP sem identificar o endereço observado e preservar acesso alternativo.

Docker pode expor portas apesar do UFW. Confira binds e filtros de forwarding nas duas famílias IP, usando conectividade positiva como controle do teste externo. Timeout em todas as portas de IPv6 é inconclusivo. Preserve chains existentes; não aplique flush global. Verifique a arquitetura realtime da versão instalada antes de copiar overrides antigos.

Preserve volumes e imagens necessárias para rollback em cleanup. Backup, update e cleanup devem ter fuso e janelas explicitamente verificados. Não declare rollback completo somente pela disponibilidade de imagem antiga.

Para configuração de e-mail/Resend, escolha de destino externo e defesa contra abuso/DDoS, leia [operação complementar](references/operations.md).

## Resultado

Relate separadamente configuração aplicada, coleta/execução comprovada, cópia externa, restauração e entrega de alerta. Finalize com OK apenas do escopo comprovado e uma próxima ação concreta para cada dependência real.

Documentação oficial: [backup](https://coolify.io/docs/core/backup-and-recovery/instance-backup), [restore](https://coolify.io/docs/core/backup-and-recovery/instance-restore), [segurança](https://coolify.io/docs/core/security-model), [Sentinel API](https://coolify.io/docs/api/endpoints/servers/update-server-sentinel), [Telegram API](https://coolify.io/docs/api/endpoints/notifications/update-current-team-telegram-notifications).
