""""
Ulitários Python para auxiliar na programação.

dir -> Apresenta todos os atributos e funções/métodos "()" disponíveis para determinado tipo de dado ou variável.

dir(tipo de dado/variável)

help -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponíveis para determinado
tipo de dado ou variável.

help(tipo de dado/variável.propriedade)
"""

# Exemplos
dir('geek')

print('geek'.__len__()) # Saída: 4
print('geek'.upper()) # Saída: GEEK
print('geek'.lower()) # Saída: geek
print('geek'.title()) # Saída: Geek
print('geek'.capitalize()) # Saída: Geek

# Exemplo com a função help
help('geek'.capitalize) # Saída: capitalize() method of builtins.str instance
help('geek'.title) # Saída: title() method of builtins.str instance
