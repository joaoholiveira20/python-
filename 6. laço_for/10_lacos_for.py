# Um algoritmo que mostra dos 5 números indicados 
# quantos impares e pares tem. 

import streamlit as st


st.title("Vefiricando números pares e impares")
st.write("contando quantos são pares e impares dos numeros indicados")


pares = 0
impares = 0

for i in range(1, 6):
    numero = st.number_input(f"Digite o {i}º número inteiro:", min_value=1, step=1)
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1 

if st.button("Verificar"):
    st.success(f"quantidade de pares: {pares}")
    st.error(f"quantidade de impares: {impares}")
    st.header("FIM!! (seu burro <3)")
    st.write("Não gosto de impares.. ")
else:
    st.warning("Informe os números.. ")

