#
# Rotina de cadastramento de usuáro.
#

import customtkinter as ctk

#
# Função de validação de CPF.
#

def valida(cpf):
    
    print("valida cpf")
    print(texto_cpf)
    confirma = True
    return confirma

#
# Rotina de gravação dos dados.
#

def processa():
    
    cadastro = {}

    
    testo = ctk.StringVar(value="Cadastramento concluído com sucesso.")
    
    confirmacao = ctk.CTkLabel(tela, textvariable=testo, text_color="red", font=("impact", 16))
    confirmacao.grid(column=0, row=5, padx=20, pady=10)
    
    #tela.destroy()
   
    
#
# Criação da tela de Cadastro.
#

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
tela = ctk.CTk()
tela.geometry("500x300")
tela.title("Cadastro de Usuários")

texto_cpf = ctk.CTkLabel(tela, text = "CPF: ")
texto_cpf.grid(column=0, row=1, padx=20, pady=10)

texto_nome = ctk.CTkLabel(tela, text = "Nome: ")
texto_nome.grid(column=0, row=2, padx=20, pady=10)

texto_email = ctk.CTkLabel(tela, text = "e-mail: ")
texto_email.grid(column=0, row=3, padx=20, pady=10)

entrada_cpf = ctk.CTkEntry(tela, placeholder_text = "Somente números")
entrada_cpf.grid(column=1, row=1, padx=10, pady=10)

entrada_nome = ctk.CTkEntry(tela, placeholder_text = "Nome completo")
entrada_nome.grid(column=1, row=2, padx=10, pady=10)

entrada_email = ctk.CTkEntry(tela, placeholder_text = "e-mail válido")
entrada_email.grid(column=1, row=3, padx=10, pady=10)
    
botao_processar = ctk.CTkButton(tela, text="  CADASTRAR  ", command = processa)
botao_processar.grid(column=1, row=4, padx=10, pady=10)
 
cpf_digitado = entrada_cpf.get()
print("cpf" + cpf_digitado)
    
valida(cpf_digitado)
   
tela.mainloop()