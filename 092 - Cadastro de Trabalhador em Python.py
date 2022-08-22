from datetime import date
dicionario = dict()
data = date.today().year
dicionario['nome'] = str(input('Nome: '))
ano_nasc = int(input("Ano de nascimento: "))
dicionario['idade'] = data - ano_nasc
dicionario["carteira_trab"] = int(input("Carteira de trabalho: "))
if dicionario["carteira_trab"] !=0:
    dicionario['ano_contratação'] = int(input("Ano de contratação: "))
    dicionario['salario'] = float(input("Salario: "))
    tempo_trabalho = data - dicionario['ano_contratação']
    dicionario['aposentadoria'] = (dicionario["idade"] - tempo_trabalho) + 35
for k,v in dicionario.items():
    print(f' - {k} tem o valor {v}')