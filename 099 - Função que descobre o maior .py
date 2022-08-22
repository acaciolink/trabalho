from time import sleep
def maior(*num):
    maior = 0
    for i,m in enumerate(num):
        if i == 0:
            maior = m
        elif m > maior:
            maior = m
    print('Analisando os valores passados...',end='')
    for v in num:
        print(v,end=' ')
    print()
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    print('-'*38)
maior(2,9,5,7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
