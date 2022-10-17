dist = float(input('Qual a distancia do trajeto: '))
valor1 = dist * 0.50
valor2 = dist * 0.45

if dist <= 200:
    print('O valor da sua passagem é R${:.2f} '. format(valor1))
else:
    print('O valor da sua passagem é R${:.2f} '.format(valor2))
