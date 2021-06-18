from src.leilao.dominio import Usuario, Lance, Leilao

jean = Usuario('Jean')
dani = Usuario('Dani')

lance_jean = Lance(jean, 100.0)
lance_dani = Lance(dani, 150.0)

leilao = Leilao('O item leiloado nesta seção é um PS5')

leilao.propor_lance(lance_jean)
leilao.propor_lance(lance_dani)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de {lance.valor}")

