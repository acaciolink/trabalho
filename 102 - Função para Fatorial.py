def fatorial(n=1,show=False):

    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c,end='')
            if c>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f

nu = int(input(' Insira o numero do fatorial: '))
print(fatorial(nu,True))