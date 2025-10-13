from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                id SERIAL PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano INTEGER NOT NULL,
                avaliacao REAL
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

#criar_tabela()


def inserir_filme(titulo, genero, ano, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES(%s, %s, %s, %s)",
            (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme: {erro}")
        finally:
            cursor.close()
            conexao.close()

#inserir_filme("avatar", "Ficção Cientifica", 2009, 8.0)

def listar_filme():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "SELECT * FROM filmes ORDER BY ID",
            )
            for linha in cursor.fetchall():
                print(f"ID {linha[0]} | NOME: {linha[1]} | IDADE: {linha[2]} | CURSO: {linha[3]}")
        except Exception as erro:
            print(f"Erro ao tentar listar filmes: {erro}")
        finally:
            cursor.close()
            conexao.close()


def atualizar_filme(id_filme, nova_atualizacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "UPDATE filmes SET avaliacao = %s WHERE Id = %s",
            (nova_atualizacao, id_filme)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar filmes: {erro}")
        finally:
            cursor.close()
            conexao.close()

#atualizar_filme(1, 9)

def deletar_filme(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM filmes WHERE id = %s",
                (id_filme,)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar deletar filme: {erro}")
        finally:
            cursor.close()
            conexao.close()

