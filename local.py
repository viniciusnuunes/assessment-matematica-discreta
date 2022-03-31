class Local():
    def __init__(self, id, local):
        self.id = id
        self.local = local
        self.ItensEntrega = []

    def __repr__(self):
        return f'ID {self.id} - {self.local}'

    def get(self):
        return self.id, self.local, self.ItensEntrega

    def associar(self, ItemEntrega):
        self.ItensEntrega.insert(0, ItemEntrega)

    def possuiItensEntrega(self):
        return self.ItensEntrega == []
