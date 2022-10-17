salario = float(input('Digite o salario: R$'))
aumento = float(input('Quanto porcento de aumento o funcionario ira receber?'))
salarioAumento = salario + (salario*aumento/100)

print('o funcionario recebe R${:.2f} e com aumento de {}% passara a receber R${:.2f}'.format(salario, aumento, salarioAumento))