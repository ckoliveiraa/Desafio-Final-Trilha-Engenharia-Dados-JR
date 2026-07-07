-- =====================================================================
-- seed.sql — Dados iniciais (popula o banco para testes)
-- =====================================================================

-- Clientes
INSERT INTO clientes (nome, email, cidade) VALUES
    ('Ana Souza',      'ana@email.com',      'São Paulo'),
    ('Bruno Lima',     'bruno@email.com',    'Rio de Janeiro'),
    ('Carla Mendes',   'carla@email.com',    'Belo Horizonte'),
    ('Diego Fernandes','diego@email.com',    'São Paulo'),
    ('Elisa Rocha',    'elisa@email.com',    'Curitiba');

-- Produtos
INSERT INTO produtos (nome, categoria, preco, estoque) VALUES
    ('Notebook Gamer',    'Eletrônicos', 4500.00, 10),
    ('Mouse sem fio',     'Eletrônicos',   90.00, 50),
    ('Teclado Mecânico',  'Eletrônicos',  320.00, 30),
    ('Cadeira de Escritório','Móveis',    780.00, 15),
    ('Livro Python',      'Livros',        120.00, 40),
    ('Fone Bluetooth',    'Eletrônicos',  250.00, 25),
    ('Mesa de Escritório','Móveis',        650.00, 8);

-- Pedidos (cliente_id, data)
INSERT INTO pedidos (cliente_id, data) VALUES
    (1, '2026-06-01'),
    (2, '2026-06-03'),
    (1, '2026-06-10'),
    (3, '2026-06-12'),
    (4, '2026-06-15'),
    (5, '2026-06-20');

-- Itens de cada pedido (pedido_id, produto_id, quantidade, preco_unitario)
INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES
    (1, 1, 1, 4500.00),   -- Ana: 1 Notebook
    (1, 2, 2,   90.00),   -- Ana: 2 Mouses
    (2, 5, 3,  120.00),   -- Bruno: 3 Livros
    (2, 3, 1,  320.00),   -- Bruno: 1 Teclado
    (3, 6, 2,  250.00),   -- Ana: 2 Fones
    (4, 4, 1,  780.00),   -- Carla: 1 Cadeira
    (4, 7, 1,  650.00),   -- Carla: 1 Mesa
    (5, 2, 4,   90.00),   -- Diego: 4 Mouses
    (6, 5, 1,  120.00),   -- Elisa: 1 Livro
    (6, 6, 1,  250.00);   -- Elisa: 1 Fone
