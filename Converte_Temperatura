# Rotina para converter temperaturas.

#
# Criação do Menu.
#

chave = True

while chave:
    
    print( " ")
    print( " ")
    print( "                      MENU" )
    print( " ")
    print( "1 - Converter de graus Celsius para graus Fahrenheit.")
    print( "2 - Converter de graus Celsius para Kelvin.")
    print( "3 - Converter de graus Fahrenheit para kelvin.")
    print( "4 - Converter de Kelvin para graus Celsius.")
    print( "9 - FIM.")

    opcao = int( input(" digite a opção desejada. "))

# 
# Cálculo da conversão.
#

    if ( opcao == 1 ): 
        valor = float( input(" Qual o valor da temperatura? ")) 
        temperatura = ( 9 / 5 * valor + 32 )
        print( "A temperatura em graus Faherenheit é " + str( temperatura ))
        space = input()
    
    elif ( opcao == 2 ):
        valor = float( input(" Qual o valor da temperatura? "))
        temperatura = valor + 273
        print( "A temperatura em Kelvin é " + str( temperatura ))
        space = input()

    elif ( opcao == 3 ):
        valor = float( input(" Qual o valor da temperatura? "))
        temperatura = ( 9 / 5 * valor + 305 )
        print( "A temperatura em Kelvin é " + str( temperatura ))
        space = input()

    elif ( opcao == 4 ):
        valor = float( input(" Qual o valor da temperatura? "))
        temperatura = valor - 273
        print( "A temperatura em graus Celsius é " + str( temperatura ))
        space = input()
        
    elif ( opcao == 9 ):
        chave = False
    else:
        print("Opção Inválida!!!")
    