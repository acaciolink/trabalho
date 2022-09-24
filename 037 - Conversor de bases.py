num = int(input(' digite um numero inteiro: '))
print('''escolha uma das bases para conversão:
[1] converter para BINARIA
[2] converter para OCTAL
[3] converter para hexadecimal''')
opcao = int(input(' sua opção:  '))
if opcao==1:
    print(' {} convertido para BINARIO é igual a {}' .format(num, bin(num)[2:]))
elif opcao == 2:
    print(' {} conversao para OCTAL é igual a {}' .format(num, oct(num)[2:]))
elif opcao== 3:
    print(' {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print(' opção invalida, tente novamente')