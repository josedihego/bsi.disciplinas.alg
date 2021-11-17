# -*- coding: utf-8 -*-


class No:
    
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
        self.pai = None

    def __str__(self):
        return str(self.chave)

class Arvore:

    # no futuro podemos remover a raiz como parâmetro graças ao inserir
    def __init__(self, raiz = None):
        self.raiz = raiz


    def caminhar_ordem(self, x):
        if(x != None):
            self.caminhar_ordem(x.esq)
            print(str(x))
            self.caminhar_ordem(x.dir)

    def caminhar_pos_ordem(self, x):
        if(x != None):
            self.caminhar_pos_ordem(x.esq)
            self.caminhar_pos_ordem(x.dir)
            print(str(x))

    def buscar(self, x, chave):
        if x == None or x.chave == chave:
            return x
        else:    
            if chave < x.chave:
                return self.buscar(x.esq, chave)
            else:
                return self.buscar(x.dir,chave)        


    def minimo(self,x):
        while(x.esq != None):
            x = x.esq
        return x 

    def minimo_recursivo(self, x):
        if(x.esq==None):
            return x
        return self.minimo_recursivo(x.esq)

    def maximo(self, x):
        while(x.dir != None):
            x = x.dir
        return x              

    def sucessor(self,x):
        # caso mais simples
        if x.dir != None:
            return self.minimo(x.dir)
        # caso mais complexo
        y = x.pai
        while(y != None and x == y.dir):
            x = y
            y = y.pai
        return y    

    def predecessor(self,x):
        # caso mais simples
        if x.esq != None:
            return self.maximo(x.esq)
        y = x.pai
        while( y != None and x == y.esq):
            x = y
            y = y.pai
        return y    

    def inserir(self,z):
        y = None
        x = self.raiz
        while(x != None):
            y = x
            if z.chave < x.chave:
                x = x.esq
            else:
                x = x.dir
        z.pai = y
        if y == None:
            self.raiz = z
        elif z.chave < y.chave:
            y.esq = z
        else:
            y.dir = z


# código pos método inserir
lista = [13,50,30,20,10,1,80,14,77,88,23,45,90,15]

lista = ['Álvaro', 'David', 'José', 'Luciano', 'Vinícius']

arvore = Arvore()

for v in lista:
    arvore.inserir(No(v))

arvore.caminhar_ordem(arvore.raiz)

'''
# código pré inserção
no30 = No(30)
no20  = No(20)
no40 = No(40)
no42 = No(42)

arvore = Arvore(no30)

no30.esq = no20
no20.pai = no30
no30.dir = no40
no40.pai = no30
no40.dir = no42
no42.pai = no40

arvore.caminhar_ordem(arvore.raiz)

y = arvore.buscar(arvore.raiz, 42)
print('Resultado da busca: '+ str(y))

min = arvore.minimo(arvore.raiz)
print('Valor mínimo: '+ str(min))

minRec = arvore.minimo_recursivo(arvore.raiz)
print('Valor mínimo com recursão: '+ str(minRec))

suc20 = arvore.sucessor(no20)
suc30 = arvore.sucessor(no30)
suc40 = arvore.sucessor(no40)
suc42 = arvore.sucessor(no42)

print(str(suc20), str(suc30), str(suc40), str(suc42))

pred42 = arvore.predecessor(no42)

print(str(pred42))
'''
