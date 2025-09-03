#maçãs calculadas

import os
os.system ("cls")

n1 = int(input("quantidade de maçãs desejadas: "))
n2 = int(input("quantidade de mangas desejadas: "))

if n2 <4:
    preco_manga = 2.40
else:
    preco_manga = 2.00

if n1 < 12:
    preco = 1.30
else:
    preco = 1.00

#caulculando

total = n1 * preco
total_manga = n2 * preco_manga
valor_total = preco + preco_manga

#valor total

print(f"preço por mangas: {preco_manga}")
print(f"preço por maçã: R${preco}")
print(f"O preço total é R$ {valor_total:.2f}")
print(f"Pix, Crédito, Débito ou Dinheiro? ")