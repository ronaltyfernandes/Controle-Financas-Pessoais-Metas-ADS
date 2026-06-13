from services.entrada_service import EntradaService
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


class EntradaController:
    def __init__(self):
        self.entrada_service = EntradaService()

    def adicionar_entrada(self):
        titulo("CADASTRO DE ENTRADA")

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

        sucesso(
            f'Entrada "{nome}" cadastrada com sucesso!'
        )

    def listar(self):
        titulo("LISTA DE ENTRADAS")

        entradas = self.entrada_service.listar()

        if not entradas:
            erro("Nenhuma entrada cadastrada.")
            return

        linhas = []

        for entrada in entradas:
            linhas.append([
                entrada.id,
                entrada.data,
                entrada.nome,
                f"R$ {entrada.valor:.2f}",
                entrada.descricao
            ])

        tabela(
            ["ID", "Data", "Nome", "Valor", "Descrição"],
            linhas
        )

    def update(self):
        titulo("ALTERAR ENTRADA")

        entradas = self.entrada_service.listar()

        if not entradas:
            erro("Nenhuma entrada cadastrada.")
            return

        self.listar()

        id_entrada = ler_int(
            "\nDigite o ID da entrada que deseja alterar: "
        )

        entrada = self.entrada_service.buscar_por_id(
            id_entrada
        )

        if not entrada:
            erro("Entrada não encontrada.")
            return

        nome = ler_texto("Novo nome: ")
        descricao = ler_texto("Nova descrição: ")
        valor = ler_float("Novo valor: ")
        data = ler_data("Nova data: ")

        atualizado = self.entrada_service.update(
            id_entrada,
            nome,
            valor,
            data, 
            descricao
        )

        if atualizado:
            sucesso(
                f'Entrada "{nome}" atualizada com sucesso!'
            )
        else:
            erro(
                "Não foi possível atualizar a entrada."
            )

    def remover(self):
        titulo("REMOVER ENTRADA")

        entradas = self.entrada_service.listar()

        if not entradas:
            erro("Nenhuma entrada cadastrada.")
            return

        self.listar()

        id_entrada = ler_int(
            "\nDigite o ID da entrada que deseja remover: "
        )

        entrada = self.entrada_service.buscar_por_id(
            id_entrada
        )

        if not entrada:
            erro("Entrada não encontrada.")
            return

        self.entrada_service.remover(
            id_entrada
        )

        sucesso(
            f'Entrada "{entrada.nome}" removida com sucesso!'
        )