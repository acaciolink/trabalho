peso = int(input(' Qual é o seu peso? (kg)'))
altura = float(input(' Qual é a sua altura? (m)'))
imc = peso/ (altura ** 2)
print (' O IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print(' Voê está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print(' Você esta na faixa dev peso ideal')
elif 25<= imc<30:
    print(' Você esta em sobrepeso')
elif 30<= imc < 40:
    print(' Você está em obesidade')
elif imc>=40:
    print(' Voê esta em obesidade morbida')
input()
