from math import sqrt

num = int(input('Digite um numero:'))
raiz = math.sqrt(num)

print('A raiz quadrada de {} é {:.2f}'.format(num, math.ceil(raiz)))