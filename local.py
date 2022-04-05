# Fila
class Local:
    def __init__(self, id, nome, ItensEntrega):
        self.id = id
        self.nome = nome
        self.ItensEntrega = [ItensEntrega]

    # def __repr__(self):
    #     return f'{self.id} - {self.nome} - Itens: {self.ItensEntrega}'

    def listar(self):
        return self.id, self.nome, self.ItensEntrega