import os
os.system("cls")

valores = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numeros = float(input(f"Digite o {i+1}º número: "))
    if numeros <0:
        valores.append(0)
    else:
        valores.append(numeros)



print("\nExibindo números ")
for i in range(QUANTIDADE):
    print(f"{i+1}º Número: {valores[i]:.0f}")


# print("\nExibindo números ")
# for i, numeros in enumerate(valores, start=1):
#     print(f"{i}º Número: {numeros:.0f}")


