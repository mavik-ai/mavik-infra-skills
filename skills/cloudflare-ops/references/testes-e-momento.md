# Quando configurar e como validar

## Momento de execução

Auditar no onboarding, antes/depois de deploy que altera domínio, origem, login, API, webhooks ou cache; também após incidente, troca de plano e mudança de estratégia de descoberta por IA. Revisão periódica só existe com agendamento real autorizado. Antes de escrita: alvo e finalidade, acesso/conta, estado anterior, plano, impacto, teste e retorno definidos. Reutilizar autorização existente, sem inferir mudanças de produção de um pedido apenas de auditoria.

| Controle | Quando usar | Pré-requisito para executar | Evidência de conclusão |
|---|---|---|---|
| DNS/proxy | Entrada ou mudança de hostname/origem | Preservar registros e e-mail; origem correta e serviço suportado | Registro salvo, resolução autoritativa e fluxo real |
| TLS strict/HTTPS | Origem com certificado válido, antes de expor serviço | Certificado/hostname/renovação validados; callbacks e acesso alternativo | Configuração relida, TLS até origem e fluxos sem loop |
| WAF/rate limit | Exploração/abuso ou proteção preventiva de rotas reais | Campos/limites do plano e volume legítimo conhecidos | Regra relida, teste limitado de rota isolada e eventos; fluxo legítimo preservado |
| Bot Fight Mode | Site público compatível com desafios | Mapear máquinas/webhooks; não prometer bypass por rota | Navegador e integrações continuam funcionando |
| Políticas IA | Decisão sobre uso do conteúdo por treinamento, busca e agentes | Aceitar efeito sobre crawlers mistos e descoberta; tráfego via borda | Política relida, eventos classificados e testes legítimos; configuração não prova bloqueio de toda IA |
| AI Labyrinth | HTML público com scraping não cooperativo | Conferir comportamento de conteúdo, plano/painel e objetivo | Estado relido e eventos Served/Crawls; eventos não são bloqueios |
| Turnstile | Login/formulário humano sujeito a abuso | Widget + Siteverify no backend; chaves por ambiente | Aceitar válido, rejeitar inválido/expirado/reutilizado; hostname/action e submissão real |
| Cache | Conteúdo público com benefício mensurável | Identificar dados privados/cookies e bypass | HIT/MISS pertinente, dados privados sem cache compartilhado, comparação antes/depois |

## API de bots e IA

Consultar GET /zones/{zone_id}/bot_management. A documentação apresenta PUT no mesmo endpoint para configuração; confirmar campos e semântica vigentes, preservar estado compatível e enviar somente campos graváveis pertinentes. Nunca copiar todos os campos retornados nem payload Enterprise numa zona Free. Campos documentados incluem fight_mode, ai_search, ai_training, ai_user e crawler_protection. Agent no painel corresponde ao campo ai_user; Labyrinth é descrito como crawler_protection. robots.txt gerenciado e sincronização de preferências são controles separados: instrução de crawling não equivale a bloqueio efetivo. Não presumir equivalência entre disallow e block; validar painel, resposta e enforcement conforme documentação atual. Não alterar ai_bots_protection legado por hábito.

Não testar a identidade de um crawler apenas trocando User-Agent: isso não reproduz classificação/verificação do fornecedor. Para regra isolada WAF/rate, use hostname/caminho de homologação e requisições limitadas; para políticas IA de zona inteira, usar zona de homologação e depois rollout autorizado. Evitar PUT no-op em produção como tentativa de permissão.

## Bateria prática

1. **Leitura:** validar token/conta/plano, recursos e políticas; classificar erro de consulta, acesso negado e ausência de recurso separadamente. Política Write não prova execução.
2. **DNS isolado autorizado:** TXT em _mavik-skill-test-{UUID}, conteúdo inofensivo, conferir inexistência, criar → GET → atualizar → GET → remover → listagem vazia. Limpar somente ID/nome/tipo/conteúdo próprios. Falha de transporte após criação pode ter resultado desconhecido: consultar nome exato antes de repetir ou encerrar, sem apagar recursos de terceiros. Não usar registros de produção existentes.
3. **Turnstile de teste:** seguir chaves públicas oficiais e dummy token; testar sucesso, rejeição e timeout-or-duplicate. Chaves de teste nunca em produção. Siteverify isolado não homologa widget/backend da aplicação nem permissão de criação do widget pela conta.
4. **Segurança em homologação:** snapshot, mudança limitada, releitura, tráfego legítimo e caso negativo, evento correspondente, reversão. Requer zona/projeto apropriados; sem eles, registrar não homologado, não aprovar a partir do DNS.
5. **Entrega:** separar concessão, escrita real, estado aplicado e resultado funcional; incluir cleanup/rollback, pendências e atualização do runbook sem segredos. Não publicar relatório de conta num pacote público.

Fontes: [API de bots](https://developers.cloudflare.com/api/resources/bot_management/methods/update/), [políticas IA](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/), [Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/), [Turnstile de teste](https://developers.cloudflare.com/turnstile/troubleshooting/testing/). Revalidar no momento de executar.
