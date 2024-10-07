# Rotina para imprimir os números primos constantes de um intervalo.

#
# Definir o intervalo.
#

primeiro = int( input( "Qual é o primeiro número do intervalo? " ))
ultimo   = int( input( "Qual é o último número do intervalo? " ))

numero  = primeiro
divisor = 3

if ( numero == 1 or numero == 4 ):
    numero = numero + 1
  
while ( ultimo > numero ):
    
    chave = True

    while ( chave ):
        
        if (( divisor > ( numero / 2 )) and ( numero != 4 )):
            print("O número " + str( numero ) + " é primo.")
            divisor = 3
            numero = numero + 1
            chave = False
        else:
            if ((( numero % 2) == 0) or ( numero % divisor == 0)):
                numero = numero + 1
                divisor = 3
                chave = False
                
            else:
                divisor = divisor + 2
                
               
print("Não existe mais números primos no intervalo.")
