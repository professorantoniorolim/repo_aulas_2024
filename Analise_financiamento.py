# Rotina para calcular o valor das prestações de um empréstimo.
#

#
# Função para calcular o montante do empréstimo.
#

def total_pago( capital , taxa , tempo ):

    valor_total = int( capital * ( 1 + taxa / 100 ) ** tempo)

    return valor_total

#
# Função de formatação de valor.
#

def formatar_valor( valor ):
    
    valor = f"R$ {valor:_.2f}"
    valor = valor.replace('.', ',').replace('_', '.')
    
    return valor

#
# Função de formatação de valor de entrada.
#

def formatar_entrada( valor ):
    
    # valor = valor.pop()
    # valor = valor.pop()
    # valor = valor.pop()
    
    valor = valor.replace('.', ',')
    
    print(valor)
    return valor   
#
# Entrada de dados.
#

chave = True
porcentagem = 3

while chave:
    
    inp_valor = input("Qual é o valor pretendido? R$ ")
    valor = int(inp_valor)
    prazo = int(input("Em quantos meses deseja pagar? "))
    montante = total_pago( valor, porcentagem, prazo )
    prest = montante / prazo
    parcela = formatar_valor(prest)
    print(f"O valor de cada uma das parcelas será de R$  {parcela}")
    
    continua = input("Deseja fazer outra simulação? (S/N) ")
    if ( continua == "n" or continua == "N" ):
        chave = False
        
print( "*** FIM DO PROGRAMA ***" )        
    