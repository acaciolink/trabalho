lista = []
maior = menor = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite o {i+1}° número: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(lista)
print(f'O maior valor é {maior} e está nas posições ',end=' ')
for i, valor in enumerate(lista):
    if valor == maior:
        print(f'{i}...', end= ' ')
print(f'\nO menor valor é {menor} e está nas posições ',end=' ')
for i, valor in enumerate(lista):
    if valor == menor:
        print(f'{i}...',end=' ')
