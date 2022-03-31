class ItemEntrega:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __repr__(self):
        return f'ID: {self.id} - {self.nome}'

    def get(self):
        return self.id, self.nome
