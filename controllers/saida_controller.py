from services.saida_service import SaidaService

class SaidaController:

    def __init__(self):
        self.saida_service = SaidaService()

    def adicionar_saida(self):
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        data = input("Data: ")
        categoria_id = int(input("ID da Categoria: "))

        self.saida_service.adicionar(nome, valor, categoria_id, data, descricao)


    def listar(self):
        saidas = self.saida_service.listar()

        for saida in saidas:
            print(
                saida.id,
                saida.nome,
                saida.valor,
                saida.categoria_id,
                saida.data,
                saida.descricao
            )