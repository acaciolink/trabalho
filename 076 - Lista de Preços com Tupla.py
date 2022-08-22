'''tupla = (('Lápis',1.75), ('Borracha',2.00),('Caderno',15.90),
         ('Estojo',25.00),('Compasso',9.99),('Mochila',120.32),
         ('Canetas',22.30),('Livro',34.90))
print('='*40)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('='*40)
for produto, preco in tupla:
    print(f'{produto:.<30} R$ {preco:.2f}')
print('='*40)'''

produtos = ('Lapis','3.00','Caderno','11.99','Caneta','2.25','Borracha','0.50','Apontador','3.45','Cola Tenaz','7.00',
            'Mochila','123.00','Compaço','5.50','Estojo','45.99')

print('-' * 60)
print('{:^60}'.format('Listagem de preços'))
print('-' * 60)
for i in range(0, len(produtos)-1 , 2):
    print('{:.<50}'.format(produtos[i]),'R${:>7}'.format(produtos[i+1]))
print('-' * 60)