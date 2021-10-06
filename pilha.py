
class Pilha:

    def __init__(self, tam):
        self.S = [None] * tam
        self.topo = -1

    def esta_vazia(self):
        return self.topo == -1

    def esta_cheia(self):
        return self.topo == len(self.S) - 1

    def empilhar(self, novo):
        if not self.esta_cheia():
            self.topo = self.topo +1
            self.S[self.topo]  = novo
        else:
            print('Pilha cheia.')

    def desempilheirar(self):
        if not self.esta_vazia():
            self.topo = self.topo -1
            return self.S[self.topo +1]
        else:
            print('Pilha vázia')

    def imprimir_pilha(self):
        i = self.topo
        while ( i >= 0):
            print(self.S[i])
            i = i - 1                

p = Pilha(6)            
p.empilhar('Alvaro')
p.empilhar('David')
p.empilhar('Haniel')
p.empilhar('José')
p.empilhar('Luciano')
p.empilhar('Mariana')

p.desempilheirar()
p.desempilheirar()
p.desempilheirar()
p.desempilheirar()
p.desempilheirar()
p.desempilheirar()
p.desempilheirar()
p.imprimir_pilha()

