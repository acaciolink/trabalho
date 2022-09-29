a = int(input(' Primeiro valor: '))
b = int(input(' Segundo valor: '))
c = int(input(' Terceiro valor: '))
# verificando qual é menor  \\
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor=c
#verificando maior
maior = a  # outra forma de fazer primeiro if
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(' Menor valor encontrado foi {}'.format(menor))
print(' Maior valor encontrado foi {}'.format(maior))
input()