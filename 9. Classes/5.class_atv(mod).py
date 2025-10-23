import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    enderenco: str

    def mostrar_dados(self):
        os.system("cls")
        print("= Mostrando resultados =")
        print(f"Seu nome: {self.nome}")
        print(f"Seu E-mail: {self.email}")
        print(f"Seu telefone: {self.telefone}")
        print(f"Seu endereço: {self.enderenco}")
        print("\nOBRIGADO POR SE CADASTRAR!! :)..")


pessoa1 = Pessoa(nome=input("Digite o seu nome: "), 
                 email=input("Digite seu E-mail: "),
                 telefone=(input("Digite o seu telefone: ")),
                 enderenco=input("Digite o seu endereço: "))

#Exibindo dados.
pessoa1.mostrar_dados()
