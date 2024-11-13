#
# Rotina para validação de login.
#

#
# Função que valida a senha.
#

def valida():
    
    confirmacao["text"] = "senha válida!"


#
# Criação da tela de login
#

from tkinter import *

tela = Tk()
tela.geometry("250x200")

tela.title("Tela de Login")

texto_usuario = Label(tela, text = "Usuário: ")
texto_usuario.grid(column=0, row=0, padx=20, pady=10)

texto_senha = Label(tela, text = "Senha: ")
texto_senha.grid(column=0, row=1, padx=20, pady=10)

entrada_usuario = Entry(tela, )
entrada_usuario.grid(column=1, row=0, padx=10, pady=10)

entrada_senha = Entry(tela, show= '*')
entrada_senha.grid(column=1, row=1, padx=10, pady=10)

botao_verifica = Button(tela, text="   Fazer Login   ", command = valida)
botao_verifica.grid(column=1, row=3, padx=10, pady=10)

confirmacao = Label(tela, text="")
confirmacao.grid(column=0, row=4, padx=10, pady=10)
                       
tela.mainloop()
