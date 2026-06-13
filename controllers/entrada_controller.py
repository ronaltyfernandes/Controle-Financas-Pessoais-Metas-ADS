from services.entrada_service import EntradaService
from utils.validaInputs import (
    ler_texto,
    ler_float,
    ler_data,
    ler_int
)


class EntradaController:
    def __init__(self):
        self.entrada_service = EntradaService()


    def adicionar_entrada(self):
        nome = ler_texto("Nome: ")
        descricao = ler_texto("Descrição: ")
        valor = ler_float("Valor: ")
        data = ler_data("Data: ")

        self.entrada_service.adicionar(
            nome,
            valor,
            data,
            descricao
        )

        print("Entrada cadastrada com sucesso!")


    def listar(self):

        entradas = self.entrada_service.listar()

        if not entradas:
            print("Nenhuma entrada cadastrada.")
            return

        for entrada in entradas:
            print(
                entrada.id,
                entrada.nome,
                entrada.valor,
                entrada.data,
                entrada.descricao
            )


    def update(self):

        entradas = self.entrada_service.listar()

        if not entradas:
            print("Nenhuma entrada cadastrada.")
            return

        self.listar()

        id_entrada = ler_int(
            "\nDigite o ID da entrada que deseja alterar: "
        )

        entrada = self.entrada_service.buscar_por_id(
            id_entrada
        )

        if not entrada:
            print("Entrada não encontrada.")
            return

        nome = ler_texto("Novo nome: ")
        descricao = ler_texto("Nova descrição: ")
        valor = ler_float("Novo valor: ")
        data = ler_data("Nova data: ")


        sucesso = self.entrada_service.update(
            id_entrada,
            nome,
            valor,
            data,
            descricao
        )

        if sucesso:
            print("Entrada atualizada com sucesso!")
        else:
            print("Não foi possível atualizar a entrada.")


    def remover(self):
        entradas = self.entrada_service.listar()

        if not entradas:
            print("Nenhuma entrada cadastrada.")
            return

        self.listar()

        id_entrada = ler_int("\nDigite o ID da entrada que deseja remover: ")

        entrada = self.entrada_service.buscar_por_id(
            id_entrada
        )

        if not entrada:
            print("Entrada não encontrada.")
            return

        self.entrada_service.remover(id_entrada)

        print("Entrada removida com sucesso!")