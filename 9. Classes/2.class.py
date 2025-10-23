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


pessoa1 = Pessoa("João", 20, 75, 1.75)

# Apresentando dados.
print("===== RESULTADO =====")
print(f"Nome: {pessoa1.nome}\nidade: {pessoa1.idade} anos\npeso: {pessoa1.peso} kg\nAltura: {pessoa1.altura}M")
