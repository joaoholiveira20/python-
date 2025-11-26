lista_clients = []

# CREATE - Adicionar / Inserir
print("CREATE - Adicionar / Inserir")
name = "Marta"
lista_clients.append(name)
print(f"O nome: {name} foi inserido com sucesso!")

# READ - Ler / Mostrar
print("\nRead - Ler / Mostrar")
print(lista_clients)

# UPDATE - Atualizar / Alterar
print("\nUpdate - Atualizar / Alterar")
nome_para_atualizar = "Marta"
if nome_para_atualizar in lista_clients:
    novo_nome = "Marta Silva"
    indice = lista_clients.index(nome_para_atualizar)
    lista_clients[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_clients)

# DELETE - Excluir / Remover
print("\nDelete - Excluir / Remover")
nome_para_excluir = "Maria"
if nome_para_excluir in lista_clients:
    lista_clients.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluído com sucesso!")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clients)
