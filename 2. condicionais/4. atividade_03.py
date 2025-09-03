#atividade 03

import os
os.system ("cls")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Dgite a segunda nota: "))
n3 = float(input("Dgite a terceira nota: "))

media = (n1 + n2 + n3) / 2

if media >= 7:
    resultado = "Aprovado"
else:
    resultado = "reprovado"


print(f"média: {media}")
print(f"resultado: {resultado}")