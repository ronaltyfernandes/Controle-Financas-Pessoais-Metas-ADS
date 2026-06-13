from services.saida_service import SaidaService
from services.categoria_service import CategoriaService
from utils.validaInputs import (
    ler_texto,
    ler_float,
    ler_data,
    ler_int
)


class SaidaController:

    def __init__(self):
        self.saida_service = SaidaService()
        self.categoria_service = CategoriaService()

    def adicionar_saida(self):

        categorias = self.categoria_service.listar()

        if not categorias:
            print("Nenhuma categoria cadastrada.")
            print("Cadastre uma categoria antes de registrar uma saída.")
            return

        nome = ler_texto("Nome: ")
        descricao = ler_texto("Descrição: ")
        valor = ler_float("Valor: ")
        data = ler_data("Data: ")

        print("\nCategorias disponíveis:")

        for categoria in categorias:
            print(f"- {categoria.nome}")

        while True:

            nome_categoria = ler_texto("Categoria: ")

            categoria = self.categoria_service.buscar_por_nome(
                nome_categoria
            )

            if categoria:
                break

            print("Categoria não encontrada.")

        self.saida_service.adicionar(
            nome,
            valor,
            categoria.id,
            data,
            descricao
        )

        print("Saída cadastrada com sucesso!")

    def listar(self):

        saidas = self.saida_service.listar()

        if not saidas:
            print("Nenhuma saída cadastrada.")
            return

        for saida in saidas:
            print(
                saida.id,
                saida.nome,
                saida.valor,
                saida.categoria_id,
                saida.data,
                saida.descricao
            )

    def update(self):

        saidas = self.saida_service.listar()

        if not saidas:
            print("Nenhuma saída cadastrada.")
            return

        self.listar()

        id_saida = ler_int(
            "\nDigite o ID da saída que deseja alterar: "
        )

        saida = self.saida_service.buscar_por_id(
            id_saida
        )

        if not saida:
            print("Saída não encontrada.")
            return

        nome = ler_texto("Novo nome: ")
        descricao = ler_texto("Nova descrição: ")
        valor = ler_float("Novo valor: ")
        data = ler_data("Nova data: ")

        categorias = self.categoria_service.listar()

        print("\nCategorias disponíveis:")

        for categoria in categorias:
            print(f"- {categoria.nome}")

        while True:

            nome_categoria = ler_texto("Categoria: ")

            categoria = self.categoria_service.buscar_por_nome(
                nome_categoria
            )

            if categoria:
                break

            print("Categoria não encontrada.")

        sucesso = self.saida_service.update(
            id_saida,
            nome,
            valor,
            categoria.id,
            data,
            descricao
        )

        if sucesso:
            print("Saída atualizada com sucesso!")
        else:
            print("Não foi possível atualizar a saída.")

    def remover(self):

        saidas = self.saida_service.listar()

        if not saidas:
            print("Nenhuma saída cadastrada.")
            return

        self.listar()

        id_saida = ler_int(
            "\nDigite o ID da saída que deseja remover: "
        )

        sucesso = self.saida_service.remover(id_saida)

        if sucesso:
            print("Saída removida com sucesso!")
        else:
            print("Saída não encontrada.")