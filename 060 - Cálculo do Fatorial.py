from math import factorial
n = int(input( ' Digite um número para calcular seu fatorial: '))
f = factorial(n)
print (' O fatorial de {} é {} .'.format(n, f))

m = int(input( ' Digite um número para calcular seu fatorial: '))
c = m
g = 1
print(' Calculando {}! = '.format(m), end='' )
while c > 0:
    print('{} x '.format(c), end='') # o end é para não pular de linha
    print (' x ' if c > 1 else ' = ', end='')
    g = g * c # ou g *= c
    c -= 1
print(' {}'.format(g))
