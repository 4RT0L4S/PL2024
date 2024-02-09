import pandas as pd

def parse_dataset(filename):
    # Ler o arquivo CSV para um DataFrame do pandas
    df = pd.read_csv(filename)

    # Renomear as colunas para remover caracteres especiais
    df.columns = df.columns.str.replace('/', '_')

    return df

def modalidades_alfabeticamente(df):
    # Lista ordenada alfabeticamente das modalidades desportivas
    modalidades_ordenadas = sorted(df['modalidade'].unique())
    return modalidades_ordenadas

def percentagens_aptos_inaptos(df):
    # Percentagens de atletas aptos e inaptos para a prática desportiva
    total_atletas = df.shape[0]
    aptos = df[df['federado'] == True].shape[0]
    inaptos = df[df['federado'] == False].shape[0]
    percentagem_aptos = (aptos / total_atletas) * 100
    percentagem_inaptos = (inaptos / total_atletas) * 100
    return percentagem_aptos, percentagem_inaptos

def distribuicao_por_idade(df):
    # Distribuição de atletas por escalão etário (intervalo de 5 anos)
    faixas_etarias = []
    for i in range(20, 100, 5):
        faixa = f'[{i}-{i+4}]'
        faixas_etarias.append(faixa)

    distribuicao = {}
    for faixa in faixas_etarias:
        inicio, fim = map(int, faixa.strip('[]').split('-'))
        distribuicao[faixa] = df[(df['idade'] >= inicio) & (df['idade'] <= fim)].shape[0]

    return distribuicao

# Chamada da função para fazer o parsing do arquivo emd.csv
dataset = parse_dataset('C:/AT Local/Ambiente de Trabalho/UNI/PL/emd.csv')

# Lista ordenada alfabeticamente das modalidades desportivas
modalidades = modalidades_alfabeticamente(dataset)
print("Modalidades desportivas ordenadas alfabeticamente:")
print(modalidades)

# Percentagens de atletas aptos e inaptos para a prática desportiva
aptos, inaptos = percentagens_aptos_inaptos(dataset)
print("\nPercentagem de atletas aptos:", aptos)
print("Percentagem de atletas inaptos:", inaptos)

# Distribuição de atletas por escalão etário (intervalo de 5 anos)
distribuicao_idade = distribuicao_por_idade(dataset)
print("\nDistribuição de atletas por escalão etário:")
for faixa, quantidade in distribuicao_idade.items():
    print(f"{faixa}: {quantidade}")
