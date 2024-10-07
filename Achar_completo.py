# Programa para localizar alguem maior de 18 anos com data completa.

#
# Obetenção da data atual.
#

from datetime import datetime

hoje = datetime.now()

ano_atual = hoje.year
mes_atual = hoje.month
dia_atual = hoje.day

#
# Localizar alguem maior de 18 anos.
#

chave = True

while chave:
    ano_nascimento = float(input("Em que ano você nasceu? "))
    maior = ano_atual - ano_nascimento   
    if maior <= 18:
        if maior == 18:
            mes_nascimento = float(input("Em que mês você nasceu? "))
            if mes_nascimento <= mes_atual:
                if mes_nascimento == mes_atual:
                    dia_nascimento = float(input("em que dia você nasceu? "))
                if dia_nascimento >= dia_atual:
                    print("Você NÃO é maior de idade!")
                else:
                    print("Você é maior de idade!")
                    chave =False
            else:
                print("Você NÃO é maior de idade!")
    else:
        print("Você é maior de idade!")
        chave = False 