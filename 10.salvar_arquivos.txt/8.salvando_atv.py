import os
from dataclasses import dataclass
os.system('cls')

@dataclass
class Funcionario:
    nome1: str
    data_admissao: int
    matricula: float
    endereco1: str
    
    def exibir_funcionarios(self):
        print(F"\nNome: {self.nome1} \nData de admissâo: {self.data_admissao} \nMatrícula: {self.matricula} \nEndereço: {self.endereco1}")
    
@dataclass
class Cliente:
    nome: str
    data_de_nascimento: float
    endereco: str
    

    def exibir_clientes(self):
        print(F"\nNome: {self.nome} \nData de nascimento: {self.data_de_nascimento} \nEndereço: {self.endereco}")


FUNCIONARIOS = 3
CLIENTES = 3

vetor_funcionarios = []
vetor_clientes = []

for i in range (FUNCIONARIOS):
    os.system("cls")
    print("FUNCIONÁRIO")
    funcionarios = Funcionario(
        nome1= input("Digite seu nome: "),
        data_admissao= int(input('Digite a sua data de admissão: ')),
        matricula= float(input('Digite a sua matricula: ')),
        endereco1= input("Digite o seu Endereço: ")
    )
    vetor_funcionarios.append(funcionarios)
    
for i in range(CLIENTES):
    os.system("cls")
    print("CLIENTE")
    clientes = Cliente(
        nome= input('Digite seu nome: '),
        data_de_nascimento= float(input('Digite sua data de nascimento: ')),
        endereco= input('Digite seu endereço: ')
    )
    vetor_clientes.append(clientes)
    

funcionarioo = "Dados_funcionario.csv"
with open(funcionarioo, "a") as arquivo_funcionarios:
    for funcionarios in vetor_funcionarios:
        arquivo_funcionarios.write(f'{funcionarios.nome1},{funcionarios.data_admissao},{funcionarios.matricula},{funcionarios.endereco1}\n')
    print('Dados salvos com sucesso.')
        
        

client = "Dados_clientes.csv"
with open(client, "a",) as arquivo_clientess:
    for clientes in vetor_clientes:
        arquivo_clientess.write(f'{clientes.nome},{clientes.data_de_nascimento},{clientes.endereco}\n')

os.system("cls")
print('Dados salvos com sucesso.')
print()
print("=== EXIBINDO DADOS DOS FUNCIONÁRIOS ===")
try:
    with open(funcionarioo, "r") as arquivo:
        lista_todos_funcionarios = arquivo.readlines() 
        for linha_funcionarios in lista_todos_funcionarios:
            nome1, data_admissao, matricula, endereco1 = linha_funcionarios.strip().split(",")
            dados_funcionarios = Funcionario(nome1=nome1, data_admissao=int(data_admissao), matricula=float(matricula), endereco1=endereco1)
            dados_funcionarios.exibir_funcionarios()
except FileNotFoundError:
    print("Arquivo não encontrado")

print("\n=== EXIBINDO DADOS DOS CLIENTES ===")
try:
    with open(client, "r") as arquivo:
        lista_todos_clientes = arquivo.readlines()
        for linha_clientes in lista_todos_clientes:
            nome, data_de_nascimento, endereco = linha_clientes.strip().split(",")
            dados_cliente = Cliente(nome=nome, data_de_nascimento=float(data_de_nascimento), endereco=endereco)
            dados_cliente.exibir_clientes()
except FileNotFoundError:
    print("Arquivo não encontrado")




