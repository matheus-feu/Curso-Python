"""
Este exemplo mostra como usar a estrutura condicional com if
"""

x = 10

if x > 5:
    print("x é maior que 5")

"""
Este exemplo mostra como usar a estrutura condicional com if e elif
"""

idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")

"""
Este exemplo mostra como usar a estrutura condicional com if, elif e else
"""

tamanho = 1.80
peso = 80

imc = peso / (tamanho ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")

