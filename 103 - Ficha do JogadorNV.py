def ficha(n=False, g=False):
    if n:
        a = n
    if g:
        b = g
    if not n:
        a = '<DESCONHECIDO'
    if not g:
        b = 0
    return f'O jogador {a} fez {b} gols no campeonato!'

nome = str(input("Nome do jogador ?"))
gols = str(input("Quantidade de gols ?"))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(nome, gols))