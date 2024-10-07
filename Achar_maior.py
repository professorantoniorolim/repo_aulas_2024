# Programa para localizar alguem maior de 18 anos.

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

maior = 0

while (maior < 18):
    ano_nascimento = float(input("Em que ano você nasceu? "))
    maior = ano_atual - ano_nascimento   

print("Você é maior de idade!" )
