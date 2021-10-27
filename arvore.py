

class No:
    
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
        self.p = None

    def __str__(self):
        return str(self.chave)

class Arvore:

    def __init__(self, raiz):
        self.raiz = raiz


    def caminhar_ordem(self, x):
        if(x != None):
            self.caminhar_ordem(x.esq)
            print(str(x))
            self.caminhar_ordem(x.dir)

no30 = No(30)
no20  = No(20)
no40 = No(40)
no42 = No(42)

arvore = Arvore(no30)

no30.esq = no20
no20.p = no30
no30.dir = no40
no40.p = no30
no40.dir = no42
no42.p = no40

arvore.caminhar_ordem(arvore.raiz)
