# Atividade

import os
os.system("cls")

# pedindo os dados

n1 = int(input("Digite o valor do produto: "))
print("""
1 - Pagamento à vista
2 - Pagamento à prazo
""")
pag = int(input("Digite o número da forma de pagamento que deseja: "))


match pag:
    case 1:
        pagamento = "à vista"
        valor_desconto = n1 * 0.10
        total = n1 - valor_desconto
        print("--- Sua conta ---")
        print(f"Valor do produto: R${n1}")
        print(f"Forma de pagamento: {pagamento}")
        print(f"Valor do desconto: R${valor_desconto}")
        print(f"total a pagar: R${total}")
    case 2:
        pagamento = "à prazo"
        parcele = int(input("quantas parcelas podendo chegar ate 6x: "))
        if parcele >= 1 and parcele <= 6:
            valor_parcele = n1 / parcele
            print("--- Sua conta ---")
            print(f"Valor do produto: R${n1}")
            print(f"Forma de pagamento: {pagamento}")
            print(f"Quantidade de parcelas: {parcele}")
            print(f"Valor da parcela: R${valor_parcele:.2f}")
            print(f"total a prazo: R${n1}.00")
        else:
            print("opção invalida")
    case _:
        print("opção indisponível")


