salario = float(input('Digite o salario: '))

salario10 = salario + (salario*10/100)
salario15 = salario + (salario*15/100)


if salario < 1500:
    print('Seu salario é de R${}, terá um reajuste de 15% e ficara R${} '.format(salario, salario15))
else:
    print('Seu salario é de R${}, terá um reajuste de 10% e ficara R${} '.format(salario, salario10))