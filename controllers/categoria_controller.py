from services.categoria_service import CategoriaService
from utils.validaInputs import ler_texto, ler_float, ler_int


class CategoriaController:
    def __init__(self):
        self.categoria_service = CategoriaService()

    def adicionar_categoria(self):

        nome = ler_texto("Nome da categoria: ").strip().lower()
        teto = ler_float("Teto de gastos: ")

        sucesso = self.categoria_service.adicionar(nome, teto)

        if sucesso:
            print("Categoria cadastrada com sucesso!")
        else:
            print("Já existe uma categoria com esse nome.")

    def listar(self):

        categorias = self.categoria_service.listar()

        if not categorias:
            print("Nenhuma categoria cadastrada.")
            return

        for categoria in categorias:
            print(
                f"{categoria.id} - "
                f"{categoria.nome} "
                f"(Teto: R$ {categoria.teto:.2f})"
            )

    def update(self):
        categorias = self.categoria_service.listar()

        if not categorias:
            print("Nenhuma categoria cadastrada.")
            return

        self.listar()

        id_categoria = ler_int("\nDigite o ID da categoria que deseja alterar: ")
        categoria = self.categoria_service.buscar_por_id(id_categoria)

        if not categoria:
            print("Categoria não encontrada.")
            return

        nome = ler_texto("Novo nome: ").strip().lower()
        teto = ler_float("Novo teto: ")

        sucesso = self.categoria_service.update(
            id_categoria,
            nome,
            teto
        )

        if sucesso:
            print("Categoria atualizada com sucesso!")
        else:
            print("Já existe uma categoria com esse nome.")

    def remover(self):
        categorias = self.categoria_service.listar()

        if not categorias:
            print("Nenhuma categoria cadastrada.")
            return

        self.listar()

        id_categoria = ler_int(
            "\nDigite o ID da categoria que deseja remover: "
        )

        categoria = self.categoria_service.buscar_por_id(
            id_categoria
        )

        if not categoria:
            print("Categoria não encontrada.")
            return

        self.categoria_service.remover(id_categoria)

        print("Categoria removida com sucesso!")
