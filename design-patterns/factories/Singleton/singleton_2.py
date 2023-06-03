def singleton(the_class):
    instances = {}

    def get_instance(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_instance


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'Tema padrão'
        self.font = 'Fonte padrão'


@singleton
class Teste:
    def __init__(self):
        print('TESTE')


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema alterado'
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
