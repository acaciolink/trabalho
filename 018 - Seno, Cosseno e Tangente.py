# from math import radians, sin, cos, tan e ai é so tirar as especificaçoes das procedures de baixo
import math
angulo= float(input(' Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(' O ângulo de {} tem seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print (' O angulo de {} tem o cosseno de {:.2f} ' .format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print(' O angulo {} tem a tangente de {:.2f}' .format(angulo, tangente))