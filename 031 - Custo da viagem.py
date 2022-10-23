distancia = float(input(' Qual é a distancia da viagem?\n '))
print(' Você esta preste a percorrer {}km' .format(distancia))
'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''

preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(' E o preço da passagem será R${:.2f}'.format(preço))
input()