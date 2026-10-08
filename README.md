```text
 __  __    _ __     _____ _  __    _    ___
|  \/  |  / \\ \   / /_ _| |/ /   / \  |_ _|
| |\/| | / _ \\ \ / / | || ' /   / _ \  | |
| |  | |/ ___ \\ V /  | || . \  / ___ \ | |
|_|  |_/_/   \_\\_/  |___|_|\_\ /_/   \_\___|
                         MAVIK.AI
```

# MAVIK.AI · Infra Skills

**Infraestrutura assistida por IA, com evidências para decidir e autorização para agir.**

Uma coleção de habilidades em português para usar no **Codex e Claude Code** ao cuidar de projetos no Coolify e na Cloudflare. Ajuda a verificar recuperação de dados, revisar segurança, conferir saúde dos serviços e identificar lacunas de monitoramento.

**Licença MIT · PT-BR · Skills instaláveis individualmente.** Projeto independente, sem afiliação oficial com Coolify ou Cloudflare.

[Escolher uma skill](#escolha-a-skill) · [Instalar](#instalação) · [Usar](#primeiro-uso) · [Segurança](SECURITY.md) · [Contribuir](CONTRIBUTING.md)

## Escolha a skill

| Skill | Quando usar | O que entrega |
|---|---|---|
| [Coolify Ops](skills/coolify-ops/README.md) | Revisar ou operar a infraestrutura de projetos Docker/Coolify | Inventário, orientações de backup/restore, segurança, saúde e alertas; execução dentro do escopo autorizado |
| [Cloudflare Ops](skills/cloudflare-ops/README.md) | Revisar DNS, TLS, acesso, segurança de borda, cache ou R2 | Diagnóstico e orientação de configuração conforme o plano e as ferramentas disponíveis |
| [Auditoria pós-deploy no Coolify](skills/auditoria-pos-deploy-coolify/README.md) | Conferir um projeto após deploy ou fazer revisão operacional | Auditoria somente leitura de backup, segurança, saúde e monitoramento, com evidências e pendências por responsável |

Cada pasta é uma skill. Instale uma, duas ou todas conforme sua necessidade. A auditoria funciona sozinha e pode reutilizar o helper de inventário quando `coolify-ops` também estiver instalada.

## Instalação

### Sem usar o terminal: copie e cole no seu agente

Abra uma conversa no **Claude Code, Codex ou AgY** que tenha acesso aos arquivos do seu computador. Copie o texto inteiro abaixo, cole na conversa e envie. Você não precisa executar comandos manualmente.

```text
Quero instalar as habilidades de infraestrutura da MAVIK.AI deste repositório:
https://github.com/mavik-ai/mavik-infra-skills

Instale estas três skills:
- coolify-ops
- cloudflare-ops
- auditoria-pos-deploy-coolify

Primeiro identifique qual ferramenta estou usando e consulte suas instruções
locais para descobrir onde ela carrega skills. No Codex, use seu instalador
de skills quando disponível. Use o formato e o diretório suportados por
esta ferramenta, sem presumir que o caminho de outra ferramenta funciona.

Leia o README do repositório e inspecione cada skill antes de instalá-la.
Use uma revisão publicada que contenha as três pastas em skills/.
Copie cada pasta completa, com suas referências e scripts.
Não execute scripts do repositório apenas para instalar as skills.
Não substitua habilidades existentes sem me apresentar as diferenças.
Não configure servidores, credenciais ou serviços externos.

Se uma skill não estiver publicada ou a ferramenta não suportar esse
formato, informe exatamente o que falta, sem inventar compatibilidade.
Instale as demais apenas quando forem compatíveis.

Ao terminar, confira os arquivos instalados e me diga:
1. Quais habilidades foram instaladas e onde.
2. Se preciso abrir uma nova conversa ou reiniciar a ferramenta.
3. Um pedido pronto para eu copiar e usar cada habilidade.
```

**Depois de instalar**, abra uma nova conversa se o agente orientar e copie um dos [pedidos de uso](#primeiro-uso). Para instalar somente uma skill, deixe apenas o nome dela na lista do pedido acima.

Isso requer um agente com acesso a arquivos e instalação de skills. Uma conversa comum no site do Claude ou ChatGPT não instala arquivos no seu computador. No AgY, o pedido orienta o agente a conferir o suporte e o caminho corretos antes de instalar; a compatibilidade ainda não foi testada neste projeto.

A release `v1.1.0` inclui as três skills. Consulte o [guia de instalação](docs/INSTALLATION.md) e os arquivos da release.

### Instalação manual, para quem prefere o terminal

### 1. Baixe o repositório

```bash
git clone --branch v1.1.0 https://github.com/mavik-ai/mavik-infra-skills.git
cd mavik-infra-skills
```

Para uma instalação reproduzível, escolha uma tag ou commit que contenha a skill desejada. A tag `v1.1.0` inclui as três skills; `v1.0.0` contém somente Coolify Ops e Cloudflare Ops. Consulte o [changelog](CHANGELOG.md) e as [releases](https://github.com/mavik-ai/mavik-infra-skills/releases).

### 2. Copie a skill para seu agente

Exemplo com a auditoria pós-deploy no Codex:

```bash
mkdir -p ~/.codex/skills
# Execute somente se a pasta de destino ainda não existir.
cp -R skills/auditoria-pos-deploy-coolify ~/.codex/skills/
```

No Claude Code:

```bash
mkdir -p ~/.claude/skills
# Execute somente se a pasta de destino ainda não existir.
cp -R skills/auditoria-pos-deploy-coolify ~/.claude/skills/
```

Troque `auditoria-pos-deploy-coolify` por `coolify-ops` ou `cloudflare-ops` para instalar outra. **Copie a pasta inteira, não apenas o SKILL.md.** Preserve e compare instalações existentes antes de atualizar; não mescle pastas automaticamente. Inicie uma nova sessão após a instalação.

No Codex, você também pode solicitar ao instalador de skills: “Instale a skill do repositório `mavik-ai/mavik-infra-skills`, na pasta `skills/auditoria-pos-deploy-coolify`”. Informe a revisão desejada quando precisar fixar a versão.

A raiz do repositório contém a apresentação do pacote; as pastas dentro de `skills/` são os diretórios instaláveis.

## Primeiro uso

### Passo a passo

1. Instale a skill desejada e inicie uma nova sessão no Codex ou Claude Code.
2. Abra o projeto que pretende revisar, para o agente consultar seus documentos e configurações.
3. Envie um dos pedidos abaixo, substituindo os exemplos pelo seu projeto, ambiente e alvo.
4. O agente identifica os acessos disponíveis e apresenta um relatório com evidências, riscos e próximas ações. Se faltar acesso, siga a orientação para disponibilizá-lo por um canal privado.
5. Leia o relatório e autorize apenas as correções que deseja executar. Para conferir uma correção já aplicada, peça uma nova verificação dos itens afetados.

### Auditoria pós-deploy no Coolify

Copie e adapte:

```text
Use $auditoria-pos-deploy-coolify para auditar o projeto MEU-PROJETO,
no ambiente PRODUÇÃO, após o deploy concluído.
Instância: https://coolify.example.com
Recurso: NOME-OU-UUID
Confira backups, segurança, saúde e monitoramento.
Faça somente leitura e apresente evidências, riscos, responsáveis
e próximas ações. Não execute correções nesta auditoria.
```

Se não souber o UUID, informe o nome do projeto e peça ao agente para identificar o recurso no inventário autorizado. O domínio acima é fictício, não um destino padrão.

### Operação assistida no Coolify

```text
Use $coolify-ops para revisar o backup e a recuperação do projeto
MEU-PROJETO no ambiente HOMOLOGAÇÃO.
Identifique a instância e os acessos autorizados nos documentos do projeto.
Apresente o diagnóstico e as mudanças propostas antes de alterar configurações.
```

### Revisão da Cloudflare

```text
Use $cloudflare-ops para revisar DNS, TLS e cache do domínio example.com.
Confira a integração com a origem e apresente riscos e recomendações
compatíveis com meu plano. Faça somente leitura nesta etapa.
```

### Como continuar após o relatório

Para detalhar uma pendência:

```text
Explique a pendência de backup externo deste relatório e prepare
uma proposta com destino, custo, retenção e validação de recuperação.
```

Para conferir uma mudança já realizada:

```text
Revalide os itens corrigidos neste relatório usando evidências atuais.
Informe o que passou e o que continua pendente.
```

Não cole tokens, chaves, senhas ou dumps na conversa. Use o painel do fornecedor, um secret store ou arquivo privado conforme o fluxo autorizado. A instalação não concede acesso à infraestrutura; se ferramentas ou permissões faltarem, o agente deve informar o limite.

## Ajuda em passos curtos

Não precisa saber os termos técnicos para começar. O agente explica o que será feito e o benefício para seu projeto; depois mostra uma visão geral curta e conduz uma etapa de cada vez. Quando precisar de uma ação sua, informa o link, o resultado esperado e uma estimativa de tempo. Você responde **feito** para seguir ou diz onde travou.

| Skill | Como ajuda seu negócio |
|---|---|
| Coolify Ops | Ajuda a cuidar do servidor e da recuperação dos seus sistemas com ações autorizadas |
| Cloudflare Ops | Ajuda a revisar acesso ao site, proteção de borda e velocidade conforme seu plano |
| Auditoria pós-deploy | Mostra o que foi comprovado e as pendências após colocar uma versão no ar |

Para começar assim, copie:

```text
Use $cloudflare-ops para revisar meu domínio.
Explique primeiro o benefício e a visão geral em até cinco etapas.
Depois me conduza em um passo de cada vez, com link e tempo estimado.
Se precisar de token, me ensine onde criar e guardar sem enviar no chat.
Espere eu responder feito antes do próximo passo que dependa de mim.
```

Troque o nome da skill conforme o objetivo. Se precisar de uma chave de acesso, o agente explica como obtê-la com as permissões necessárias e guardá-la privadamente. Você não deve enviar a chave na conversa.

Pode escrever **pausar**, **continuar** ou **cancelar**. Pausar/cancelar interrompe a orientação e os lembretes; não apaga o que foi feito. Quando houver suporte a timer na sessão, o agente pode fazer até dois contatos após o tempo estimado de uma etapa. Sem esse recurso, ele informa que precisa esperar você voltar; não promete acompanhamento automático.

## Como funciona

1. O agente identifica o alvo, o escopo e os acessos autorizados.
2. Consulta configuração e evidências disponíveis, sem tratar histórico como prova atual.
3. Apresenta controles comprovados, falhas, itens pendentes e verificações inconclusivas.
4. Propõe próximas ações; operações seguem a autorização específica do usuário.

Configuração habilitada não comprova resultado. Agenda de backup, objeto fora do host, restauração, coleta de métricas e entrega de alerta são evidências distintas.

## Requisitos e limites

- **Agente:** Codex ou Claude Code com suporte a skills e ferramentas para o acesso escolhido.
- **Helper Coolify:** Python 3.10+, curl e SSH opcional. Sem dependências Python externas; API exercitada em Coolify 4.4.2, com versão e permissões a revalidar no uso.
- **Cloudflare:** acesso autorizado à API/painel e documentação atual. CLI, Terraform e MCP são opcionais.
- **Auditoria:** procedimento do agente, sem script próprio; reaproveitamento do inventário Coolify é opcional.
- **Operação:** instalar skills não provisiona R2, Access, Telegram, backups ou monitoramento contínuo. Não instala daemon, webhook ou autorremediação.

Relatórios com inventário real são privados. O helper Coolify coleta inventário; seu código de saída zero não aprova segurança. Nenhuma skill concede permissão para deploy, exclusão de dados, gastos ou envio de mensagens.

## Estrutura

```text
mavik-infra-skills/
├── README.md                 Apresentação e instalação
├── LICENSE                   Licença MIT
├── CHANGELOG.md               Histórico por skill
├── CONTRIBUTING.md            Como contribuir
├── SECURITY.md                Como reportar problemas
├── .github/workflows/ci.yml   Validação do pacote
└── skills/
    ├── coolify-ops/           Guia, referências e helper
    ├── cloudflare-ops/        Guia e referências
    └── auditoria-pos-deploy-coolify/  Guia de auditoria
```

Cada skill possui `SKILL.md` para instruções do agente, `agents/openai.yaml` para apresentação no Codex e `README.md` para quem instala. Referências e scripts existem apenas quando necessários ao seu uso.

## Validação e manutenção

```bash
python3 -m unittest discover -s skills/coolify-ops/scripts -p 'test_*.py'
python3 -m compileall -q skills/coolify-ops/scripts
git diff --check
```

Os testes usam respostas simuladas e não acessam servidores reais. Instruções e checklists também precisam de revisão; testes do helper não homologam infraestrutura.

O pacote segue SemVer, com mudanças por skill no changelog. A distribuição standalone [Coolify Ops v1.0.0](https://github.com/mavik-ai/coolify-ops/releases/tag/v1.0.0) permanece separada; este repositório concentra a evolução do pacote conjunto. Evite cópias duplicadas da mesma skill em diretórios de descoberta concorrentes.

---

**MAVIK.AI · Infra Skills** — documentação operacional e habilidades reutilizáveis para quem constrói e mantém aplicações com IA.

[Changelog](CHANGELOG.md) · [Segurança](SECURITY.md) · [Contribuir](CONTRIBUTING.md) · [Licença](LICENSE)
