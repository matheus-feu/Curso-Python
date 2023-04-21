"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    - not, is

Operadores binários:
    - and, or

Regras de funcionamento:
    - Para o 'and', ambos os valores precisam ser True
    - Para o 'or', um ou outro valor precisa ser True
    - Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
    - Para o 'is', o valor é comparado com um segundo.
"""

# Variáveis do tipo booleano
ativo = True
logado = True

# Exemplo de utilização do 'and'
if ativo and logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# Exemplo de utilização do 'or'
if ativo or logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# Exemplo de utilização do 'not'
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem vindo usuário')


# Exemplo de utilização do 'is'
if ativo is True:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
