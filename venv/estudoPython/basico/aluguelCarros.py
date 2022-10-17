diaria = float(input('Dias com o veiculo: '))
kmRodado = float(input('KM rodado: '))
valorDiaria = 60
valorKM = 0.15

valorTotalDiaria = diaria * valorDiaria
valorTotalKM = valorKM * kmRodado

total = valorTotalDiaria + valorTotalKM

print('Você ficou {} dia(s) com o veiculo, rodou {}KM, o valor total sera R${:.2f}'.format(diaria, kmRodado, total))