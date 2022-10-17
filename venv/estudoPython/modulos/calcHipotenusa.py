from math import hypot

co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))

hipo = hypot(co , ca)

print('A hipotenusa vai medir {:.2f} '.format(hipo))

