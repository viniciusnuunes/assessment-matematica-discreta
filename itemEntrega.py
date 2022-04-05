# Pilha
class ItemEntrega:
    def __init__(self):
        self.itensEntrega = []

    def vazio(self):
        return self.itensEntrega == []

    def empilhar(self, item):
        self.itensEntrega.append(item)

    def desempilhar(self):
        return self.itensEntrega.pop()

    def topo(self):
        return self.itensEntrega[len(self.itensEntrega)-1]

    def tamanho(self):
        return len(self.itensEntrega)
