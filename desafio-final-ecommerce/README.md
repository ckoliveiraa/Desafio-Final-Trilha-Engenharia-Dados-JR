# 🛒 Mini Loja — Projeto Final (Python + SQL)

Aplicação de linha de comando que simula os relatórios de uma pequena loja
virtual. Os dados ficam em um banco **SQLite** e são consultados com **Python**.

Este repositório é a **solução de referência** do desafio final do curso.

---

## 🎯 O que o projeto faz

- Cria um banco de dados com 4 tabelas relacionadas (clientes, produtos, pedidos e itens).
- Popula o banco com dados de exemplo.
- Oferece um menu no terminal para gerar relatórios:
  - Lista de produtos e filtro por categoria
  - Pedidos detalhados (juntando várias tabelas)
  - Faturamento por cliente, por categoria e por pedido
  - Ranking de produtos mais vendidos

---

## 🗂️ Estrutura do projeto

```
desafio-final-ecommerce/
├── README.md              # este arquivo
├── requirements.txt       # dependências (opcional / bônus)
├── .gitignore
├── data/
│   ├── schema.sql         # criação das tabelas + VIEW
│   ├── seed.sql           # dados iniciais
│   └── loja.db            # banco gerado (NÃO versionado)
├── src/
│   ├── database.py        # conexão e criação do banco
│   ├── queries.py         # todas as consultas SQL
│   └── main.py            # menu principal (ponto de entrada)
└── tests/
    └── test_queries.py    # testes automatizados (bônus)
```

---

## 🧩 Modelo de dados

```
clientes (1) ──< pedidos (1) ──< itens_pedido >── (1) produtos
```

- Um **cliente** faz vários **pedidos**.
- Um **pedido** contém vários **itens**.
- Cada **item** aponta para um **produto**.

---

## 🚀 Como executar

Pré-requisito: **Python 3.10+** instalado.

```bash
# 1. Criar o banco de dados (só na primeira vez)
python src/database.py --reset

# 2. Rodar a aplicação
python src/main.py
```

> Dica: se você rodar `python src/main.py` sem ter criado o banco,
> ele é criado automaticamente na primeira execução.

---

## ✅ Rodar os testes (bônus)

Recomendado usar um **ambiente virtual (`.venv`)** para isolar as dependências:

```bash
# 1. Criar o ambiente virtual
python -m venv .venv

# 2. Ativar o ambiente virtual
#    Windows (PowerShell):
.venv\Scripts\Activate.ps1
#    Windows (CMD):
#    .venv\Scripts\activate.bat
#    Linux / macOS:
#    source .venv/bin/activate

# 3. Instalar as dependências e rodar os testes
pip install -r requirements.txt
pytest -v
```

> Para sair do ambiente virtual depois, digite `deactivate`.
> A pasta `.venv/` já está no `.gitignore` — não precisa versioná-la.

---

## 🧠 Conceitos praticados

| Área    | Conceitos |
|---------|-----------|
| **SQL** | `CREATE TABLE`, PK/FK, `JOIN`, `WHERE`, `GROUP BY`, `SUM`/`COUNT`, `ORDER BY`, `VIEW` |
| **Python** | módulos, funções, `sqlite3`, tratamento de erros, entrada do usuário |
| **Git** | commits organizados, `.gitignore`, `README`, estrutura de pastas |

---

## 👤 Autor

- Nome do aluno: _preencher_
- Turma / Curso: _preencher_
