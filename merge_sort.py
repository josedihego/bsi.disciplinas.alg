# -*- coding: utf-8 -*-
import math
import time
from random import randrange



def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j+1]
    # eliminamos as linhas 8 e 9 pois não usaremos sentinelas
    i = 0
    j = 0
    for k in range(p, r+1):
        if(i < n1 and j < n2):
            if L[i] < R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
        elif i == n1:
            A[k] = R[j]
            j = j + 1
        elif j == n2:
            A[k] = L[i]
            i = i + 1


def merge_sort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


L = []

for i in range(0,1000000):
    #n = randrange(0,10000)
    L.append(i)

print('tamanho de L=', len(L))

inicio = time.time()
merge_sort(L, 0, len(L)-1)
fim = time.time()

print('Tempo para ordenacao com merge sort:', fim-inicio)

'''
L = [4.16, 7, -1, -3, -1 * math.pi, math.pi, 10, 11, 456.77]
print('antes:', L)
merge_sort(L, 0, len(L)-1)
print('depois:', L)


L = [math.pi, -1 * math.pi]
print('antes:', L)
merge_sort(L, 0, len(L)-1)
print('depois:', L)

L = []
print('antes:', L)
merge_sort(L, 0, len(L)-1)
print('depois:', L)
'''
