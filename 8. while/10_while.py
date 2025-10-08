import os
os.system("cls")

pares = 0 
impares = 0
quantidade_pares = 0 
quantidade_impares = 0 
contador_geral = 0 
soma_pares = 0
soma_geral = 0

while True:
    numeros = int(input("Digite um número: "))
  
    if numeros > 0:
            contador_geral += 1
            soma_geral += numeros
            if numeros % 2 == 0:
                pares += 1
                quantidade_pares += 1
                soma_pares += numeros
            else:
                impares += 1
                quantidade_impares += 1
                
    if numeros == 0:
        break 

media_pares = soma_pares / pares if pares != 0 else 0 
media_geral = soma_geral / contador_geral if contador_geral != 0 else 0 

# if pares != 0:
#     media_pares = soma_pares / quantidade_pares
# else:
#     media_pares = 0 


    # media = soma_pares / contador_geral
    # media_geral = soma_geral / contador_geral


print("===RESULTADO===")
print(f"quantidade pares: {quantidade_pares}")
print(f"quantidade impares: {quantidade_impares}")
print(f"Média pares: {media_pares:2.2f}")
print(f"Média geral: {media_geral:2.2f}")