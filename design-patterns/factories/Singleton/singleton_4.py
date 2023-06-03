from typing import Dict


class Singleton(type):
    __instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class MyClass(metaclass=Singleton):
    def __init__(self):
        self.name = 'MyClass'
        self.font = 'Arial'
        self.size = 12


if __name__ == '__main__':
    s1 = MyClass()
    s1.name = 'Singleton'

    s2 = MyClass()
    s3 = MyClass()

    print(s3.font)
    print(s1 == s2 == s3)
