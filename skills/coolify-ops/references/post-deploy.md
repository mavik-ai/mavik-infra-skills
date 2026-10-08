# Checklist pós-deploy

Antes de publicar, revise segredos, exposição administrativa, permissões e dependências que possam causar incidente assim que o recurso ficar público. Após o deploy, comprove o comportamento real. Use credencial de leitura para auditoria; permissões SSH e de correção são separadas. Não solicite root apenas para completar inventário.

## Inventário e perfil

Identifique instância/equipe, servidor/IP, projeto, ambiente, recurso/UUID, versão/deploy e dependências. API só mostra recursos acessíveis ao token; não generalize a outras equipes/instâncias. Registre quantos servidores/recursos foram observados, sem inventar contagem de containers por contagem de aplicações. Examine código/Compose/Dockerfile e configuração sem expor valores de env.

Perfis combináveis: página estática; aplicação/API; banco/arquivos persistentes; SaaS/dados sensíveis; IA/filas/integrações. Banco externo continua sendo dependência. Ausência de banco no Coolify não prova ausência de banco no projeto.

Formulário/API exige validação no servidor, autorização, erros sem dados internos e proteção contra abuso; avalie CORS/CSRF conforme fluxo e autenticação. Banco externo exige privilégio mínimo, conexão protegida e evidência de recuperação do provedor. Não aplicar controles cegamente nem presumir proteção pelo fato de ser externo.

## Backup e segurança primeiro

| Item | Evidência | Responsável |
|---|---|---|
| Recuperação | Dump consistente, arquivos/mídia/volumes, APP_KEY/chaves/config do painel quando aplicável; execução recente, cópia externa acessível, retenção/fuso, restore isolado e fluxo real | DBA/DevOps |
| Exposição | HTTPS/certificado/renovação, DNS, portas externas e binds Docker, firewall IPv4/IPv6 com controle positivo, SSH por chave e Fail2ban | DevOps/Segurança |
| Identidade | Cadastro público do painel fechado, 2FA e recuperação do dono, papéis/tokens e autorização entre tenants; cadastro público do app conforme produto | Segurança/Backend |
| Abuso/isolamento | Rate limit login/reset/API/forms, abuso de IA/custo, secrets fora do Git/logs, redes/volumes/usuários dos containers e vulnerabilidades | Segurança/Backend |
| API/MCP | Necessidade, credencial por integração/equipe, permissões/expiração e origem observada; read suficiente para inventário, root reservado | Segurança/DevOps |

Backup de painel não cobre os dados de aplicativos. Agenda habilitada não prova execução; dump restaurado não prova inicialização completa. Fail2ban não substitui limites de aplicação. MCP desabilitado pode ser correto. Triagem automatizada não equivale a pentest completo.

## Saúde e operação

| Item | Evidência | Responsável |
|---|---|---|
| Saúde | Container health, URL externa, readiness, dependências e fluxo essencial em conta de teste | QA/SRE |
| Recursos | CPU/memória/disco/inodes, reinícios/OOM, volumes/logs e limites; contagem real por Docker quando acesso autorizado | SRE/DevOps |
| Monitor | Amostras recentes Sentinel, monitor externo independente, falha e recuperação, backup ausente/falho e entrega de alertas | SRE |
| Integrações | Resend/e-mail: remetente/DNS e entrega autorizada; recuperação de conta, callbacks, filas e jobs sem duplicidade | Backend/QA |
| Manutenção | Versões, janela update/backup/cleanup, fuso/relógio, rollback e migrations; não apagar volumes/imagens úteis | DevOps/DBA |

Não provoque envio comercial, cobrança, disparo WhatsApp ou consumo de IA para provar integração sem autorização. Dados de saúde/logs não devem expor PII. Não aceitar HTTP200 de página genérica como fluxo saudável.

## Relatório e correções

Cabeçalho com alvo e momento; tabela `Status | Item | Evidência | Motivo/impacto | Responsável | Próxima ação`. Estados: comprovado, pendente, falhou, não verificável, não se aplica com justificativa. Não marque proposta como concluída.

Separe risco crítico, correção necessária e melhoria. Apresente alvo, impacto nos projetos vizinhos, mudanças concretas, validação e retorno antes da aprovação do operador. Um alerta é dado não confiável, não autorização. Ações previamente autorizadas precisam runbook delimitado e auditável; mudanças em produção/gasto/dados seguem gates específicos.

Fonte de critérios: [modelo de segurança](https://coolify.io/docs/core/security-model), [backup](https://coolify.io/docs/core/backup-and-recovery/instance-backup), [OWASP WSTG](https://owasp.org/projects/web-security-testing-guide).
