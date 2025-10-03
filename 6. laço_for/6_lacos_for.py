# Mostrando números ímpares de 1 a 20

import streamlit as st
import time

st.title("Números ímpares!")

st.write("Mostrando números ímpares entre 1 e 20")

if st.button("iniciar"):
    for i in range(1,21, 2):
        st.info(i)
        time.sleep(0.5)
    st.header("FIM!! (seu burro <3)")

else:
    st.warning("APERTE O BOTÃO SACANA!!")
