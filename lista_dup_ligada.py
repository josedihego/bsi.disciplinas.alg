class No:
    def __init__(self, chave):
        self.chave = chave
        self.prox = None
        self.ant = None


class Lista:
    def __init__(self):
       self.inicio = None

    def inserir(self, novo):
        novo.prox = self.inicio
        if self.inicio != None:
            self.inicio.ant = novo
        self.inicio = novo
        novo.ant = None 

    def remover(self, para_rem):
        if para_rem.ant != None:
            para_rem.ant.prox = para_rem.prox
        else:
            self.inicio = para_rem.prox
        if para_rem.prox != None:
            para_rem.prox.ant = para_rem.ant


l = Lista()
x = No(3.55)
l.inserir(No(4))
l.inserir(No('Maria'))
l.inserir(x)
l.inserir(No(22))
l.remover(x)
l.inserir(No('João'))

