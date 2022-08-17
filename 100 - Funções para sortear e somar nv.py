from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores:', end=' ')
    for i in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print(' FIM!')
    print('-' * 40)
def somapar(lista):
    print(f'Somando os valores pares: de {lista}', end='')
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f' Temos {soma}')
    print('-' * 40)

n = []
sorteio(n)
somapar(n)