# MAVIK.AI · Auditoria pós-deploy no Coolify

Skill em português para conferir a proteção e a operação de projetos no Coolify após um deploy ou durante uma revisão. Entrega um diagnóstico somente leitura, com evidências, riscos, responsáveis e próximas ações.

**Parte do MAVIK.AI Infra Skills · MIT · PT-BR.** Projeto independente, sem afiliação oficial ao Coolify.

## O que verifica

| Área | Verificação |
|---|---|
| Backup | Execuções, cópia externa, arquivos/volumes, retenção e evidência de recuperação |
| Segurança | TLS, exposição, acessos, segredos e controles relevantes ao aplicativo |
| Saúde | Deploy atual, serviços, dependências, erros e recursos do host |
| Monitoramento | Coleta recente, eventos, entrega de alertas e cobertura externa |

## Instalar

A partir da raiz do repositório, copie esta pasta inteira para `~/.codex/skills/` ou `~/.claude/skills/`, preservando instalações existentes. Inicie uma nova sessão. Veja o [guia de instalação do pacote](https://github.com/mavik-ai/mavik-infra-skills/blob/v1.1.0/README.md#instalação).

Disponível no pacote a partir da tag `v1.1.0`; a tag `v1.0.0` não inclui esta skill. Não exige scripts próprios. Se `coolify-ops` estiver instalada, o agente pode reutilizar seu helper de inventário; sem ela, usa as ferramentas de leitura disponíveis.

## Usar

> Use $auditoria-pos-deploy-coolify para auditar meu projeto no Coolify. Confira os quatro pilares e apresente evidências e pendências antes de propor correções.

Para começar: instale a pasta, inicie uma nova sessão, abra seu projeto e envie o pedido acima. Acrescente o ambiente, a URL da instância e o nome ou UUID do recurso. Veja o [passo a passo e exemplos completos](https://github.com/mavik-ai/mavik-infra-skills/blob/v1.1.0/README.md#primeiro-uso).

Informe projeto, ambiente e instância autorizados. Credenciais devem permanecer no painel, secret store ou arquivo privado, nunca na conversa. O procedimento completo está em [SKILL.md](SKILL.md).

## Resultado e limites

O relatório distingue comprovado, falhou, pendente, não verificável e não se aplica. Cada item indica evidência, impacto, responsável e próxima ação. Ausência de evidência não significa ausência do recurso.

A skill não altera produção, envia testes, executa restore ou instala monitoramento por conta própria. Configuração de Telegram não comprova entrega de incidentes; backup agendado não comprova recuperação. Ações adicionais seguem o escopo autorizado.
