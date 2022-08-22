lista = []
lista_impar = []
lista_par = []

while True:
    n = int(input("Digite um número:   "))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    resp = str(input("Quer continuar ? [s/n]  ")).strip().upper()
    if resp == 'N':
        break

print(f'LISTA COMPLETA {lista}')
print(f'LISTA PAR {lista_par}')
print(f'LISTA IMPAR {lista_impar}')