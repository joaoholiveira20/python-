import os
import time
os.system("cls")

lista_clients = []

while True:
    print("""
        1 - Adicionar / Inserir
        2 - Ler / Mostrar
        3 - Atualizar / Alterar
        4 - Excluir / Remover
        5 - Sair
    """)
    alternativa = int(input("Digite o número doque deseja fazer: "))


    match alternativa:
        case 1:
            os.system("cls")
            print("CREATE - Adicionar / Inserir")
            nome = input("Digite seu nome: ")
            lista_clients.append(nome)
            print(f"O nome: {nome} foi inserido com sucesso!")

        case 2:
            os.system("cls")
            print("\nRead - Ler / Mostrar")
            print(lista_clients)

        case 3:
            os.system("cls")
            print("\nUpdate - Atualizar / Alterar")
            nome_para_atualizar = input("Digite o nome para atualizar: ")
            if nome_para_atualizar in lista_clients:
                novo_nome = input("Digite o novo nome: ")
                indice = lista_clients.index(nome_para_atualizar)
                lista_clients[indice] = novo_nome
                print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
            else:
                print(f"O nome {nome_para_atualizar} não foi encontrado.")

            print(lista_clients)

        case 4:
            os.system("cls")
            print("\nDelete - Excluir / Remover")
            nome_para_excluir = input("Digite o nome para excluir: ")
            if nome_para_excluir in lista_clients:
                lista_clients.remove(nome_para_excluir)
                print(f"{nome_para_excluir} foi excluído com sucesso!")
            else:
                print(f"O nome {nome_para_excluir} não foi encontrado.")

            print(lista_clients)
        
        case 5:
            print("Encerrando programa...")
            break

        case _:
            os.system("cls")
            print("opção invalida.")

