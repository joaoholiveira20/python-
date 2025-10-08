import os
os.system("cls")

# Função para fazer a soma dos números.
def somar(n1, n2): 
    resultado = n1 + n2
    return resultado

 # Função para fazer a subtração entre os números.
def subtracao(n1, n2):
    resultado = n1 - n2
    return resultado

# Função para fazer a divisão dos números.
def divisao(n1, n2): 
    resultado = n1 / n2  if n2 != 0 else "Divisão por zero."
    return resultado
    # if n2 == 0:
    #     print("Divisão por zero.")
    # else:
    #     return n1 / n2

# Função para fazer a multiplicação dos números.
def multiplicacao(n1, n2): 
    resultado = n1 * n2
    return resultado

# Função para mostrar os resultados dos calculos feitos por outras funções.
def mostrar_resultado(): 
    os.system("cls")
    print("\n==RESULTADO DOS CALCULOS DELES==")
    print(f"A soma entre os números é: {soma}")
    print(f"A subtração entre os números é: {sub}")
    print(f"A divisão entre os números é: {div}")
    print(f"A multiplicação entre os números é: {mult}")

print("==DIGITE OS NÚMEROS==") # Pedindo os números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = somar(numero1, numero2) # Jogando os números para a função soma.
sub = subtracao(numero1, numero2) # Jogando os números para a função subtração.
div = divisao(numero1, numero2) # Jogando os números para a função divisão.
mult = multiplicacao(numero1, numero2) # Jogando os números para a função multiplicação.

mostrar_resultado() # Chamando a função pra mostrar os resultados.