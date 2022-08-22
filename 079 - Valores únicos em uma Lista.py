numeros = list()
continuar = ''
cont = 0
localiza = ''
while True:
    if cont == 0:
        numeros.append(int(input('Digite um valor: ')))
        print('Valor adicionado com sucesso!')
        cont +=1
    elif cont > 0:
        n = (int(input('Digite um valor: ')))
        localiza = numeros.count(n)
        if localiza == 0:
            numeros.append(n)
            print('Valor adicionado com sucesso!')
        else:
            print('Valor já foi digitado! Não vou adicionado!')
            localiza = ''
    continuar = str(input('Deseja continuar?[s/n] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Os valores digitados foram:{numeros}', end='')
