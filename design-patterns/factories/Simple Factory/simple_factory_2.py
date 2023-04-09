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
    def __init__(self, tipo: str) -> None:
        self.veiculo = self.get_veiculo(tipo)

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

    def get_cliente(self) -> None:
        self.veiculo.buscar_cliente()


if __name__ == "__main__":
    from random import choice

    veiculos_disponiveis = ["carro_luxo", "carro_popular", "moto_popular", "moto_luxo"]

    for veiculos in range(10):
        veiculo = VeiculoFactory(choice(veiculos_disponiveis))
        veiculo.get_cliente()
