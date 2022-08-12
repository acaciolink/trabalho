jogador = dict()
gols = list()
lista = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
    gols.clear()
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols da na partida{i+1}: ?')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    copia = jogador.copy()
    lista.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar ?")).upper().strip()
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15} ',end='')
print()
print('-='*30)
for k,v in enumerate(lista):
    print(f'{k:>2} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

while True:
    resp = int(input("Mostrar dados de qual jogador ? (999 para parar): "))
    if resp == 999:
        break
    if resp >= len(lista):
        print(f'ERRO! Não existe jogador com código {resp}')
    else:
        print(f'== LEVANTAMENTO DO JOGADOR {lista[resp]["nome"]}')
        for i,g in enumerate(lista[resp]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-=' * 30)