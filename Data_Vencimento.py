#
# Rotina para calcular a data de vencimento de uma venda.
#

#
# Função para determinar se ano é bissexto.
#

def bissexto( ano ):

    resto_4 = ano % 4
    resto_100 = ano % 100

    def_bissexto = False

    if ( resto_4 == 0 or resto_100 == 0 ):
            def_bissexto = True

    return def_bissexto

#
# Função para montar tabela de dias dos meses de um ano.
#

def tabela_mes( confirma_bissexto ):

    if confirma_bissexto:
        mes_dias = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    else:
        mes_dias = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    return mes_dias

#
# Definir data de vencimento.
#

data_venda = input("Qual a data da venda? dd/mm/aaaa ")
prazo_pgto = int(input("Qual o prazo de pagamento? "))

ano_venda = int(data_venda[ 6 ] + data_venda[ 7 ] + data_venda[ 8 ] + data_venda[ 9 ])
mes_venda = int(data_venda[ 3 ] + data_venda[ 4 ])
dia_venda = int(data_venda[ 0 ] + data_venda[ 1 ])

#
# Definir quantidade de meses para o vencimento.
#

qtde = prazo_pgto / 30
qtde_mes = int(qtde)

mes_tabela = tabela_mes(ano_venda)
resto_dia = mes_tabela[mes_venda - 1] - dia_venda
resto_pgto = prazo_pgto - resto_dia

if qtde_mes <= 1:

    if resto_pgto < 0:
        dia_pgto = dia_venda + prazo_pgto
        mes_pgto = mes_venda
        ano_pgto = ano_venda
        data_vencimento = str(dia_pgto) + "/" + str(mes_pgto) + "/" + str(ano_pgto)
        print(data_vencimento)

    elif resto_pgto == 0:
        dia_pgto = mes_tabela[mes_venda - 1]
        mes_pgto = mes_venda
        ano_pgto = ano_venda
        data_vencimento = str(dia_pgto) + "/" + str(mes_pgto) + "/" + str(ano_pgto)
        print(data_vencimento)

    else:
        if ( resto_pgto <= mes_tabela[mes_venda] ):
            dia_pgto = resto_pgto
            mes_pgto = mes_venda + 1
            ano_pgto = ano_venda
            data_vencimento = str(dia_pgto) + "/" + str(mes_pgto) + "/" + str(ano_pgto)
            print(data_vencimento)

else:
    i = 0
    qtde_dia = mes_tabela[mes_venda - 1] - dia_venda
    
    while ( qtde_mes > 0 ):
        qtde_dia = qtde_dia + mes_tabela[mes_venda + i]
        if ( qtde_dia <= prazo_pgto ):
            i = i + 1
        


    dia_pgto = 0
    mes_pgto = mes_venda
    ano_pgto = ano_venda
    data_vencimento = str(dia_pgto) + "/" + str(mes_pgto) + "/" + str(ano_pgto)

    print(resto_pgto, data_vencimento)
