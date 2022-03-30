class ItemEntrega:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __repr__(self):
        return f'ID: {self.id} - {self.nome}'

    def inserir(self):
        return self.id, self.nome

    def get(self):
        return self.id, self.nome

    def remover(self, id):
        tamanho = self.tamanho()

        for idx, item in enumerate(self.itens):
            if id == item[0]:
                self.itens.pop(idx)
                print(f'Volume {id} removido com sucesso')

        if tamanho == self.tamanho():
            print('Item não localizado')

    def mostrarItens(self):
        return self.itens

    def topo(self):
        return self.itens[len(self.itens) - 1]

    def tamanho(self):
        return len(self.itens)

    def vazio(self):
        return self.itens == []
