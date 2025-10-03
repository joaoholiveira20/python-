import os
os.system("cls")

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"Resultado: {numero} * {i} = {resultado}")

numero = int(input("Digite um número: "))

tabuada(numero)
