import ply.lex as lex

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'COMMA',
    'OPERATOR',
    'NUMBER'
)

t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_FROM = r'[fF][Rr][Oo][Mm]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_COMMA = r','
t_OPERATOR = r'>='

def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    reserved_keywords = {
        'SELECT': 'SELECT',
        'FROM': 'FROM',
        'WHERE': 'WHERE'
    }
    t.type = reserved_keywords.get(t.value.upper(), 'IDENTIFIER')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore  = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

data = 'Select id, nome, salário from empregados WHERE salário >= 820'
lexer.input(data)

for token in lexer:
    print(token)