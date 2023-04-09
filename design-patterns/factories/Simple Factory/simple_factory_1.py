"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando o cliente...")


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto de luxo está buscando o cliente...")


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto popular está buscando o cliente...")


class VeiculoFactory:
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


if __name__ == "__main__":
    from random import choice

    veiculos_disponiveis = ["carro_luxo", "carro_popular", "moto_popular", "moto_luxo"]

    for veiculos in range(10):
        veiculo = VeiculoFactory.get_veiculo(choice(veiculos_disponiveis))
        veiculo.buscar_cliente()
