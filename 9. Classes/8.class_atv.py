import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def informacoes(self):
        print(f"Seu nome: {self.nome}")
        print(f"Seu E-mail: {self.email}")
        print(f"Seu endereço: {self.endereco}")

    def mostrar_nome(self):
        print(f"Seu nome: {self.nome}")

#Lista (vetor)
lista_pessoa = []

for i in range(2):
    pessoa= Pessoa(nome=input("Informe seu nome: "),
                    email=input("Informe o seu E-mail: "),
                    endereco=input("Digite seu endereço: "))
    lista_pessoa.append(pessoa)



os.system("cls")
print("\n=== Mostrando dados da pessoa ===")
for pessoa in lista_pessoa:
    pessoa.informacoes()
print("\n=== Mostrando os nomes ===")
for pessoa in lista_pessoa:
    pessoa.mostrar_nome()
