numero = int(input(' Me diga um numero qualquer: '))
resultado = numero % 2
#print(' O resultado foi {}'.format(resultado)) porque oreso de impar é 1 e par é 0
if resultado==0:
    print(' O numero {} é PAR'.format(numero))
else:
    print(' O numero {} é IMPAR'.format(numero))