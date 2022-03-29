from itemEntrega import ItemEntrega


class Local(ItemEntrega):
    def __init__(self):
        # ('10', 'ministro gabriel de pizza 777'), ('11', 'elvira da fonseca 109'), ('18', 'adhemar bebiano 525')
        self.locais = []
        self.id = ''
        self.local = ''
        self.ItemEntrega = ItemEntrega

    def inserir(self, id, local):
        self.locais.insert(0, (id, local))

    def associar(self, idLocal, ItemEntrega):
        for idx, local in enumerate(self.locais):
            if idLocal == local[0]:
                print(local)

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
