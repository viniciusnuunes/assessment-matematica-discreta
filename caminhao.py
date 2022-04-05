class Caminhao():
    def __init__(self, placa, Locais):
        self.placa = placa
        self.locais = [Locais]
        self.itensEntrega = []

    def listar(self):
        return self.placa, self.locais