import os
from dataclasses import dataclass

os.system("cls")


@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float


    def mostrar_dados(self):
        print(f"\nSeu nome: {self.nome}")
        print(f"Sua idade: {self.idade}")
        print(f"Seu peso: {self.peso:.1f}")
        print(f"Sua altura: {self.altura:.2f}")

lista_cliente = []

for i in range(0, 3):
    os.system("cls")
    print(f"Pessoa {i+1}")
    cliente = pessoa(nome=input("Digite seu nome: "),
                     idade=int(input("Digite a sua idade: ")),
                     peso=float(input("Digite seu peso (kg): ")),
                     altura=float(input("Digite a sua altura: ")))
    lista_cliente.append(cliente)

os.system("cls")
print("=== Mostrando dados ===")
for cliente in lista_cliente:
    cliente.mostrar_dados()