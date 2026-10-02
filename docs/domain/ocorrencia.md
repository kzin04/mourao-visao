# Ocorrência

## Definição

Uma ocorrência representa um problema urbano identificado pelo
Mourão Visão e que pode ser submetido à validação e atendimento.

## Atributos

| Campo | Descrição | Obrigatório |
|---|---|---|
| id | Identificador único | Sim |
| tipo | Tipo do problema | Sim |
| status | Estado atual | Sim |
| prioridade | Prioridade operacional | Sim |
| latitude | Latitude do problema | Sim |
| longitude | Longitude do problema | Sim |
| descricao | Descrição complementar | Não |
| criada_em | Data de criação | Sim |
| atualizada_em | Data da última atualização | Sim |

## Estados

- PENDENTE
- VALIDADA
- PROGRAMADA
- EM_EXECUCAO
- RESOLVIDA
- DESCARTADA


## Regras de negócio

- Uma ocorrência representa um problema urbano consolidado.
- Uma ocorrência pode possuir múltiplas detecções.
- Uma detecção representa uma observação individual realizada pelo sistema.
- A prioridade não deve depender exclusivamente da confiança da IA.
- Uma ocorrência pode ser validada, programada, executada, resolvida ou descartada.
- Alterações relevantes de status deverão ser registradas em histórico.
- A localização da ocorrência deve representar o local do problema, e não necessariamente a localização atual do veículo.