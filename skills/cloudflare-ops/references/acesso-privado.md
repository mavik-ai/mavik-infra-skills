# Cloudflare · Obter acesso privado

Leia esta referência apenas se faltar acesso necessário. Reutilize conexão autorizada existente; não obrigue a emitir token se painel/conector já permitem a leitura. Entregue um passo de cada vez conforme [condução guiada](conducao-guiada.md).

## Visão geral para o usuário

“Vamos criar uma chave que permite consultar apenas o domínio escolhido e guardá-la fora da conversa. São cinco etapas: abrir o painel, escolher permissões, preparar o destino privado, criar a chave e validar o acesso.”

## Etapas que o agente deve conduzir

1. **Abrir · 2–3 min.** Link: [Cloudflare](https://dash.cloudflare.com/). Entre na conta correta; para token de usuário, abra **My Profile → API Tokens**. Resultado esperado: lista de tokens, sem copiar nenhum segredo para a conversa. Espere feito.
2. **Permissões · 3–5 min.** Clique **Create Token** e escolha token personalizado. Antes de preencher, o agente fornece somente as permissões de leitura necessárias ao escopo e restringe conta/zona. Para consulta DNS de um domínio, `Zone / DNS / Read` é um exemplo; não cobre WAF, TLS ou R2. Não use modelo de edição DNS para auditoria sem reduzir seu acesso. Confirme o domínio e uma expiração adequada; não imponha filtro de IP sem saber a origem legítima. Espere feito.
3. **Preparar o destino privado · 2–3 min.** Combine um secret store ou arquivo local privado fora do Git e explique como inserir sem expor no chat/logs. Se não houver entrada privada segura, resolva isso antes de criar a chave. Resultado esperado: destino disponível e caminho conhecido, sem segredo gravado ainda. Espere feito.
4. **Criar · 2–3 min.** Revise o resumo e clique **Create Token**. A chave é mostrada uma vez: salve no destino privado combinado, sem foto ou envio ao chat. Espere feito, nunca o token.
5. **Validar · agente.** Confirme o armazenamento privado e faça a leitura mínima autorizada. Token de usuário pode ser validado pela rota oficial de verificação; tokens de conta têm escopo/rotas próprios. Não deduza permissões completas apenas pelo status ativo.

## Escolher o caminho correto

| Objetivo | Caminho do painel | Acesso que precisa ser confirmado |
|---|---|---|
| Consultar/configurar DNS, TLS e proteção do site | **My Profile → API Tokens** para usuário; **Manage Account → Account API Tokens** para conta | Permissões específicas dos endpoints e recursos necessários; conferir compatibilidade do token de conta |
| Criar/administrar buckets R2 | **Armazenamento de objetos R2 → Detalhes da conta → Gerenciar tokens de API** | Token R2 administrativo apenas quando provisionamento foi autorizado |
| Salvar/ler backups em bucket existente | Mesmo painel R2 | Credencial S3 de objetos restrita ao bucket, com operações necessárias |

“Conta” descreve a identidade do token; “R2” descreve seu escopo. Um token de conta criado na tela R2 não vira acesso geral ao site. Não peça outra credencial se a existente já atende à operação autorizada.

Para tokens gerais de conta, o caminho [oficial](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/) é selecionar a conta e abrir gerenciamento da conta/tokens. Para usuário, o perfil é uma alternativa válida, não substituição obrigatória do R2. Leia os rótulos do painel atual e confirme escopo antes de orientar.

Se a tarefa for configuração já autorizada, apresente as permissões de escrita mínimas dos endpoints que serão usados, restritas ao domínio/conta; não limite o tutorial a Read quando Write for necessário. Comece com leitura quando possível e não peça Edit de tudo, Global API Key ou poder de criar tokens sem necessidade. Templates são pontos de partida: revisar permissões antes de emitir.

## R2: guia individual para a tela de armazenamento

Entregue uma etapa por mensagem, não a sequência inteira ao usuário:
1. **Abrir · 2–3 min.** Entre no painel da conta correta e abra **Armazenamento e bancos → Armazenamento de objetos R2**. Resultado: página R2. Se o produto pedir ativação com cobrança, explique custo e aguarde autorização; não contrate.
2. **Localizar · 2–3 min.** Em **Detalhes da conta**, clique **Gerenciar tokens de API**. Para integração durável com suporte adequado, escolha **Criar token de API de conta**. Token de usuário também existe; não exigir conta quando papel ou operação não permitem.
3. **Definir acesso e destino · 3–5 min.** Explique nome, bucket e permissão. Backup em bucket existente normalmente precisa **Leitura/gravação para objeto**, restrita ao bucket. **Administrador com leitura/gravação** permite administrar/excluir buckets: use só para provisionamento delimitado, não como credencial padrão de backup. Combine o destino privado antes de criar. Explique expiração e rotação; **Sempre** não é padrão universal. Filtro de IP exige origem legítima conhecida.
4. **Criar e guardar · 2–3 min.** Gere a credencial e guarde **Access Key ID** e **Secret Access Key** no destino privado. Para S3, confirme endpoint da conta/jurisdição; não confunda ID da conta com ID de zona ou do bucket. Chave secreta não deve ir para o chat. Espere feito.
5. **Validar · agente.** Confira acesso ao bucket com leitura mínima autorizada. Listar objetos não prova backup enviado/restaurado. Escrita de objeto de teste e sua limpeza exigem escopo próprio; não sobrescreva ou exclua dados reais.

[Documentação R2](https://developers.cloudflare.com/r2/api/tokens/) distingue permissões administrativas de permissões de objetos; estas últimas são para API compatível com S3. Não use credencial de objetos para presumir acesso à REST API de gerenciamento.

Links de painel podem ser construídos a partir de ID de conta autorizado e validado, quando a rota atual for conhecida. Nunca fixe ID de uma conta real no pacote público; ofereça o caminho pelo menu como alternativa. Se uma tela diferir, peça apenas o rótulo ou erro sem segredos e ajuste pela documentação vigente.

## Guardar sem expor

Antes de a pessoa criar a chave, escolha com ela um destino seguro disponível: secret store, formulário privado do fornecedor ou arquivo local privado fora do Git. Não use o `.env` do aplicativo por padrão: um token administrativo não precisa ir para containers ou frontend. Se um env privado já existir, preserve seu conteúdo e ignore-o no Git antes de gravar. Explique o caminho e o nome da variável, nunca o valor.

Para inserir pelo terminal, confirme que a entrada é diretamente humana, oculta e não capturada por logs/transcrição da ferramenta; não solicite token em comando, argumento, histórico de shell ou ferramenta de perguntas do chat. Use um mecanismo de entrada privada suportado; não prometa privacidade apenas porque a tela oculta caracteres. Se o ambiente não oferecer isso, guie a pessoa para um editor local privado ou secret store. Nunca peça “cole aqui”. Verifique existência/permissões sem imprimir conteúdo; arquivo privado 600 e diretório 700 quando o sistema suportar.

Depois de a pessoa responder feito, valide somente leitura no recurso autorizado. Relate sucesso/falha sem resposta bruta. Token ativo não comprova acesso aos recursos; permissões insuficientes não justificam pedir acesso total. Se um segredo foi exposto, explique a necessidade de revogação e substituição, respeitando o escopo autorizado.

Fonte consultada em 08/10/2026: [criação de API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/). Revalidar navegação e permissões no uso.
