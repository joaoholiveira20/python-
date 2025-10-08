# algotitmo que informa se esta correto ou não o login ou senha

import streamlit as st


st.title("Login e senha")


st.header("Vamos verificar seu login e senha")

login = "joao"
senha = "1234"


# variaveis internas do streamlit. (guardam valores da sessão.)
st.session_state.setdefault("campo", False)
st.session_state.setdefault("tentativas", 0)



login2 = st.text_input("Escreva seu login: ", disabled=st.session_state.campo)
senha2 = st.text_input("Digite sua senha: ", type="password", disabled=st.session_state.campo)

if st.button("Verificar"):
    if login2 == login and senha2 == senha:
        st.success("Estar correto!") 
        st.balloons()
    else:
        st.session_state.tentativas +=1
        if st.session_state.tentativas <= 3:
            st.error(f"Login ou senha incorretos. tentativas: {st.session_state.tentativas} ")
        else:
            st.session_state.campo = True
            st.error("Número de tentativas inválidas. ")