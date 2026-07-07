"""
database.py
-----------
Responsável pela conexão com o banco SQLite e pela criação/carga inicial
das tabelas a partir dos arquivos data/schema.sql e data/seed.sql.
"""

import os
import sqlite3

# Caminhos (baseados na localização deste arquivo, para funcionar de qualquer lugar)
PASTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_BANCO = os.path.join(PASTA_BASE, "data", "loja.db")
CAMINHO_SCHEMA = os.path.join(PASTA_BASE, "data", "schema.sql")
CAMINHO_SEED = os.path.join(PASTA_BASE, "data", "seed.sql")


def conectar():
    """Abre uma conexão com o banco e devolve o objeto de conexão.

    Usamos row_factory para acessar as colunas pelo nome (ex.: linha['nome']).
    """
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON;")  # ativa as chaves estrangeiras
    return conexao


def _executar_script(conexao, caminho_arquivo):
    """Lê um arquivo .sql e executa todo o seu conteúdo."""
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conexao.executescript(arquivo.read())


def criar_banco(reiniciar=False):
    """Cria o banco de dados.

    Se reiniciar=True, apaga o arquivo existente e recria tudo do zero.
    """
    if reiniciar and os.path.exists(CAMINHO_BANCO):
        os.remove(CAMINHO_BANCO)

    # Se o banco já existe e não é para reiniciar, não faz nada.
    if os.path.exists(CAMINHO_BANCO) and not reiniciar:
        print("Banco já existe. Use --reset para recriar do zero.")
        return

    conexao = conectar()
    try:
        _executar_script(conexao, CAMINHO_SCHEMA)  # cria as tabelas
        _executar_script(conexao, CAMINHO_SEED)     # insere os dados iniciais
        conexao.commit()
        print("Banco criado e populado com sucesso! ->", CAMINHO_BANCO)
    except sqlite3.Error as erro:
        conexao.rollback()
        print("Erro ao criar o banco:", erro)
    finally:
        conexao.close()


# Permite rodar "python src/database.py" para (re)criar o banco.
if __name__ == "__main__":
    import sys

    reset = "--reset" in sys.argv
    criar_banco(reiniciar=reset)
