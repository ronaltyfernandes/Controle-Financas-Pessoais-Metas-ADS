from models.categoria import Categoria

class CategoriaService:

    ARQUIVO = "data/categorias.txt" 

    def adicionar(self, nome, teto):
        categorias = self.listar()
        novo_id = 1

        if categorias: novo_id = max(c.id for c in categorias) + 1

        with open(self.ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{novo_id};{nome};{teto}\n")


    def listar(self):
        categorias = []
        try:
            with open(self.ARQUIVO, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    id, nome, teto = linha.strip().split(";")

                    categorias.append(
                        Categoria(
                            int(id),
                            nome,
                            float(teto)
                        )
                    )

        except FileNotFoundError: pass

        categorias.sort(key=lambda c: c.nome)

        return categorias


    def remover(self, id_categoria):
        categorias = self.listar()

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:
            for categoria in categorias:
                if categoria.id != id_categoria:
                    arquivo.write(
                        f"{categoria.id};{categoria.nome};{categoria.teto}\n"
                    )


    def calcular_gastos(self):
        categorias = self.listar()
        resultado = {}

        for categoria in categorias: resultado[categoria.nome] = 0

        try:
            with open("data/saidas.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    id_saida, data, descricao, valor, categoria_id = linha.strip().split(";")
                    categoria_id = int(categoria_id)

                    for categoria in categorias:
                        if categoria.id == categoria_id: resultado[categoria.nome] += float(valor)

        except FileNotFoundError: pass

        return resultado