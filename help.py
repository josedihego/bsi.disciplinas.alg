

ponto = '(12.3,-11.4)'

valores =  ponto.replace('(','').replace(')','').split(',')
x = float(valores[0])
y = float(valores[1])

print('Ponto 2D: ', x, ' , ', y)

print(type(x))
print(type(y))



