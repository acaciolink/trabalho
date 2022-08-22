dicionario = dict()
gols = list()

dicionario['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou ?'))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols da na partida{i+1}: ?')))
dicionario['gols'] = gols[:]
dicionario['total'] = sum(gols)
print("=-"*40)
print(dicionario)
print("=-"*40)
for k,v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print("=-"*40)
print(f'O jogador {dicionario["nome"]} jogou {partidas} partidas')
for i,gol in enumerate(gols):
    print(f'Na {i+1}° partida, fez {gol} ')
print(f'Foi um total de {sum(gols)} gols')
print("=-"*40)