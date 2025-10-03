import os
os.system("cls")

def numeros(numero):
    if numero >0:   
        print(f"o número {numero} é positivo! ")
    else: 
        print(f"o número {numero} é negativo! ")


numero = int(input("Digite um número: "))

numeros(numero)


