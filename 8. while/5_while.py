# import os
# os.system("cls")
# tentativas = 0
# login_salvo = "joao"
# senha_salva = "123"

# max_tentativas = 3
# for i in range(3):
#     while True:
#         if tentativas >=3:
#             break
#         print(f"\nTentativa: {tentativas+1}")
#         login = input("Digite seu login: ")
#         senha = input("Digite sua senha: ")

#         if login == login_salvo and senha == senha_salva:
#             print("Login feito com sucesso!!")
#             break
#         else:
#             print("login ou senha incorretos..")
#             tentativas += 1




# algotitmo que informa se esta correto ou não o login ou senha

import streamlit as st

login = "joao"
senha = "1234"

st.title("Login e senha")

st.header("Vamos verificar seu login e senha")


login2 = st.text_input("Escreva seu login: ")
senha2 = st.text_input("Digite sua senha: ", type="password")

if st.button("Verificar"):
    if login2 == login and senha2 == senha:
        st.success("Estar correto!") 
        st.balloons()
    else:
        st.error("Login ou senha incorretos. ")
