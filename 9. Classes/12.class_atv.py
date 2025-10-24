import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    cpf: str
    telefone: str


    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")


    def dados_sms_marketing(self):
        print(f"Telefone: {self.telefone}")

dados_cliente = []

for i in range(3):
    os.system("cls")
    cliente = pessoa(nome=input("Digite seu nome: "),
                     cpf=input("Digite seu CPF: "),
                     telefone=input("Digite seu telefone: "))
    dados_cliente.append(cliente)


os.system("cls")
print("=== Mostrando dados ===")
for cliente in dados_cliente:
    cliente.mostrar_dados()
    

print("\n   === dados marketing === ")
for cliente in dados_cliente:
    cliente.dados_sms_marketing()