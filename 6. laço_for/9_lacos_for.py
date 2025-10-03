# somandos 5 números que op usuario informar 
# e mostrando o resultado de todos somados

import streamlit as st



st.title("CÁLCULO")

st.write("Todos os números seram somados")


n1 = st.number_input("Digite o primeiro número", min_value=1, step=1)
n2 = st.number_input("Digite o segundo número", min_value=1, step=1)
n3 = st.number_input("Digite o terceiro número", min_value=1, step=1)
n4 = st.number_input("Digite o quarto número", min_value=1, step=1)
n5 = st.number_input("Digite o quinto número", min_value=1, step=1)

if st.button("SOMA"):
    resultado = n1 + n2 + n3 + n4 + n5
    st.write(f"SOMA: {n1} + {n2} + {n3} + {n4} + {n5} = {resultado}")
    st.header("FIM!! (seu burro <3)")
else:
    st.warning("Informe os números")