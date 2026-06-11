class Entrada:
    def __init__(self, id, nome, valor, categoria_id, data, descricao):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.data = data
        self.descricao = descricao
        self.categoria_id = categoria_id


    def __str__(self):
        return f'{self.id}: {self.nome}, {self.valor}, {self.data}, {self.descricao}, {self.categoria_id}'