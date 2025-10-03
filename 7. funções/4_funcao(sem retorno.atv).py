import os
os.system("cls")

# função com passagem de parâmetros.
# Criando uma função
def saudacao(nome, idade, altura, peso):
    print(f"\nOlá, {nome}! Bem-vindo(a) ao nosso site.")
    print(f"Sua idade é {idade} anos.")
    print(f"Sua altura é {altura} cm")
    print(f"Seu peso é {peso:.1f}Kg")


print("Solicitando dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite a sua peso: "))

# Chamando a função.
saudacao(nome, idade, altura, peso)




