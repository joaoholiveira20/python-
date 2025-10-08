import os
os.system("cls")

soma = 0
quantidade_numeros = 0


while True:
    nota = float(input("Digite um número: "))
    # quantidade_notas = quantidade_notas + 1
    #soma = soma + nota
    if nota <0:
        break
    quantidade_numeros += 1
    soma += nota

media = soma / quantidade_numeros

print("===RESULTADO===")
print(f"A média entre os números são: {media:.2f}")



    