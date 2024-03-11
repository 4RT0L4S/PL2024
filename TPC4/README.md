# Somador On/Off

## Autor

Tiago Azevedo Campos Moreira, A100541

## Descrição

Este programa constroi um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
Select id, nome, salario From empregados Where salario >= 820
Funcionalidades : 
- 'SELECT',
- 'FROM',
- 'WHERE',
- 'VIRGULA',
- 'NUMERO',
- 'IGUAL',
- 'PONTO',
- 'PONTOVIRGULA',
- 'MAIOR',
- 'MENOR',
- 'MAIOReIGUAL',
- 'MENOReIGUAL',
- 'VARIAVEL'

## Funcionamento

O programa analisa um ficheiro input e traduz cada elemento numa das funcionalidades existentes, atribuindo lhe um tipo e escrevendo no ficheiro output a respetiva atribuiçao.