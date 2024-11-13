#
# Testes de comandos de manipulação de arquivos.
#

#
### Abrir um arquivo no modo leitura.
#

# var = open("comandos_arquivos/arq_txt.txt","r")

#
### Ler todo o arquivo.
#

# print(var.read())

# variavel = var.read()
# print(variavel)

#
### Ler apenas um registro.
#

# registro = var.readline()
# print(registro)

# i=0
# while i < 3:
#     registro = var.readline()
#     print(registro)
#     i=i+1

# lista = var.readlines()
# print(lista)

# a = input("continuar?")

# for linha in lista:
#     if "dados" in linha:
#         print(linha)

# registro = var.readline()
# print(registro)
#
### Modo append, acrescenta um registro.
#

# var = open("comandos_arquivos/arq_txt.txt","a")

# dados = "dados de entrada"
# var.write(dados + "\n")

# var.write("Santiago\n")
# var.write("Santiago\n")
# var.write("Santiago\n")

#
### Modo write, cria um arquivo para adicionar registro.
#

# var = open("comandos_arquivos/arq_txt_bkp.txt", "w")

# var.write("Salete\n")
# var.write("Bernardo\n")
# var.write("Francisco\n")

#
### Modo write, cria um arquivo para adicionar registro com campos.
#

var = open("comandos_arquivos/arqr_txt.txt","a")

dados = "123456" + "Paulo"
var.write(dados + "\n")

# var.write("Santiago\n")
# var.write("Santiago\n")
# var.write("Santiago\n")

#
### Criar arquivo.
#

# var = open("comandos_arquivos/arq_txt_bkp2.txt", "x")

# var.write("Santiago\n")
# var.write("Bernardo\n")
# var.write("Francisco\n")

#
### Exclusão de arquivo ou pastas importando biblioteca os .
#

# import os

# os.remove("comandos_arquivos/arq_txt_bkp2.txt") # só apaga se o arquivo estiver fechado.

# os.rmdir("comandos_arquivos/pasta")  # só apaga se a pasta estiver vazia.

#
### Fechar o arquivo.
#

var.close()

