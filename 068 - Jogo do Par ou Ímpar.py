from random import randint
v = 0
while True:
    jogador = int(input(' Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input(' Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f' Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR'if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print(' VOCE VENCEU!')
            v += 1
        else:
            print(' VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print(' VOCE VENCEU!')
            v += 1
        else:
            print(' VOCE PERDEU!')
            break
    print(' Vamos jogar novamente...')
print(f' GAME OVER! \nVoce venceu {v} vezes.')
