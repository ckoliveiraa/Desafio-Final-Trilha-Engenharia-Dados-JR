"""
Testes automatizados (bônus) com pytest.
Rode com:  pytest -v

Estes testes criam um banco em memória, aplicam o schema + seed e
verificam se as consultas devolvem resultados coerentes.
"""

import os
import sqlite3

import pytest

# Permite importar os módulos da pasta src/
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import queries  # noqa: E402

PASTA_DATA = os.path.join(os.path.dirname(__file__), "..", "data")


@pytest.fixture
def conexao():
    """Cria um banco temporário em memória para cada teste."""
    con = sqlite3.connect(":memory:")
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON;")
    for arquivo in ("schema.sql", "seed.sql"):
        with open(os.path.join(PASTA_DATA, arquivo), "r", encoding="utf-8") as f:
            con.executescript(f.read())
    yield con
    con.close()


def test_listar_produtos(conexao):
    produtos = queries.listar_produtos(conexao)
    assert len(produtos) == 7  # o seed cadastra 7 produtos


def test_filtro_por_categoria(conexao):
    eletronicos = queries.produtos_por_categoria(conexao, "Eletrônicos")
    assert len(eletronicos) == 4
    # Todos devem ter preço maior que zero
    assert all(linha["preco"] > 0 for linha in eletronicos)


def test_faturamento_por_cliente(conexao):
    resultado = queries.faturamento_por_cliente(conexao)
    # Deve vir ordenado do maior para o menor total
    totais = [linha["total_gasto"] for linha in resultado]
    assert totais == sorted(totais, reverse=True)


def test_produto_mais_vendido(conexao):
    top = queries.produtos_mais_vendidos(conexao, limite=1)
    assert len(top) == 1
    assert top[0]["total_vendido"] > 0
