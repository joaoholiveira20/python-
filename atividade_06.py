#maçãs calculadas

import os
os.system ("cls")

n1 = int(input("quantidade de naçãs desejadas: "))

if n1 < 12:
    preco = 1.30
else:
    preco = 1.00

#caulculando

total = n1 * preco

#valor total

print(f"preço por maçã: {preco}")
print(f"O preço total é R$ {total:.2f}")