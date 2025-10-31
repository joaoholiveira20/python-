import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: str


QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    os.system("cls")
    aluno = Aluno(
        nome=input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        email=input("Digite seu E-mail: "),
        telefone=input("Digite seu telefone: ")
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_aluno.txt"

with open(arquivo, "a") as arquivo_aluno:
    for aluno in lista_alunos:
        aluno.salvando_dados()
        arquivo_aluno.write(f"\nnome: {aluno.nome} \nidade: {aluno.idade} \nE-mail: {aluno.email} \nTelefone: {aluno.telefone}")
    print("salvo com sucesso!")