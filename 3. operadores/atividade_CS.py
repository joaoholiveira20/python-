#atividade operadores logicos

import os 
os.system ("cls")

login_salvo = "joao"
senha_salva = "123456"

login = input("Digite o seu login: ")
senha = input("Digite a sua senha: ")

if login == login_salvo and senha == senha_salva:
    resultado = "Bem-vindo"
else:
    resultado = "Login ou senha inválidos"

print(f"resultado: {resultado}")
print("FIM!!")

