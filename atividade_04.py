#calculos 

import os
os.system ("cls")


# pedindos dados
n1  = int(input("Digite o primeiro numero: "))
n2  = int(input("Digite o segundo numero: "))

# operações matematicas
#soma 
soma = n1 + n2

#Subtração
sub = n1 - n2

#multiplicação
mult = n1 * n2

media = ( n1 + n2) / 2

maior = max(n1, n2)
menor = min(n1, n2)

#Exibindo dados:
print (f"primeiro numero: {n1}")
print (f"segundo numero: {n2}")
print (f"média: {media}")
print (f"soma: {soma}")
print (f"produto: {mult}")
if n1 == n2:
   print("os numeros são iguais!!")
else:
   print (f"maior valor: {maior}")
   print (f"menor valor: {menor}")