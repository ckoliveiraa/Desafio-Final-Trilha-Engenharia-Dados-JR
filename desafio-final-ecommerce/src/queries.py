"""
queries.py
----------
Reúne as consultas SQL do projeto em funções Python.
Cada função recebe uma conexão e devolve uma lista de linhas (sqlite3.Row).

Aqui aparecem os principais conceitos de SQL cobrados no desafio:
- SELECT / WHERE
- JOIN entre tabelas
- GROUP BY com funções de agregação (SUM, COUNT, AVG)
- ORDER BY
- uso de uma VIEW
"""


def listar_produtos(conexao):
    """Lista todos os produtos ordenados por categoria e nome."""
    sql = """
        SELECT id, nome, categoria, preco, estoque
        FROM produtos
        ORDER BY categoria, nome;
    """
    return conexao.execute(sql).fetchall()


def produtos_por_categoria(conexao, categoria):
    """Filtra produtos de uma categoria específica (exemplo de WHERE com parâmetro)."""
    sql = """
        SELECT nome, preco, estoque
        FROM produtos
        WHERE categoria = ?
        ORDER BY preco DESC;
    """
    return conexao.execute(sql, (categoria,)).fetchall()


def pedidos_detalhados(conexao):
    """Mostra cada item comprado juntando 4 tabelas (JOIN)."""
    sql = """
        SELECT
            ped.id             AS pedido,
            cli.nome           AS cliente,
            ped.data           AS data,
            prod.nome          AS produto,
            item.quantidade    AS qtd,
            item.preco_unitario AS preco,
            (item.quantidade * item.preco_unitario) AS subtotal
        FROM pedidos ped
        JOIN clientes cli     ON cli.id = ped.cliente_id
        JOIN itens_pedido item ON item.pedido_id = ped.id
        JOIN produtos prod    ON prod.id = item.produto_id
        ORDER BY ped.id;
    """
    return conexao.execute(sql).fetchall()


def faturamento_por_cliente(conexao):
    """Total gasto por cada cliente (JOIN + GROUP BY + SUM + ORDER BY)."""
    sql = """
        SELECT
            cli.nome                                  AS cliente,
            COUNT(DISTINCT ped.id)                    AS qtd_pedidos,
            SUM(item.quantidade * item.preco_unitario) AS total_gasto
        FROM clientes cli
        JOIN pedidos ped      ON ped.cliente_id = cli.id
        JOIN itens_pedido item ON item.pedido_id = ped.id
        GROUP BY cli.nome
        ORDER BY total_gasto DESC;
    """
    return conexao.execute(sql).fetchall()


def faturamento_por_categoria(conexao):
    """Quanto cada categoria de produto faturou (GROUP BY em produtos)."""
    sql = """
        SELECT
            prod.categoria                             AS categoria,
            SUM(item.quantidade)                       AS unidades_vendidas,
            SUM(item.quantidade * item.preco_unitario) AS faturamento
        FROM itens_pedido item
        JOIN produtos prod ON prod.id = item.produto_id
        GROUP BY prod.categoria
        ORDER BY faturamento DESC;
    """
    return conexao.execute(sql).fetchall()


def produtos_mais_vendidos(conexao, limite=3):
    """Ranking dos produtos com maior quantidade vendida."""
    sql = """
        SELECT
            prod.nome            AS produto,
            SUM(item.quantidade) AS total_vendido
        FROM itens_pedido item
        JOIN produtos prod ON prod.id = item.produto_id
        GROUP BY prod.nome
        ORDER BY total_vendido DESC
        LIMIT ?;
    """
    return conexao.execute(sql, (limite,)).fetchall()


def faturamento_por_pedido(conexao):
    """Usa a VIEW criada no schema.sql para listar o total de cada pedido."""
    sql = "SELECT * FROM vw_faturamento_pedido ORDER BY total_pedido DESC;"
    return conexao.execute(sql).fetchall()
