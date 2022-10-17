valorCarteira = float(input('Quanto tenho na carteira?? '))
cotacaoDolarDia = float(input('Cotação do dolar no dia: '))
compra = valorCarteira / cotacaoDolarDia

print('Tenho R${}, e consigo comprar U${:.2f} na cotação atual '.format(valorCarteira, compra))
