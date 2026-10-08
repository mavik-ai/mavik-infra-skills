# Operação: backup, canais e defesa

## Backup

Separe banco/configuração/chaves do painel de bancos, uploads e volumes de aplicações. Escolha destino externo compatível com S3 em outro domínio de falha; exemplos são S3, R2 e B2. Compare região, custo, retenção, criptografia e compatibilidade antes de escolher. Nenhum fornecedor ou bucket é padrão obrigatório. Configure credencial restrita, agenda/fuso, retenção e alerta de falha/ausência. Comprove objeto externo e restauração isolada; mantenha APP_KEY correspondente para recuperar segredos do painel. Backup de volume em escrita pode ser inconsistente. Não declare migração completa por um dump restaurado.

## Telegram

Um bot pode centralizar eventos de várias aplicações. Configure token atual e destino autorizado na equipe correta, valide identidade, selecione falhas/recuperação e teste recebimento com autorização. Token rotacionado invalida cópias antigas. Bot de envio não é agente executor. Métricas Sentinel não provam limiares configurados nem detecção de queda total; utilize monitor externo independente para essa cobertura.

## Resend e e-mail

Coolify suporta e-mail por SMTP/Resend. Configure remetente e domínio verificado, DNS necessário, chave restrita e eventos desejados. Teste entrega autorizada. E-mail do painel não configura automaticamente aplicações: cada projeto precisa de sua própria integração, gestão de segredo, limites/retries e fluxos de recuperação/convite. Não solicite tokens em chat.

## DDoS e abuso

Para HTTP público, avalie proxy Cloudflare ou equivalente, WAF e rate limit conforme plano. Proteja origem contra acesso que contorne o proxy, preservando validação de certificados, webhooks, healthchecks e acesso administrativo. Faça inventário IPv4/IPv6 e teste conectividade antes de restringir. SSH/painel devem ter acesso limitado e recuperação alternativa. Firewall local/Fail2ban não protegem sozinhos contra saturação da conexão; mitigação volumétrica requer upstream/provedor. WAF não substitui autorização, validação no backend, patches e isolamento. Nada oferece blindagem total.

Fontes oficiais: [Coolify e-mail](https://coolify.io/docs/core/notifications/channels/email), [Telegram](https://coolify.io/docs/core/notifications/channels/telegram), [origem Cloudflare](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/).
