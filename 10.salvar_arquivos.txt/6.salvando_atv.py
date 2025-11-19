import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nidade: {self.idade} \npeso: {self.peso} \nAltura: {self.altura} \nCPF: {self.cpf}\n")

lista_paciente = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: ")),
        peso= float(input("Digite seu peso: ")),
        altura= float(input("Digite sua altura: ")),
        cpf= int(input("Digite seu CPF: "))
    )
    lista_paciente.append(paciente)
    print() # Pular uma linha.

nome_do_arquivo = "dados_pacientes.csv"
with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_paciente:
        arquivo_pacientes.write(f"\nnome: {paciente.nome} \nidade: {paciente.idade} \npeso: {paciente.peso} \nAltura: {paciente.altura} \nCPF: {paciente.cpf}")
    print("Dados salvos com sucesso.")

# print("\nExibindo lista de pacientes:")
# for paciente in lista_paciente:
#     paciente.exibir_dados()

# print("\nExibindo todos os pacientes: ")
# try:
#     # "r" - read - leitura 
#     with open(nome_do_arquivo, "r") as arquivo:
#         # Recebe todos os dados do arquivo de uma vez.
#         lista_todos_pacientes = arquivo.readlines()
#         for paciente in lista_todos_pacientes:
#             print(f"- {paciente.strip()}")
# except FileNotFoundError:
#     print("O arquivo não foi encontrado. ")

print("\nExibindo todos os pacientes: ")
lista = []
try:
    # "r" - read - leitura 
    with open(nome_do_arquivo, "r") as arquivo:
        # Recebe todos os dados do arquivo de uma só vez.
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade, peso, altura, cpf = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade), peso=peso, altura=float(altura),cpf=int(cpf)) 
            lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado. ")


    