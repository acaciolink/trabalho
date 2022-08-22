from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for i in range(i, f, p):
            print(i, end=' ')
            sleep(0.3)
        print(" FIM!")
        print('-' * 30)
    else:
        cont = i
        while cont >= f:
            print(cont,end=' ')
            sleep(0.3)
            cont -= p
        print(" FIM!")
        print('-' * 30)
contador(1, 11, 1)
contador(10, -1, 2)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("passo: "))
contador(inicio, fim, passo)