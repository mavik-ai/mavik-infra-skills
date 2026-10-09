# MAVIK.AI · Checklist Cloudflare para negócios

Definição solicitada em 08/10/2026. Checklist de cobertura, não autorização para aplicar mudanças. Antes de cada execução, conferir plano, documentação do endpoint, permissões efetivas e objetivo do negócio. Recursos pagos exigem custo e autorização explícitos. “Negócios” não significa contratar o plano Business.

## Como conduzir

Apresente as cinco frentes abaixo e trabalhe uma de cada vez. Inventarie automaticamente o que puder ler; entregue apenas uma ação manual por mensagem, com link e estimativa. Cada controle recebe: aplicável? | benefício | estado observado | plano/custo | permissão | mudança proposta | evidência/teste | rollback | responsável. Estados: não verificado, pendente, não aplicável, aplicado, testado. Nunca marcar cobertura como configuração concluída.

## 1. Conta e acesso

- [ ] Confirmar conta, proprietário, equipe, domínios e ambientes autorizados; revisar membros e menor privilégio.
- [ ] Verificar 2FA, recuperação e acesso alternativo com o proprietário, sem pedir códigos de recuperação ou tratar token como acesso ao perfil.
- [ ] Inventariar tokens, validade, recursos e armazenamento privado; separar administração de credenciais de aplicação.
- [ ] Conferir plano, assinaturas, orçamento e responsável por cobrança; não conceder Billing Edit para configurar DNS.
- [ ] Revisar logs de auditoria disponíveis e preservar configuração anterior sem segredos.

## 2. Domínio, HTTPS e e-mail

- [ ] Identificar registrador, delegação, estado da zona e acesso para trocar nameservers; revisar DNSSEC/DS antes da migração.
- [ ] Conferir A/AAAA/CNAME, subdomínios, IPv6 e proxy conforme serviço; preservar MX/TXT e verificações de terceiros.
- [ ] Validar certificado da origem, Full (strict), HTTPS e redirecionamentos; HSTS só depois de avaliar hosts e reversibilidade.
- [ ] Revisar SPF, DKIM e DMARC com o provedor de envio; não inventar DKIM nem alterar política DMARC sem avaliar remetentes legítimos.
- [ ] Testar resolução, aplicação, login e serviços de e-mail pertinentes; Email Routing é opcional e não substitui envio transacional/SMTP.

## 3. Proteção e acesso ao servidor

- [ ] Conferir proteção DDoS e WAF efetivos no plano, regras gerenciadas e eventos; ajustar regras customizadas sem bloquear tráfego legítimo.
- [ ] Avaliar bots e limites de requisição em login/formulários/APIs; Bot Fight Mode não admite exceção por rota via WAF Skip e pode quebrar webhooks.
- [ ] Avaliar Turnstile nos formulários humanos, com validação no backend; desafio humano não serve a webhooks/máquinas.
- [ ] Avaliar Access para painéis internos, políticas de identidade e service tokens específicos; preservar callbacks e acesso alternativo.
- [ ] Revisar bypass da origem; Tunnel/firewall/certificados exigem intervenção na origem e testes próprios, não apenas token Cloudflare.

## 4. Desempenho e funcionalidades do negócio

- [ ] Medir disponibilidade, latência e cache antes/depois; configurar cache de conteúdo público e bypass de login, carrinho, sessão, API privada e dados entre empresas.
- [ ] Revisar compressão e protocolos disponíveis; validar WebSocket/SSE, uploads e streaming usados pelo produto.
- [ ] Organizar redirects e regras de configuração/transformação apenas conforme rotas reais; testar SEO, campanhas e callbacks.
- [ ] Avaliar Pages/Workers, R2, Images ou Stream somente quando resolvem necessidade concreta, com limites, custos e integração definida.
- [ ] Avaliar recursos específicos como API Shield, Load Balancing, Waiting Room, Zaraz/Web Analytics e Cloudflare for SaaS conforme arquitetura, plano e privacidade; não ativar o catálogo inteiro.

## 5. Operação, dados e comprovação

- [ ] Definir alertas disponíveis por plano, destinatário e responsável; testar entrega autorizada. Configurar canal não comprova monitoramento contínuo.
- [ ] Conferir erros, tráfego e eventos de segurança; definir retenção, privacidade e rotina de revisão conforme ferramentas disponíveis.
- [ ] Se R2 armazenar backups: bucket privado, credencial restrita, agendamento real, retenção e restauração isolada testada; R2 sozinho não faz backup.
- [ ] Para disponibilidade: verificar Health Checks/monitor externo e, quando necessário, failover; produto pago não será contratado automaticamente.
- [ ] Registrar mudanças, testes de negócio, rollback e pendências; saúde da aplicação/servidor exige revisão além da borda Cloudflare.

## Token: base e módulos

