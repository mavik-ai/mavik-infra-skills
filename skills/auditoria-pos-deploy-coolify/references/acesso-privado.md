# Coolify · Obter acesso privado

Use só quando faltar acesso; reutilize credencial/conector já autorizado. Não forneça domínio padrão: use a instância confirmada. Entregue as etapas individualmente conforme [condução guiada](conducao-guiada.md).

## Visão geral para o usuário

“Precisamos de acesso de leitura para conferir seu projeto sem alterar o servidor. Vamos abrir seu painel, localizar os tokens, preparar o destino privado, criar uma chave limitada e validar o acesso.”

## Etapas que o agente deve conduzir

1. **Abrir · 2–3 min.** Forneça link da instância confirmada. Peça login e seleção da equipe proprietária do projeto. Resultado esperado: painel da equipe correta. Espere feito.
2. **Encontrar · 2–3 min.** Abra **Keys & Tokens → API Tokens**. Se o nome variar, consulte documentação/versão e peça apenas rótulos sem segredos. Espere feito.
3. **Preparar o destino privado · 2–3 min.** Combine um secret store ou arquivo local privado fora do Git e explique como inserir sem expor no chat/logs. Se não houver entrada privada segura, resolva isso antes de criar a chave. Resultado esperado: destino disponível e caminho conhecido, sem segredo gravado ainda. Espere feito.
4. **Criar · 3–5 min.** Dê descrição identificável e expiração adequada. Para inventário, selecione `read`; não peça `root`, `write`, `deploy` ou `read:sensitive` por padrão. Crie o token e salve imediatamente no destino privado combinado; o segredo aparece uma vez. Espere feito, nunca o valor.
5. **Validar · agente.** Carregue privadamente como `COOLIFY_API_TOKEN` quando usar o helper existente e faça consulta de leitura na equipe/recurso. Não imprima token nem payload completo. API desativada ou allowlist pode impedir acesso: explique a causa e proponha ajuste delimitado, sem habilitar ou remover proteção automaticamente.

API em instância própria pode exigir habilitação; verifique a condição antes de propor alteração. Token pertence à equipe selecionada na criação. Verificação de acesso não comprova proteção, backup ou monitoramento.

## Guardar sem expor

Antes de a pessoa criar a chave, escolha com ela um destino seguro disponível: secret store, formulário privado do fornecedor ou arquivo local privado fora do Git. Não use o `.env` do aplicativo por padrão: um token administrativo não precisa ir para containers ou frontend. Se um env privado já existir, preserve seu conteúdo e ignore-o no Git antes de gravar. Explique o caminho e o nome da variável, nunca o valor.

Para inserir pelo terminal, confirme que a entrada é diretamente humana, oculta e não capturada por logs/transcrição da ferramenta; não solicite token em comando, argumento, histórico de shell ou ferramenta de perguntas do chat. Use um mecanismo de entrada privada suportado; não prometa privacidade apenas porque a tela oculta caracteres. Se o ambiente não oferecer isso, guie a pessoa para um editor local privado ou secret store. Nunca peça “cole aqui”. Verifique existência/permissões sem imprimir conteúdo; arquivo privado 600 e diretório 700 quando o sistema suportar.

Depois de a pessoa responder feito, valide somente leitura no recurso autorizado. Relate sucesso/falha sem resposta bruta. Token ativo não comprova acesso aos recursos; permissões insuficientes não justificam pedir acesso total. Se um segredo foi exposto, explique a necessidade de revogação e substituição, respeitando o escopo autorizado.

Fonte consultada em 08/10/2026: [API Tokens do Coolify](https://coolify.io/docs/core/security/credentials/api-tokens). Revalidar comportamento na versão instalada.
