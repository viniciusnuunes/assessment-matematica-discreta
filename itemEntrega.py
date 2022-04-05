# Pilha
class ItensEntrega:
    def __init__(self):
        self.itens = []

    # def __repr__(self):
    #     final = ''
    #     for i in self.itens:
    #         final += f'{str(i)} '
        
    #     return final

    def vazio(self):
        return self.itens == []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        return self.itens.pop()

    def topo(self):
        return self.itens[len(self.itens)-1]

    def tamanho(self):
        return len(self.itens)

    def listar(self):
        return self.itens
