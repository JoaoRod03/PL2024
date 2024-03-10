import ply.lex as lex

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'ID',
    'VALOR',
    'SAIR',
    'NUMERO'
]

t_LISTAR = r'listar'
t_MOEDA = r'moeda'
t_SELECIONAR = r'selecionar'
t_SAIR = r'sair'
t_ignore = ' \t,'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]+'
    t.type = 'ID'
    return t

def t_VALOR(t):
    r'\d+e|\d+c'
    if 'e' in t.value:
        t.value = int(t.value.split('e')[0]) * 100
    else:
        t.value = int(t.value[:-1])
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f'Carater ilegal: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

products = {1: {'nome': 'Água', 'preco': 50}, 2: {'nome': 'Bolo', 'preco': 60}}
saldo = 0

def adicionar_moeda(valor):
    global saldo
    saldo += valor
    print(f"< SALDO = {saldo//100}e{saldo%100}c")

def listar():
    for id, produto in products.items():
        print(f"< {id} {produto['nome']} {produto['preco']}c")

def selecionar(id):
    global saldo
    if id in products and saldo >= products[id]["preco"]:
        saldo -= products[id]["preco"]
        print(f"< Compra realizada: {products[id]['nome']}. Saldo atual: {saldo//100}e{saldo%100}c")
    else:
        print("< Saldo insuficiente ou produto inexistente!")

def verificar_input(input):
    lexer.input(input)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'LISTAR':
            listar()
        elif tok.type == 'MOEDA':
            adicionar_moeda(tok.value)
        elif tok.type == 'ID':
            selecionar(tok.value)
        elif tok.type == 'SAIR':
            global saldo
            print(f"< Troco = {saldo//100}e{saldo%100}c")
            saldo = 0

while True:
    input = input('>> ')
    verificar_input(input)
    if input == 'SAIR':
        break