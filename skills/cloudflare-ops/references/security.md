# Segurança de borda e origem

## Inventário somente leitura

Confirme IDs, zona/plano/status, DNS e proxy por hostname, TLS, certificados, regras WAF/rate/cache, Access/Tunnel e dependências externas. APIs têm escopos de zona e conta diferentes; evite coletar R2 secrets e tokens. Audite registros DNS-only que revelem origem, e-mail e serviços administrativos. Não faça proxy web em MX.

## Controles e validação

| Controle | Benefício | Validação/risco |
|---|---|---|
| Proxy em HTTP público | Tráfego passa pela borda | Testar DNS, Host/SNI e origem; DNS sozinho não protege IP conhecido |
| Full (strict) | TLS validado até origem | Certificado válido/hostname/renovação; não usar Flexible; HSTS após compatibilidade e rollback |
| Allowlist das redes Cloudflare ou Tunnel | Evitar bypass direto | IPv4/IPv6, ACME, healthcheck, webhooks e acesso de emergência; restringir web sem bloquear SSH cegamente |
| AOP/mTLS | Autenticar borda na origem | Certificado global identifica rede Cloudflare; certificado próprio oferece escopo mais forte |
| Access no painel | Identidade antes da administração | IdP/MFA, deny por padrão, acesso de recuperação; API/CI usam Service Auth/service token e token da aplicação |
| WAF | Mitigar padrões de exploração | Plano e falsos positivos; não excluir todos os webhooks de toda proteção |
| Rate limiting | Conter abuso | Limites IP não são quotas exatas; backend limita usuário/tenant/IA/custo |
| Turnstile | Proteger fluxos humanos | Siteverify no servidor, hostname/action; tokens únicos expiram em 5 minutos; não desafiar chamadas máquina |

Cloudflare Free oferece recursos reduzidos; consulte tabela WAF e campos permitidos antes de compor regra, sem copiar exemplo Enterprise. Desafios de navegador não funcionam em webhooks/API de máquinas. Preserve assinatura, idempotência, timeout e retries no backend. Valide IP cliente somente a partir de proxy confiável; headers diretos podem ser forjados.

Não existe blindagem total. Firewall local/Fail2ban não impedem saturação upstream. HTTP proxy não protege automaticamente SSH, UDP, STUN/TURN ou banco. Avalie provedor para DDoS direto ao IP. Nenhuma medida substitui patches, autorização tenant e backups.

Fontes: [origem](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/), [TLS](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/), [WAF](https://developers.cloudflare.com/waf/), [Turnstile](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/), [service tokens](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).
