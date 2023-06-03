class Meta(type):
    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Pessoa(metaclass=Meta):

    def __new__(cls, *args, **kwargs):
        print('O método __new__ foi chamado')
        return super().__new__(cls)

    def __init__(self, nome):
        print('O método __init__ foi chamado')
        self.nome = nome

    # Método mágico que retorna a representação em string do objeto
    def __call__(self, x, y):
        print('Chamando o método call', self.nome, x + y)


if __name__ == '__main__':
    p1 = Pessoa('Luiz')

