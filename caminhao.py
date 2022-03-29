from local import Local


class Caminhao(Local):
    def __init__(self):
        self.caminhoes = []        
        self.placa = ''
        self.Local = Local

    def inserir(self, placa):
        self.caminhoes.append(placa)

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
