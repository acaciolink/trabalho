frase = str(input(' Digite uma frase: ')).upper().strip()
l = str(input(' escolha uma letra: ')).upper ()
print(' A letra',l, ' escolhida aparece {} vezes na frase. '.format(frase.count (l)))
print(' A primeira letra ',l,'apareceu na posição {}' .format(frase.find(l)+1))
print(' A ultima letra', l , 'apareceu na posição {}' .format(frase.rfind(l)+1))   # rfind - apartir da direita

