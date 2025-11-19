import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nidade: {self.idade}")

lista_paciente = []
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade: "))
    )
    lista_paciente.append(paciente)
    print() # Pular uma linha.

nome_do_arquivo = "dados_pacientes.csv"
with open(nome_do_arquivo, "w") as arquivo_pacientes:
    for paciente in lista_paciente:
        arquivo_pacientes.write(f"\nnome: {paciente.nome} \nidade: {paciente.idade}")
        print("Dados salvos com sucesso.")

print("\nExibindo lista de pacientes:")
for paciente in lista_paciente:
    paciente.exibir_dados()



