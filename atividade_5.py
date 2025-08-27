#votação 

import os 
os.system ("cls")

idade = int(input(" informe sua idade: "))

if idade <16:
    print("Não pode votar")
elif idade <18:
    print("Voto opcional")
elif idade <=65:
    print("Voto obrigatório")
else:
    print("não é obrigado a votar")
