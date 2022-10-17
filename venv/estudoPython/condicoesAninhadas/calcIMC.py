print('''[ 1 ] MASCULINO
[ 2 ] FEMININO''')
sexo = int(input('informe seu sexo: '))

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if sexo == 1:
    if imc <= 20:
        print('IMC {:.2f} Abaixo do normal'.format(imc))
    elif imc < 24.9:
        print('IMC {:.2f} Normal'.format(imc))
    elif imc < 29.9:
        print('IMC {:.2f} Obesidade Leve'.format(imc))
    elif imc < 39.9:
        print('IMC {:.2f} Obesidade Moderada'.format(imc))
    else:
        print('IMC {:.2f} Obesidade Morbida'.format(imc))
elif sexo == 2:
    if imc < 19:
        print('IMC {:.2f} Abaixo do normal'.format(imc))
    elif imc < 23.9:
        print('IMC {:.2f} Normal'.format(imc))
    elif imc <28.9:
        print('IMC {:.2f} Obesidade Leve'.format(imc))
    elif imc < 38.9:
        print('IMC {:.2f} Obesidade Moderada'.format(imc))
    else:
        print('IMC {:.2f} Obesidade Morbida'.format(imc))
else:
    print('')
