from services.categoria_service import CategoriaService
from utils.validaInputs import ler_texto, ler_float, ler_int
from utils.interface import tabela, erro, sucesso, titulo


class CategoriaController:
    def __init__(self):
        self.categoria_service = CategoriaService()

    def adicionar_categoria(self):
        titulo("CADASTRO DE CATEGORIA")

        nome = ler_texto(
            "Nome da categoria: "
        ).strip().lower()

        teto = ler_float("Teto de gastos: "
        )

        if self.categoria_service.adicionar(nome, teto):
            sucesso(
                f'Categoria "{nome}" cadastrada com sucesso!'
            )
        else:
            erro(
                f'A categoria "{nome}" já existe.'
        )

    def listar(self):
        titulo("LISTA DE CATEGORIAS")

        categorias = self.categoria_service.listar()

        if not categorias:
            erro("Nenhuma categoria cadastrada.")
            return

        linhas = []

        for categoria in categorias:
            linhas.append([
                categoria.id,
                categoria.nome,
                f"R$ {categoria.teto:.2f}"
            ])

        tabela(
            ["ID", "Categoria", "Teto"],
            linhas
        )

    def update(self):
        titulo("ALTERAR CATEGORIA")

        categorias = self.categoria_service.listar()

        if not categorias:
            erro("Nenhuma categoria cadastrada.")
            return

        self.listar()

        id_categoria = ler_int(
            "\nDigite o ID da categoria que deseja alterar: "
        )

        categoria = self.categoria_service.buscar_por_id(
            id_categoria
        )

        if not categoria:
            erro("Categoria não encontrada.")
            return

        nome = ler_texto(
            "Novo nome: "
        ).strip().lower()

        teto = ler_float(
            "Novo teto: "
        )

        atualizado = self.categoria_service.update(
            id_categoria,
            nome,
            teto
        )

        if atualizado:
            sucesso(
                f'Categoria "{nome}" atualizada com sucesso!'
            )
        else:
            erro(
                f'A categoria "{nome}" já existe.'
            )

    def remover(self):
        titulo("REMOVER CATEGORIA")

        categorias = self.categoria_service.listar()

        if not categorias:
            erro("Nenhuma categoria cadastrada.")
            return

        self.listar()

        id_categoria = ler_int(
            "\nDigite o ID da categoria que deseja remover: "
        )

        categoria = self.categoria_service.buscar_por_id(
            id_categoria
        )

        if not categoria:
            erro("Categoria não encontrada.")
            return

        self.categoria_service.remover(
            id_categoria
        )

        sucesso(
            f'Categoria "{categoria.nome}" removida com sucesso!'
        )