Escolha recursos de uma conta e zonas específicas, não “Todas as contas” por padrão. Para diagnóstico, Read; para configuração autorizada, Edit nos grupos necessários. Nomes abaixo são os da documentação oficial; traduções e variantes Write/Cache Settings podem aparecer no painel. Confira a permissão aceita no endpoint antes de prometer cobertura. Um token não garante suporte a todos os produtos.

| Escopo | Grupo de permissão | Uso |
|---|---|---|
| Zona | Zone — Read | Descobrir/verificar a zona; Edit apenas se criar/alterar a própria zona fizer parte do escopo |
| Zona | DNS — Edit | Registros DNS autorizados |
| Zona | Zone Settings — Edit | Configurações gerais pertinentes |
| Zona | SSL and Certificates — Edit | TLS e certificados pertinentes |
| Zona | Zone WAF — Edit | Regras de segurança pertinentes |
| Zona | Cache Rules — Edit | Regras de cache; Cache Purge separado somente se necessário |
| Zona | Analytics — Read | Medições disponíveis |

Essa base é uma proposta para operação da borda, não o mínimo de toda tarefa. Remova grupos não usados. Acrescente módulos somente após escolher os controles:

| Módulo | Permissões a conferir no endpoint/painel |
|---|---|
| Redirects/configuração/headers | Zona: Single Redirect, Config Rules, Transform Rules — Edit conforme regra |
| Turnstile | Conta: Turnstile — Edit; verificar compatibilidade do tipo de token; segredo de validação do widget separado |
| Access/Tunnel | Conta: Access: Apps and Policies, organizações/identidade e Cloudflare Tunnel conforme operação; credencial de conector separada |
| Alertas | Conta: Notifications — Edit; analytics/auditoria somente leitura conforme endpoint |
| R2/Pages/Workers/outros | Permissões específicas do produto escolhido; manter R2 runtime restrito ao bucket e sem administração desnecessária |

Não adicionar gestão de membros/tokens, cobrança ou acesso total por conveniência. 2FA, recuperação, registrador, aplicação e origem podem exigir outro acesso ou ação humana. Prefira token geral de conta para automação durável quando o produto suporta; token de usuário pode ser necessário para produtos incompatíveis. O fluxo específico R2 não equivale a token geral de DNS/TLS/WAF.

## Primeiro passo na tela de criação

Nome sugerido: `mavik-cloudflare-ops`. Não emitir antes de selecionar conta/zonas e grupos pertinentes. Revisar prazo de uso; 30 dias pode servir para configuração inicial, mas é proposta, não regra do fornecedor. Restringir IP somente se o IP de saída do executor for conhecido e estável. Preparar armazenamento privado antes de gerar. Conferir resumo, salvar privadamente e testar somente leitura; nunca escrever para descobrir permissão.

## Fontes e limites

Documentação consultada em 08/10/2026:

- [Permissões](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) e [tokens da conta/compatibilidade](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/).
- [Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/).
- [Alertas por plano](https://developers.cloudflare.com/notifications/notification-available/) e [Health Checks](https://developers.cloudflare.com/health-checks/).
- As referências [configuração por projeto](configuracao-projeto.md), [segurança](security.md), [performance](performance.md) e [operação](operations.md) contêm procedimentos e fontes adicionais.

Checklist definido e fontes consultadas; conta não auditada integralmente, módulos não homologados nesta tarefa. Conferir documentação específica de cada produto quando selecionado, sem alegar leitura integral do catálogo.


## Interpretação dos testes de cobertura

Política com Write comprova concessão declarada, não execução de mudança. Liste política por recurso quando autorizado; nunca faça alteração experimental em produção. Listagem vazia comprova acesso ao endpoint, não produto configurado. HTTP 404 em entrypoint não prova falta de permissão: conferir listagem de rulesets e deployment da fase. HTTP 403 exige diagnóstico, não ampliação automática do token. Audit Logs v2 exigem since/before; usar GraphQL Analytics para métricas em lugar de endpoint REST descontinuado. Matriz de compatibilidade e comportamento observado podem divergir; relatar o endpoint testado e não extrapolar leitura para criação/edição (incluindo Turnstile).


## Proteções gratuitas e crawlers de IA

Conferir controles por zona e disponibilidade efetiva: Free Managed Ruleset, regras customizadas e uma regra de rate limiting conforme limites atuais do Free. Não confundir WAF por zona com rulesets de conta Enterprise. Bots de IA podem ser legítimos; decidir pelo negócio quais comportamentos permitir. A documentação atual separa políticas Search, Agent e Training, com Allow, Block em todas as páginas ou Block nas páginas com anúncios. Bloqueio de Training inclui crawlers mistos Search/Training e pode afetar descoberta; não prometer preservar todos os buscadores. O controle legado Block AI bots está em depreciação desde setembro/2026. Conferir endpoint/API atual e configuração da zona antes de produzir payload; essa política não foi aplicada nem homologada na bateria de leitura. Não prometer bloquear todo scraping ou ataque. Fonte: https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/ e https://developers.cloudflare.com/waf/.
