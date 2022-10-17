tempo = int(input('Quanto tempo tem seu carro? '))

if tempo <= 3:
    print('Seu carro tem {} anos. É novo  '.format(tempo))
else:
    print('Seu carro tem {} anos. É velho '.format(tempo))