# verifique a idade de uma pessoa.
# se menor que 18, mostre: menor de idade.
# caso contrário, mostre: maior de idade.
# usando streamlit.

import streamlit as st

st.title("Verificando a idade")

idade = st.number_input("Digite a sua idade: ", min_value=0, max_value=130, step=1)

if st.button("Verificar"):
    if idade <18:
        st.write("Menor de idade.")
    else:
        st.write("Maior de idade.")

else:
    st.warning("Por favor, Digite a idade. ")
