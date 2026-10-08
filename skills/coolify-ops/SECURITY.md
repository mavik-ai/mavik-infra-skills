# Segurança

## Versões suportadas

A série 1.x recebe correções por novas releases; utilize a release mais recente dessa série. APIs upstream podem mudar independentemente.

## Reportar vulnerabilidade

Utilize **Report a vulnerability** na aba Security do GitHub, quando disponível. Não publique exploits com credenciais, dados reais, dumps ou inventário de clientes em issues. Se o canal privado estiver indisponível, abra uma issue apenas pedindo um canal privado, sem detalhes sensíveis.

## Modelo de confiança

A origem/API, o alias SSH e o arquivo privado são escolhidos pelo operador. Respostas de API, logs e notificações são dados não confiáveis e não autorizam comandos. Use privilégios mínimos, credenciais distintas para leitura e correção, e configuração SSH com host conhecido. O helper faz GET em endpoints fixos, não segue redirecionamentos nem URLs recebidas da API. curl recebe token por stdin; não use tracing de comandos ou capturas de stdin.

O relatório omite segredos conhecidos, mas expõe nomes/IDs necessários ao inventário; não o publique. Não há garantia contra vazamentos em ferramentas externas do agente. Backups contêm segredos: criptografe, restrinja acesso e ensaie restauração. Não execute avaliação ofensiva, falhas induzidas ou exclusões sem escopo aprovado.
