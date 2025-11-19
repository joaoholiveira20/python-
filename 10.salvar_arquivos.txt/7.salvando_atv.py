import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    nascimento: str
    rg: str
    cpf: str

    def exibindo_dados(self):
        print(f"Nome: {self.nome} \nData de nascimento: {self.nascimento} \nRG: {self.rg} \nCPF: {self.cpf}\n")


lista_usuario = []
QUANTIDADE_USUARIOS = 2

for i in range(QUANTIDADE_USUARIOS):
    usuario = Pessoa(
        nome=input("Digite seu nome: "),
        nascimento=input("Digite sua data de nascimento: "),
        rg=input("Digite seu RG: "),
        cpf=input("Digite seu CPF: ")
    )
    lista_usuario.append(usuario)
    print()

nome_do_arquivo = "Funcioarios.csv"
with open(nome_do_arquivo, "a") as arquivo_usuario:
    for usuario in lista_usuario:
        arquivo_usuario.write(f"{usuario.nome}, {usuario.nascimento}, {usuario.rg}, {usuario.cpf}")
    print("Dados salvos com sucesso!")

print("\nExibindo lista de usuarios.")
for usuario in lista_usuario:
    usuario.exibindo_dados()

print("\nExibindo todos os usuarios.")
try:
    with open(nome_do_arquivo, "r") as arquivo:
        for linha_usuario in arquivo: # Itera diretamente sobre o arquivo
            nome, nascimento, rg, cpf = linha_usuario.strip().split(",")
            dados_usuario = Pessoa(nome=nome, nascimento=nascimento, rg=rg, cpf=cpf)
            dados_usuario.exibindo_dados() # Exibe imediatamente            
except FileNotFoundError:
    print("Arquivo não encontrado.")