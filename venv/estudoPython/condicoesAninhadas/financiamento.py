salario = float(input('Informe seu salario: R$ '))
valorCasa = float(input('Informe o valor da casa que você deseja financiar: R$ '))
anos = float(input('informe em quantos anos você quer pagar o financiamento: '))

parcela = anos * 12
valorParcela = valorCasa / parcela
minimo = salario * 30 / 100

if valorParcela <= minimo:
    print('Financiamento Aprovado')
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, anos))
    print('a prestação será de R${:.2f} '.format(valorParcela))
else:
    print('Sua parcela atengiu mais de \33[0;41m 30% \33[m do seu salario')
    print('Financiamento Recusado')



