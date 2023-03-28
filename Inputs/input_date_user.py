"""
Recebendo dados do usuários, e convertendo para o tipo de dado correto

input() -> Todo dado recebido via input é do tipo String.

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie"""

# Entrada de dados
print("Qual o seu nome? ")

nome = input()  # Input -> Entrada dos dados
print(f'Seja bem vindo(a) {nome}')

idade = input("Qual a sua idade? ")


# Saída
print(f'{nome} tem {idade} anos')

"""
int(idade) -> cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'{nome} nasceu em {2023 - int(idade)}')