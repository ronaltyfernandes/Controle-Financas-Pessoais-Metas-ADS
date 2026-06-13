from services.relatorio_service import RelatorioService
from utils.validaInputs import ler_int
from utils.interface import (
    titulo,
    erro,
    sucesso,
    tabela
)


class RelatorioController:
    def __init__(self):
        self.relatorio_service = RelatorioService()

    def entradas_mes(self):
        titulo("RELATÓRIO DE ENTRADAS")

        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        entradas = self.relatorio_service.entradas_mes(
            mes,
            ano
        )

        if not entradas:
            erro("Nenhuma entrada encontrada.")
            return

        linhas = []

        for entrada in entradas:
            linhas.append([
                entrada["data"],
                entrada["nome"],
                f"R$ {entrada['valor']:.2f}"
            ])

        tabela(
            ["Data", "Nome", "Valor"],
            linhas
        )
    
    def saidas_mes(self):
        titulo("RELATÓRIO DE SAÍDAS")

        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        saidas = self.relatorio_service.saidas_mes(
            mes,
            ano
        )

        if not saidas:
            erro("Nenhuma saída encontrada.")
            return

        linhas = []

        for saida in saidas:
            linhas.append([
                saida["data"],
                saida["nome"],
                f"R$ {saida['valor']:.2f}"
            ])

        tabela(
            ["Data", "Nome", "Valor"],
            linhas
        )
    
    def saidas_mes(self):
        titulo("RELATÓRIO DE SAÍDAS")

        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        saidas = self.relatorio_service.saidas_mes(
            mes,
            ano
        )

        if not saidas:
            erro("Nenhuma saída encontrada.")
            return

        linhas = []

        for saida in saidas:
            linhas.append([
                saida["data"],
                saida["nome"],
                f"R$ {saida['valor']:.2f}"
            ])

        tabela(
            ["Data", "Nome", "Valor"],
            linhas
        )
        
    def movimentacoes_mes(self):
        titulo("MOVIMENTAÇÕES DO MÊS")

        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        movimentacoes = self.relatorio_service.movimentacoes_mes(
            mes,
            ano
        )

        if not movimentacoes:
            erro("Nenhuma movimentação encontrada.")
            return

        linhas = []

        for mov in movimentacoes:
            linhas.append([
                mov["data"],
                mov["tipo"],
                mov["nome"],
                f"R$ {mov['valor']:.2f}"
            ])

        tabela(
            ["Data", "Tipo", "Nome", "Valor"],
            linhas
        )
    
    def resumo_financeiro_mes(self):
        titulo("RESUMO FINANCEIRO MENSAL")

        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        resumo = self.relatorio_service.resumo_financeiro_mes(
            mes,
            ano
        )

        linhas = [
            ["Entradas", f"R$ {resumo['entradas']:.2f}"],
            ["Saídas", f"R$ {resumo['saidas']:.2f}"],
            ["Saldo", f"R$ {resumo['saldo']:.2f}"]
        ]

        tabela(
            ["Indicador", "Valor"],
            linhas
        )
    
    def gastos_por_categoria(self):
        titulo("GASTOS POR CATEGORIA")

        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        gastos = self.relatorio_service.gastos_por_categoria(
            mes,
            ano
        )

        if not gastos:
            erro("Nenhum dado encontrado.")
            return

        linhas = []

        for item in gastos:
            status = (
                "EXCEDIDO"
                if item["estourou"]
                else "OK"
            )

            linhas.append([
                item["categoria"],
                f"R$ {item['gasto']:.2f}",
                f"R$ {item['teto']:.2f}",
                status
            ])

        tabela(
            [
                "Categoria",
                "Gasto",
                "Teto",
                "Status"
            ],
            linhas
        )

        for item in gastos:
            if item["estourou"]:
                excesso = (
                    item["gasto"]
                    - item["teto"]
                )

                erro(
                    f'{item["categoria"]}: teto excedido em '
                    f'R$ {excesso:.2f}'
                )
    
    def resumo_financeiro_ano(self):
        titulo("RESUMO FINANCEIRO ANUAL")

        ano = ler_int("Ano: ")

        resumo = self.relatorio_service.resumo_financeiro_ano(
            ano
        )

        if resumo["saldo"] > 0:
            situacao = "SUPERÁVIT"
        elif resumo["saldo"] < 0:
            situacao = "DÉFICIT"
        else:
            situacao = "EQUILÍBRIO"

        linhas = [
            ["Entradas", f"R$ {resumo['entradas']:.2f}"],
            ["Saídas", f"R$ {resumo['saidas']:.2f}"],
            ["Saldo", f"R$ {resumo['saldo']:.2f}"],
            ["Situação", situacao]
        ]

        tabela(
            ["Indicador", "Valor"],
            linhas
        )

        if situacao == "SUPERÁVIT":
            sucesso("Situação financeira positiva.")
        elif situacao == "DÉFICIT":
            erro("Situação financeira negativa.")