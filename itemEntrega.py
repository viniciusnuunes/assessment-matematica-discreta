class ItemEntrega:
    def __init__(self):
        self.Itens = []
        self.idVolume = ''
        self.nomeVolume = ''

    def inserir(self, id, item):
        self.Itens.insert(0, (id, item))

    def remover(self, id):
        tamanho = self.tamanho()

        for idx, item in enumerate(self.Itens):
            if id == item[0]:
                self.Itens.pop(idx)
                print(f'Volume {id} removido com sucesso')

        if tamanho == self.tamanho():
            print('Item não localizado')

    def mostrarItens(self):
        return self.Itens

    def topo(self):
        return self.Itens[len(self.Itens) - 1]

    def tamanho(self):
        return len(self.Itens)

    def vazio(self):
        return self.Itens == []
