# Contribuir

Abra issue com comportamento esperado/observado e versão, usando dados fictícios. Mantenha instruções reutilizáveis e scripts sem dependências desnecessárias. Não adicione alvos fixos ou autorização implícita para mutações.

Antes de propor PR:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 -m compileall -q scripts
git diff --check
```

Novas decisões de segurança exigem teste de regressão. Testes não usam credenciais ou rede real. Atualize documentação e changelog. Releases usam tag `vMAJOR.MINOR.PATCH`, notas e arquivos de distribuição com SHA-256. Não publique execução operacional como prova de proteção universal.
