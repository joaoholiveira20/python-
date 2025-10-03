#verificando  a média
# se maior ou igual a 7, mostre como aprovado
# caso contrário,  mostre como reprovado

import streamlit as st

st.title("Verificando a média")

nota1 = st.number_input("Digite sua primeira nota: ", min_value=1.0, max_value=10.0)
nota2 = st.number_input("Digite sua segunda nota: ", min_value=1.0, max_value=10.0)
nota3 = st.number_input("Digite sua terceira nota: ", min_value=1.0, max_value=10.0)

media = (nota1 + nota2 + nota3) / 3

if st.button("verificar"):
    if media >= 7:
        st.info(f"Média: {media:.1f}")
        st.success(" VOCÊ FOI APROVADO!!!")
    elif media >=4:
        st.info(f"Média: {media:.1f}")
        st.warning("VOCê ESTÁ NA RECUPERAÇÃO!!")
    else:
        st.info(f"Média: {media:.1f}")
        st.error("VOCÊ FOI REPROVADO!!")

else:
    st.info("Digite a sua média! ")

# success - verde
# warning - amarelo
# info - azul
# error - vermelho