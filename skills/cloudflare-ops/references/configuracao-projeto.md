# Cloudflare · Configuração por projeto

## Resultado esperado

Configurar e validar os controles pertinentes ao produto, usando o plano e o escopo autorizados. “Completo” significa cobertura explícita do projeto, não habilitar todos os produtos Cloudflare. Use relatório de controle disponível, aplicado, testado, não aplicável e pendente. Não afirme ter lido toda a documentação: cite páginas consultadas e limites do levantamento.

## 1. Acesso e necessidade

Confira conexão, conta, zona e tipo de token sem revelar segredos. Identifique endpoints alcançáveis por leituras mínimas. Antes de qualquer escrita, registre o que o usuário autorizou; inventarie configuração existente, dependências e meios de retorno. Liste permissões faltantes por operação sem pedir acesso total.

Identifique domínio/registrador, origem, stack, público/regiões, rotas humanas e chamadas de máquinas. Use arquivos/configuração antes de perguntar. Separe site público, painel administrativo, API, webhook de pagamento/WhatsApp, streaming, e-mail e armazenamento. Verifique plano e recursos realmente disponíveis.

## 2. Domínio sem Cloudflare ou ainda pendente

Se não houver conta/acesso, guie login/criação de conta e acesso pelo painel, sem contratar produtos. Adicionar zona não migra automaticamente o site nem o e-mail. Primeiro preserve e revise registros atuais: A/AAAA/CNAME e também MX/TXT, SPF/DKIM/DMARC, verificações e serviços terceiros. Scan automático pode ser incompleto.

Prepare nameservers atribuídos à zona e instrução específica do registrador. Troca de nameservers é mudança de produção; token Cloudflare não dá acesso ao registrador. Preserve configuração anterior e revise DNSSEC/DS antes da mudança para evitar falha de resolução. Não mande remover registro DS cegamente. Respeite autorização e conduza a ação manual um passo por vez.

Valide delegação autoritativa, estado da zona, resolvers públicos e hostname real; um cache local resolvendo não prova propagação completa. Diferencie propagação DNS, emissão de certificado e disponibilidade da aplicação. Consulta pending exige retorno posterior ou espera limitada; nunca prometa prazo exato nem repita consultas indefinidamente.

Fontes: [onboarding do domínio](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/), [nameservers e DNSSEC](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/), [proxy por serviço](https://developers.cloudflare.com/dns/proxy-status/use-cases/).

## 3. Base de DNS, TLS e proteção

| Controle | Escolha por projeto | Validação antes de concluir |
|---|---|---|
| DNS/proxy | Proxy somente onde protocolo/porta/serviço suportam; preserve e-mail e verificações de terceiros | Resolução, hostname, resposta pública e integridade dos serviços existentes |
| TLS | Prefira Full (strict) quando origem tem certificado adequado; prepare origem antes de mudar | Cadeia/hostname/validade, HTTPS de ponta a ponta e ausência de loop; certificado de origem não é necessariamente confiável para navegador direto |
| Redirecionamento HTTPS | Aplicar conforme aplicação e callbacks; HSTS só após verificar todos os hosts e reversibilidade | Login, cookies, links, callbacks e HTTP→HTTPS; não habilitar preload por padrão |
| WAF gratuito | Confira o Free Managed Ruleset, normalmente implantado por padrão no Free, e regras customizadas possíveis no plano; preserve regras atuais. Não confundir com rulesets completos de planos superiores | Controles efetivos, capacidade do plano e falsos positivos em fluxos legítimos |
| Anti-bot | Avalie Bot Fight Mode para tráfego do projeto; não ligar por padrão em SaaS/API com máquinas | Integrações, callbacks, automações e fluxos humanos continuam funcionando; WAF Skip/Allow e Page Rules não excepcionam Bot Fight Mode por rota; não prometer bypass `/api/*` |

Proxy/WAF não substituem controles do backend nem impedem bypass direto de origem exposta. Alterar firewall/Tunnel/Access é etapa de origem e identidade com acesso alternativo e escopo autorizados; não bloquear servidor apenas por possuir token Cloudflare.

Fontes: [WAF inicial](https://developers.cloudflare.com/waf/get-started/), [compatibilidade de desafios](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/), [TLS strict](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/), [WAF](https://developers.cloudflare.com/waf/), [Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/), [Bots Free](https://developers.cloudflare.com/bots/plans/free/).

## 4. Controles conforme produto

- **Site/landing:** cache só de conteúdo realmente público; forms humanos podem usar Turnstile. Examine e-mail, widgets e integrações antes de desafios. Cache não prova site mais rápido; meça antes/depois quando houver acesso.
- **SaaS/API:** bypass para dados autenticados e entre tenants; preserve webhooks/callbacks e SSE/WebSocket. Não aplicar desafio humano a máquina nem Cache Everything global. Challenge Page retorna HTML e pode quebrar fetch esperando JSON; não tratar pre-clearance humano como solução para webhooks.
- **Login/reset/formulário:** regras e rate limits conforme campos/limites do plano, com tráfego real esperado; backend continua responsável por usuário/tenant e custo. Nunca inventar bot score de plano não contratado.
- **Turnstile:** criação do widget não conclui proteção; integrar site e validar token no servidor com hostname/action conforme caso. Se aplicação precisa mudar, prepare essa entrega no rito do projeto, sem anunciar concluído após salvar no painel.
- **Backup/uploads R2:** produto separado de DNS/WAF, com bucket privado, orçamento, credencial de runtime restrita e evidência de recuperação para backups. Não habilitar armazenamento cobrado para “completar” um site que não precisa dele.

[Validação Turnstile](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/) e [cache por projeto](performance.md) orientam esses controles.

## 5. Aplicar e comprovar

Prepare diff limitado ao alvo, benefício, impactos, custo e retorno. Se a configuração de produção estiver autorizada, execute por API/ferramenta disponível usando escopo mínimo, uma alteração ou grupo dependente por vez; não peça novo OK para cada ação já coberta. Se não estiver, conclua a proposta verificável antes de solicitar aprovação. Não use escrita experimental como teste de permissão.

Releia estado salvo e teste fluxo público, login, API/webhook e e-mail pertinentes sem dados privados, mensagens comerciais ou pagamentos. Não provoque ataque. Contraste aplicação de configuração com fluxo homologado. Testes que exigem credencial, provedor ou efeitos não autorizados ficam como pendência, não como sucesso.

Entregue registro por controle: requisito → configuração anterior → mudança → fonte → evidência → retorno. Documentação no projeto sem segredos; bloqueios com uma próxima ação concreta. Sem API executora, conduza o painel e registre somente o que foi confirmado, sem chamar instrução de configuração aplicada.
