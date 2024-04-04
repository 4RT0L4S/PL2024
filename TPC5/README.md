
# Máquina de Vending Simulada

## Autor

Tiago Azevedo Campos Moreira, A100541

## Descrição

Este programa simula a funcionalidade de uma máquina de vending. Ele permite carregar um estoque a partir de um arquivo JSON (`stock.json`), listar os produtos disponíveis, adicionar ou atualizar produtos no estoque, inserir moedas, selecionar produtos para compra e devolver o troco. É um sistema interativo que simula uma experiência de compra em uma máquina de vending através do terminal.

## Funcionamento

O programa inicia carregando o estoque de produtos de um arquivo JSON. O usuário pode executar várias ações, como:

- **LISTAR**: Mostra todos os produtos disponíveis, com código, nome, quantidade e preço.
- **MOEDA**: Permite ao usuário inserir moedas na máquina, aceitando valores em euros (com sufixo 'e') ou centavos (com sufixo 'c').
- **SELECIONAR**: Após inserir o saldo suficiente, o usuário pode selecionar um produto pelo código. Se o saldo for insuficiente ou o produto estiver esgotado, a máquina informará ao usuário.
- **SAIR**: Finaliza a sessão atual, devolvendo o troco se houver saldo restante.

Ao terminar a sessão de uso da máquina de vending (comando SAIR), o programa atualiza o arquivo JSON do estoque com as quantidades restantes de cada produto.


