from fastapi import FastAPI
from funcao import listar_filme, atualizar_filme, deletar_filme, inserir_filme

#Rodar o fastapi
# python -m uvicorn api:app --reload

#Testar api FastAPI
# /docs > Documentação Swagger
# /redoc > Documentação redoc

#Iniciar o fastapi
app = FastAPI(title="Gerenciador de Filmes")

# GET = Pegar / Listar
# POST = Criar / Enviar 
# PUT = Atualiar
# DELETE = Deletar

@app.get("/")
def home():
    return {"mensagem": "Quero chocolate"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}