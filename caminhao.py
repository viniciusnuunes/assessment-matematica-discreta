# Lista
class Caminhao():
    def __init__(self, placa, Local, ItemEntrega):
        self.caminhoes = []
        self.placa = placa
        self.Locais = [Local]
        self.ItensEntrega = [ItemEntrega]

    def vazio(self):
        return self.caminhoes == []

    def inserir(self, caminhao):
        return self.caminhoes.append(caminhao)
    
    def remover(self):
        return self.caminhoes.pop()

    def associarLocal(self, Local):
        self.Locais.insert(0, Local)

    def associarItemEntrega(self, ItemEntrega):
        self.ItensEntrega.insert(0, ItemEntrega)
