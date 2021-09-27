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

def converter_lista_em_texto(l):
    res = ''
    for e in l:
        res = res + ' '+ e
    return res[1:]    

entrada = open('L0Q2.in','r')

todo_texto_entrada = entrada.read()

linhas_texto = todo_texto_entrada.split('\n')

arquivo_saida = open('L0Q2.out', 'w')

for linha in linhas_texto:
    nomes = linha.split(' ')
    merge_sort(nomes,0, len(nomes)-1)
    arquivo_saida.write(converter_lista_em_texto(nomes) +'\n')
