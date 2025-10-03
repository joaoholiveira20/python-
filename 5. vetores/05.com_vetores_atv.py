import os
os.system("cls")

lista_numeros = []

QUANTIDADE_NUMEROS = 5

for i in range(5):
    numero = int(input(f"Digite o {i+1}ª numero: "))
    lista_numeros.append(numero)

maior = max(lista_numeros)
menor = min(lista_numeros)

print("\nMostrando os números. ")
for i in range(5):
    print(f"{i+1}ª Número: {lista_numeros[i]} ")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")