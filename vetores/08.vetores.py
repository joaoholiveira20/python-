import os
os.system("cls")

numeros_positivo = []
numeros_negativos = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero <0:
        numeros_negativos.append(numero)
    else:
        numeros_positivo.append(numero)
        

print("\n=====RESULTADO=====")
print(f"Números negativos: {len(numeros_negativos)}")
print(f"Soma dos números positivos: {sum(numeros_positivo):.0f}")