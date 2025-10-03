import os
os.system("cls")

# Criando um vetor (lista).
lista_notas = []

# Inserindo nota.
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)
    
# Média:
media = sum(lista_notas) / len(lista_notas)

# Mostrar notas:
for i in range(3):
    print(f"Nota: {lista_notas[i]}")

print(f"Média: {media:2.1f}")
print("Fim!!")