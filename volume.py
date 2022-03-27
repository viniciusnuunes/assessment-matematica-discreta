class Volume:
    def __init__(self):
        self.volumes = ['banana', 'laranja', 'maca']

    def inserir(self, item):
        self.volumes.insert(0, item)

    def remover(self, nomeDoItem):
        
        try:
            self.volumes.remove(nomeDoItem)
            print(f'Volume {nomeDoItem} removido com sucesso')
        except:
            raise Exception('Item não localizado')

    def mostrarVolumes(self):
        return self.volumes

    def topo(self):
        return self.volumes[len(self.volumes) - 1]

    def tamanho(self):
        return len(self.volumes)

    def vazio(self):
        return self.volumes == []
