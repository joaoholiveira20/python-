import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str


@dataclass
class pessoa:
    nome: str
    email: str
    endereco: Endereco

    def mostrando_dados(self):
        print(f"Seu nome: {self.nome}")
        print(f"Seu E-mail: {self.email}")
        print(f"\n=== Seu endereço ===")
        print(f"Seu endereço: {self.endereco.logradouro} \nnúmero: {self.endereco.numero} \nCidade: {self.endereco.cidade}")



pessoa1 = pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite seu E-mail: "),
                 endereco=Endereco(logradouro=input("Digite seu bairro: "),
                                   numero=input("Digite o numero do seu logradouro: "),
                                   cidade=input("Digite a sua cidade: ")))




os.system("cls")
print("=== mostrando dados ===")
pessoa1.mostrando_dados()