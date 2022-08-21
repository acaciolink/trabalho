l = []
while True:
    l.append(int(input("Digite um valor: ")))
    r = ' '
    while r not in 'SN':
        r = str(input("Quer continuar ?[s/n]  ")).strip().upper()
    if r == 'N':
        break
print(f'Voce digitou {len(l)} elementos.')
print('-='*40)
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são {l}')
print('-='*40)
if 5 in l:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')