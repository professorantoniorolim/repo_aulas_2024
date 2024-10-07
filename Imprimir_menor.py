# Rotina para imprimir o menor número de uma série.

q = int( input( 'Quantos números há na série? ' ) )
menor = int( input( "Digite o primeiro número da série: " ))

while ( q != 1 ):
    
    numero = int( input("Qual é o próximo número da série: "))
    if ( numero <= menor ):
        menor = numero
    q = q - 1
    
print( f"O menor número é: {menor}" )
