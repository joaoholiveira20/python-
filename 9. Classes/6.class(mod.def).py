import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int


    def mostrar_dados(self):
        print(f"Seu nome: {self.nome}")
        print(f"Sua idade: {self.idade}")

print("\nSolicitando os dados da pessoa. ")
pessoa1 = Pessoa(nome=input("Digite o seu nome: "), 
                 idade=int(input("Digite a sua idade: ")))

pessoa2 = Pessoa(nome=input("Digite o seu nome: "), 
                 idade=int(input("Digite a sua idade: ")))


print("\n= Exibindo dados =")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
