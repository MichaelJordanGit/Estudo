from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Informe seu ano de nascimento: '))
idade = anoAtual - anoNasc

print('''1 - Masculino
2 - Feminino''')
sexo = int(input('sexo: '))

if sexo == 1:
    print('Sexo Masculino alistamento obrigatorio')
    if idade < 18:
        print('Nao alista ainda')
    elif idade == 18:
        print('Alista ')
    elif idade > 18:
        print('Passou do prazo')
    else:
        print('')

elif sexo == 2:
    print('Sexo feminino não precisa alista')


