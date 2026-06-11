from controllers.categoria_controller import CategoriaController
from controllers.entrada_controller import EntradaController
from controllers.saida_controller import SaidaController

categoria_controller = CategoriaController()
entrada_controller = EntradaController()
saida_controller = SaidaController()


def menu_categorias():
    while True:
        print("\n=== CATEGORIAS ===")
        print("1 - Adicionar categoria")
        print("2 - Listar categorias")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1": categoria_controller.adicionar_categoria()
        elif opcao == "2": categoria_controller.listar()
        elif opcao == "0": break

        else: print("Opção inválida.")


def menu_entradas():
    while True:
        print("\n=== ENTRADAS ===")
        print("1 - Adicionar entrada")
        print("2 - Listar entradas")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1": entrada_controller.adicionar_entrada()
        elif opcao == "2": entrada_controller.listar()
        elif opcao == "0": break

        else: print("Opção inválida.")


def menu_saidas():
    while True:
        print("\n=== SAÍDAS ===")
        print("1 - Adicionar saída")
        print("2 - Listar saídas")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1": saida_controller.adicionar_saida()
        elif opcao == "2": saida_controller.listar()
        elif opcao == "0": break

        else: print("Opção inválida.")


while True:
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Categorias")
    print("2 - Entradas")
    print("3 - Saídas")
    print("0 - Encerrar programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1": menu_categorias()
    elif opcao == "2": menu_entradas()
    elif opcao == "3": menu_saidas()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else: print("Opção inválida.")