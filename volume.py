class Volume:
    def __init__(self):
        self.volumes = []

    def inserir(self, item):
        self.volumes.append(item)

    def remover(self, nomeDoItem):
        for item in self.volumes:
            if nomeDoItem == item:
                self.volumes.remove(item)
                print(f'Volume {item} removido com sucesso')
                continue

            raise Exception('Item não localizado')

    def mostrarVolumes(self):
        return self.volumes

    def topo(self):
        return self.volumes[len(self.volumes) - 1]

    def tamanho(self):
        return len(self.volumes)

    def vazio(self):
        return self.volumes == []
