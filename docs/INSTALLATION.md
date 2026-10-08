# Instalação por subpasta

Cada pasta skills/<nome> é uma skill independente. Não instale a raiz do repositório.

1. Escolha a release publicada na aba Releases; não presuma disponibilidade de uma tag antes da publicação.
2. Baixe o ZIP individual e o SHA256SUMS da mesma release.
3. Confira SHA-256 e extraia a pasta para ~/.codex/skills ou ~/.claude/skills, preservando qualquer instalação anterior.
4. Reinicie a sessão e invoque $cloudflare-ops ou $coolify-ops.

No Codex, o instalador suporta repo mavik-ai/mavik-infra-skills e paths skills/cloudflare-ops / skills/coolify-ops. O método Git foi validado; erro de certificados no Python local deve ser corrigido ou contornado pelo transporte Git sem desabilitar TLS.

## Documentação antes do merge

Enquanto o PR inicial não foi integrado, o README e as referências estão na branch do PR. A branch main só recebe o pacote depois de CI e scan de segurança concluídos. Resultado neutral por erro de serviço não é scan aprovado.

A publicação da skill não configura infraestrutura. Tokens devem permanecer privados e mudanças exigem escopo autorizado.
