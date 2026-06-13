from colorama import Fore, Style, init
import os
from shutil import get_terminal_size


init(autoreset=True)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def titulo(texto):
    print(f"\n{Fore.CYAN}{'=' * 40}")
    print(texto.center(40))
    print(f"{'=' * 40}{Style.RESET_ALL}")


def cabecalho(titulo):
    largura = get_terminal_size().columns - 2

    print(
        Fore.CYAN +
        f"\n╔{'═'* largura}╗"
    )

    print(
        Fore.CYAN +
        f"║{titulo.center(largura)}║"
    )

    print(
        Fore.CYAN +
        f"╚{'═' * largura}╝" +
        Style.RESET_ALL
    )


def opcao(numero, texto):
    print(Fore.YELLOW + f"[{numero}] " + Fore.WHITE + texto)


def voltar():
    print(Fore.RED +"[0] Voltar")


def erro(msg):
    print(Fore.RED +f"\n✖ {msg}")


def sucesso(msg):
    print(
        Fore.GREEN +
        f"\n✔ {msg}"
    )
    

def info(msg):
    print(Fore.CYAN +f"\nℹ {msg}")

def aviso(msg):
    print(Fore.YELLOW +f"\n⚠ {msg}")

def entrada(msg):
    return input(Fore.YELLOW +f"➜ {msg}" +Fore.WHITE)

def separador():
    print(Fore.CYAN +"─" * 60)

from colorama import Fore, Style


def tabela(cabecalhos, linhas):
    if not linhas:
        erro("Nenhum registro encontrado.")
        return

    larguras = []

    for i, cabecalho in enumerate(cabecalhos):
        largura = len(str(cabecalho))

        for linha in linhas:
            largura = max(
                largura,
                len(str(linha[i]))
            )

        larguras.append(largura)

    topo = (
        "┌" +
        "┬".join(
            "─" * (largura + 2)
            for largura in larguras
        ) +
        "┐"
    )

    meio = (
        "├" +
        "┼".join(
            "─" * (largura + 2)
            for largura in larguras
        ) +
        "┤"
    )

    rodape = (
        "└" +
        "┴".join(
            "─" * (largura + 2)
            for largura in larguras
        ) +
        "┘"
    )

    print()
    print(Fore.CYAN + topo)

    # Cabeçalho
    print(
        Fore.CYAN +
        "│" +
        "│".join(
            f" {str(cabecalho):^{larguras[i]}} "
            for i, cabecalho in enumerate(cabecalhos)
        ) +
        "│"
    )

    print(Fore.CYAN + meio)

    # Dados
    for indice, linha in enumerate(linhas):
        cor = (
            Fore.WHITE
            if indice % 2 == 0
            else Fore.LIGHTBLACK_EX
        )

        valores = []

        for i, valor in enumerate(linha):
            texto = str(valor)

            # Valores monetários alinhados à direita
            if texto.startswith("R$"):
                valores.append(
                    f" {texto:>{larguras[i]}} "
                )

            # IDs alinhados ao centro
            elif i == 0:
                valores.append(
                    f" {texto:^{larguras[i]}} "
                )

            # Texto alinhado à esquerda
            else:
                valores.append(
                    f" {texto:<{larguras[i]}} "
                )

        print(
            cor +
            "│" +
            "│".join(valores) +
            "│"
        )

    print(Fore.CYAN + rodape)

    print(
        Fore.YELLOW +
        f"\nTotal de registros: {len(linhas)}"
    )

    print(Style.RESET_ALL)