class Caminhao():
    def __init__(self, placa):
        self.placa = placa
        self.Locais = []
        self.ItensEntrega = []

    def inserir(self, placa):
        self.caminhoes.append(placa)

    def get(self):
        return self.placa, self.Locais, self.ItensEntrega

    def associarLocal(self, Local):
        self.Locais.insert(0, Local)

    def associarItemEntrega(self, ItemEntrega):
        self.ItensEntrega.insert(0, ItemEntrega)

    def remover(self, placa):
        tamanho = self.tamanho()

        for idx, local in enumerate(self.caminhoes):
            if placa == local[0]:
                self.caminhoes.pop(idx)
                print(f'Volume {placa} removido com sucesso')

        if tamanho == self.tamanho():
            print('Local não localizado')

    def mostrarCaminhoes(self):
        return self.caminhoes

    def topo(self):
        return self.caminhoes[len(self.caminhoes) - 1]

    def tamanho(self):
        return len(self.caminhoes)

    def vazio(self):
        return self.caminhoes == []
