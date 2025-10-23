import os
os.system("cls")
from dataclasses import dataclass

# Estrutura de dados: classes
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                  idade=int(input("Digite a sua idade: ")), 
                  peso=float(input("Digite seu peso: ")), 
                  altura=float(input("Digite a sua altura: ")))



# Apresentando dados.
print("\n===== RESULTADO =====")
print(f"Nome: {pessoa1.nome}\nidade: {pessoa1.idade} anos\npeso: {pessoa1.peso} kg\nAltura: {pessoa1.altura}M")
