dicionario = dict()
lista = list()
media = soma = 0
while True:
    dicionario.clear()
    dicionario['nome'] = str(input("Nome: "))
    while True:
        dicionario['sexo'] = str(input("Sexo M/F: ")).strip().upper()
        if dicionario['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite o sexo corretamente M/F: ')
    dicionario['idade'] = int(input("Idade: "))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    while True:
        resp = str(input("Quer continuar ?")).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Responsa apenas S OU N: ')
    if resp == 'N':
        break
media = soma / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A media de idades é {media:.2f} anos')
print('C) As mulheres cadastradas foram', end=' ')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end= ' ')
print()
print('D) Lista de pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        for k,v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<<ENCERRADO>>>')