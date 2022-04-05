# Fila
class Locais:
    def __init__(self):
        self.locais = []

    # def __repr__(self):
    #     return f'{self.locais}'

    def vazio(self):
        return self.locais == []

    def enfileirar(self, local):
        self.locais.insert(0, local)

    def desenfileirar(self):
        return self.locais.pop()

    def tamanho(self):
        return len(self.locais)

    def listar(self):
        return self.locais
