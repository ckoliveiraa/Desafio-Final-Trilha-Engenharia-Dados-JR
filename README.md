# 🏁 Desafio Final Trilha Engenharia Dados JR

## 🎯 Objetivo

Construir uma pequena aplicação de terminal para uma **loja virtual**, que
guarda seus dados em um banco **SQLite** e gera relatórios usando **Python**.
Ao final, você deve **publicar o projeto no seu GitHub**.

O desafio consolida três habilidades:
1. Modelar e consultar dados com **SQL**.
2. Organizar e integrar código em **Python**.
3. Versionar e publicar com **Git/GitHub**.

---

## 📋 Requisitos obrigatórios

### 1. Banco de dados (SQL)
- [ ] Criar **pelo menos 4 tabelas** com relacionamento (chaves primária e estrangeira).
      Sugestão: `clientes`, `produtos`, `pedidos`, `itens_pedido`.
- [ ] Popular as tabelas com dados de exemplo (mínimo 5 clientes e 5 produtos).
- [ ] Escrever consultas que usem: `JOIN`, `WHERE`, `GROUP BY` e uma função de
      agregação (`SUM`, `COUNT` ou `AVG`).
- [ ] Criar **uma `VIEW`** OU uma consulta de agregação mais elaborada.

### 2. Aplicação (Python)
- [ ] Conectar ao banco usando o módulo `sqlite3`.
- [ ] Organizar o código em **funções** (e, de preferência, em mais de um arquivo).
- [ ] Ter um **menu no terminal** que deixa o usuário escolher qual relatório ver.
- [ ] Usar **tratamento de erros** (`try/except`) em pelo menos um ponto.

### 3. GitHub
- [ ] `README.md` explicando o projeto e **como rodar**.
- [ ] `requirements.txt` (mesmo que vazio/comentado) e `.gitignore`.
- [ ] Estrutura de pastas organizada (ex.: `src/`, `data/`).
- [ ] Histórico com **pelo menos 3 commits** com mensagens claras.
- [ ] **Não commitar direto na `main`**: criar uma **branch de trabalho**
      (ex.: `feature/banco-de-dados`), desenvolver nela e depois abrir um
      **Pull Request** para a `main`.
- [ ] Repositório **público** com o link entregue ao instrutor.

### ⭐ Bônus (opcional)
- [ ] Testes automatizados com `pytest`.
- [ ] Ambiente virtual (`venv`).
- [ ] Um gráfico simples (ex.: `matplotlib`) ou exportar um relatório em CSV.
- [ ] Permitir que o usuário **cadastre** novos produtos/pedidos (INSERT via Python).

---

## 📦 O que entregar

1. Link do repositório público no GitHub.
2. O `README.md` deve permitir que qualquer pessoa rode o projeto seguindo os passos.

---

## 💡 Passo a passo sugerido

1. Desenhe no papel as tabelas e como elas se ligam.
2. Escreva o `schema.sql` (tabelas) e o `seed.sql` (dados).
3. Crie o `database.py` para conectar e montar o banco.
4. Crie o `queries.py` com uma função para cada consulta.
5. Crie o `main.py` com o menu que chama as consultas.
6. Escreva o `README.md`.
7. `git init` → primeiro commit → crie o repo no GitHub → `git push`.

> 💡 **Fluxo de Git esperado:** não trabalhe direto na `main`. Crie uma
> **branch de trabalho** para cada parte do projeto (ex.: `feature/banco`,
> `feature/consultas`, `feature/menu`), faça seus commits nela e depois abra
> um **Pull Request** para a `main`. Pesquise os comandos que faltarem — faz
> parte do aprendizado. 😉

---

## 🔒 Solução de referência (gabarito)

Existe uma resolução completa e funcional na pasta
**[`desafio-final-ecommerce/`](./desafio-final-ecommerce/)**.

> ⚠️ **LEIA COM ATENÇÃO — é de extrema importância que você faça o desafio sozinho.**
>
> O aprendizado está no processo de **errar, pesquisar e resolver por conta própria**.
> Copiar o gabarito anula todo o objetivo do desafio.
>
> **Use a solução de referência apenas para:**
> - tirar uma **dúvida pontual** quando estiver realmente travado (ex.: a sintaxe de um `JOIN`);
> - **conferir/corrigir** o seu resultado **depois** de já ter tentado.
>
> **Não use para:** copiar arquivos, ver a resposta antes de tentar, ou pular etapas.
>
> 💡 Sugestão: só abra o gabarito depois de ter passado pelo menos **30 minutos**
> tentando resolver o ponto em que travou.

---

Bom desafio! 🚀
