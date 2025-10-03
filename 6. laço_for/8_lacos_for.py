# Contagem regressiva a partir de um número 
# que o usuario informar até 1

import streamlit as st
import time


st.title("Contagem regressiva")

st.header("Informe um número")
n1 = st.number_input("Digite um número", min_value=1, max_value=100, step=1)

if st.button("Contagem regressiva"):
    for i in range(n1, 0, -1):
        st.write(i)
        time.sleep(1)
    # st.balloons()
    # st.snow()
    st.header("FIM!! (seu burro<3)")