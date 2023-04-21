class Funcionario():
    """Classe de funcionário"""

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        """Função de ler os próprios dados dele"""
        return {'nome': self.nome, 'salario': self.salario}


class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome, salario):
        """Função de atualizar os dados do funcionário"""
        self.nome = nome
        self.salario = salario

        return self.dados()


if __name__ == '__main__':
    admin = Admin('José', 14000)
    funcionario = Funcionario('João', 5000)

    print(admin.dados())
    print(funcionario.dados())

    print(admin.atualizar_dados('José Aldo', 8000))