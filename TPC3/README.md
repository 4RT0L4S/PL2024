# Somador On/Off

## Autor

Tiago Azevedo Campos Moreira, A100541

## Descrição

Este programa em Python implementa um somador on/off que soma todas as sequências de dígitos encontradas em um texto. Ele respeita os seguintes requisitos:

- Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é desligado.
- Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é novamente ligado.
- Sempre que encontrar o caractere “=”, o resultado da soma é colocado na saída.

## Funcionamento

O programa analisa o texto linha por linha, identificando as palavras "On" e "Off" para ligar e desligar a soma, respectivamente. Em seguida, ele encontra todas as sequências de dígitos em cada linha e as soma se o comportamento de soma estiver ligado. Quando o caractere "=" é encontrado, o resultado da soma é impresso na saída.