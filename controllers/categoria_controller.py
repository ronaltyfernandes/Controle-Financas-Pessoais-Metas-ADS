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

    # def calcular_gastos(self):

    #     gastos = self.categoria_service.calcular_gastos()

    #     if not gastos:
    #         print("Nenhum gasto encontrado.")
    #         return

    #     print("\n=== GASTOS POR CATEGORIA ===")

    #     for nome, valor in gastos.items():
    #         print(f"{nome}: R$ {valor:.2f}")

    #     categorias = self.categoria_service.listar()
        # gastos = self.categoria_service.calcular_gastos()

        # print("\n=== VERIFICAÇÃO DE TETOS ===")

        # for categoria in categorias:

        #     gasto = gastos.get(categoria.nome, 0)

        #     print(
        #         f"{categoria.nome}: "
        #         f"R$ {gasto:.2f} / "
        #         f"R$ {categoria.teto:.2f}"
        #     )

        #     if gasto > categoria.teto:
        #         print(
        #             f"⚠ ALERTA: teto excedido em "
        #             f"R$ {(gasto - categoria.teto):.2f}"
        #         )