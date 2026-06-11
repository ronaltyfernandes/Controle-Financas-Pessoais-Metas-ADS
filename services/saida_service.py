from models.saida import Saida

class SaidaService:

    ARQUIVO = "data/saidas.txt" 

    def adicionar(self, nome, valor, categoria_id, data, descricao):
        print("print self:")

        saidas = self.listar()

        novo_id = 1

        if saidas:
            novo_id = max(c.id for c in saidas) + 1

        with open(self.ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{novo_id};{nome};{valor};{categoria_id};{data};{descricao}\n")


    def listar(self):
        saidas = []

        try:
            with open(self.ARQUIVO, "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    id, nome, valor, categoria_id, data, descricao = linha.strip().split(";")

                    saidas.append(
                        Saida(
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

        saidas.sort(key=lambda c: c.nome)

        return saidas


    def remover(self, id_saida):
        saidas = self.listar()

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:

            for saida in saidas:

                if saida.id != id_saida:

                    arquivo.write(
                        f"{saida.id};{saida.nome};{saida.valor};{saida.categoria_id};{saida.data};{saida.descricao}\n"
                    )


    def calcular_gastos(self):
        saidas = self.listar()

        resultado = {}

        for saida in saidas:
            resultado[saida.nome] = 0

        try:

            with open("data/saidas.txt", "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    id_saida, data, descricao, valor, entrada_id = linha.strip().split(";")

                    entrada_id = int(entrada_id)
                    id_saida = int(id_saida)

                    for saida in saidas:

                        if saida.id == id_saida:
                            resultado[saida.nome] += float(valor)

        except FileNotFoundError:
            pass

        return resultado
