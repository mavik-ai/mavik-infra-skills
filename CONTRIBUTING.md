# Contribuir

Abra issue com escopo por skill e exemplos fictícios. Mudanças independentes devem ter PRs separados. Não incluir dados/segredos/relatórios reais. Instruções devem preservar autorização e consultar capacidades do plano/versão.

Execute os comandos de validação do README, revise referências locais e campos YAML. Nova lógica não trivial precisa regressão; alterações documentais precisam revisão comportamental. Não transformar exemplos de fornecedor em alvo padrão. Releases do pacote: tag vX.Y.Z, changelog por skill, pacotes individuais/completo e checksums.

O instalador é validado com `python3 -m unittest discover -s scripts -p 'test_*.py'`, sempre em destinos temporários. Não use instalações reais para testar substituição ou falhas.
