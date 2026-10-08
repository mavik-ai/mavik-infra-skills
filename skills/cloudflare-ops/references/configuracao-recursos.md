# Configuração de recursos para negócios · MAVIK.AI

Referência pesquisada em 08/10/2026. Disponibilidade anunciada não comprova configuração na conta. Confirmar plano e endpoint antes de aplicar. Para itens além deste guia, selecionar a entrada no [catálogo](catalogo-atual.md) e consultar o setup específico; não improvisar payloads de produtos novos.

## Antes de configurar

1. Identificar objetivo, conta, zona, plano e ambiente; inventariar domínio, origem, e-mail e rotas.
2. Verificar acesso de leitura e permissões por endpoint. Token ativo não comprova escrita; token R2 não deve ser tratado como acesso geral.
3. Separar páginas públicas, login, dados privados, APIs, webhooks, uploads e streaming.
4. Preparar proposta por controle: benefício, alvo, diff, custo, teste, rollback e responsável.
5. Aplicar apenas o escopo autorizado; testar tráfego legítimo e proteção pretendida e registrar evidências sem segredos.

Começar pela base aplicável: DNS/proxy e origem HTTPS, proteção por rota, cache público, observabilidade. Produtos de banco, IA, vídeo e redes corporativas entram quando resolvem uma necessidade concreta. Não ativar o catálogo em massa.

## Domínio, origem e identidade

