class Caminhao():
    def __init__(self, placa, Locais):
        self.placa = placa
        self.locais = [Locais]
        self.itensEntrega = []

    def empilharItens(self, item):        
        self.itensEntrega.append(item)

    def listar(self):
        return self.placa, self.locais, self.itensEntrega
