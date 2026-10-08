# Changelog

SemVer para o pacote. Cada entrada identifica a skill alterada.

## [1.2.0] - 2026-10-08

### Adicionado
- Instalador automático Python para as três skills no Codex, Claude Code ou ambos; respeita CODEX_HOME quando configurado.
- Atualização explícita com backup fora da descoberta e recuperação em caso de falha durante a troca.
- Testes isolados do instalador incorporados ao CI.

### Documentação
- Comandos de instalação, pedido copiável para o agente, atualização, backup e diagnóstico.
- Instalação não requer tokens nem altera infraestrutura; sessões reais dos agentes permanecem uma validação separada.

## [1.1.0] - 2026-10-08

### Documentação
- cloudflare-ops: conexão/permissões como primeiro passo, onboarding de domínio, configuração por produto/plano, tutorial R2 separado de DNS/TLS/WAF e gates de validação de fluxos.
- As três skills agora conduzem iniciantes com benefício, visão geral curta, um passo manual por vez, obtenção privada de acesso e pausa/retomada. Lembretes limitados a dois por espera e condicionados ao runtime.
- Apresentação MAVIK.AI com marca ASCII, catálogo, instalação Codex/Claude Code, exemplos de uso e README por skill.
- Pedido copiável de instalação assistida para iniciantes, com descoberta da ferramenta e tratamento explícito de compatibilidade e skills não publicadas.

### Adicionado
- auditoria-pos-deploy-coolify: auditoria somente leitura dos quatro pilares, com evidências e pendências por responsável; reaproveitamento opcional do helper coolify-ops. Não instala monitoramento contínuo.

## [1.0.0] - 2026-10-08

### Adicionado
- Pacote MAVIK Infra Skills com subpastas instaláveis independentemente.
- cloudflare-ops: DNS/TLS/origem/Access/WAF, cache, R2 e ferramentas; operação assistida com autorização.
- Documentação de instalação individual, metadados, licença MIT, políticas e CI.
- Distribuição completa e individual com SHA-256.

### Incorporado
- coolify-ops baseada na release standalone1.0.0, com marca MAVIK na apresentação e instrução de instalação por subpasta. Helper preservado; comando coolify-ops mantido.

### Limites
- Nenhum segredo, inventário real ou dado privado incluído.
- Sem monitor contínuo, provisionamento automático ou mudança em produção.
