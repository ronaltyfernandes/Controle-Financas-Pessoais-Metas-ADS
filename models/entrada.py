class Entrada:
    def __init__(self, id, data, nome, valor, descricao):
        self.id = id
        self.data = data
        self.nome = nome
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f'{self.id}: {self.data}; {self.nome}, R$ {self.valor:.2f}, {self.descricao}'