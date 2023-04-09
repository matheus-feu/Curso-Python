"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança para criar objetos, enquanto Abstract Factory usa a composição para criar objetos.

Princípio: programe para interfaces, não para implementações
"""

from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def get_client(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def get_client(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def get_client(self) -> None:
        print('Carro de luxo ZN está sendo entregue para o cliente')


class CarroPopularZN(VeiculoPopular):
    def get_client(self) -> None:
        print('Carro popular ZN está sendo entregue para o cliente')


class MotoPopularZN(VeiculoPopular):
    def get_client(self) -> None:
        print('Moto popular ZN está sendo entregue para o cliente')


class MotoLuxoZN(VeiculoLuxo):
    def get_client(self) -> None:
        print('Moto de luxo ZN está sendo entregue para o cliente')


class CarroLuxoZS(VeiculoLuxo):
    def get_client(self) -> None:
        print('Carro de luxo ZS está sendo entregue para o cliente')


class CarroPopularZS(VeiculoPopular):
    def get_client(self) -> None:
        print('Carro popular ZS está sendo entregue para o cliente')


class MotoPopularZS(VeiculoPopular):
    def get_client(self) -> None:
        print('Moto popular ZS está sendo entregue para o cliente')


class MotoLuxoZS(VeiculoLuxo):
    def get_client(self) -> None:
        print('Moto de luxo ZS está sendo entregue para o cliente')


class VeiculoFactory(ABC):
    """Classe abstrata que define os métodos que serão implementados pelas
    subclasses concretas."""
    @staticmethod
    @abstractmethod
    def get_carro_luxo(self) -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_carro_popular(self) -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo(self) -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_moto_popular(self) -> VeiculoPopular: pass


class ZonaNorteFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()


class ZonaSulFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()


class Cliente:
    def get_vehicles_by_clients(self) -> None:
        for factory in [ZonaNorteFactory(), ZonaSulFactory()]:
            carro_luxo = factory.get_carro_luxo()
            carro_luxo.get_client()

            carro_popular = factory.get_carro_popular()
            carro_popular.get_client()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.get_client()

            moto_popular = factory.get_moto_popular()
            moto_popular.get_client()


if __name__ == "__main__":
    cliente = Cliente()
    cliente.get_vehicles_by_clients()
