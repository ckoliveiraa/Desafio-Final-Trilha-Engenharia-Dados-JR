"""
main.py
-------
Ponto de entrada da aplicação: um menu no terminal que executa as
consultas definidas em queries.py e mostra os resultados em tabelas.

Como rodar:
    python src/database.py --reset   (primeira vez, cria o banco)
    python src/main.py
"""

import os

from database import conectar, criar_banco, CAMINHO_BANCO
import queries


def imprimir_tabela(titulo, linhas):
    """Imprime uma lista de sqlite3.Row como uma tabela simples no terminal."""
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)

    if not linhas:
        print("(nenhum resultado)")
        return

    # Cabeçalho a partir dos nomes das colunas
    colunas = linhas[0].keys()
    print(" | ".join(str(c) for c in colunas))
    print("-" * 60)

    # Linhas de dados
    for linha in linhas:
        valores = []
        for coluna in colunas:
            valor = linha[coluna]
            # Formata números com casas decimais para ficar mais legível
            if isinstance(valor, float):
                valor = f"{valor:.2f}"
            valores.append(str(valor))
        print(" | ".join(valores))


def menu():
    """Mostra as opções e devolve a escolha do usuário."""
    print("\n" + "*" * 60)
    print("           MINI LOJA - PAINEL DE RELATÓRIOS")
    print("*" * 60)
    print("1  - Listar todos os produtos")
    print("2  - Filtrar produtos por categoria")
    print("3  - Ver pedidos detalhados")
    print("4  - Faturamento por cliente")
    print("5  - Faturamento por categoria")
    print("6  - Produtos mais vendidos (top 3)")
    print("7  - Faturamento por pedido (usando VIEW)")
    print("0  - Sair")
    return input("Escolha uma opção: ").strip()


def main():
    # Cria o banco automaticamente na primeira execução.
    if not os.path.exists(CAMINHO_BANCO):
        print("Banco não encontrado. Criando pela primeira vez...")
        criar_banco(reiniciar=True)

    conexao = conectar()
    try:
        while True:
            opcao = menu()

            if opcao == "0":
                print("Até logo!")
                break
            elif opcao == "1":
                imprimir_tabela("Produtos", queries.listar_produtos(conexao))
            elif opcao == "2":
                categoria = input("Digite a categoria (ex.: Eletrônicos): ").strip()
                imprimir_tabela(
                    f"Produtos da categoria '{categoria}'",
                    queries.produtos_por_categoria(conexao, categoria),
                )
            elif opcao == "3":
                imprimir_tabela("Pedidos detalhados", queries.pedidos_detalhados(conexao))
            elif opcao == "4":
                imprimir_tabela("Faturamento por cliente", queries.faturamento_por_cliente(conexao))
            elif opcao == "5":
                imprimir_tabela("Faturamento por categoria", queries.faturamento_por_categoria(conexao))
            elif opcao == "6":
                imprimir_tabela("Produtos mais vendidos", queries.produtos_mais_vendidos(conexao))
            elif opcao == "7":
                imprimir_tabela("Faturamento por pedido", queries.faturamento_por_pedido(conexao))
            else:
                print("Opção inválida! Tente novamente.")
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
    finally:
        conexao.close()


if __name__ == "__main__":
    main()
