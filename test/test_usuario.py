import pytest

from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes.lance_invalido import LanceInvalido


@pytest.fixture
def joao():
    return Usuario('João', 100.0)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_o_valor_da_carteira_quando_usuario_propor_um_lance(joao, leilao):
    joao.propor_lance(leilao, 50.0)
    assert joao.carteira == 50.0


def test_deve_permitir_propor_lance_quando_valor_eh_menor_que_a_carteira(joao, leilao):
    joao.propor_lance(leilao, 1.0)
    assert joao.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(joao, leilao):
    joao.propor_lance(leilao, 100.0)
    assert joao.carteira == 0.0


def test_nao_deve_permitir_propor_lance_quando_o_valor_eh_maior_que_o_da_carteira(joao, leilao):
    with pytest.raises(LanceInvalido):
        joao.propor_lance(leilao, 200.0)
