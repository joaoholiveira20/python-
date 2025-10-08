import os
os.system("cls")

soma = 0
quantidade_notas = 0


while True:
    nota = float(input("Digite uma nota: "))
    # quantidade_notas = quantidade_notas + 1
    #soma = soma + nota
    quantidade_notas += 1
    soma += nota
    mais_notas = input ("Deseja inserir mais uma nota? \nUse (S OU N):").lower()

    if mais_notas == "n":
        break

media = soma / quantidade_notas

print("===RESULTADO===")
print(f"A média entre as notas são: {media:.2f}")



    