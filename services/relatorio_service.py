from services.saida_service import SaidaService
from services.categoria_service import CategoriaService
from services.entrada_service import EntradaService
from datetime import datetime


class RelatorioService:
    def __init__(self):
        self.saida_service = SaidaService()
        self.categoria_service = CategoriaService()
        self.entrada_service = EntradaService()

    def movimentacoes_mes(self, mes, ano):
        movimentacoes = []
        entradas = self.entrada_service.listar()

        for entrada in entradas:
            data = datetime.strptime(
                entrada.data,
                "%d/%m/%Y"
            )

            if data.month == mes and data.year == ano:
                movimentacoes.append({
                    "tipo": "Entrada",
                    "data": entrada.data,
                    "nome": entrada.nome,
                    "valor": entrada.valor,
                    "descricao": entrada.descricao
                })

        saidas = self.saida_service.listar()

        for saida in saidas:
            data = datetime.strptime(
                saida.data,
                "%d/%m/%Y"
            )
            if data.month == mes and data.year == ano:
                movimentacoes.append({
                    "tipo": "Saída",
                    "data": saida.data,
                    "nome": saida.nome,
                    "valor": saida.valor,
                    "descricao": saida.descricao
                })

        movimentacoes.sort(
            key=lambda mov: datetime.strptime(
                mov["data"],
                "%d/%m/%Y"
            )
        )

        return movimentacoes

    def gastos_por_categoria(self, mes, ano):

        categorias = self.categoria_service.listar()
        saidas = self.saida_service.listar()

        resultado = []

        for categoria in categorias:
            total = 0

            for saida in saidas:
                data = datetime.strptime(
                    saida.data,
                    "%d/%m/%Y"
                )

                if (
                    saida.categoria_id == categoria.id
                    and data.month == mes
                    and data.year == ano
                ):
                    total += saida.valor

            resultado.append({
                "categoria": categoria.nome,
                "teto": categoria.teto,
                "gasto": total,
                "estourou": total > categoria.teto
            })

        resultado.sort(
            key=lambda item: item["categoria"]
        )

        return resultado

    def entradas_mes(self, mes, ano):
        entradas = self.entrada_service.listar()
        resultado = []

        for entrada in entradas:
            data = datetime.strptime(
                entrada.data,
                "%d/%m/%Y"
            )

            if data.month == mes and data.year == ano:
                resultado.append({
                    "data": entrada.data,
                    "nome": entrada.nome,
                    "valor": entrada.valor,
                    "descricao": entrada.descricao
                })

        resultado.sort(
            key=lambda item:
            datetime.strptime(
                item["data"],
                "%d/%m/%Y"
            )
        )

        return resultado

    def saidas_mes(self, mes, ano):
        saidas = self.saida_service.listar()
        resultado = []

        for saida in saidas:
            data = datetime.strptime(
                saida.data,
                "%d/%m/%Y"
            )

            if data.month == mes and data.year == ano:
                resultado.append({
                    "data": saida.data,
                    "nome": saida.nome,
                    "valor": saida.valor,
                    "descricao": saida.descricao
                })

        resultado.sort(
            key=lambda item:
            datetime.strptime(
                item["data"],
                "%d/%m/%Y"
            )
        )

        return resultado

    def resumo_financeiro_mes(self, mes, ano):
        total_entradas = 0
        total_saidas = 0

        for entrada in self.entrada_service.listar():
            data = datetime.strptime(
                entrada.data,
                "%d/%m/%Y"
            )

            if data.month == mes and data.year == ano:
                total_entradas += entrada.valor

        for saida in self.saida_service.listar():
            data = datetime.strptime(
                saida.data,
                "%d/%m/%Y"
            )

            if data.month == mes and data.year == ano:
                total_saidas += saida.valor

        return {
            "entradas": total_entradas,
            "saidas": total_saidas,
            "saldo": total_entradas - total_saidas
        }

    def resumo_financeiro_ano(self, ano):
        total_entradas = 0
        total_saidas = 0

        entradas = self.entrada_service.listar()

        for entrada in entradas:
            data = datetime.strptime(
                entrada.data,
                "%d/%m/%Y"
            )

            if data.year == ano:
                total_entradas += entrada.valor

        saidas = self.saida_service.listar()

        for saida in saidas:
            data = datetime.strptime(
                saida.data,
                "%d/%m/%Y"
            )

            if data.year == ano:
                total_saidas += saida.valor

        return {
            "ano": ano,
            "entradas": total_entradas,
            "saidas": total_saidas,
            "saldo": total_entradas - total_saidas
        }
