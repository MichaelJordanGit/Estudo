print('-'*25)
print('Analise de triangulos')
print('-'*25)
seg1 = float(input('Segmento 1: '))
seg2 = float(input('Segmento 2: '))
seg3 = float(input('Segmento 3: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos formam um triangulo')
else:
    print('Os segmentos não formam um triangulo')

