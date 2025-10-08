import os
import time

# função
def limpa_tela():
    time.sleep(3) # Esperar 3 segundos
    os.system("cls")

# Função para somar.
def calcular_media(n1, n2):
    calcular = (n1 + n2) / 2
    return calcular

# Função com parâmetros e sem retorno.
def mostrar_resultado(media):
    print(f"Resultado: {media}")
    if media >= 7:
        print(f"Aprovado.")
    else:
        print(f"Reprovado.")

# Código principal. 
limpa_tela() # Chamando a função
primeiro_numero  = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

media = calcular_media(primeiro_numero, segundo_numero)

mostrar_resultado(media) # Chamando a função