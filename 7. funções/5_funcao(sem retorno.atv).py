import os
os.system("cls")

def numeros(numero):
    if numero % 2 == 0:   
        print(f"o número {numero} é par!")
    else: 
        print(f"o número {numero} é impar!")


numero = int(input("Digite um número: "))

numeros(numero)


