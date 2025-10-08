import os
import time

# função
def limpa_tela():
    time.sleep(3) # Esperar 3 segundos
    os.system("cls")

# Função para somar.
def somar(n1, n2):
    calcular = n1 + n2
    return calcular

# Função com parâmetros e sem retorno.
def mostrar_resultado(soma):
    print(f"Resultado: {soma}")

# Código principal. 
limpa_tela() # Chamando a função
primeiro_numero  = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

soma = somar(primeiro_numero, segundo_numero)

mostrar_resultado(soma) # Chamando a função