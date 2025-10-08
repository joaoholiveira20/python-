import os
os.system("cls")

def centimetros(n1):
    resultado = n1 * 100
    return resultado


n1 = int(input("Digite o valor em metros: "))

converter = centimetros(n1)


os.system("cls")
print("===RESULTADO===")
print(f"O valor em centimetros é: {converter}cm")