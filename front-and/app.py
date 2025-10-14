import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes",page_icon="🎬")
st.title("Gerenciador de Filmes 🎬")

#Menu laterak
menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar Filme", "Atualizar Filmes", "Deletar"])

if menu == "Catálogo":
    st.subheader("Todos os Filmes Disponíveis")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
                st.dataframe(filmes)
        else:
            st.error("Nenhum filme disponível")   
    else:
        st.error("Erro ao acessar a API")

elif menu == "Adicionar Filme":
    st.subheader("Adicionar Filmes")
    titulo_filme = st.text_input("Digite o nome do filme: ")
    genero_filme = st.text_input("Digite o gênero do filme: ")
    ano_filme = st.number_input("Digite o ano do filme:", max_value=2030, min_value=1880, step=10)
    avaliacao_filme = st.number_input("Digite a avaliação do filme: ", max_value=10.0, min_value=0.0, step=0.1)
    if st.button("Salvar"):
        dados = {"titulo": titulo_filme, "genero": genero_filme, "ano": ano_filme, "avaliacao": avaliacao_filme}
        response = requests.post(f"{API_URL}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesso!")
        else:
             st.error("Erro ao adicionar o filme")

elif menu == "Atualizar Filmes":
    st.subheader("Atualizar Filmes")
    