| Controle | Quando e como configurar | Como validar e limites |
|---|---|---|
| DNS/proxy | Zona ativa; A/AAAA/CNAME elegíveis em proxy para HTTP/HTTPS. Preservar MX, SPF, DKIM, verificações e registros do provedor de e-mail. Revisar AAAA e DNS-only que revelem a origem. | Consultar NS/A/AAAA, testar todos os hosts e certificado. Proxy comum não protege qualquer porta/protocolo. [Limites](https://developers.cloudflare.com/dns/proxy-status/limitations/). |
| DNSSEC | Ativar assinatura e publicar DS no registrador. Em migração comum, retirar DS antigo e esperar TTL antes da troca de NS; depois publicar novo DS. | Verificar cadeia DS/DNSKEY e ausência de SERVFAIL. Desativação exige coordenar DS e assinatura, respeitando TTL. [Procedimento](https://developers.cloudflare.com/dns/dnssec/). |
| Full (strict), HTTPS, TLS | Preparar HTTPS válido na origem, com hostname correspondente; então strict e redirecionamento HTTPS. Propor TLS mínimo 1.2 conforme clientes reais, TLS 1.3 quando suportado. | Validar origem, HTTP→HTTPS, login e callbacks; investigar 526 e loops. TLS mínimo por hostname depende de produto/plano específico. [Strict](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/). |
| HSTS | Só após HTTPS estável em todos os hosts afetados. Definir max-age; includeSubDomains e preload exigem inventário e decisão específica. | Conferir header e navegador. Desativar no painel não remove política já armazenada; manter HTTPS durante max-age. [HSTS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/http-strict-transport-security/). |
| Proteção da origem / AOP | Restringir acesso direto e exigir certificado cliente quando aplicável. Preparar servidor antes de habilitar AOP; certificado global identifica rede Cloudflare, não exclusivamente uma conta. | Borda deve funcionar e acesso direto indevido deve falhar. AOP não atua em hostnames servidos por Tunnel. Depende de servidor/firewall além do token. [AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/). |

Para gestão empresarial, revisar membros, MFA e papéis no painel; não presumir que um token pode configurar todas as preferências pessoais de segurança. Token geral deve ter escopos por módulo e expiração apropriada. Não usar Global API Key como padrão. [Tokens de conta](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/).

## Ataques, bots e IA

| Controle | Quando e como configurar | Como validar e limites |
|---|---|---|
| DDoS | Proteção automática para tráfego elegível pela Cloudflare; revisar eventos e overrides disponíveis. | Conferir exposição da origem e tráfego pela borda. Não realizar ataque para testar. [DDoS](https://developers.cloudflare.com/ddos-protection/). |
| WAF custom rules | Expressões estreitas por host, rota, método e sinais. Revisar ordem; Skip somente no controle necessário. | Trace, eventos e teste legítimo/bloqueio controlado. Free: 5 regras; regex Business+. Não aplicar allowlist ampla que ignore outras proteções. [Custom rules](https://developers.cloudflare.com/waf/custom-rules/). |
| Managed Rules | Habilitar rulesets permitidos; tratar falso positivo por regra/rota, testando uploads e payloads legítimos. | Free Managed Ruleset no Free; Managed e OWASP a partir de Pro. Body inspecionado tem limite; não substitui validação do backend. [Managed Rules](https://developers.cloudflare.com/waf/managed-rules/). |
| Rate limiting | Login, recuperação e rotas caras: escolher contagem, período e ação com baseline. APIs precisam resposta compatível. | Teste pequeno autorizado, NAT e recuperação; Free tem 1 regra. Atraso/contadores distribuídos impedem quota financeira exata. [Rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/). |
| BFM / SBFM / Bot Management | Escolher conforme visitantes e automação legítima. BFM pode desafiar webhooks/APIs; SBFM permite exceções delimitadas. | Testar browser, API, webhook e monitor. BFM não aceita Skip de custom rules; não recomendar habilitação indiscriminada. [BFM](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/). |
| Turnstile | Widget no front, Siteverify obrigatório no backend; verificar success, hostname e action; segredo privado. | Testar ausência, replay, expiração e falha de rede. Tokens duram 300 segundos e são de uso único. Dummy keys validam fluxo de teste, não integração real. [Backend](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/). |
| Políticas de bots IA | Escolher separadamente Search, Agent e Training conforme descoberta, acesso e uso de conteúdo; revisar Allow/Block e política de páginas com anúncios. | Conferir política efetiva e eventos. Allow não ignora os demais controles; bloquear pode reduzir descoberta/referrals. Defaults recentes não comprovam estado de zonas antigas. [Políticas](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/). |
| AI Crawl Control | Observar operadores em domínio proxied antes de bloquear; revisar regra WAF gerada e interação com Skip. | Free tem sinais/janela limitados; erro de request não significa bloqueio pela política IA. User-Agent falsificado não prova classificação de bot real. [Início](https://developers.cloudflare.com/ai-crawl-control/get-started/). |
| Managed robots.txt | Conferir arquivo existente, sitemap e preferências search/ai-input/ai-train antes de gerenciar diretivas. | Buscar robots.txt entregue. Instrução para crawler cooperativo não é barreira técnica. [robots.txt](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/). |
| AI Labyrinth | Conteúdo HTML onde rastreamento de links honeypot seja pertinente. | Observar Served/Crawls; não bloqueia nem desafia. Links antigos podem gerar eventos depois da desativação. [Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/). |

Bloqueio de bots de IA e uso de IA no negócio são objetivos diferentes: Workers AI, AI Gateway, AI Search, Vectorize e Agents exigem aplicação, autenticação e limites próprios. Não são melhorias automáticas de segurança do domínio.

## Desempenho e regras

| Recurso | Configuração por necessidade | Validação |
|---|---|---|
| Cache Rules / Response Rules | Assets e conteúdo compartilhável; bypass de sessão/dados privados. Revisar Authorization, cookies, query e key. Nunca forçar cache autenticado por padrão. | Duas sessões/tenants e anônimo; body, cookies, CF-Cache-Status/Age e purge. Regras conflitantes e Workers podem alterar resultado. Response Rules podem remover Set-Cookie. [Cache](https://developers.cloudflare.com/cache/how-to/cache-rules/), [comportamento](https://developers.cloudflare.com/cache/concepts/cache-behavior/). |
| Redirects / Bulk Redirects | Migração de URL, canonicalização e catálogo grande de destinos. Preservar paths/query de acordo com objetivo. | Status, destino final, ausência de loops e métodos pertinentes. |
| Transform / Configuration Rules | Reescrever URL/headers e ajustar configuração por rota. Revisar headers de confiança e aplicação. | Trace e request/response reais; alterações não podem ampliar confiança em headers do cliente. |
| Origin / Compression Rules | Ajustar destino/SNI ou compressão por tráfego elegível e plano. | Conferir origem efetiva, TLS, conteúdo e headers de compressão. |
| Snippets / Cloud Connector / Custom Errors | Código pequeno de borda, destinos cloud ou respostas de erro específicas quando necessário. | Confirmar plano, ordem/fase, limites e comportamento em falha; não ativar sem caso de uso. |

As famílias Rules exigem tráfego proxied; quotas/campos variam por recurso e plano. Conferir referência específica e usar Trace antes de rollout. Page Rules antigas não devem ser copiadas cegamente. [Catálogo de Rules](https://developers.cloudflare.com/rules/).

Medir antes de recomendar APO/Images/Smart Shield/Cache Reserve/Argo: ganho depende de stack e origem, pode exigir assinatura. Streaming e WebSockets exigem validação própria; cache não substitui otimização de banco/aplicação. [Cache](https://developers.cloudflare.com/cache/).

## Operação e integrações

| Recurso | Como configurar corretamente | Evidência exigida |
|---|---|---|
| Access | Aplicação e identidade; Include seleciona, Require restringe e Exclude retira correspondências daquela política. Service Auth para máquinas; Bypass somente quando endpoint público é necessário. | Usuário permitido/negado, expiração e máquina sem credencial. Bypass desliga controle/log Access; não substitui autorização tenant. [Políticas](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/). |
| Tunnel | Instalar cloudflared, configurar hostname/rotas, TLS/SNI/CA e Access conforme exposição desejada; retirar acesso público desnecessário. | Connector conectado e app ponta a ponta são provas distintas. Validar JWT/Protect with Access. noTLSVerify não deve ser solução permanente. [Origem HTTPS](https://developers.cloudflare.com/tunnel/troubleshooting/https-origins/). |
| R2 / backups | Bucket privado, retenção adequada, credencial por bucket e backend de backup compatível com S3. API de gerenciamento usa token; clientes S3 usam Access Key ID/Secret, não copiar Bearer para campo S3. | Gravação/leitura e restauração isolada com checksum e RPO/RTO; listar bucket não prova backup. [Credenciais](https://developers.cloudflare.com/r2/api/tokens/). |
| Alerts / Analytics | Condição, dataset, janela, destino e responsável; validar segredo do webhook no receptor. | Teste entregue e confirmação do destinatário; política existente não prova entrega nem reação. Canais/tipos variam. [Alerts](https://developers.cloudflare.com/notifications/). |
| DMARC / e-mail | Inventariar remetentes, SPF e DKIM; começar pela observação antes de políticas de rejeição. Distinguir roteamento, envio e proteção de caixas. | Autenticação real e relatórios; não sobrescrever DNS do provedor. [DMARC](https://developers.cloudflare.com/dmarc-management/). |

Terraform/Pulumi: importar e revisar estado/plan antes de aplicar; proteger estado com dados sensíveis. Workers/Pages/bancos/filas: requerem código, bindings, migrações e testes próprios. Serviços corporativos e betas do catálogo exigem setup específico; a skill identifica o caminho, consulta documentação e declara lacunas, sem prometer capacidade executora universal.

## Critério de encerramento

Registrar por controle: não aplicável, proposta, configurado, validado ou não verificável. Uma resposta 403 não prova ausência do produto; 404 de entrypoint pode indicar regra não implantada. Leitura bem-sucedida não homologa escrita. Nunca declarar “conta totalmente configurada” só porque o token foi verificado.
