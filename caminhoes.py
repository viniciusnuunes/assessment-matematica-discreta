# Lista
class Caminhoes():
    def __init__(self):
        self.caminhoes = []

    def vazio(self):
        return self.caminhoes == []

    def inserir(self, caminhao):
        return self.caminhoes.append(caminhao)

    def remover(self):
        return self.caminhoes.pop()

    def listar(self):
        return self.caminhoes

    def listarItensEntrega(self):
        return self.itensEntrega
    
    def listarLocais(self):
        return self.locais

    def empilharItens(self):
        for listaLocais in self.locais:
            locais = listaLocais.listar()

            for local in locais:
                local = local.listar()

                for itemEntrega in local[2]:
                    itens = itemEntrega.listar()

                    for item in itens:
                        self.itensEntrega.append(item)