import os
os.system("cls")

mes = int(input("Digite um numero: "))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Opção inválida, Digite um número de 1 a 12!!")
