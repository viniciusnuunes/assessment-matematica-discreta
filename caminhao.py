class Caminhao():
    def __init__(self, placa):
        self.placa = placa
        self.Locais = []
        self.ItensEntrega = []

    def __repr__(self):
        return f'Placa: {self.placa}'

    def get(self):
        return self.placa, self.Locais, self.ItensEntrega

    def associarLocal(self, Local):
        self.Locais.insert(0, Local)

    def associarItemEntrega(self, ItemEntrega):
        self.ItensEntrega.insert(0, ItemEntrega)

    def possuiLocais(self):
        return self.Locais != []

    def possuiItens(self):
        return self.ItensEntrega != []

    def quantidadeItensEntrega(self):
        return len(self.ItensEntrega)
