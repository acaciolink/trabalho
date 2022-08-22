print('=' * 30)
print('{:^20}'.format("BANCO BV"))
print('=' * 30)

valor = int(input("Que valor você quer sacar ? R$"))
total = valor
ced = 50
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO BV! Tenha um ótimo dia!')