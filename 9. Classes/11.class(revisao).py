import os
os.system("cls")
from dataclasses import dataclass


# Criando uma classe.
@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone: str

    # Função apenas para desta classe
    def mostrar_dados_cliente(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")

# Criando dois clientes com as características definidas na classe
# Vetor
lista_de_clientes = []

for i in range(3):
    dados_cliente = Cliente(nome=input("Digite seu nome: "), 
                    endereco=input("Digite seu endereço: "), 
                    telefone=input("Digite seu telefone: "))
    lista_de_clientes.append(dados_cliente)



# Mostrando dados do cliente.
for dados_cliente in lista_de_clientes:
    # Posição: 0, 1, 2
    dados_cliente.mostrar_dados_cliente()
