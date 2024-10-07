# Demonstração de comandos de repetição no Python.

#
# Comando FOR com array
#

nomes = ["João", "José", "Pedro", "Paulo", "Joaquim"]

for nome in nomes:
    print("Olá " + nome +  "!")

print("Fim...")

numeros = [1, 2, 3, 4, 5, 6]

for i, num in enumerate(numeros):
    soma = num + 10
    print("O número é: ", i)
    print("A soma é: ", soma)
# 
# Comando WHILE.
#

n = 0

while (n <= 5):
    print( n )
    n = n + 1
    
print('Fim do WHILE!')
