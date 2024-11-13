#
# Rotina para converter temperaturas com nova tela.
#


#
# Função de cálculo da opções desejada.
#

def escolha_1():
    
    valor = float(valor_entrada.get())
    temperatura = ( 9 / 5 * valor + 32 )
    conversao["text"] = ( "A temperatura em graus Faherenheit é " + str( temperatura ))
    
def escolha_2():
    
    valor = float(valor_entrada.get())
    temperatura = valor + 273
    conversao["text"] = ( "A temperatura em Kelvin é " + str( temperatura ))
        
def escolha_3():
     
    valor = float(valor_entrada.get())
    temperatura = ( 9 / 5 * valor + 305 )
    conversao["text"] = ( "A temperatura em Kelvin é " + str( temperatura ))
    
def escolha_4():
   
    valor = float(valor_entrada.get())
    temperatura = valor - 273
    conversao["text"] = ( "A temperatura em graus Celsius é " + str( temperatura ))
   
#
# Criação do Menu.
#

from tkinter import *

tela = Tk()
tela.geometry("650x400")

tela.title("Menu Inicial")

texto_usuario = Label(tela, text = "          Converção de unidade de medida de temperatura. ")
texto_usuario.grid(column=0, row=0, padx=10, pady=10)

pergunta = Label(tela, text = "Digite o valor da temperatura:")
pergunta.grid(column=0, row=1, padx=1, pady=15)

valor_entrada = Entry(tela, borderwidth = 3 )
valor_entrada.grid(column=1, row=1, padx= 1, pady=15)

opcao_1 = Button(tela, text="1 - Converter de graus Celsius para graus Fahrenheit.", command = escolha_1)
opcao_1.grid(column=0, row=2, ipadx=25, pady=10)

opcao_2 = Button(tela, text="2 - Converter de graus Celsius para Kelvin.", command = escolha_2)
opcao_2.grid(column=0, row=3, ipadx=50, pady=10)

opcao_3 = Button(tela, text="3 - Converter de graus Fahrenheit para kelvin.", command = escolha_3)
opcao_3.grid(column=0, row=4, ipadx=20, pady=10)

opcao_4 = Button(tela, text="4 - Converter de Kelvin para graus Celsius.", command = escolha_4)
opcao_4.grid(column=0, row=5, ipadx=20, pady=10)

conversao = Label(tela, text="")
conversao.grid(column=0, row=7, padx=10, pady=10)
    
tela.mainloop()
