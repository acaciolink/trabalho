print('{:=^40}'.format(' LOJAS GUANABARA'))
preco = float(input(' Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro
[2] à vista cartão
[3] 2x no cartão
[4] 3x no cartão''')
opcao = int(input(' Qual é a opção? '))
if opcao == 1:
    total =preco - (preco * 10/100)
elif opcao ==2:
    total = preco -(preco * 5/100)
    print(' Sua compra de R$ {:.2f} vai custar R$ {} no final.'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(' Sua compra será parcelada em 2x de R${:.2f} SEM JUROS '.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input(' Quantas parcelas? '))
    parcela = total / totparc
    print(' Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print(' \n OPÇÂO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print(' Sua compra de R${:.2f} vai custar R${:.2f} no final .'.format(preco, total))

input()



