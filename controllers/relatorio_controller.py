from services.relatorio_service import RelatorioService
from utils.validaInputs import ler_int


class RelatorioController:
    def __init__(self):
        self.relatorio_service = RelatorioService()

    def entradas_mes(self):
        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")
        entradas = self.relatorio_service.entradas_mes(mes, ano)

        if not entradas:
            print("\nNenhuma entrada encontrada.")
            return

        print(f"\n=== ENTRADAS {mes:02d}/{ano} ===")

        for entrada in entradas:
            print(
                f"{entrada['data']} | "
                f"{entrada['nome']} | "
                f"R$ {entrada['valor']:.2f}"
            )

    def saidas_mes(self):
        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        saidas = self.relatorio_service.saidas_mes(mes, ano)

        if not saidas:
            print("\nNenhuma saída encontrada.")
            return

        print(
            f"\n=== SAÍDAS {mes:02d}/{ano} ==="
        )

        for saida in saidas:
            print(f"{saida['data']} | {saida['nome']} | R$ {saida['valor']:.2f}")

    def movimentacoes_mes(self):
        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        movimentacoes = (self.relatorio_service.movimentacoes_mes(mes, ano))

        if not movimentacoes:
            print("\nNenhuma movimentação encontrada.")
            return

        print(f"\n=== MOVIMENTAÇÕES {mes:02d}/{ano} ===")

        for mov in movimentacoes:
            print(
                f"{mov['data']} | "
                f"{mov['tipo']} | "
                f"{mov['nome']} | "
                f"R$ {mov['valor']:.2f}"
            )

    def resumo_financeiro_mes(self):
        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")

        resumo = (self.relatorio_service.resumo_financeiro_mes(mes, ano))

        print(f"\n=== RESUMO FINANCEIRO {mes:02d}/{ano} ===")
        print(f"Total de Entradas: R$ {resumo['entradas']:.2f}")
        print(f"Total de Saídas: R$ {resumo['saidas']:.2f}")
        print(f"Saldo Final: R$ {resumo['saldo']:.2f}")

    def gastos_por_categoria(self):
        mes = ler_int("Mês: ")
        ano = ler_int("Ano: ")
        gastos = (self.relatorio_service.gastos_por_categoria(mes, ano))

        if not gastos:
            print("\nNenhum dado encontrado.")
            return

        print(f"\n=== GASTOS POR CATEGORIA {mes:02d}/{ano} ===")

        for item in gastos:
            print(f"\nCategoria: {item['categoria']}")
            print(f"Gasto: R$ {item['gasto']:.2f}")
            print(f"Teto: R$ {item['teto']:.2f}")

            if item["estourou"]:
                excesso = (
                    item["gasto"]
                    - item["teto"]
                )
                print(f"⚠ ALERTA: teto excedido em R$ {excesso:.2f}")

    def resumo_financeiro_ano(self):
        ano = ler_int("Ano: ")
        resumo = (self.relatorio_service.resumo_financeiro_ano(ano))

        print(f"\n=== RESUMO FINANCEIRO {ano} ===")
        print(f"Total de Entradas: R$ {resumo['entradas']:.2f}")
        print(f"Total de Saídas: R$ {resumo['saidas']:.2f}")
        print(f"Saldo Final: R$ {resumo['saldo']:.2f}")

        if resumo["saldo"] > 0: print("Situação: Superávit")
        elif resumo["saldo"] < 0: print("Situação: Déficit")
        else: print("Situação: Equilíbrio")