# Cache e desempenho

Defina política por hostname/rota antes de criar Cache Rules. Cloudflare é camada de entrega, não correção de query/backend lento. Meça cenário/região iguais antes/depois: TTFB, LCP, tamanho de assets, taxa de hit e erros. Não invente ganho percentual.

| Conteúdo | Política inicial | Evidência |
|---|---|---|
| Landing pública | Cache apenas se resposta realmente pública | Invalidação no deploy e conteúdo correto |
| Assets com hash | Cache-Control longo/immutable conforme aplicação | Novo deploy não serve bundle antigo incompatível |
| Login/app/API/console | Bypass e no-store para conteúdo privado | Duas sessões/tenants não compartilham resposta |
| Webhook/callback/POST | Sem cache nem challenge humano | Assinatura/retry/idempotência funcionam |
| SSE/WebSocket | Sem cache, reconexão e heartbeat | Streaming por domínio proxied, sem buffering indevido |
| Arquivos privados | URL assinada/permissões por tenant | Expiração, tamanho/tipo e acesso negado sem autorização |

Não usar Cache Everything global; cookie/Authorization e headers da origem precisam análise. Cache de arquivo público não autoriza publicar uploads privados. Verifique precedência de regras e não dependa de Page Rules antigas para novas configurações. Não ligar otimizações de JavaScript automaticamente; testar CSP, consentimento e formulários.

WebSocket suportado exige reconexão após encerramentos. Limites de upload/timeout/portas dependem do plano/produto. Voz WebRTC e TURN requer arquitetura separada; HTTP/SSE não cobre UDP. A aplicação deve respeitar proxy confiável para redirects/cookies/URLs e IP real.

Fontes: [cache](https://developers.cloudflare.com/cache/get-started/), [bypass cookie](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/), [WebSockets](https://developers.cloudflare.com/network/websockets/), [portas](https://developers.cloudflare.com/fundamentals/reference/network-ports/).
