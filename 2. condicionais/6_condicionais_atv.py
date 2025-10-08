import streamlit as st

st.title("Números")

n1 = st.number_input("Digite o primeiro número: ", min_value=1, step=1)
n2 = st.number_input("Digite o segundo número: ", min_value=1, step=1)

media = (n1 + n2) / 2
soma = n1 + n2
mult = n1 * n2

if st.button("Resultados"):
    st.info(f"MÉDIA: {media}")
    st.info(f"SOMA: {soma}")
    st.info(f"PRODUTO: {mult}")
    if n1 == n2:
        st.success("OS NÚMEROS SÃO IGUAIS!!")
    else: 
        if n1 > n2:
            st.success(f"Maior número: {n1}")
            st.error(f"Menor número: {n2}")
        else: 
            st.success(f"Maior número: {n2}")
            st.error(f"Menor número: {n1}")
else: 
    st.warning("Digite os números")