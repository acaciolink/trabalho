while (True):
    frase = str(input(' Digite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    print(' Você digitou a frase {}'.format(frase))
    inverso = junto[::-1]
    '''for letra in range(len(junto) -1, -1, -1):
        inverso += junto[letra]'''
    if inverso == junto:
        print(' O inverso de {} é {}'.format(junto,inverso))
        print(' Temos um palindro!')
    else:
        print(' A frase não é um palindro! ')
    print(junto, inverso)
    print ('')
