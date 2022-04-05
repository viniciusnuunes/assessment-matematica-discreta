# Fila
class Local:
    def __init__(self, id, nome, ItemEntrega):
        self.locais = []
        self.id = id
        self.nome = nome
        self.ItensEntrega = [ItemEntrega]

    def vazio(self):
        return self.locais == []

    def enfileirar(self, local):
        self.locais.insert(0, local)

    def desenfileirar(self):
        return self.locais.pop()

    def associar(self, ItemEntrega):
        return self.ItensEntrega.insert(0, ItemEntrega)

    def tamanho(self):
        return len(self.locais)