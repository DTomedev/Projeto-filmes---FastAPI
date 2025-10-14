from fastapi import FastAPI
from funcao import listar_filme, atualizar_filme, deletar_filme, inserir_filme, buscar_filme

#Rodar o fastapi
# python -m uvicorn api:app --reload

#Testar api FastAPI
# /docs > Documentação Swagger
# /redoc > Documentação redoc

#Iniciar o fastapi
app = FastAPI(title="Gerenciador de Filmes")

# GET = Pegar / Listar
# POST = Criar / Enviar 
# PUT = Atualizar
# DELETE = Deletar

@app.get("/")
def home():
    return {"mensagem": "Bem-Vindo ao Gerenciador de Filmes"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}


@app.get("/filmes")
def exibir_filmes():
    filmes = listar_filme()
    lista = []
    for linha in filmes:
        lista.append({"id": linha[0],
            "titulo": linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avaliacao": linha[4]
            })
        
    return {"filmes": lista}


@app.put("/filmes/{id_filme}")
def update_filmes(id_filme: int, novo_titulo: str, novo_genero: str, nova_avaliacao: float):
    atualizar_filme(id_filme, novo_titulo, novo_genero, nova_avaliacao)
    filme = buscar_filme(id_filme)
    if filme:
        atualizar_filme(id_filme, novo_titulo, novo_genero, nova_avaliacao)
        return { "mensagem": "Filme atualizado com sucesso!"}
    else:
        return { "erro": "FIlme não encontrado"}

