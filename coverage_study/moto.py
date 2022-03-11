from . import exceptions


class Moto:

    def __init__(self, marca, modelo, cor, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.ano = ano
        self.combustivel = 100
        self.ligado = False

    def __repr__(self) -> str:
        return f"<Moto({self.marca}, {self.modelo}, {self.cor})>"

    # decorators
    def _ligado(func):
        def wrapper(self, *args, **kwargs):
            if self.ligado:
                return func(self, *args, **kwargs)
            else:
                raise exceptions.VeiculoDesligado
        return wrapper

    def _combustivel(func):
        def wrapper(self, *args, **kwargs):
            if self.combustivel:
                return func(self, *args, **kwargs)
            else:
                raise exceptions.SemCombustivel
        return wrapper

    # methods
    def ligar(self):
        self.ligado = True
        print("ligado")
        return self.ligado

    @_ligado
    def desligar(self):
        self.ligado = False
        print("desligado")
        return self.ligado

    @_ligado
    @_combustivel
    def andar(self, km):
        print("." * km + "🛵")
        self.combustivel = max(0, self.combustivel - (10 * km))

    def abastecer(self):
        print("tanque cheio")
        self.combustivel = 100
