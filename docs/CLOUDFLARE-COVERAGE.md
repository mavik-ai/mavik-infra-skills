# Cloudflare Ops 1.3.0: cobertura e evidências

Em 08/10/2026, o diretório oficial Cloudflare apresentou 138 entradas entre produtos, famílias e guias. Todas estão indexadas no [catálogo](../skills/cloudflare-ops/references/catalogo-atual.md), com finalidade e primeiro caminho de configuração. O [guia operacional](../skills/cloudflare-ops/references/configuracao-recursos.md) aprofunda pré-requisitos, validação e riscos dos controles usuais.

A consulta das visões gerais não representa leitura integral das subpáginas, suporte universal do token, disponibilidade gratuita ou configuração de produção. Cada módulo escolhido exige confirmação atual de setup, API, plano e escopo. A [bateria de testes](../skills/cloudflare-ops/references/testes-e-momento.md) define evidências por controle e momento.

Validação local desta entrega: 10 testes do helper Coolify e 10 testes do instalador passaram, compileall e diff-check sem erros; catálogo conferido com 138 entradas únicas e links locais válidos. Scan direcionado dos arquivos da entrega sem credenciais identificadas. CI remoto deve confirmar o HEAD do PR.

Versão preparada: 1.3.0. Não há nova tag/release publicada nesta entrega; instruções fixadas na release 1.2.0 foram preservadas. Nenhuma mudança de infraestrutura ou compra foi realizada.
