# Rotina para cálculo de área de um triangulo retângulo.

import math

h = float(input('Digite o comprimento da hipotenusa: '))
c1 = float(input('Digite o comprimento do cateto: '))

#
# Cálculo do segundo cateto.
#

c2 = math.sqrt( (h * h) - (c1 * c1) )

#
# Cálculo da área.
#

area = (c1 * c2) / 2

print("O valor da área é: " + str( area ))
