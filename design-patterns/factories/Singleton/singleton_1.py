"""
Singleton tem a intenção de garantir que uma classe tenha somente uma instância e fornecer um ponto global de acesso a ela.
"""


class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self):
        self.tema = 'Tema padrão'
        self.font = 'Fonte padrão'


if __name__ == '__main__':
    s1 = Singleton()

    s1.tema = 'Tema alterado'
    print(s1.tema)

    s2 = Singleton()
    print(s1.tema)
