

class SemCombustivel(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.default_message = "Sem combustivel"
        super().__init__(self.default_message, *args, **kwargs)


class VeiculoDesligado(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.default_message = "Veiculo desligado"
        super().__init__(self.default_message, *args, **kwargs)
