class Funcionario():
    aumento = 1.04

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}

    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento

    @classmethod
    def definir_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento

    @classmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True


if __name__ == '__main__':
    funcionario = Funcionario('João', 5000)
    print(funcionario.dados())
    funcionario.aplicar_aumento()
    print(funcionario.dados())

    Funcionario.definir_novo_aumento(1.05)
    funcionario.aplicar_aumento()
    print(funcionario.dados())

    import datetime

    minha_data = datetime.date(2019, 4, 20)  # 20/04/2019 - Sábado
    print(Funcionario.dia_util(minha_data))
