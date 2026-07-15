# ADR-0001 — Mobile First

Status: Aceito

## Contexto

O MiniCandy nasceu para ser desenvolvido prioritariamente em um dispositivo Android utilizando Termux.

A arquitetura não deve depender de Android Studio ou de um computador para as tarefas essenciais de desenvolvimento.

## Decisão

O MiniCandy será um SDK mobile-first.

Toda funcionalidade deve considerar o desenvolvimento local no Android como ambiente de primeira classe.

Quando possível, comandos como:

- mc doctor
- mc setup android
- mc sync
- mc build
- mc install
- mc release

devem funcionar integralmente no Termux.

## Consequências

### Positivas

- Desenvolvimento em qualquer lugar.
- Ambiente reproduzível.
- Menor dependência de ferramentas externas.
- Experiência consistente.

### Negativas

- A CLI precisará abstrair diferenças entre Termux e desktop.
- Algumas integrações exigirão tratamento específico para Android.

## Motivação

Reduzir a carga cognitiva do desenvolvedor e permitir que a criatividade aconteça em qualquer lugar.

