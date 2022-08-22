while (True):
    casa = float(input(' valor da casa: R$  '))
    salario = float(input(' salario do comprador: R$ '))
    anos = int(input(' quantos anos de financiament? '))
    prestacao = casa/(anos * 12)
    minimo = salario *30/100
    print(' para pagar uma casa de R${:>2f} em {} anos ' .format(casa, anos), end='')
    print(' a prestação será de R$ {:.2f} '.format(prestacao))
    if prestacao <= minimo:
        print(' emprestimo concedido')
    else:
        print(' emprestimo negado')






