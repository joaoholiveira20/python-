# Algoritmo que multiplique um numero até 10 que o usuario escolha

import streamlit as st
import time

st.title("TABUADA!")

st.header("Coloque um número e será multiplicado")

n1 = st.number_input("Digite um número", min_value=0, max_value=100, step=1)

if st.button("Mostrar multiplicações"):
    st.header(f"Tabuada do {n1}")
    for i in range(1,11):
        resultado = n1 * i
        st.write(f"{n1} x {i} = {resultado}")
        time.sleep(0.4)
    st.header("FIM!! (seu burro<3)")