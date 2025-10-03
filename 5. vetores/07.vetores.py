import os
os.system("cls")


lista_pratos = []
precos_pratos = []

while True:
    opcao = int(input("""
Código    Prato         Valor
1         Picanha        R$ 25,00
2         Lasanha        R$ 20,00
3         Strogonoff     R$ 18,00
4         Bife acebolado R$ 15,00
5         Pão com ovo    R$ 5,00
                      
Digite a opção desejada: """))

    # Verificando opção digitada.
    match opcao:
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

    if opcao >= 1 and opcao <=5:
        lista_pratos.append(prato)
        precos_pratos.append(valor)

    resposta = input("Deseja escolher outro prato? \nResponda com S ou N: ").lower()
    if resposta == "n":
        break
    os.system("cls")

if sum(precos_pratos) == 0:
    print("\nnenhum prato foi escolhido")
else:
    print("\n= PRATOS ESCOLHIDOS=")
    for prato in lista_pratos:
        print(f"Prato: {prato}")

    print(f"\nTotal: R$ {sum(precos_pratos):.2f}")

print("\nVolte sempre!")




        