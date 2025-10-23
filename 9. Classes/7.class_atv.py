import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    email: str
    endereco: str

    def informacoes(self):
        print(f"Seu nome: {self.nome}")
        print(f"Seu E-mail: {self.email}")
        print(f"Seu endereço: {self.endereco}")

    def dados_entrega(self):
        print(f"Seu nome: {self.nome}")
        print(f"Seu endereço: {self.endereco}")

    def dados_email_marketing(self):
        print(f"Seu nome: {self.nome}")
        print(f"Seu E-mail: {self.email}")

print("== Solicitando dados. ==")
pessoa1 = pessoa(nome=input("Digite seu nome: "),
                 email=input("Infomr seu E-mail: "),
                 endereco=input("Digite seu endereço: "))


os.system("cls")
print("=== Mostrando dados ===")
pessoa1.informacoes()

print("\n=== Dados da entrega ===")
pessoa1.dados_entrega()

print("\n=== Dados do E-mail ===")
pessoa1.dados_email_marketing()