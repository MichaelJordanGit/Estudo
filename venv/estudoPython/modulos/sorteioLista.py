import random

n1 = str(input('1º aluno: '))
n2 = str(input('2º aluno: '))
n3 = str(input('3º aluno: '))
n4 = str(input('4º aluno: '))

list = [n1, n2, n3, n4]
sort = random.choice(list)

print('O aluno escolhido foi {} '.format(sort))
