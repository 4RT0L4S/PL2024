import re

def somador_on_off(texto):
    soma = 0
    somar = False  # O somador começa desligado
    resultado = []

    # Divide o texto em partes baseado em 'On', 'Off' ou '='
    partes = re.split('(on|off|=)', texto, flags=re.IGNORECASE)

    for parte in partes:
        if re.match('on', parte, re.IGNORECASE):
            somar = True
        elif re.match('off', parte, re.IGNORECASE):
            somar = False
        elif parte == "=":
            resultado.append(str(soma))
        else:
            if somar:
                # Soma todos os números encontrados na parte atual do texto
                numeros = re.findall(r'\d+', parte)
                soma += sum(int(numero) for numero in numeros)

    return ' '.join(resultado)

# Teste do programa
texto = "123abcdefong45ttt 1 pp==off=12onoffon33=="
print(somador_on_off(texto))