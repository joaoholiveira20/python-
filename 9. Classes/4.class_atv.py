import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    enderenço: str


pessoa1 = Pessoa(nome=input("Digite o seu nome: "), 
                 email=input("Digite seu E-mail: "),
                 telefone=(input("Digite o seu telefone: ")),
                 enderenço=input("Digite o seu endereço: "))

os.system("cls")
print("= Mostrando resultados =")
print(f"Seu nome: {pessoa1.nome}\nSeu E-mail: {pessoa1.email}\nSeu telefone: {pessoa1.telefone}\nSeu endereço: {pessoa1.enderenço}")
print("\nOBRIGADO POR SE CADASTRAR!! :)..")