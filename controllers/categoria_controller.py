from services.categoria_service import CategoriaService

class CategoriaController:
    def __init__(self):
        self.categoria_service = CategoriaService()

    def adicionar_categoria(self):
        nome = input("Nome: ")
        teto = float(input("Teto: "))

        self.categoria_service.adicionar(nome, teto)
    
    def listar(self):
        categorias = self.categoria_service.listar()

        for categoria in categorias:
            print(
                categoria.id,
                categoria.nome,
                categoria.teto
            )

    def update_categoria(self, id_categoria):
        nome = input("Novo nome: ")
        teto = float(input("Novo teto: "))

        self.categoria_service.update(id_categoria, nome, teto)
    
    def remover(self, id_categoria):
        self.categoria_service.remover(id_categoria)