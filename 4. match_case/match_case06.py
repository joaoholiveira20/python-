#atividade

import os
os.system("cls")
print("""
    M - Masculino
    F - Fmeninino
""")
genero = input ("qual o seu Gênero (M OU F): ")


match genero:
    case "m":
        altura = float(input("Qual a sua altura: "))
        resultado_m= (72.7 * altura) - 58
        print(f"Seu peso ideal é: Kg {resultado_m:2.2f}")
    case "f":
        altura = float(input("Qual a sua altura: "))
        resultado_f = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é: Kg {resultado_f:2.2f}")
    case _:
        print("opção invalida")
