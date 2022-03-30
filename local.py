class Local():
    def __init__(self, id, local):
        self.id = id
        self.local = local
        self.ItensEntrega = []

    def inserir(self, id, local):
        self.locais.insert(0, (id, local))

    def get(self):
        return self.id, self.local, self.ItensEntrega

    def associar(self, ItemEntrega):
        self.ItensEntrega.append(ItemEntrega)

    def remover(self, id):
        tamanho = self.tamanho()

        for idx, local in enumerate(self.locais):
            if id == local[0]:
                self.locais.pop(idx)
                print(f'Volume {id} removido com sucesso')

        if tamanho == self.tamanho():
            print('Local não localizado')

    def mostrarLocais(self):
        return self.locais

    def topo(self):
        return self.locais[len(self.locais) - 1]

    def tamanho(self):
        return len(self.locais)

    def vazio(self):
        return self.locais == []
