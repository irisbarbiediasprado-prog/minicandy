# TESTING.md — Estratégia de Validação do MiniCandy

## Objetivo

O MiniCandy utiliza o próprio CLI como ferramenta de validação.

Sempre valide a menor parte possível do sistema antes de executar o pipeline completo.

## Pirâmide de Validação

    mc icon import
            │
            ├── Importer
            ▼
    mc scan
            │
            ├── Banco
            ▼
    mc generate
            │
            ├── Geradores
            ▼
    mc build
            │
            ├── Android
            ▼
    mc install
            │
            ├── Instalação
            ▼
    mc apply
            │
            └── Pipeline completo

## Qual comando executar?

### Importer

    ./mc icon import settings

### Banco

    ./mc scan

### Geradores

    ./mc generate

### Android

    ./mc build

### Instalação

    ./mc install

### Pipeline completo

    ./mc apply <icone>

## Ordem

    Implementar
            ↓
    Validar a menor unidade afetada
            ↓
    Commit
            ↓
    Push

## Princípios

- Valide apenas o que mudou.
- Use o menor comando capaz de provar a alteração.
- Execute `mc apply` apenas para validar integração.
- Quanto menor o escopo do teste, mais rápido é o diagnóstico.
