
# Gramática Independente de Contexto

## Autor

Tiago Azevedo Campos Moreira, A100541

## Implementação

### Terminais
    T = {'?', 'var', '=', '*', 'num', '/', '(', ')', '-', '!'}

### Não-terminais
    N = {S, Atribuição, Expressão, Termo, Fator}

### Símbolo Inicial
    S

### Produções
    S -> '?' Atribuição 
        | '!' Expressão 
        | var '=' Expressão
    LA(S) = {'?', '!', 'var'}

    Atribuição -> var '=' Expressão
    LA(Atribuição) = {var}

    Expressão -> Termo 
        | Expressão '+' Termo 
        | Expressão '-' Termo
    LA(Expressão) = {'num', '('}

    Termo -> Fator 
        | Termo '*' Fator 
        | Termo '/' Fator
    LA(Termo) = {'num', '('}

    Fator -> 'num' 
        | '(' Expressão ')'
    LA(Fator) = {'num', '('}
