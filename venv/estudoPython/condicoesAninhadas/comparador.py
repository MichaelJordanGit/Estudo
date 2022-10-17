num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num1 > num2:
    print('o numero {} é maior que o numero {}'.format(num1,num2))
elif num2 > num1:
    print('o numero {} é maior que o numero {} '.format(num2, num1))
elif num1 == num2:
    print('o numero {} e o numero {} são iguais '.format(num1, num2))
elif num2 == num1:
    print('o numero {} e o numero {} são iguas '.format(num2, num1))
else:
    print('Opção invalida. Tente Novamente !!!!!')