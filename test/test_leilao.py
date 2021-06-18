from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes.lance_invalido import LanceInvalido


class TestLeilao(TestCase):
    def setUp(self):
        self.joao = Usuario('João', 500.0)
        self.lance_joao = Lance(self.joao, 100.0)
        self.leilao = Leilao('O item leiloado nesta seção será um PS5')
        self.leilao.propor_lance(self.lance_joao)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_tiver_lances_em_ordem_crescente(self):
        maria = Usuario('Maria', 500.0)
        lance_maria = Lance(maria, 150.0)
        self.leilao.propor_lance(lance_maria)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_lances_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            maria = Usuario('Maria', 500.0)
            lance_maria = Lance(maria, 90.0)
            self.leilao.propor_lance(lance_maria)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_tiver_apenas_um_lance(self):
        menor_valor_esperado = 100.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quanto_tiver_tres_lances(self):
        maria = Usuario('Maria', 500.0)
        jose = Usuario('José', 500.0)

        lance_maria = Lance(maria, 150.0)
        lance_jose = Lance(jose, 200.00)

        self.leilao.propor_lance(lance_maria)
        self.leilao.propor_lance(lance_jose)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_quando_nao_houver_lances(self):
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

    def test_deve_permitir_propor_um_lance_quando_tiver_usuarios_diferentes(self):
        maria = Usuario('Maria', 500.0)
        lance_maria = Lance(maria, 150.0)
        self.leilao.propor_lance(lance_maria)
        quantidade_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances_recebidos)

    def test_nao_deve_permitir_o_mesmo_usuario_propor_duas_vezes_seguidas(self):
        with self.assertRaises(LanceInvalido):
            lance_joao_200 = Lance(self.joao, 200.0)
            self.leilao.propor_lance(lance_joao_200)
