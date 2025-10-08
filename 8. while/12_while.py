
import os
os.system("cls")

#definindo variáveis
menor_idade = 9999
maior_idade = 0
quantidade_salario = 0
mulheres5k = 0
while True:
    os.system("cls")
    print("""
    Còdigo | Descrição
    1   | Adicionar pessoa
    2   | Exibir resultados
    3   | Sair    

    """)
    
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            #solicitando dados. 
            idade = int(input("Digite a idade: "))
            sexo = input("Informe o sexo - use F ou M: ").upper()
            salario = float(input("Digite o valor salário: "))


            # média de salários
            quantidade_salario += 1
            soma_salario += salario

            if idade < menor_idade:
                menor_idade = idade

            if idade > maior_idade:
                maior_idade = idade

            # Quantidade de mulheres com salário >= 5k.
            if salario >= 5000 and sexo == "F":
                mulheres5k += 1  

        case 2:
            media_salarial = soma_salario / quantidade_salario if quantidade_salario != 0 else 0
            if menor_idade == 9999:
                menor_idade = 0
                 
            print("\n =Exibindo resultado = ")
            print(f"Média de salários do grupo: {media_salarial}")
            print(f"Menor idade do grupo: {menor_idade}")
            print(f"Maior idade do grupo: {maior_idade}")
            print(f"Quantidade de mulheres com salário acima de 5 mil: {mulheres5k}")
            input("Pressione enter para continuar...")
        case 3:
            print("Saindo de programa.")
            break     
        case _:
            print("Opção invalida, tente novamente.")
            input("Pressione enter para continuar...")



            