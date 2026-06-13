class Entrada:
    def __init__(self, id, nome, valor, data, descricao):
        self.id = id
        self.data = data
        self.nome = nome
        self.valor = valor
        self.descricao = descricao


    def __str__(self):
        return f'{self.id}: {self.data} - {self.nome}, {self.valor}, {self.descricao}'