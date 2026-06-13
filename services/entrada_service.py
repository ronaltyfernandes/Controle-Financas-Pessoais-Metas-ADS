from models.entrada import Entrada


class EntradaService:
    ARQUIVO = "data/entradas.txt"

    def adicionar(self, nome, valor, data, descricao):
        entradas = self.listar()

        novo_id = 1

        if entradas:
            novo_id = max(e.id for e in entradas) + 1

        with open(self.ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"{novo_id};{data};{nome};{valor};{descricao}\n"
            )

        return True

    def buscar_por_id(self, id_entrada):
        for entrada in self.listar():
            if entrada.id == id_entrada:
                return entrada

        return None

    def listar(self):
        entradas = []

        try:
            with open(self.ARQUIVO, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    id, data, nome, valor, descricao = (
                        linha.strip().split(";")
                    )

                    entradas.append(
                        Entrada(
                            data,
                            int(id),
                            nome,
                            float(valor),
                            descricao
                        )
                    )

        except FileNotFoundError:
            pass

        entradas.sort(key=lambda e: e.data)

        return entradas

    def update(
        self,
        id_entrada,
        novo_nome,
        novo_valor,
        nova_data,
        nova_descricao
    ):

        entradas = self.listar()

        entrada_encontrada = False

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:

            for entrada in entradas:

                if entrada.id == id_entrada:
                    entrada.data = nova_data
                    entrada.nome = novo_nome
                    entrada.valor = novo_valor
                    entrada.descricao = nova_descricao

                    entrada_encontrada = True

                arquivo.write(
                    f"{entrada.id};"
                    f"{entrada.data};"
                    f"{entrada.nome};"
                    f"{entrada.valor};"
                    f"{entrada.descricao}\n"
                )

        return entrada_encontrada

    def remover(self, id_entrada):
        entradas = self.listar()
        entrada_encontrada = False

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:

            for entrada in entradas:
                if entrada.id != id_entrada:
                    arquivo.write(
                        f"{entrada.id};"
                        f"{entrada.nome};"
                        f"{entrada.valor};"
                        f"{entrada.data};"
                        f"{entrada.descricao}\n"
                    )

                else: entrada_encontrada = True

        return entrada_encontrada
