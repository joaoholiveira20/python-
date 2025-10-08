import os
os.system("cls")

def inflacao(n1):
    if n1 <100:
        return n1 * 1.10 # Aumenta 10%
    else:
        return n1 * 1.20 # Aumenta em 20%
    
preco_produto = float(input("Digite o valor do produto: R$ "))

preco_inflacionado = inflacao(preco_produto)

print(f"O novo preço do produto é: R$ {preco_inflacionado:.2f}")