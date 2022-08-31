print(' Gerador de PA')
print('-='*10)
primeiro = int(input(' Primeiro termo: '))
razao = int(input(' Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0: # != significa diferente
    total = total + mais
    while cont <= total:
        print(' {} →'.format(termo) ,end=" " )
        cont += 1
        termo += razao
    print(' PAUSA')
    mais = int(input(' Quantos termos você quer mostrar a mais?  '))
print(' Progressão finalizada com {} termos mostrados.'.format(total))