from controllers.categoria_controller import CategoriaController
from controllers.entrada_controller import EntradaController
from controllers.saida_controller import SaidaController
from controllers.relatorio_controller import RelatorioController

from utils.interface import *

categoria_controller = CategoriaController()
entrada_controller = EntradaController()
saida_controller = SaidaController()
relatorio_controller = RelatorioController()


def menu_categorias():
    while True:
        limpar_tela()

        cabecalho("GERENCIAMENTO DE CATEGORIAS")
        opcao(1, "Adicionar categoria")
        opcao(2, "Listar categorias")
        opcao(3, "Atualizar categoria")
        opcao(4, "Remover categoria")

        print()
        voltar()

        opcao_escolhida = input(Fore.GREEN +"\n➜ Escolha uma opção: ")

        if opcao_escolhida == "1": categoria_controller.adicionar_categoria()
        elif opcao_escolhida == "2": categoria_controller.listar()
        elif opcao_escolhida == "3": categoria_controller.update()
        elif opcao_escolhida == "4": categoria_controller.remover()
        elif opcao_escolhida == "0": break

        else:
            erro("Opção inválida.")

        input("\nPressione ENTER para continuar...")


def menu_entradas():
    while True:
        limpar_tela()
        
        cabecalho("GERENCIAMENTO DE ENTRADAS")
        opcao(1, "Adicionar entrada")
        opcao(2, "Listar entradas")
        opcao(3, "Atualizar entrada")
        opcao(4, "Remover entrada")
        print()
        voltar()

        opcao_escolhida = input(Fore.GREEN +"\n➜ Escolha uma opção: ")

        if opcao_escolhida == "1": entrada_controller.adicionar_entrada()
        elif opcao_escolhida == "2": entrada_controller.listar()
        elif opcao_escolhida == "3": entrada_controller.update()
        elif opcao_escolhida == "4": entrada_controller.remover()
        elif opcao_escolhida == "0": break

        else:erro("Opção inválida.")

        input("\nPressione ENTER para continuar...")

def menu_saidas():
    while True:
        limpar_tela()

        cabecalho("GERENCIAMENTO DE SAÍDAS")
        opcao(1, "Adicionar saída")
        opcao(2, "Listar saídas")
        opcao(3, "Atualizar saída")
        opcao(4, "Remover saída")

        print()
        voltar()

        opcao_escolhida = input(Fore.GREEN + "\n➜ Escolha uma opção: ")

        if opcao_escolhida == "1": saida_controller.adicionar_saida()
        elif opcao_escolhida == "2": saida_controller.listar()
        elif opcao_escolhida == "3":saida_controller.update()
        elif opcao_escolhida == "4":saida_controller.remover()
        elif opcao_escolhida == "0":break

        else:erro("Opção inválida.")

        input("\nPressione ENTER para continuar...")

def menu_relatorios():
    while True:
        limpar_tela()

        cabecalho("RELATÓRIOS FINANCEIROS")
        opcao(1, "Entradas do mês")
        opcao(2, "Saídas do mês")
        opcao(3, "Movimentações completas")
        opcao(4, "Resumo financeiro mensal")
        opcao(5, "Gastos por categoria")
        opcao(6, "Resumo financeiro anual")

        print()
        voltar()

        opcao_escolhida = input(Fore.GREEN + "\n➜ Escolha uma opção: ")

        if opcao_escolhida == "1": relatorio_controller.entradas_mes()
        elif opcao_escolhida == "2": relatorio_controller.saidas_mes()
        elif opcao_escolhida == "3": relatorio_controller.movimentacoes_mes()
        elif opcao_escolhida == "4": relatorio_controller.resumo_financeiro_mes()
        elif opcao_escolhida == "5": relatorio_controller.gastos_por_categoria()
        elif opcao_escolhida == "6": relatorio_controller.resumo_financeiro_ano()
        elif opcao_escolhida == "0": break

        else:
            erro("Opção inválida.")

        input("\nPressione ENTER para continuar...")

while True:
    limpar_tela()

    cabecalho("CONTROLE DE FINANÇAS PESSOAIS")
    opcao(1, "Categorias")
    opcao(2, "Entradas")
    opcao(3, "Saídas")
    opcao(4, "Relatórios")

    print()
    print(Fore.RED + "[0] Encerrar programa")

    print()
    opcao_escolhida = input(
        Fore.GREEN +
        "\n➜ Escolha uma opção: "
    )

    if opcao_escolhida == "1": menu_categorias()
    elif opcao_escolhida == "2": menu_entradas()
    elif opcao_escolhida == "3": menu_saidas()
    elif opcao_escolhida == "4": menu_relatorios()
    elif opcao_escolhida == "0":
        sucesso("Programa encerrado.")
        break

    else:
        erro("Opção inválida.")
        input("\nPressione ENTER...")
