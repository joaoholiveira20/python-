# atividade

import os
os.system("cls")

#Menu 
print("""
Código \t\t prato \t\t  Valor
   1 \t\t Picanha \t R$25,00
   2 \t\t Lasanha \t R$20,00
   3 \t\t Strogonoff \t R$18,00
   4 \t\tBife Acebolado \t R$15,00   
   5 \t\t Pão com ovo \t R$5,00
""")

codigo = int(input("Digite o código do prato desejado: "))

match codigo:
    case 1:
        prato = "Picanha"
        valor = 25.00
    case 2:
        prato = "Lasanha"
        valor = 20.00
    case 3:
        prato = "Strogonoff"
        valor = 18.00
    case 4:
        prato = "Bife Acebolado"
        valor = 15.00
    case 5:
        prato = "Pão com ovo"
        valor = 5.00
    case _:
        prato = "prato inválido"
#exibição

print("===Seu pedido===")
print(f"Prato: {prato}")
print(f"Valor: R${valor}")

