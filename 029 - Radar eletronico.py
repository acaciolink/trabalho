velocidade = float(input(' Qua é a velocidade atual do carro?\n '))100

if velocidade > 80:
    print(' MULTADO! Você excedeu o limite permitido que é de 88km/h ')
    multa = (velocidade-80)*7
    print(' Você deve pagar uma multa de R${:.2f}!'.format(multa))
print(' Tenha um bom dia! Dirija com segurança!')