# Keylogger Simples com `pynput`

Este é um projeto básico que implementa um keylogger utilizando a biblioteca `pynput` em Python. O programa registra as teclas pressionadas em um arquivo de texto especificado.

## ⚠️ Aviso Importante

**Este software é fornecido somente para fins educacionais e/ou uso pessoal. O autor não se responsabiliza por quaisquer ações que utilizem este software de forma inadequada ou para atividades ilegais. Por favor, use este código de forma ética e responsável.**

## Requisitos

- Python 3.6 ou superior
- Biblioteca `pynput`

## Instalação

1. Clone ou baixe este repositório.
2. Certifique-se de que a biblioteca `pynput` está instalada executando o comando:

   ```bash
   pip install pynput

## Como Funciona
O código configura um listener para capturar as teclas pressionadas.

As teclas pressionadas são salvas em um arquivo chamado keyloggeroutput.txt.

O programa encerra a captura quando a tecla ESC é pressionada ou até que feche o terminal.
