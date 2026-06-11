from models.entrada import Entrada

class EntradaService:

    ARQUIVO = "data/entradas.txt" 

    def adicionar(self, nome, valor, categoria_id, data, descricao):
        print("print self:")

        entradas = self.listar()

        novo_id = 1

        if entradas:
            novo_id = max(c.id for c in entradas) + 1

        with open(self.ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{novo_id};{nome};{valor};{categoria_id};{data};{descricao}\n")


    def listar(self):

        entradas = []

        try:
            with open(self.ARQUIVO, "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    id, nome, valor, categoria_id, data, descricao = linha.strip().split(";")

                    entradas.append(
                        Entrada(
                            int(id),
                            nome,
                            float(valor),
                            int(categoria_id),
                            data,
                            descricao
                        )
                    )

        except FileNotFoundError:
            pass

        entradas.sort(key=lambda c: c.nome)

        return entradas


    def remover(self, id_entrada):

        entradas = self.listar()

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:

            for entrada in entradas:

                if entrada.id != id_entrada:

                    arquivo.write(
                        f"{entrada.id};{entrada.nome};{entrada.valor};{entrada.categoria_id};{entrada.data};{entrada.descricao}\n"
                    )


    def calcular_gastos(self):

        entradas = self.listar()

        resultado = {}

        for entrada in entradas:
            resultado[entrada.nome] = 0

        try:

            with open("data/saidas.txt", "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    id_saida, data, descricao, valor, entrada_id = linha.strip().split(";")

                    entrada_id = int(entrada_id)
                    id_saida = int(id_saida)

                    for entrada in entradas:

                        if entrada.id == entrada_id:
                            resultado[entrada.nome] += float(valor)

        except FileNotFoundError:
            pass

        return resultado