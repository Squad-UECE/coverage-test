

class SemCombustivel(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.default_message = "Sem combustivel"
        super().__init__(self.default_message, *args, **kwargs)


class CarroDesligado(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.default_message = "Carro desligado"
        super().__init__(self.default_message, *args, **kwargs)
