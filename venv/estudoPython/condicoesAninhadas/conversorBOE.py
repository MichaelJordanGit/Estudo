numero = int(input('Digite um numero: '))
print('''Escolha uma das bases para converter:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

op = int(input('Escolha uma opção:'))

if op == 1:
    print('O numero {} convertido em BINARIO é {} '.format(numero, bin(numero)[2:]))
elif op == 2:
    print('O numero {} convertido em OCTAL é {} '.format(numero, oct(numero)[2:]))
elif op == 3:
    print('O numero {} convertido em HEXADECIMAL é {} '.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida!!!!')