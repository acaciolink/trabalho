def area(l,c):
    a = l*c
    print(f'A área de um terreno {l}x{c} é de {a:.2f}')


print('- - - CONTROLE DE TERRENO - - - ')
largura = float(input("LARGURA: "))
comprimento = float(input("COMPRIMENTO: "))

area(largura,comprimento)