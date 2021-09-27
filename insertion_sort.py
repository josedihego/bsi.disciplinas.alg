# -*- coding: utf-8 -*-
import time
from random import randrange

def ordenar_por_insercao(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1 
        while i >= 0 and A[i] > key:
            A[i+1] = A [i]
            i = i - 1
        A[i+1]  = key  

L = []

for i in range(0,1000000):
    #n = randrange(0,10000)
    L.append(i)

print('tamanho de L=', len(L))


inicio = time.time()
ordenar_por_insercao(L)
fim = time.time()

print('Tempo para ordenacao com insertion sort:', fim-inicio)