class Saida:
    def __init__(self, id, data, nome, valor, categoria_id, descricao):
        self.id = id
        self.data = data
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.categoria_id = categoria_id

    def __str__(self):
        return f'{self.id}: {self.data}, {self.nome}, R$ {self.valor}, {self.categoria_id}, {self.descricao}'