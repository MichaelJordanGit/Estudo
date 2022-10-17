import math

angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('o angulo é {:.2f}, seno é {:.2f}, cosseno {:.2f} e tangente {:.2f} '.format(angulo, seno, coss, tan))