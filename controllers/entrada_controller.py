from services.entrada_service import EntradaService

class EntradaController:

    def __init__(self):
        self.entrada_service = EntradaService()

    def adicionar_entrada(self):
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        data = input("Data: ")
        categoria_id = int(input("ID da Categoria: "))

        self.entrada_service.adicionar(nome, valor, categoria_id, data, descricao)


    def listar(self):
        entradas = self.entrada_service.listar()

        for entrada in entradas:
            print(
                entrada.id,
                entrada.nome,
                entrada.valor,
                entrada.categoria_id,
                entrada.data,
                entrada.descricao
            )