
import os
os.system("cls")

# Criando um vetor (lista).
lista_notas = []

# Inserindo nota.
for i in range(4):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)
    
# Média:
media = sum(lista_notas) / len(lista_notas)

# Mostrar notas:
for i in range(4):
    print(f"Nota {i+1}ª: {lista_notas[i]}")

print(f"Média: {media:2.1f}")
if media >= 7:
    print("Aprovado!")
elif media >= 5: 
    print("Recupereção!")
else:
    print("Reprovado..")
print("Fim!!")