# Rotina para achar a rota mais rápida e a mais econômica.

#
# Definir a quantidade de rotas possíveis.
#

quantidade =  int( input("Qual a quantidade de rotas? "))

tempo_rota = [] 
consumo_rota = []
menor_consumo = 0
rota_rapida = 0
rota = 0

#
# Processamento individual das rotas.
#

while ( rota < quantidade ):
    
    totaliza_tempo = 0
    totaliza_consumo = 0
    totaliza_peso = 0
   
    
#
# Definir quantidade de trechos na rota.
#

    trechos = int( input("Quantos trechos existe nesta rota? "))

    
#
# Obter os dados de cada trecho.
#

    while ( trechos > 0 ):
        
        velocidade_media = float( input("Velocidade média no trecho? "))
        tamanho_trecho = float( input("Tamanho do trecho? "))
        
        tempo_trecho = tamanho_trecho / velocidade_media
        consumo_trecho = velocidade_media * tempo_trecho
        totaliza_tempo = totaliza_tempo + tempo_trecho
        totaliza_consumo = totaliza_consumo + consumo_trecho 
        totaliza_peso = totaliza_peso + velocidade_media
        
        trechos = trechos - 1
        
    consumo_medio = totaliza_consumo / totaliza_peso
    consumo_rota.append( consumo_medio ) 
    tempo_rota.append( totaliza_tempo )
    rota = rota + 1
        
#
# Definir a rota mais economica.
#

menor_consumo = consumo_rota[ 0 ]
rota_atual = 0

for consumo in consumo_rota:
    rota_atual = rota_atual + 1

    if ( menor_consumo >= consumo ):
        menor_consumo = consumo
        rota_economica = rota_atual
    
print("A rota mais econômica é a rota " + str( rota_economica ))

# 
# Definir a rota mais rapida.
#
  
menor_tempo = tempo_rota[ 0 ]     
rota_atual = 0    

for tempo in tempo_rota:
    rota_atual = rota_atual + 1
    
    if ( menor_tempo >= tempo ):
        menor_consumo = tempo
        rota_rapida = rota_atual  
        
print("A rota mais rápida é a rota " + str( rota_rapida ))  
  