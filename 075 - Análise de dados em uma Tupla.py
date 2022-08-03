num = (int(input(' Digite um número:')),
        int(input(' Digite outro número:')),
        int(input(' Digite mais um número:')),
        int(input(' Digite o ultimo número: ')))
print(f'Você digitou os valores {num}')
print ('digite um numero:',end='')
g = int(input())
if g in num:
        print(f'O valor {g} apareceu {num.count (g)} vezes')
else:
        print(f'O valor {g} não foi digitado nenhuma vez')
print('digite um numero:', end='')
l = int(input())
if l in num:
        print(f'O valor {l} apareceu na {num.index(l)+1}° posição')
else:
        print(f'O valor {l} não foi digitado em nenhuma posição')
print('Os valores pares  digitados foram:', end='')
for n in num:
        if n % 2 == 0:
                print(n, end=' ')