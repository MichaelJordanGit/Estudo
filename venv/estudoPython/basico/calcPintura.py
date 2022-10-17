alt = float(input('Altura da parede: '))
lar = float(input('Largura da parede: '))
area = alt * lar

pint = area / 2

print('area {:.2f}m² necessita de {:.2f}L de tinta '.format(area, pint))