# Programa para calcular o fatorial de um número qualquer.

#
# Entrada do número.
#

n = float(input('Qual é o número? '))

# Cálculo crescente do fatorial.

total = 1
fator = 1

while (fator <= n):
    total = total * fator
    fator = fator + 1

print("O resultado é " + str(total))

# Cálculo decrescente do fatorial.

print('===================')

fator = total = int( n )

while (fator > 1):
    fator = fator - 1
    total = total * fator

print("O resultado é: " + str(total))
