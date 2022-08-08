dicionario = {"nome": str(input('Nome: ')), "media": float(input("Média: "))}
if dicionario['media'] >= 7:
    dicionario["Situacao"] = 'Aprovado'
else:
    dicionario["Situacao"] = 'Reprovado'
for k, v in dicionario.items():
    print(f'- {k} é igual a {v}')