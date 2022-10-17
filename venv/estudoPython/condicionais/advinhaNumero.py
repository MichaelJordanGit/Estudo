import random

num = random.randint(0,5)
chute = int(input('Digite um numero entre 0 e 5: '))
if chute == num:
    print('Você acertou!!!')

else:
    print('Você errou!!! TENTE NOVAMENTE')
