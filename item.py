# Criação de um único item
class Item:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    # def __repr__(self):
    #     return f'{self.id} - {self.nome}'

    def listar(self):
        return self.id, self.nome
