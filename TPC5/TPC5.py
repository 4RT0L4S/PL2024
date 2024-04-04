import json

# Caminho para o arquivo JSON do stock
STOCK_FILE_PATH = 'stock.json'

def load_stock():
    try:
        with open(STOCK_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_stock(stock):
    with open(STOCK_FILE_PATH, 'w') as file:
        json.dump(stock, file, indent=4)

def list_products(stock):
    if not stock:
        print("Nenhum produto disponível.")
        return
    print("cod | nome | quantidade | preço")
    print("--------------------------------")
    for item in stock:
        print(f'{item["cod"]}  {item["nome"]}  {item["quant"]}  {item["preco"]}')

def add_or_update_product(stock, cod, nome, quant, preco):
    updated = False
    for item in stock:
        if item['cod'] == cod:
            item['quant'] += quant
            updated = True
            break
    if not updated:
        stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})

def insert_coins(saldo):
    print("Insira suas moedas (e para euros, c para centavos, 'fim' para terminar):")
    while True:
        coin = input("Moeda: ")
        if coin == 'fim':
            break
        try:
            if coin.endswith('e'):
                saldo += float(coin[:-1])
            elif coin.endswith('c'):
                saldo += float(coin[:-1]) / 100
            else:
                print("Formato inválido. Use 'e' para euros e 'c' para centavos.")
                continue
        except ValueError:
            print("Valor inválido. Tente novamente.")
    return saldo

def select_product(stock, saldo):
    cod = input("Código do produto: ")
    for item in stock:
        if item['cod'] == cod:
            if item['quant'] <= 0:
                print("Produto esgotado.")
                return saldo, False
            if saldo < item['preco']:
                print("Saldo insuficiente.")
                return saldo, False
            item['quant'] -= 1
            saldo -= item['preco']
            print(f'Produto dispensado: {item["nome"]}. Saldo restante: {saldo:.2f}e.')
            return saldo, True
    print("Produto não encontrado.")
    return saldo, False

def return_change(saldo):
    if saldo > 0:
        print(f"Devolvendo troco de {saldo:.2f}e.")
    else:
        print("Nenhum troco para devolver.")

def init_vending_machine():
    stock = load_stock()
    print("Bem-vindo à máquina de vending!")
    saldo = 0
    while True:
        print("\nComandos disponíveis: LISTAR, MOEDA, SELECIONAR, SAIR")
        cmd = input(">> ").upper()
        if cmd == "LISTAR":
            list_products(stock)
        elif cmd == "MOEDA":
            saldo = insert_coins(saldo)
            print(f"Saldo atual: {saldo:.2f}e")
        elif cmd == "SELECIONAR":
            saldo, _ = select_product(stock, saldo)
        elif cmd == "SAIR":
            return_change(saldo)
            break
        else:
            print("Comando desconhecido.")
    save_stock(stock)

if __name__ == '__main__':
    init_vending_machine()
