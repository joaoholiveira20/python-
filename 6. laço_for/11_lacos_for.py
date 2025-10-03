# Algoritmo que mostra a média de 4 números 
# informados pelo usuario 

import streamlit as st


st.title("MÉDIA")

st.write("Mostrando as médias dos valores infomados")

n1 = st.number_input("Digite o primeiro número", min_value=1, step=1)
n2 = st.number_input("Digite o segundo número", min_value=1, step=1)
n3 = st.number_input("Digite o terceiro número", min_value=1, step=1)
n4 = st.number_input("Digite o quarto número", min_value=1, step=1)



if st.button("Mostrar média"):
    resultado = (n1 + n2 + n3 + n4 ) / 4
    st.success(f"MÉDIA: {resultado}")
    st.header("FIM!! (seu burro <3)")
else:
    st.warning("Informe os números")