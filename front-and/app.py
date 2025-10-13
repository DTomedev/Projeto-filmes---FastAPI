import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes",page_icon="🎬")
st.title("Gerenciador de Filmes 🎬")

#Menu laterak
menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar Filme"])

if menu == "Catálogo":
    st.subheader("Todos os Filmes Disponíveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(f"**{filme['titulo']}**")
    else:
        st.error("Erro ao acessar a API")

elif menu == "Adicionar Filme":
    st.subheader("Adicionar Filmes")
    