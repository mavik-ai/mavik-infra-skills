# Instalação automática — v1.2.0

O pacote contém `coolify-ops`, `cloudflare-ops` e `auditoria-pos-deploy-coolify`. O instalador local instala as três pastas completas. Requer Git e Python 3.10+; não exige token nem conexão com Coolify/Cloudflare.

## 1. Baixar e instalar

```bash
git clone --branch v1.2.0 https://github.com/mavik-ai/mavik-infra-skills.git
cd mavik-infra-skills
python3 scripts/install.py --target both
```

Escolha `--target codex`, `--target claude` ou `--target both`. No Codex, o destino padrão é `~/.codex/skills/`; se `CODEX_HOME` já estiver configurado, usa `CODEX_HOME/skills/`. No Claude Code usa `~/.claude/skills/`. O script mostra os caminhos efetivos.

Prefere não usar terminal? Copie o [pedido de instalação assistida](../README.md#sem-usar-o-terminal-copie-e-cole-no-seu-agente) no agente local. Ele pode baixar a tag, revisar o instalador e executá-lo por você. Conversas web comuns não instalam arquivos no computador.

## 2. Abrir uma nova sessão e usar

| Skill | Codex | Claude Code |
|---|---|---|
| Operação Coolify | `$coolify-ops` | `/coolify-ops` |
| Operação Cloudflare | `$cloudflare-ops` | `/cloudflare-ops` |
| Auditoria pós-deploy | `$auditoria-pos-deploy-coolify` | `/auditoria-pos-deploy-coolify` |

Abra o projeto e informe ambiente/alvo. Consulte os [exemplos de primeiro uso](../README.md#primeiro-uso). O instalador verifica arquivos; isso não prova execução de uma auditoria real nem credenciais disponíveis.

## 3. Atualizar sem perder a instalação anterior

Se alguma pasta já existir, a instalação normal aborta antes de substituir qualquer skill. Confira as diferenças da versão e só então autorize atualização:

```bash
python3 scripts/install.py --target both --update
```

O instalador salva as pastas anteriores em `~/.mavik-infra-skills/backups/`, em um diretório exclusivo identificado na saída. Os backups ficam fora dos locais de descoberta. Prepare todas as cópias antes das trocas; em caso de erro durante a troca, tenta restaurar os destinos anteriores. Falhas do sistema de arquivos também podem impedir a recuperação: mantenha o backup e revise o erro exibido antes de repetir.

Os destinos e o diretório privado de preparação/backup precisam estar no mesmo sistema de arquivos para as trocas por rename. Se CODEX_HOME estiver em outro disco, a instalação pode retornar erro de troca entre sistemas de arquivos; use o instalador nativo do Codex ou a cópia manual nesse caso.

Não execute dois instaladores ao mesmo tempo. O procedimento não migra alterações locais para a versão nova: elas permanecem no backup para comparação. Destinos de skill que sejam links simbólicos são recusados; revise a instalação compartilhada manualmente em vez de substituir o link. Nenhum backup anterior é apagado automaticamente.

Para recuperar uma versão anterior, feche as sessões, localize a pasta do alvo/skill dentro do backup, preserve a versão atual fora do diretório de skills e recoloque a pasta antiga no destino informado. Não mescle pastas nem deixe duas cópias da mesma skill no diretório de descoberta. Abra uma nova sessão depois.

## Instalar somente uma skill

O instalador do pacote instala as três. Para escolher apenas uma, use o instalador nativo do Codex (repo `mavik-ai/mavik-infra-skills`, ref `v1.2.0`, path `skills/<nome>`), ou copie somente sua pasta inteira para o destino da ferramenta. Preserve instalações existentes. A raiz do repositório não é uma skill.

## ZIPs e integridade

A [release v1.2.0](https://github.com/mavik-ai/mavik-infra-skills/releases/tag/v1.2.0) oferece três ZIPs individuais, pacote completo e `SHA256SUMS`. Para usar o instalador, extraia o **pacote completo** e execute `scripts/install.py` de dentro dele. ZIPs individuais servem à cópia manual.

Baixe os ZIPs desejados e o arquivo de checksums da mesma release. Use `shasum -a 256 -c SHA256SUMS` no diretório dos downloads: os ZIPs baixados devem retornar OK; os não baixados aparecem como ausentes. Não instale arquivo com checksum divergente.

## Diagnóstico

| Mensagem/situação | Próxima ação |
|---|---|
| `python3` ou Git ausente | Disponibilize Python 3.10+ e Git; não precisa instalar dependências Python |
| Destino existente | Compare versões e use `--update` somente se quiser substituir com backup |
| Link simbólico | Revise o destino compartilhado manualmente; o instalador não altera o link |
| Falha de permissão | Confira acesso ao caminho mostrado; não use sudo para instalar skills pessoais |
| Skill não aparece | Abra nova sessão, confira o caminho efetivo e conflitos com outras instalações |

## Fontes e limites

Os caminhos Codex foram conferidos no instalador local da ferramenta; o runtime e diretório configurado devem ser confirmados no uso. Claude Code documenta skills pessoais e comandos em [Extend Claude with skills](https://code.claude.com/docs/en/skills). Consulta em 08/10/2026.

Instalação/atualização foram testadas em diretórios temporários, sem alterar skills pessoais. Não houve homologação de uma sessão Claude Code ou Codex recém-iniciada, nem de AgY. Instalar não ativa daemon, monitor contínuo, webhooks ou serviços externos. Credenciais permanecem em armazenamento privado.
