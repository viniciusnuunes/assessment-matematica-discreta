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

    def listarLocais(self):
        for caminhao in self.caminhoes:
            caminhao = caminhao.listar()
            print(
                f'Caminhão {caminhao[0].upper()} fará a entrega nos seguintes Locais:')
            for locais in caminhao[1]:
                locais = locais.listar()
                for local in locais:
                    local = local.listar()
                    print(f'{local[0]} - {local[1]}')

    def listarItensEntrega(self):
        for caminhao in self.caminhoes:
            caminhao = caminhao.listar()
            print(
                f'Caminhão {caminhao[0].upper()} entregará os seguintes Itens:')
            for locais in caminhao[1]:
                locais = locais.listar()
                for local in locais:
                    local = local.listar()
                    for itensEntrega in local[2]:
                        item = itensEntrega.listar()
                        for i in item:
                            i = i.listar()
                            print(f'{i[0]} - {i[1]}')

    def empilharItens(self):
        for c in self.caminhoes:
            caminhao = c.listar()

            for ls in caminhao[1]:
                locais = ls.listar()

                for l in locais:
                    local = l.listar()

                    for itemEntrega in local[2]:
                        item = itemEntrega.listar()

                        for i in item:
                            c.empilharItens(i)

            print('Itens Empilhados com sucesso no caminhão ' +
                  caminhao[0].upper())

    def imprimirRotina(self):
        for caminhao in self.caminhoes:
            caminhao = caminhao.listar()
            print(f'Percurso do caminhão {caminhao[0].upper()}')

            for locais in caminhao[1]:
                locais = locais.listar()
                for local in reversed(locais):
                    local = local.listar()
                    print(f'    Visitando o ponto de entrega {local[1]}. Foram entregues os itens:')
                    for itensEntrega in local[2]:
                        item = itensEntrega.listar()
                        for i in item:
                            i = i.listar()
                            print(f'        {i[1].upper()} - {local[1].upper()}')