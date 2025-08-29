#atividdae match:

import os 
os.system("cls")

n1 = int(input("Dgite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
carac = input ("Digite um caracter: ")

match carac:
    case "+":
        resultado = n1 + n2
    case "*":
        resultado = n1 * n2
    case "-":
        resultado = n1 - n2
    case "/":
        resultado = n1 / n2
    case _:
        resultado = "opção inválida"

print(f"Primeiro número: {n1}")
print(f"Segundo número: {n2}")
print(f"operador escolhido: {carac}")
print(f"Resultado: {resultado}")

