valor = float(input('Valor do produto: R$'))
desconto = float(input('Desconto em %: ' ))

valornovo = valor - (valor*desconto/100)


#variavel pode ser usada mais de uma vez dentro da mesma linha de codigo

print('o produto custa R${:.2f} e com {} desconto fica R${:.2f}' .format(valor,desconto ,valornovo ))