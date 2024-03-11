import ply.lex as lex

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'VIRGULA',
    'NUMERO',
    'IGUAL',
    'PONTO',
    'PONTOVIRGULA',
    'MAIOR',
    'MENOR',
    'MAIOReIGUAL',
    'MENOReIGUAL',
    'VARIAVEL'
)

t_SELECT = r'Select'
t_FROM = r'From'
t_WHERE = r'Where'
t_VIRGULA = r'\,'
t_NUMERO = r'\d+'
t_PONTO = r'\.'
t_PONTOVIRGULA = r'\;'
t_IGUAL = r'\='
t_MAIOR = r'\>'
t_MENOR = r'\<'
t_MAIOReIGUAL = r'\>\='
t_MENOReIGUAL = r'\<\='

def t_VARIAVEL(t):
    r'[a-zA-Z_]\w*'
    if t.value == 'Select':
        t.type = 'SELECT'
    elif t.value == 'From':
        t.type = 'FROM'
    elif t.value == 'Where':
        t.type = 'WHERE'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        data = f_in.read()
        lexer.input(data)

        while True:
            tok = lexer.token()
            if not tok:
                break
            f_out.write(f"{tok.value} = {tok.type}\n")

if __name__ == '__main__':
    main()
