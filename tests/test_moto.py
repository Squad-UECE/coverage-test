import pytest

from coverage_study import __version__
from coverage_study.moto import Moto
from coverage_study import exceptions

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def moto():
    return Moto('Honda', 'CG 150CC', 'Vermelha', 'ABC-4041', 2010)


class TestMoto:
    def test__ligado(self, moto):
        assert Moto._ligado(lambda x: x).__name__ == 'wrapper'

    def test__combustivel(self, moto):
        moto.combustivel = 0
        with pytest.raises(
            exceptions.SemCombustivel
        ) as sem_combustivel:
            Moto._combustivel(lambda x: x)(moto)

        assert "Sem combustivel" in str(sem_combustivel.value)

    def test_init(self, moto):
        assert isinstance(moto, Moto) == True

    def test_repr(self, moto):
        assert "Moto(" in repr(moto)

    def test_desligar_erros(self, moto):
        with pytest.raises(
            exceptions.VeiculoDesligado
        ) as sem_combustivel:
            moto.desligar()
        
        assert "Veiculo desligado" in str(sem_combustivel.value)

    def test_desligar(self, moto):
        moto.ligar()
        assert moto.desligar() == False

    def test_andar(self, moto):
        moto.ligar()
        assert moto.andar(10) == None

    def test_abastecer(self, moto):
        moto.abastecer()
        assert moto.combustivel == 100
