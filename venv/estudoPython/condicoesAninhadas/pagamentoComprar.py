preco = float(input('Preço das comprar: '))
print('=' * 50)
print('Escolha uma forma de pagamento:')
print('''[ 1 ] Av. Dinheiro/Cheque
[ 2 ] Av. no Cartão
[ 3 ] Cartão 2x
[ 4 ] Cartão 3x ou mais''')
opcao = int(input('Informe a forma de pagamento: '))
if opcao == 1:
    total = preco - (preco * 10/100)
    print('Sua compra de R${:.2f}, vai custar R${:.2f} no final '.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5/100)
    print('Sua compra de R${:.2f}, vai custar R${:.2f} no final '.format(preco, total))
elif opcao == 3:
    total = preco * 2
    print('Sua compra de ')
elif opcao == 4:
    numParc = int(input('Quantas parcelas você deseja fazer: '))
    parcela = preco + (preco * (20/100))
    if numParc >= 3 and numParc <= 12:
        print('Sua compra de R${:.2f} sera parcelada em {:.2f} vezes e tem 20% de juros '.format(preco, numParc))
        print('de R${:.2f} ficara {:.2f} '.format(preco, parcela))
    else:
        print('Escolha entre 3 e 12 parcelas!!!!')



