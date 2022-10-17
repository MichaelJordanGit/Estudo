nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))

media = (nota1 + nota2) / 2

if media <= 5:
    print('\33[1;31m Reprovado\33[m')
    print('media {:.2f} '.format(media))
elif media > 5 and media <6.9:
    print('\33[1;93m Recuperação\33[m')
    print('media {:.2f} '.format(media))
elif media > 7:
    print('\33[1;34m Aprovado \33[m')
    print('media {:.2f} '.format(media))
else:
    print('')
