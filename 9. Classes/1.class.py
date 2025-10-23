import os
from dataclasses import dataclass
os.system("cls")

# Estrutua de dados: classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:      
    nome: str
    idade: int
    peso: float

# Exemplo de uso da classe.
pessoa1 = Pessoa(nome="João",cpf="215.458.529-00", idade=20)
pet1 = Pet(nome="Totó", idade=4, peso=2.100)

print("Exibindo dados da Pessoa.")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nCPF: {pessoa1.cpf}\n")

print("Exibindo dados do Pet.")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\nPeso: {pet1.peso}")
