while (True):
    primeiro = int(input(' Primeiro termo:  '))
    razao = int(input(' Razão: '))
    decimo = primeiro + ( 10 - 1) * razao
    for c in range(primeiro, decimo + razao, razao):
        print(' {}  '.format(c), end=" → ") # seta alt 26 no teclado quadrado
    print('ACABOU')
    print('')
    print('')
    23
    print('')