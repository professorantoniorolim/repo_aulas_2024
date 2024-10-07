# Rotina para imprimir o maior número de uma sequência de "n" números.

#
# Definição da quantidade de números da sequência.
#

n = float( input("Qual é a quantidade de números? "))

maior = float(input("Digite o primeiro número: "))
n = n -1

while (n > 0):
   
    num = float(input("Digite o próximo número: "))
    if (maior < num):
        maior = num
    n = n - 1
    
print("O maior número é " + str(maior))
