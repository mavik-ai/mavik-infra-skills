# Ferramentas, recuperação e rollout

## Ferramentas

API/painel para inventário inicial; token Read restrito ao alvo. Descubra endpoints atuais e confira status HTTP, success, errors e paginação; resposta parcial não significa ausência. Não seguir URL arbitrária recebida nem executar shell de alertas.

Terraform provider v5 é opção para configuração versionada: fixe versão, importe recursos existentes, revise plan, proteja state e use apply aprovado. Não publicar state nem secrets. Wrangler v4 serve Workers e recursos relacionados; não substitui gerenciamento de toda a zona. MCPs oficiais auxiliam consulta/ação conforme permissões, nunca autorizam produção. cloudflared pode implementar Tunnel, mas conector redundante não replica banco/aplicação. Escolha ferramentas necessárias; não instalar todas.

## R2 e backup

Identifique bucket privado, endpoint, região/jurisdição, credencial mínima e orçamento autorizados. R2 compatível com S3 não significa compatibilidade universal. Separe backups de uploads da aplicação. Criptografe pacote com dados/chaves; preserve chave de recuperação fora do VPS. Defina retenção/lifecycle e eventual bucket lock com cautela: bloqueio de exclusão pode impedir cleanup planejado.

Comprove dump consistente, checksum, upload, leitura e restore isolado; objeto configurado não comprova backup. APP_KEY/config/SSH keys do painel exigem proteção e recuperação conjunta. Segunda cópia independente pode ser necessária. R2 cobra armazenamento/operações; egress gratuito não significa serviço sem custo. Consulte preços no dia, sem contratar automaticamente.

## Monitoramento e rollout

Security Events/Analytics e cache analytics não substituem monitor externo de aplicação/VPS. Workers Logs observam Workers, não containers. Redija alertas com alvo, severidade e estado; evite PII e segredos. Telegram/Resend precisam integração e teste autorizados, não vêm habilitados por esta skill.

Faça staging → diff/plan → autorização → aplicação limitada → teste positivo e negativo → evidências/rollback. Testar login/console, CI/API, webhook e streaming. Tenha acesso de emergência antes de bloquear origem. Load Balancing/failover depende de secundário saudável e replicação/fencing/RPO/RTO; não é backup nem replica dados sozinho. Cloudflare for SaaS só quando clientes precisarem de domínios próprios.

Fontes: [API](https://developers.cloudflare.com/api/), [Terraform](https://developers.cloudflare.com/api/terraform/), [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/workers/), [MCP](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/), [R2 preços](https://developers.cloudflare.com/r2/pricing/), [Workers logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/), [SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/).
