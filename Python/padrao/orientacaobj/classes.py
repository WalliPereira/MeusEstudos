class vendedor() :
    def __init__(self, nome,):
        self.nome = nome
        self.vendas = 0 

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateuMeta(self, meta):
        if self.vendas > meta:
            print(self.nome, 'Bateu a meta')
        else:
            print(self.nome, 'Nao bateu a meta')