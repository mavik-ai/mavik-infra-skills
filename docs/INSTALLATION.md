# Instalação — v1.1.0

O pacote contém três skills independentes: `coolify-ops`, `cloudflare-ops` e `auditoria-pos-deploy-coolify`. Não instale a raiz do repositório.

1. Abra a [release v1.1.0](https://github.com/mavik-ai/mavik-infra-skills/releases/tag/v1.1.0).
2. Baixe o ZIP da skill desejada e `SHA256SUMS`; confira o arquivo com `shasum -a 256 -c SHA256SUMS` no diretório dos downloads. Arquivos não baixados aparecem como ausentes; o ZIP escolhido deve retornar OK.
3. Extraia a pasta completa para `~/.codex/skills/` ou `~/.claude/skills/`. Preserve e compare instalações anteriores antes de substituir.
4. Reinicie a sessão e invoque `$coolify-ops`, `$cloudflare-ops` ou `$auditoria-pos-deploy-coolify`.

## Instalar pelo Git

```bash
git clone --branch v1.1.0 https://github.com/mavik-ai/mavik-infra-skills.git
cd mavik-infra-skills
mkdir -p ~/.codex/skills
# Copie apenas se o destino não existir.
cp -R skills/auditoria-pos-deploy-coolify ~/.codex/skills/
```

Troque o nome para instalar outra skill; no Claude Code, use `~/.claude/skills/`. Cada pasta inclui seu README, SKILL.md, metadados e referências necessárias.

No instalador do Codex, informe repo `mavik-ai/mavik-infra-skills`, ref `v1.1.0` e path `skills/<nome>`. O método Git foi validado; erros locais de certificados devem ser corrigidos sem desabilitar TLS.

Consulte os [exemplos de uso](../README.md#primeiro-uso). A auditoria funciona independentemente e reutiliza o helper de Coolify Ops quando disponível. Instalar uma skill não configura infraestrutura, concede acesso ou instala monitoramento contínuo. Guarde credenciais em destino privado.
