seg1 = float(input('Informe o segmento 1: '))
seg2 = float(input('Informe o segmento 2: '))
seg3 = float(input('Informe o segmento 3: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos formam um triangulo')
    if seg1 == seg2 == seg3:
        print('O triangulo é EQUILATERO')
    elif seg1 != seg2 != seg3:
        print('Triangulo ESCALENO')
    else:
        print('Triangulo ISOCELES')

else:
    print('Não forma triangulo')
