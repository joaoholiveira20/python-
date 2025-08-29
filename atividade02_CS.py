#atividade operadores logicos

import os 
os.system ("cls")

idade = int(input("Digite a sua idade: "))

if idade >= 18 and idade <= 65:
    resultado = "é obrigatorio a votar!"
else:
    resultado = " não é obrigatorio a votar!"

print(f"Vc: {resultado}")