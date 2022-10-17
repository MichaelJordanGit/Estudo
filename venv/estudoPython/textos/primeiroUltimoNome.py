n = str(input('Digite um nome completo aleatorio: ')).strip()
nome = n.split() # vai fatiar a String em uma lista
print('Prazer em conhecer voce!')
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))