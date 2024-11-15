# Rotina para achar a rota mais rápida e a mais econômica.

#
# Função para achar menor valor.
#

def menor_valor( tabela ):
    tabela_menor = tabela[ 0 ]
    tabela_atual = 0
    
    for valor in tabela:
        tabela_atual = tabela_atual + 1
        
        if ( tabela_menor >= valor ):
            tabela_menor = valor
            valor_menor = tabela.index(valor)
            
    return valor_menor   

#
# Criação da fução de entrada de tabela.
#

def entrada_dados( texto ):
    valores_digitados = []
    chave = True
    
    while chave:
        valor = input( texto )
        if valor == ("f" or "F"):
            chave = False
        else:
            valor_entrada = float(valor)
            valores_digitados.append(valor_entrada)
    
    return valores_digitados

#
# Definir a quantidade de rotas possíveis.
#

quantidade =  int( input("Qual a quantidade de rotas? "))

tempo_rota = [] 
consumo_rota = []
menor_consumo = 0
rota_rapida = 0
rota = 1

#
# Processamento individual das rotas.
#

while ( rota <= quantidade ):
    
    totaliza_tempo = 0
    totaliza_consumo = 0
    totaliza_peso = 0  
  
#
# Obter os dados de cada trecho.
#

    texto_velocidade = "Digite a velocidade média da rota " + str( rota ) + " neste trecho: "
    tabela_velocidade = entrada_dados( texto_velocidade ) 
        
    texto_tamanho = "Digite o comprimento média da rota " + str( rota ) + " neste trecho: "      
    tabela_tamanho = entrada_dados( texto_tamanho )

    quantidade_velocidade = len( tabela_velocidade )
    quantidade_tamanho = len( tabela_tamanho )
    
    if ( quantidade_velocidade != quantidade_tamanho ):
                
        print('ERRO!!! QUANTIDADE DE VELOCIDADE E COMPRIMENTOS NÃO CONFERE NESTA  ROTA')
        break

#
# Cálculo do tempo total e consumo da rota.
#
    trecho = 1
    
    while ( trecho <= quantidade_tamanho ):       
          
        tempo_trecho = tabela_tamanho[ 0 ] / tabela_velocidade[ 0 ]
        consumo_trecho = tabela_velocidade[ 0 ] * tempo_trecho
        totaliza_tempo = totaliza_tempo + tempo_trecho
        totaliza_consumo = totaliza_consumo + consumo_trecho 
        totaliza_peso = totaliza_peso + tabela_velocidade[ 0 ]
        consumo_medio = totaliza_consumo / totaliza_peso
        
        trecho = trecho + 1
        tabela_tamanho.pop( 0 )
        tabela_velocidade.pop( 0 )
        
        
        consumo_rota.append( consumo_medio ) 
        tempo_rota.append( totaliza_tempo )
    
    rota = rota + 1 

#
# Impressão da rota mais econômica e da rota mais rápida.
#

rota_economica = menor_valor( consumo_rota )  
print("A rota mais econômica é a rota " + str( rota_economica ))
    
rota_rapida = menor_valor( tempo_rota )        
print("A rota mais rápida é a rota " + str( rota_rapida ))  
