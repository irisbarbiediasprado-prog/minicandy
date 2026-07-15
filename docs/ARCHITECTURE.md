# Arquitetura

## Visão

O MiniCandy é um SDK mobile-first para desenvolvimento de icon packs Android.

A CLI é apenas uma interface.

Toda lógica de negócio deve existir em módulos reutilizáveis.

O desenvolvimento acontece prioritariamente no Termux.

---

## Princípios Arquitetônicos

### Carga Cognitiva

O MiniCandy existe para reduzir a carga cognitiva do desenvolvedor.

Toda nova funcionalidade deve responder à pergunta:

"Isso reduz ou aumenta a quantidade de coisas que o usuário precisa lembrar?"

Se aumentar, provavelmente está na camada errada.

---

### Comandos representam intenções

Um comando nunca representa uma implementação.

Correto:

mc build
mc release
mc install
mc doctor

Evitar:

gradlew assembleDebug
python generate.py
python scan.py

---

### Camadas

commands/
        │
        ▼
android/
database/
doctor/
generators/
setup/
        │
        ▼
Projeto Android

Os comandos apenas orquestram.

Toda regra de negócio pertence às camadas inferiores.

---

## Estrutura

cli/

├── commands/      Interface da CLI
├── android/       Build, Install e Release
├── database/      Banco de dados do projeto
├── doctor/        Auditorias
├── generators/    Geradores Android
├── core/          Infraestrutura compartilhada
├── models/        Modelos
├── services/      Serviços reutilizáveis
└── utils/         Utilitários

assets/

├── pixelart/
└── database/

app/

Projeto Android

---

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
mc build
 │
 ▼
mc install
 │
 ▼
mc release

---

## Filosofia de Desenvolvimento

Infraestrutura antes de funcionalidades.

Automação antes de documentação.

Reutilização antes de duplicação.

Um módulo deve possuir apenas uma responsabilidade.

Sempre que uma tarefa exigir vários comandos consecutivos, ela deve ser candidata a um novo comando do MiniCandy.

---

## Objetivo

Permitir que um desenvolvedor crie, compile, teste e publique um icon pack Android utilizando apenas um dispositivo Android.

