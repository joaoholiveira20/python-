import streamlit as st
import time


st.title("Laço de repetição - FOR")

st.header("Contagem. ")

numero = st.number_input("Digite um número: ", step=1)


if st.button("Iniciar"):
    for i in range(1,numero+1, 3):
        st.success(i)
        time.sleep(0.8)
    st.header("FIM!! (seu burro <3)")
else:
    st.warning("Digita um número ai (seu burro <3)")