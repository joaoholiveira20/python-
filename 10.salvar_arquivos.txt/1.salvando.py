import os
os.system("cls")

# Texto que desejo salvar.
texto = input("Digite seu nome: ")

#Definir nome do arquivo para salvar.
nome_arquivo = "exemplo.txt"

#comando para salvar.
with open(nome_arquivo, "a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("Salvo com sucesso!")