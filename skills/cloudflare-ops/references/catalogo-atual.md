# Catálogo Cloudflare para negócios · MAVIK.AI

Levantamento documental de 08/10/2026. O [diretório oficial](https://developers.cloudflare.com/directory/) contém 138 entradas nesta consulta: produtos, famílias e guias. Isso não significa 138 funcionalidades gratuitas nem 138 operações homologadas pelo token.

Esta tabela ajuda a escolher o recurso pelo problema. A coluna final indica o primeiro caminho de configuração e validação; antes de aplicar, abrir a documentação vinculada e conferir setup, disponibilidade, limites, permissões e API atuais. A consulta das páginas de visão geral não equivale à leitura integral de todas as subpáginas. Produtos em beta, parceiros ou contrato exigem confirmação de elegibilidade. Nenhum item desta lista concede autorização de contratação.

Para controles usuais de um negócio, ler [configuração e validação](configuracao-recursos.md). Para execução prática, ler [testes e momento](testes-e-momento.md). Não carregar o catálogo inteiro em cada atendimento: selecionar apenas os itens relacionados ao objetivo.

| Recurso e documentação oficial | Quando usar e primeiro caminho de configuração/validação |
|---|---|
| [1.1.1.1](https://developers.cloudflare.com/1.1.1.1/) | Resolução DNS pública nos dispositivos; configurar resolvedor e testar resolução |
| [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) | Restringir painéis e aplicações por identidade; configurar aplicação, política e teste permitido/negado |
| [Account](https://developers.cloudflare.com/fundamentals/account/) | Administrar conta, membros e acesso; revisar papéis e tokens com menor privilégio |
| [Agent Lee](https://developers.cloudflare.com/agent-lee/) | Assistente operacional do painel; conferir beta, acesso e ações propostas antes de executar |
| [Agent Memory](https://developers.cloudflare.com/agent-memory/) | Memória persistente de agentes; depende de acesso à beta privada e integração de dados |
| [Agents](https://developers.cloudflare.com/agents/) | Construir agentes com estado e comunicação; integrar SDK, identidade e persistência |
| [AI](https://developers.cloudflare.com/ai/) | Guia de soluções de IA; selecionar produto conforme inferência, busca ou agentes |
| [AI controls](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/) | Controlar MCP e acesso de IA no Zero Trust; configurar portais e políticas por ferramenta |
| [AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/) | Observar e controlar crawlers de IA; selecionar operadores e conferir regra efetiva |
| [AI Gateway](https://developers.cloudflare.com/ai-gateway/) | Intermediar chamadas de modelos; configurar provedor, autenticação, limites e logs privados |
| [AI Search](https://developers.cloudflare.com/ai-search/) | Busca gerenciada sobre dados; configurar fonte, indexação e testes de relevância/permissões |
| [Analytics](https://developers.cloudflare.com/analytics/) | Analisar uso e proteção; selecionar métricas, escopo e janela disponíveis |
| [API documentation](https://developers.cloudflare.com/api/) | Referência de endpoints; conferir schema, permissões e erros antes do payload |
| [API Shield](https://developers.cloudflare.com/api-shield/) | Proteger APIs; inventariar endpoints e configurar validação/autenticação conforme plano |
| [Argo Smart Routing](https://developers.cloudflare.com/argo-smart-routing/) | Otimizar caminho até a origem; conferir oferta Smart Shield e medir latência antes/depois |
| [Artifacts](https://developers.cloudflare.com/artifacts/) | Armazenar artefatos versionados via Git; configurar repositório, acesso e recuperação de versão |
| [Automatic Platform Optimization](https://developers.cloudflare.com/automatic-platform-optimization/) | Acelerar WordPress; integrar plugin e testar conteúdo público e sessões |
| [Basin](https://developers.cloudflare.com/basin/) | Plataforma de dados; selecionar ingestão, catálogo e consulta conforme arquitetura |
| [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) | Catalogar tabelas Iceberg em R2; definir bucket, catálogo e acesso ao motor de consulta |
| [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) | Ingerir dados em fluxo; configurar entrada, transformação e destino com teste ponta a ponta |
| [Basin SQL](https://developers.cloudflare.com/basin-sql/) | Consultar tabelas Iceberg do catálogo; validar schema, consulta e consumo antes de integrar |
| [Billing](https://developers.cloudflare.com/billing/) | Acompanhar cobrança; revisar assinaturas, consumo e alertas sem contratar automaticamente |
| [Bots](https://developers.cloudflare.com/bots/) | Controlar automação abusiva; escolher modalidade conforme APIs, visitantes e plano |
| [Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) | Isolar navegação empresarial; configurar políticas Gateway e testar sessão isolada |
| [Browser Run](https://developers.cloudflare.com/browser-run/) | Executar navegador remoto; integrar binding/API, limites e isolamento dos dados |
| [BYOIP](https://developers.cloudflare.com/byoip/) | Usar endereços IP próprios; validar elegibilidade, prefixos e procedimento de anúncio |
| [Cache](https://developers.cloudflare.com/cache/) | Reduzir carga de conteúdo público; definir regras, bypass privado e teste de duas sessões |
| [Cache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/) | Persistir cache de origem; conferir Smart Shield, elegibilidade dos objetos e custo |
| [CASB](https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/) | Revisar segurança de SaaS; conectar aplicação com consentimento e analisar achados |
| [Challenges](https://developers.cloudflare.com/cloudflare-challenges/) | Validar visitantes suspeitos; escolher desafio compatível e testar acessibilidade e clientes |
| [China Network](https://developers.cloudflare.com/china-network/) | Entregar serviços na China; conferir contrato, requisitos locais e integração autorizada |
| [Client-side security](https://developers.cloudflare.com/client-side-security/) | Identificar scripts e risco no navegador; inventariar scripts, políticas e alertas |
| [Cloudflare CLI](https://developers.cloudflare.com/cf/) | Administrar recursos pelo terminal; conferir CLI beta, autenticação e suporte do comando |
| [Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/) | Construir plataformas para clientes; selecionar SaaS ou execução de código isolado |
| [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) | Aceitar domínios de clientes; configurar custom hostnames, certificados e origem fallback |
| [Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) | Guia de conceitos e conta; validar onboarding e modelo de acesso |
| [Cloudflare Images](https://developers.cloudflare.com/images/) | Armazenar e transformar imagens; configurar entrega, variantes e acesso privado |
| [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) | Conectar nós privados; instalar cliente nos nós e validar rotas e acesso |
| [Cloudflare Network Firewall](https://developers.cloudflare.com/cloudflare-network-firewall/) | Filtrar tráfego de rede; definir regras por protocolo com validação sem interromper gestão |
| [Cloudflare Observability](https://developers.cloudflare.com/observability/) | Observar aplicações e serviços; instrumentar sinais e selecionar datasets disponíveis |
| [Cloudflare OHTTP Relay](https://developers.cloudflare.com/ohttp-relay/) | Separar identidade e conteúdo de requisições; integrar cliente, relay e gateway OHTTP |
| [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) | Segurança de usuários e redes; definir organização, identidade, dispositivos e políticas |
| [Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) | Conectar locais empresariais; preparar appliance, IPsec e rotas com plano de retorno |
| [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) | Aplicar Zero Trust em dispositivos; distribuir cliente, registrar organização e testar políticas |
| [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) | Publicar origem via conexão de saída; configurar connector, hostname e TLS da origem |
| [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) | Acessar redes privadas; configurar connector, rotas, cliente e políticas Zero Trust |
| [Cloudflare Wallets](https://developers.cloudflare.com/wallets/) | Identidade para pagamentos de agentes; distinguir reserva atual de funcionalidades anunciadas |
| [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) | Interligar filiais e nuvens; projetar túneis, rotas e redundância sob contrato |
| [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/) | Medir visitas e experiência; instalar beacon quando necessário e confirmar eventos |
| [Containers](https://developers.cloudflare.com/containers/) | Executar containers integrados a Workers; preparar imagem, binding e testes de ciclo de vida |
| [D1](https://developers.cloudflare.com/d1/) | Banco SQL com semântica SQLite; criar schema/migrações e validar recuperação e limites |
| [Data Localization Suite](https://developers.cloudflare.com/data-localization/) | Controlar locais de inspeção e dados; mapear requisito e configurar componentes contratados |
| [Data Loss Prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/) | Detectar dados sensíveis; escolher perfis e integrar inspeção com testes de falso positivo |
| [DDoS Protection](https://developers.cloudflare.com/ddos-protection/) | Mitigar ataques distribuídos; usar tráfego elegível e revisar eventos/overrides disponíveis |
| [Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/) | Diagnosticar experiência dos dispositivos; configurar cliente e testes de conectividade |
| [DMARC Management](https://developers.cloudflare.com/dmarc-management/) | Analisar autenticação de e-mail; revisar SPF/DKIM e relatórios antes de endurecer DMARC |
| [DNS](https://developers.cloudflare.com/dns/) | Gerenciar registros do domínio; preservar e-mail e validar NS, registros, proxy e DNSSEC |
| [DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/) | Proteger nameservers próprios; configurar servidores upstream e política de cache sob contrato |
| [Durable Objects](https://developers.cloudflare.com/durable-objects/) | Coordenar estado por objeto; definir classes/bindings e testar persistência e concorrência |
| [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) | Executar código criado em runtime; definir isolamento, bindings e acesso permitido |
| [Email security](https://developers.cloudflare.com/cloudflare-one/email-security/) | Proteger caixas de e-mail; integrar provedor e validar phishing/falsos positivos |
| [Email Service](https://developers.cloudflare.com/email-service/) | Enviar ou rotear e-mail; separar envio beta de roteamento e validar domínio/destinatários |
| [Flagship](https://developers.cloudflare.com/flagship/) | Controlar funcionalidades sem redeploy; criar flags e testar segmentação e fallback |
| [Fraud Detection](https://developers.cloudflare.com/bots/additional-configurations/sequence-rules/) | Detectar sequências suspeitas; cadastrar endpoints e regras conforme assinatura |
| [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) | Filtrar saída dos usuários; configurar DNS/rede/HTTP e testar sites permitidos e bloqueados |
| [Geo Key Manager](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/) | Restringir localização de chaves TLS; conferir certificado elegível e configurar pela API |
| [Google tag gateway for advertisers](https://developers.cloudflare.com/google-tag-gateway/) | Servir tags Google pelo domínio; validar medição, consentimento e integração |
| [GraphQL Analytics API](https://developers.cloudflare.com/analytics/graphql-api/) | Consultar métricas programaticamente; escolher dataset/período e validar resultado |
| [Health Checks](https://developers.cloudflare.com/health-checks/) | Verificar origem e avisar falhas; configurar endpoint, critérios e destino de alerta |
| [Hyperdrive](https://developers.cloudflare.com/hyperdrive/) | Conectar Workers a banco externo; configurar credencial privada e testar acesso/pooling |
| [Internal DNS](https://developers.cloudflare.com/dns/internal-dns/) | Resolver nomes privados; criar zonas/views e políticas Gateway conforme plano |
| [K2](https://developers.cloudflare.com/k2/) | Manter log durável de eventos; configurar produtor/consumidor e retenção na beta paga |
| [Key Transparency Auditor](https://developers.cloudflare.com/key-transparency/) | Auditar transparência de chaves E2EE; verificar protocolo e evidência do log |
| [Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/) | Manter chave TLS sob controle externo; preparar servidor de chaves e conectividade |
| [KV](https://developers.cloudflare.com/kv/) | Armazenar valores distribuídos; configurar namespace e considerar consistência eventual |
| [Leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/) | Detectar credenciais vazadas em login; configurar campos e resposta da aplicação |
| [Learning Paths](https://developers.cloudflare.com/learning-paths/) | Aprender fluxos por objetivo; seguir trilha correspondente sem tratar guia como produto |
| [Load Balancing](https://developers.cloudflare.com/load-balancing/) | Distribuir tráfego entre origens; criar pools/monitores e testar falha e recuperação |
| [Log Explorer](https://developers.cloudflare.com/log-explorer/) | Consultar logs armazenados; configurar dataset, retenção e consultas conforme custo |
| [Logs](https://developers.cloudflare.com/logs/) | Coletar/exportar eventos; selecionar campos, destino, retenção e proteção de dados |
| [Magic Transit](https://developers.cloudflare.com/magic-transit/) | Proteger infraestrutura IP; preparar prefixos, túneis e roteamento sob contrato |
| [Monetization Gateway](https://developers.cloudflare.com/monetization-gateway/) | Cobrar por acesso de agentes; beta fechada, elegibilidade regional e autorização financeira |
| [MoQ](https://developers.cloudflare.com/moq/) | Entregar mídia por QUIC; conferir versão do protocolo e interoperabilidade do cliente |
| [Multi-Cloud Networking](https://developers.cloudflare.com/multi-cloud-networking/) | Conectar redes de nuvens; configurar contas, rotas e acessos com plano de retorno |
| [Network](https://developers.cloudflare.com/network/) | Entender conectividade da rede; selecionar portas, protocolos e produto adequado |
| [Network Error Logging](https://developers.cloudflare.com/network-error-logging/) | Investigar falhas percebidas pelo navegador; conferir suporte e coletor de relatórios |
| [Network Flow](https://developers.cloudflare.com/network-flow/) | Analisar fluxos de roteadores; integrar exportação de flow e validar alertas |
| [Network Interconnect](https://developers.cloudflare.com/network-interconnect/) | Conexão direta à rede Cloudflare; contratar conexão e configurar rotas redundantes |
| [Network visibility](https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/) | Guia de visibilidade de rede; escolher sinais e ferramentas conforme incidente |
| [Notifications](https://developers.cloudflare.com/notifications/) | Receber alertas úteis; definir condição, destino e responsável e testar entrega |
| [OAuth documentation](https://developers.cloudflare.com/fundamentals/oauth/) | Autorizar integração sem token longo compartilhado; implementar consentimento e escopos |
| [Pages](https://developers.cloudflare.com/pages/) | Hospedar aplicações/sites; configurar build, deploy, env privado e domínio de teste |
| [Posture checks](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/) | Exigir dispositivo saudável; integrar sinal e testar política com dispositivo conforme/não conforme |
| [Privacy Pass](https://developers.cloudflare.com/privacy-pass/) | Provar atributos com privacidade; integrar protocolo e validar tokens conforme caso de uso |
| [Privacy Proxy](https://developers.cloudflare.com/privacy-proxy/) | Proxy privado de saída; integrar autenticação/protocolo conforme contrato |
| [Public to private](https://developers.cloudflare.com/dns/private-origins/) | Publicar hostname para origem privada; configurar conectividade e DNS conforme produto Enterprise |
| [Pulumi](https://developers.cloudflare.com/pulumi/) | Gerenciar infraestrutura em código; importar estado, revisar preview e proteger credenciais |
| [Queues](https://developers.cloudflare.com/queues/) | Processar trabalho assíncrono; definir produtores, consumidores, retries e fila de falhas |
| [R2](https://developers.cloudflare.com/r2/) | Armazenar arquivos/backups; criar bucket privado e credencial restrita e testar restauração |
| [Radar](https://developers.cloudflare.com/radar/) | Pesquisar tendências da Internet; consultar API e respeitar licença dos dados |
| [Randomness Beacon](https://developers.cloudflare.com/randomness-beacon/) | Obter aleatoriedade pública verificável; validar assinatura e uso apropriado ao protocolo |
| [Rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/) | Conter abuso de rotas; definir contagem/período e testar recuperação e NAT |
| [Realtime](https://developers.cloudflare.com/realtime/) | Construir comunicação ao vivo; selecionar SFU, TURN ou SDK e validar rede/identidade |
| [Realtime SFU](https://developers.cloudflare.com/realtime/sfu/) | Distribuir mídia WebRTC; controlar publicação/assinatura e testar múltiplos participantes |
| [RealtimeKit](https://developers.cloudflare.com/realtime/realtimekit/) | Integrar experiência de chamadas; configurar SDK, participantes e permissões no backend |
| [Reference Architecture](https://developers.cloudflare.com/reference-architecture/) | Consultar arquiteturas de solução; adaptar dependências ao objetivo do negócio |
| [Registrar](https://developers.cloudflare.com/registrar/) | Registrar/renovar domínio; conferir TLD, DNSSEC, renovação e autorização de gasto |
| [Resource Tagging](https://developers.cloudflare.com/resource-tagging/) | Organizar recursos por projeto; definir tags e conferir tipos suportados |
| [Rules](https://developers.cloudflare.com/rules/) | Alterar comportamento na borda; escolher fase e expressão e validar ordem com Trace |
| [Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/) | Implantar conjuntos de regras; conferir fase, schema, ordem e compatibilidade do plano |
| [Sandboxes](https://developers.cloudflare.com/sandbox/) | Executar código não confiável; configurar isolamento, APIs permitidas e limites no plano pago |
| [Secrets Store](https://developers.cloudflare.com/secrets-store/) | Centralizar segredos; conferir beta, integração suportada e binding sem expor valores |
| [Security Center](https://developers.cloudflare.com/security-center/) | Inventariar superfície e achados; revisar ativos e priorizar recomendações verificáveis |
| [Smart Shield](https://developers.cloudflare.com/smart-shield/) | Reduzir pressão sobre origem; avaliar componentes, assinatura e métricas de efeito |
| [Spectrum](https://developers.cloudflare.com/spectrum/) | Proteger TCP/UDP; conferir protocolo/plano e configurar aplicação com teste de conexão |
| [Speed](https://developers.cloudflare.com/speed/) | Medir desempenho e localizar gargalos; usar medições sintéticas e reais antes de ajustar |
| [SSL/TLS](https://developers.cloudflare.com/ssl/) | Criptografar borda e origem; preparar certificado da origem e validar Full strict/HTTPS |
| [Stream](https://developers.cloudflare.com/stream/) | Hospedar vídeo ao vivo ou gravado; configurar ingestão, playback e acesso protegido |
| [Support](https://developers.cloudflare.com/support/) | Resolver incidentes com suporte; reunir IDs/horários sem segredos e verificar canal/plano |
| [Tenant](https://developers.cloudflare.com/tenant/) | Provisionar contas de clientes parceiros; conferir elegibilidade e API de provisioning |
| [Terraform](https://developers.cloudflare.com/terraform/) | Gerenciar infraestrutura declarativa; importar estado, revisar plan e evitar sobrescrever recursos |
| [Time Services](https://developers.cloudflare.com/time-services/) | Sincronizar relógios; configurar NTP/NTS e validar fonte e desvio |
| [TURN Service](https://developers.cloudflare.com/realtime/turn/) | Conectar WebRTC atrás de NAT/firewall; emitir credenciais e testar relay real |
| [Turnstile](https://developers.cloudflare.com/turnstile/) | Proteger formulários; integrar widget e Siteverify obrigatório no backend |
| [Vectorize](https://developers.cloudflare.com/vectorize/) | Busca vetorial; definir modelo/dimensões, indexar e testar relevância e isolamento |
| [Version Management](https://developers.cloudflare.com/version-management/) | Testar versões de configuração de zona; conferir Enterprise e validar staging/rollback |
| [WAF](https://developers.cloudflare.com/waf/) | Filtrar ataques web; selecionar rulesets/regras e testar fluxos legítimos e bloqueio controlado |
| [Waiting Room](https://developers.cloudflare.com/waiting-room/) | Ordenar picos de visitantes; definir capacidade/rotas e testar fila conforme plano |
| [WARP Client](https://developers.cloudflare.com/warp-client/) | Conexão privada do usuário consumidor; distinguir cliente pessoal de organização Zero Trust |
| [Web Search API](https://developers.cloudflare.com/web-search/) | Dar busca atual a agentes; conferir beta, autenticação e qualidade das respostas |
| [Web3](https://developers.cloudflare.com/web3/) | Acessar redes distribuídas; configurar gateway compatível e avaliar dependências/custo |
| [Workers](https://developers.cloudflare.com/workers/) | Executar código e servir aplicações; configurar projeto, bindings e deploy em homologação |
| [Workers AI](https://developers.cloudflare.com/workers-ai/) | Executar modelos; escolher modelo, autenticação, orçamento e testes de resposta |
| [Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) | Registrar métricas próprias; definir datapoints e consultas SQL com privacidade |
| [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/) | Executar código de clientes isoladamente; definir dispatch, limites e bindings por cliente |
| [Workers VPC](https://developers.cloudflare.com/workers-vpc/) | Conectar Workers a serviços privados; configurar serviço/binding e testar rede e autorização |
| [Workflows](https://developers.cloudflare.com/workflows/) | Executar processos duráveis; definir etapas idempotentes, retries e teste de retomada |
| [Zaraz](https://developers.cloudflare.com/zaraz/) | Gerenciar ferramentas de terceiros na borda; configurar consentimento e validar eventos/duplicação |
