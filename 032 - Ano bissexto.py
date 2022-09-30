from datetime import date   # importa a data do ano atual
ano = int(input(' Que ano quer analizar?\n '))
#if ano == 0:
#    amo = date.today().year      \\esse comandousa o import
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' O ano {} é BISSEXTO '.format(ano))
else:print(' O ano {} NÃO é BISSEXTO '.format(ano))
input()