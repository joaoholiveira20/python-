#verificando  a média
# Solicite ao usuário a média do aluno
# se maior ou igual a 7, mostre como aprovado
# caso contrário,  mostre como reprovado

import streamlit as st

st.title("Verificando a média")

nota1 = st.number_input("Digite sua primeira nota: ", min_value=0.1, max_value=10.0)
nota2 = st.number_input("Digite sua segunda nota: ", min_value=0.1, max_value=10.0)

media =  nota1 + nota2 / 2

if st.button("verificar"):
    if media >= 7:
        st.success(" VOCÊ FOI APROVADO!!!")
    else:
        st.error("VOCÊ FOI REPROVADO!!")

else:
    st.info("Digite a sua média! ")

# success - verde
# warning - amarelo
# info - azul
# error - vermelho