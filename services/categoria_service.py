from models.categoria import Categoria

class CategoriaService:
    ARQUIVO = "data/categorias.txt" 

    def adicionar(self, nome, teto):
        categoria_existente = self.buscar_por_nome(nome)

        if categoria_existente: return False

        categorias = self.listar()
        novo_id = 1
        if categorias: novo_id = max(c.id for c in categorias) + 1

        with open(self.ARQUIVO, "a", encoding="utf-8") as arquivo: arquivo.write(f"{novo_id};{nome};{teto}\n")

        return True


    def buscar_por_id(self, id_categoria):
        for categoria in self.listar():

            if categoria.id == id_categoria:
                return categoria

        return None


    def buscar_por_nome(self, nome):

        for categoria in self.listar():
            if categoria.nome.lower() == nome.lower(): return categoria

        return None


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


    def update(self, id_categoria, novo_nome, novo_teto):

        categorias = self.listar()

        categoria_encontrada = False

        for categoria in categorias:

            if (
                categoria.nome.lower() == novo_nome.lower()
                and categoria.id != id_categoria
            ):
                return False

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:

            for categoria in categorias:

                if categoria.id == id_categoria:

                    categoria.nome = novo_nome
                    categoria.teto = novo_teto
                    categoria_encontrada = True

                arquivo.write(
                    f"{categoria.id};{categoria.nome};{categoria.teto}\n"
                )

        return categoria_encontrada


    def remover(self, id_categoria):
        categorias = self.listar()

        categoria_encontrada = False

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:

            for categoria in categorias:

                if categoria.id != id_categoria:
                    arquivo.write(
                        f"{categoria.id};{categoria.nome};{categoria.teto}\n"
                    )
                else:
                    categoria_encontrada = True

        return categoria_encontrada

