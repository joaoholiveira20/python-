#atividade

import os
os.system("cls")

genero = input ("qual o seu Gênero (M OU F): ")
altura = float(input("Qual a sua altura: "))

match genero:
    case "m":
        resultado_m= (72.7 * altura) - 58
        print(f"Seu peso ideal é: {resultado_m:2.2f}")
    case "f":
        resultado_f = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é: Kg:{resultado_f:2.2f}")
    case _:
        print("opção invalida")
