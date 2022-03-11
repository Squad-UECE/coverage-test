import pytest

from coverage_study import __version__
from coverage_study.main import Carro
from coverage_study import exceptions

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def carro():
    return Carro('Fiat', 'Palio', 'Prata', 'ABC-4040', 2010)


class TestCarro:
    def test__ligado(self, carro):
        assert Carro._ligado(lambda x: x).__name__ == 'wrapper'

    def test__combustivel(self, carro):
        carro.combustivel = 0
        with pytest.raises(
            exceptions.SemCombustivel
        ) as sem_combustivel:
            Carro._combustivel(lambda x: x)(carro)

        assert "Sem combustivel" in str(sem_combustivel.value)

    def test_init(self, carro):
        assert isinstance(carro, Carro) == True

    def test_repr(self, carro):
        assert "Carro(" in repr(carro)

    # def test_ligar(self, carro):
    #     assert carro.ligar() == True, "Error"

    def test_desligar_erros(self, carro):
        with pytest.raises(
            exceptions.CarroDesligado
        ) as sem_combustivel:
            carro.desligar()
        
        assert "Carro desligado" in str(sem_combustivel.value)

    def test_desligar(self, carro):
        carro.ligar()
        assert carro.desligar() == False

    def test_andar(self, carro):
        carro.ligar()
        assert carro.andar(10) == None

    # def test_quando_anda_combustivel_diminui(self, carro):
    #     old_combustivel = carro.combustivel
    #     carro.ligar()
    #     carro.andar(10)
    #     assert old_combustivel > carro.combustivel
    
    def test_abastecer(self, carro):
        carro.abastecer()
        assert carro.combustivel == 100
