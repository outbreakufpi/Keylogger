# Keylogger Simples com `pynput`

Este é um projeto básico que implementa um keylogger utilizando a biblioteca `pynput` em Python. O programa registra as teclas pressionadas em um arquivo de texto especificado.

## Aviso Legal

Este código é destinado **somente para uso pessoal** e **para fins educacionais**. Ele deve ser utilizado **somente em dispositivos que você tem permissão para monitorar**. Qualquer uso indevido do código, como monitorar ou registrar as atividades de outras pessoas sem seu consentimento, **é estritamente proibido** e pode ser **ilegal**, de acordo com as leis de privacidade e proteção de dados pessoais, como a **Lei Geral de Proteção de Dados (LGPD)**.

**Eu não me responsabilizo por qualquer uso indevido do código**, e **qualquer pessoa que use este código é totalmente responsável por suas ações**. O uso deste código em dispositivos de outras pessoas sem permissão pode resultar em **violações de privacidade** e **consequências legais**.

**Use com responsabilidade.**


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
