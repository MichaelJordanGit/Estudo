frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes na frase' .format(frase.count('A')))
print('A letra A foi encontrada a primeira vez na posição {} '.format(frase.find('A')+1))
print('A letra A é encontrada a ultima vez na posição {} '.format(frase.rfind('A')+1)) # rfind procura o parametro da direita p esquerda
print(len(frase))