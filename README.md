# 🏁 Desafio Final Trilha Engenharia Dados JR

## 🎯 O desafio final: o seu pipeline, do zero

Quatro aulas construindo um pipeline sobre um dado que alguém escolheu para você.
O desafio final é fazer tudo de novo com um dado que **você escolhe**, do arquivo
de origem até os indicadores, com **Python, SQL, IA e git** — do jeito que fizemos
com a Olist.

O passo que não foi mostrado é o mais difícil de todos: **decidir sozinho quais
perguntas o dado responde.**

---

## ✅ Pré-requisitos

Antes de começar este desafio, você precisa:

- [ ] Ter concluído a **trilha de SQL**.
- [ ] Ter concluído a **trilha de Python/Git e IA**.
- [ ] Ter assistido às **aulas ao vivo** do **Projeto_olist**.

---

## 📋 Requisitos do projeto

| Requisito | Como fica |
|---|---|
| **Fonte escolhida por você** | Um dataset do Kaggle ou uma API pública, sobre um tema que você conhece. A Olist também vale, desde que feita de outro jeito: outras perguntas, outros indicadores e outras transformações — não o pipeline do curso copiado. Se for Kaggle, a licença precisa permitir uso público, porque o repositório é público. |
| **Duas tabelas ou mais** | Ligadas por uma chave, para existir pelo menos um `JOIN`. Não há mínimo de linhas. |
| **Três camadas** | Dado bruto, dado transformado e indicadores, cada camada separada da outra. Os nomes são seus: `raw`, `refined` e `marts` no curso; `bronze`, `silver` e `gold` ou qualquer outro serve, desde que a separação exista. **Na camada bruta, nada é alterado.** |
| **Testes unitários** | Testes com `pytest`, rodando com dado inventado e sem abrir o banco do projeto, como no passo 4.6. |
| **Repositório público no GitHub pessoal** | Na sua conta, não em conta de empresa nem em fork do repositório do curso. |
| **Histórico de commits** | O projeto construído aos poucos, com um commit por etapa e mensagem dizendo o que mudou — não o projeto inteiro em um commit só. O histórico é lido junto com o código: ele mostra a ordem em que as coisas aconteceram. |
| **Dashboard** · _opcional_ | Se fizer, ele lê só da camada de indicadores, sem nenhum cálculo na tela, como o painel da seção 07. |

### 🤖 A IA entra em todas as etapas — e você confere todas

O README termina com uma seção curta: **em que etapa a IA errou ou assumiu algo
que você não pediu, e como você descobriu** — quase sempre contando linhas antes
e depois.

> Um projeto em que a IA não errou nenhuma vez é um projeto em que ninguém conferiu.

---

## 📝 O README do seu projeto

É a primeira coisa que a correção abre. Ele precisa ter:

- [ ] A **fonte do dado** (link e, se for Kaggle, a licença).
- [ ] O que é **uma linha de cada tabela**.
- [ ] As **três camadas** e os **indicadores** que saem delas.
- [ ] **Como rodar do zero**, em comandos, incluindo os testes.
- [ ] A **seção sobre a IA**.

Quem clona o repositório tem que chegar aos indicadores **só lendo o README**.

---

## 📦 Entrega

O **link do repositório** deve ser entregue no **formulário dentro da
plataforma**, na **Trilha de Engenharia de Dados JR**.

Projeto incompleto também se entrega: **uma etapa travada com a dúvida escrita
no README vale mais que um projeto inteiro copiado.**

---

## 🔎 Critério principal

É o do curso inteiro:

- cada indicador tem um arquivo **`.sql`** de onde saiu;
- cada decisão sobre o dado tem um **motivo escrito**;
- o histórico do **git** conta a ordem em que as coisas aconteceram.

---

Bom desafio! 🚀
