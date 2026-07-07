-- =====================================================================
-- schema.sql — Estrutura do banco de dados da Mini Loja (E-commerce)
-- Banco: SQLite
-- 4 tabelas com relacionamentos (chaves primárias e estrangeiras)
-- =====================================================================

-- Garante que as chaves estrangeiras sejam validadas
PRAGMA foreign_keys = ON;

-- Apaga as tabelas se já existirem (facilita recriar o banco do zero)
DROP TABLE IF EXISTS itens_pedido;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS clientes;

-- ---------------------------------------------------------------------
-- Tabela: clientes
-- ---------------------------------------------------------------------
CREATE TABLE clientes (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    nome     TEXT    NOT NULL,
    email    TEXT    NOT NULL UNIQUE,
    cidade   TEXT    NOT NULL
);

-- ---------------------------------------------------------------------
-- Tabela: produtos
-- ---------------------------------------------------------------------
CREATE TABLE produtos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT    NOT NULL,
    categoria TEXT    NOT NULL,
    preco     REAL    NOT NULL CHECK (preco >= 0),
    estoque   INTEGER NOT NULL CHECK (estoque >= 0)
);

-- ---------------------------------------------------------------------
-- Tabela: pedidos (cada pedido pertence a UM cliente)
-- ---------------------------------------------------------------------
CREATE TABLE pedidos (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    data       TEXT    NOT NULL,   -- formato 'AAAA-MM-DD'
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- ---------------------------------------------------------------------
-- Tabela: itens_pedido (liga pedidos e produtos — relação N:N)
-- ---------------------------------------------------------------------
CREATE TABLE itens_pedido (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id      INTEGER NOT NULL,
    produto_id     INTEGER NOT NULL,
    quantidade     INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario REAL    NOT NULL,   -- preço no momento da compra
    FOREIGN KEY (pedido_id)  REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

-- ---------------------------------------------------------------------
-- VIEW: faturamento por pedido (exemplo de consulta reaproveitável)
-- Soma o valor total (quantidade * preço) de cada pedido.
-- ---------------------------------------------------------------------
CREATE VIEW IF NOT EXISTS vw_faturamento_pedido AS
SELECT
    p.id                                  AS pedido_id,
    c.nome                                AS cliente,
    p.data                                AS data,
    SUM(i.quantidade * i.preco_unitario)  AS total_pedido
FROM pedidos p
JOIN clientes c      ON c.id = p.cliente_id
JOIN itens_pedido i  ON i.pedido_id = p.id
GROUP BY p.id, c.nome, p.data;
