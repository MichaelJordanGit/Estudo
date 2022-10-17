from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Informe seu ano de nascimento: '))
idade = anoAtual - anoNasc

if idade <= 9:
    print('{} anos Atleta Mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print('{} anos Atleta Infantil'.format(idade))
elif idade > 14 and idade <= 19:
    print('{} anos Atleta Junior'.format(idade))
elif idade > 19 and idade <= 25:
    print('{} anos Atleta Sênior'.format(idade))
elif idade > 25:
    print('{} anos Atleta Master'.format(idade))

