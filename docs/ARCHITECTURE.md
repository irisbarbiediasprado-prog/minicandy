# Arquitetura

## Filosofia

O MiniCandy é um SDK para desenvolvimento de icon packs Android.

Toda lógica fica em módulos reutilizáveis.

Os comandos apenas orquestram.

## Estrutura

cli/
├── commands/      # Interface da CLI
├── core/          # Infraestrutura compartilhada
├── database/      # Banco de dados do projeto
├── doctor/        # Auditorias
├── generators/    # Geração de arquivos Android
├── models/        # Modelos
├── services/      # Serviços reutilizáveis
└── utils/         # Utilitários

assets/
├── pixelart/
└── database/

app/
└── Projeto Android

## Pipeline

PNG
 │
 ▼
mc icon import
 │
 ▼
mc scan
 │
 ▼
icons.json
 │
 ▼
mc generate
 │
 ▼
drawable.xml
appfilter.xml
 │
 ▼
mc stats
 │
 ▼
mc build
 │
 ▼
mc install
 │
 ▼
mc release

## Princípios

- Simplicidade
- Zero dependências externas
- Desenvolvimento no Termux
- Um comando, uma responsabilidade
- Reutilização acima de duplicação
