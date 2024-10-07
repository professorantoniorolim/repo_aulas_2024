# Rotina para calcular o tempo médio e a quantidade de atendimento por caixa.

fila = [ 3, 5, 8, 1, 2, 5, 5, 3, 4, 6 ]

tempo_cx1 = 0
tempo_cx2 = 0
tempo_cx3 = 0
tempo_total_cx1 = 0
tempo_total_cx2 = 0
tempo_total_cx3 = 0
atendimento_cx1 = 0
atendimento_cx2 = 0
atendimento_cx3 = 0

#
# Define tamanho da fila.
#

clientes = len( fila )

while clientes != 0:
    
#
# Caixa 1.
#
    if tempo_cx1 == 0:
        tempo_cx1 = fila[0]
        tempo_total_cx1 = tempo_total_cx1 + tempo_cx1
        atendimento_cx1 = atendimento_cx1 + 1
        fila.pop(0)
        clientes = len( fila )
        
    else:
        tempo_cx1 = tempo_cx1 - 1
 
#
# Caixa 2.
#
    if tempo_cx2 == 0:
        tempo_cx2 = fila[0]
        tempo_total_cx2 = tempo_total_cx2 + tempo_cx2
        atendimento_cx2 = atendimento_cx2 + 1
        fila.pop(0)
        clientes = len( fila )
    else:
        tempo_cx2 = tempo_cx2 - 1
        
#
# Caixa 3.
#
    if tempo_cx3 == 0:
        tempo_cx3 = fila[0]
        tempo_total_cx3 = tempo_total_cx3 + tempo_cx1
        atendimento_cx3 = atendimento_cx3 + 1
        fila.pop(0)
        clientes = len( fila )
    else:
        tempo_cx3 = tempo_cx3 - 1
        
#
# Final do dia>
#

media_cx1 = tempo_total_cx1 / atendimento_cx1
media_cx2 = tempo_total_cx2 / atendimento_cx2
media_cx3 = tempo_total_cx3 / atendimento_cx3

print("O caixa 1 fez " + str( atendimento_cx1 ) + " atendimento e sua média de tempo foi " + str( media_cx1 ))
print("O caixa 2 fez " + str( atendimento_cx2 ) + " atendimento e sua média de tempo foi " + str( media_cx2 ))   
print("O caixa 3 fez " + str( atendimento_cx3 ) + " atendimento e sua média de tempo foi " + str( media_cx3 ))   
