import os
os.system("cls")

lista_numeros = []
impares = 0
pares = 0
QUANTIDADE_NUMEROS = 6

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite {i+1} número: "))
    lista_numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nInformando os números: ")
# for i in range(QUANTIDADE_NUMEROS):
#     print(f"{i+1}ª número infromado: {lista_numeros[i]:.0f}")

# ForEach (para cada)
for numero in lista_numeros:
    print(f"Número: {numero}")


print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de impares: {impares}")