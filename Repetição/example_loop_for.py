"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

Estrutura C ou Java:

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python:

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
- Dicionário
    dicionario = {'nome': 'Geek', 'idade': 40}
- Conjunto
    conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
- Arquivo
    arquivo = open('texto.txt')
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):  # range(valor_inicial, valor_final)
    print(numero)