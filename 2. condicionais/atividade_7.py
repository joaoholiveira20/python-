#notas 

import os
os.system ("cls")

nome = input("Digite seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >=9:
    conceito = "A"
elif media >=7.5:
    conceito = "B"
elif media >=6:
    conceito = "C"
elif media >=4:
    conceito = "D"
else:
    conceito = "E"
    

if media > 6:
    resultado = "aprovado"
else:
    resultado = "reprovado"

print(f"seu nome: {nome}")
print(f"conceito: {conceito}")
print(f"resultado: {resultado}")