from src.leilao.excecoes.lance_invalido import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propor_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise LanceInvalido('Valor proposto não pode ser maior do que o valor da carteira do usuário!')

        lance = Lance(self, valor)
        leilao.propor_lance(lance)
        self.__carteira -= valor


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.menor_lance = 0.0
        self.maior_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def propor_lance(self, lance: Lance):
        if self._lance_valido(lance):
            self._aplica_lance(lance)

    def _tem_lances(self):
        return self.lances

    def _usuario_eh_diferente(self, lance):
        if self.lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('Os usuário deste lance deve ser diferente do usuário do último lance!')

    def _valor_eh_maior_que_do_ultimo_lance(self, lance):
        if lance.valor > self.lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance atual deve ser maior do que o valor do último lance!')

    def _lance_valido(self, lance):
        return not self._tem_lances() or (self._usuario_eh_diferente(lance) and
                                          self._valor_eh_maior_que_do_ultimo_lance(lance))

    def _aplica_lance(self, lance):
        if not self._tem_lances():
            self.menor_lance = lance.valor

        self.maior_lance = lance.valor

        self.__lances.append(lance)

    def __str__(self):
        return (
            f"O leilão do item {self.descricao} teve como menor lance o valor de {self.menor_lance}"
            f"e o maior lance no valor de {self.maior_lance}."
        )
