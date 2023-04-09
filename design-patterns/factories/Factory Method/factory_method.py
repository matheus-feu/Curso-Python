"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def get_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def get_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente...")


class CarroPopular(Veiculo):
    def get_cliente(self) -> None:
        print("Carro popular está buscando o cliente...")


class MotoLuxo(Veiculo):
    def get_cliente(self) -> None:
        print("Moto de luxo está buscando o cliente...")


class MotoPopular(Veiculo):
    def get_cliente(self) -> None:
        print("Moto popular está buscando o cliente...")


class VeiculoFactory(ABC):
    def __init__(self, tipo: str) -> None:
        self.veiculo = self.get_veiculo(tipo)

    @staticmethod
    @abstractmethod
    def get_veiculo(tipo: str) -> Veiculo:
        pass

    def get_cliente(self) -> None:
        self.veiculo.get_cliente()


class ZNVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:
        if tipo == "carro_luxo":
            return CarroLuxo()
        if tipo == "carro_popular":
            return CarroPopular()
        if tipo == "moto_popular":
            return MotoPopular()
        if tipo == "moto_luxo":
            return MotoLuxo()
        assert 0, "O Veículo não existe"


class ZSVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:
        if tipo == "carro_luxo":
            return CarroLuxo()
        if tipo == "moto_luxo":
            return MotoLuxo()
        assert 0, "O Veículo não existe"


if __name__ == "__main__":
    from random import choice

    veiculos_disponiveis_zn = ["carro_luxo", "carro_popular", "moto_popular", "moto_luxo"]
    veiculos_disponiveis_zs = ["carro_luxo", "moto_luxo"]

    print("Veiculos da Zona Norte:\n")

    for veiculos in range(10):
        veiculo = ZNVeiculoFactory(choice(veiculos_disponiveis_zn))
        veiculo.get_cliente()

    print()

    print("Veiculos da Zona Sul:\n")

    for veiculos in range(10):
        veiculo = ZSVeiculoFactory(choice(veiculos_disponiveis_zs))
        veiculo.get_cliente()
