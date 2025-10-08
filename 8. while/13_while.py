import os
os.system("cls")

menor_salario = 9999
maior_salario = 0
quantidade_salario = 0
total_familia = 0
menor_salario = 0
maior_salario = 0


while True:
    os.system("cls")
    print("""
    Còdigo | Descrição
    1   | Adicionar família
    2   | Sair e exibir resultados
    """)

    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            total_familia += 1
            salario_familia = float(input("Digite o salário da família: "))
            filhos = int(input("Digite a quantidade de filhos: "))
            input("Aperte enter para continuar..")

            # média de salários
            quantidade_salario += 1
            soma_salario += salario_familia

            # média de filhos
            media_filhos = filhos / total_familia

        case 2:
            media_salarial = soma_salario / quantidade_salario if quantidade_salario != 0 else 0
            print("--- RESULTADO ---")
            print(f"Total de fámilias: {total_familia}")
            print(f"Média de salários: {media_salarial}")
            print(f"Maior salário: {max(salario_familia)}")
            print(f"Menor salário: {min(salario_familia)}")







