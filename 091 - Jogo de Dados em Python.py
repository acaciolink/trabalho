from random import randint
from time import sleep
dicionario = {}
print('Valores sorteados: ')
for i in range(1, 5):
    dicionario[f'Jogador{i}'] = randint(1, 6)
for k, v in dicionario.items():
    sleep(0.5)
    print(f'O {k} tirou {v} no dado')
print('-------------------------------------')
print('------ RANKING DOS JOGADORES --------')
j = 1
for i in sorted(dicionario, key=dicionario.get, reverse=True):
    sleep(0.5)
    print(f'{j}° Lugar: {i} com {dicionario[i]}')
    j += 1
print('-------------------------------------')