

class Fila:

    def __init__(self, n):
        self.F = [0] * n
        self.inicio = 0
        self.fim = 0

    def esta_vazia(self):  
        return self.inicio == self.fim

    def esta_cheia(self):
        return self.inicio == (self.fim + 1) % len(self.F) 

    def enfileirar(self, novo):
        if(not self.esta_cheia()):
            self.F[self.fim] = novo
            self.fim = (self.fim + 1) % len(self.F)
        else:
            print('Fila cheia. Volte outro dia :(')  

    def desenfileirar(self):
        if(not self.esta_vazia()):
            resultado = self.F[self.inicio]
            self.inicio = (self.inicio + 1) % len(self.F)
            return resultado
        else:
           print('Pode ir para casa. Fila vazia :)')     



