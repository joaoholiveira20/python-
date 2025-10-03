# Escrever um algoritmo que mostra os
# números pares entre 100 e 120.

import streamlit as st
import time


st.title("Laço de repetição - FOR")

st.write("mostrando números pares entre 100 e 120.")


if st.button("Iniciar"):
    for i in range(100,121, 2):
        st.success(i)
        time.sleep(0.4)
    st.header("FIM!! (seu burro <3)")