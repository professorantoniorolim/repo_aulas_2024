#
# Rotina para validação de login usando o CustomTkinter.
#

import customtkinter

#
# Função que valida a senha.
#

def valida():
    
    testo = customtkinter.StringVar(value="Usuário ou Senha inválida!")
    
    confirmacao = customtkinter.CTkLabel(tela, textvariable=testo, text_color="red", font=("impact", 16))
    confirmacao.grid(column=0, row=5, padx=20, pady=10)


#
# Criação da tela de login
#

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

tela = customtkinter.CTk()
tela.geometry("500x300")

tela.title("Fazer Login")

texto_usuario = customtkinter.CTkLabel(tela, text = "Usuário: ")
texto_usuario.grid(column=0, row=1, padx=20, pady=10)

texto_senha = customtkinter.CTkLabel(tela, text = "Senha: ")
texto_senha.grid(column=0, row=2, padx=20, pady=10)

entrada_usuario = customtkinter.CTkEntry(tela, placeholder_text = "CPF ou e-mail")
entrada_usuario.grid(column=1, row=1, padx=10, pady=10)

entrada_senha = customtkinter.CTkEntry(tela, placeholder_text = "Digite a senha", show= '*')
entrada_senha.grid(column=1, row=2, padx=10, pady=10)

lembra_senha = customtkinter.CTkCheckBox(tela, text = "Lebrar a senha?")
lembra_senha.grid(column=1, row=3, padx=10, pady=10)

botao_verifica = customtkinter.CTkButton(tela, text="   Fazer Login   ", command = valida)
botao_verifica.grid(column=1, row=4, padx=10, pady=10)
                       
tela.mainloop()
