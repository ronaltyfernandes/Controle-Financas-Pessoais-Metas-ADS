from models.saida import Saida


class SaidaService:
    ARQUIVO = "data/saidas.txt"

    def adicionar(self, nome, valor, categoria_id, data, descricao):
        saidas = self.listar()
        novo_id = 1

        if saidas:
            novo_id = max(s.id for s in saidas) + 1

        with open(self.ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"{novo_id};{data};{nome};{valor};{categoria_id};{descricao}\n"
            )

        return True

    def buscar_por_id(self, id_saida):
        for saida in self.listar():
            if saida.id == id_saida:
                return saida

        return None

    def listar(self):
        saidas = []

        try:
            with open(self.ARQUIVO, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    id, data, nome, valor, categoria_id, descricao = (
                        linha.strip().split(";")
                    )

                    saidas.append(
                        Saida(
                            int(id),
                            data,
                            nome,
                            float(valor),
                            int(categoria_id),
                            descricao
                        )
                    )

        except FileNotFoundError:
            pass

        saidas.sort(key=lambda s: s.data)

        return saidas

    def update(
        self,
        id_saida,
        novo_nome,
        novo_valor,
        nova_categoria_id,
        nova_data,
        nova_descricao
    ):

        saidas = self.listar()
        saida_encontrada = False

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:
            for saida in saidas:
                if saida.id == id_saida:
                    saida.data = nova_data
                    saida.nome = novo_nome
                    saida.valor = novo_valor
                    saida.categoria_id = nova_categoria_id
                    saida.descricao = nova_descricao

                    saida_encontrada = True

                arquivo.write(
                    f"{saida.id};"
                    f"{saida.data};"
                    f"{saida.nome};"
                    f"{saida.valor};"
                    f"{saida.categoria_id};"
                    f"{saida.descricao}\n"
                )

        return saida_encontrada

    def remover(self, id_saida):
        saidas = self.listar()
        saida_encontrada = False

        with open(self.ARQUIVO, "w", encoding="utf-8") as arquivo:
            for saida in saidas:
                if saida.id != id_saida:
                    arquivo.write(
                        f"{saida.id};"
                        f"{saida.data};"
                        f"{saida.nome};"
                        f"{saida.valor};"
                        f"{saida.categoria_id};"
                        f"{saida.descricao}\n"
                    )
                else:
                    saida_encontrada = True

        return saida_encontrada
