from services.saida_service import SaidaService
from services.categoria_service import CategoriaService
from utils.validaInputs import (
    ler_texto,
    ler_float,
    ler_data,
    ler_int
)

from utils.interface import (
    titulo,
    sucesso,
    erro,
    tabela
)


class SaidaController:
    def __init__(self):
        self.saida_service = SaidaService()
        self.categoria_service = CategoriaService()

    def adicionar_saida(self):
        titulo("CADASTRO DE SAÍDA")

        categorias = self.categoria_service.listar()

        if not categorias:
            erro("Nenhuma categoria cadastrada.")
            erro("Cadastre uma categoria antes de registrar uma saída.")
            return

        nome = ler_texto("Nome: ")
        descricao = ler_texto("Descrição: ")
        valor = ler_float("Valor: ")
        data = ler_data("Data: ")

        linhas = []

        for categoria in categorias:
            linhas.append([
                categoria.id,
                categoria.nome
            ])

        tabela(
            ["ID", "Categoria"],
            linhas
        )

        while True:
            nome_categoria = ler_texto(
                "Nome da Categoria: "
            ).strip().lower()

            categoria = self.categoria_service.buscar_por_nome(
                nome_categoria
            )

            if categoria:
                break

            erro("Categoria não encontrada.")

        self.saida_service.adicionar(
            nome,
            valor,
            categoria.id,
            data,
            descricao
        )

        sucesso(
            f'Saída "{nome}" cadastrada com sucesso!'
        )

    def listar(self):
        titulo("LISTA DE SAÍDAS")

        saidas = self.saida_service.listar()

        if not saidas:
            erro("Nenhuma saída cadastrada.")
            return

        linhas = []

        for saida in saidas:
            categoria = self.categoria_service.buscar_por_id(
                saida.categoria_id
            )

            nome_categoria = (
                categoria.nome
                if categoria
                else "Não encontrada"
            )

            linhas.append([
                saida.id,
                saida.data,
                saida.nome,
                f"R$ {saida.valor:.2f}",
                nome_categoria,
                saida.descricao
            ])

        tabela(
            [
                "ID",
                "Data",
                "Nome",
                "Valor",
                "Categoria",
                "Descrição"
            ],
            linhas
        )

    def update(self):
        titulo("ALTERAR SAÍDA")

        saidas = self.saida_service.listar()

        if not saidas:
            erro("Nenhuma saída cadastrada.")
            return

        self.listar()

        id_saida = ler_int(
            "\nDigite o ID da saída que deseja alterar: "
        )

        saida = self.saida_service.buscar_por_id(
            id_saida
        )

        if not saida:
            erro("Saída não encontrada.")
            return

        nome = ler_texto("Novo nome: ")
        descricao = ler_texto("Nova descrição: ")
        valor = ler_float("Novo valor: ")
        data = ler_data("Nova data: ")

        categorias = self.categoria_service.listar()

        linhas = []

        for categoria in categorias:
            linhas.append([
                categoria.id,
                categoria.nome
            ])

        tabela(
            ["ID", "Categoria"],
            linhas
        )

        while True:
            nome_categoria = ler_texto(
                "Categoria: "
            ).strip().lower()

            categoria = self.categoria_service.buscar_por_nome(
                nome_categoria
            )

            if categoria:
                break

            erro("Categoria não encontrada.")

        atualizado = self.saida_service.update(
            id_saida,
            nome,
            valor,
            categoria.id,
            data,
            descricao
        )

        if atualizado:
            sucesso(
                f'Saída "{nome}" atualizada com sucesso!'
            )
        else:
            erro(
                "Não foi possível atualizar a saída."
            )

    def remover(self):
        titulo("REMOVER SAÍDA")

        saidas = self.saida_service.listar()

        if not saidas:
            erro("Nenhuma saída cadastrada.")
            return

        self.listar()

        id_saida = ler_int(
            "\nDigite o ID da saída que deseja remover: "
        )

        saida = self.saida_service.buscar_por_id(
            id_saida
        )

        if not saida:
            erro("Saída não encontrada.")
            return

        removido = self.saida_service.remover(
            id_saida
        )

        if removido:
            sucesso(
                f'Saída "{saida.nome}" removida com sucesso!'
            )
        else:
            erro(
                "Não foi possível remover a saída."
            )