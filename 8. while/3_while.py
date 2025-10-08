# Verificando média de aluno a partir da nota que o usuario informar

import streamlit as st

st.title("Verificando média")

st.write("Vamos verificar sua média")

nota = st.number_input("Digite a 1ª nota: ", min_value=0, max_value=10)
nota2 = st.number_input("Digite a 2ª nota: ", min_value=0, max_value=10)


if st.button("Verificar"):
    if nota < 0 or nota > 10 or nota2 <0 or nota > 10:
        st.warning("A nota deve ser entre 0 e 10. ")
    else: 
        media = (nota + nota2) / 2
        st.info(f"Sua Média é: {media}")


# import os
# os.system("cls")

# print("Laço de repetição - while")


# QUANTIDADE_NOTA = 2
# soma = 0

# for i in range(QUANTIDADE_NOTA):
#     while True:
#         nota = int(input(f"Digite a {i+1}ª nota: "))
#         if nota >= 0 and nota <=10:
#             break
#     soma = soma + nota

# media = soma / QUANTIDADE_NOTA

# print(f"Média: {media}")