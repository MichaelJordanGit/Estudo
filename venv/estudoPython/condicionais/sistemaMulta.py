velocidade = float(input('Digite a velocidade: '))
limite = 80
multa = (velocidade - limite) * 7
excedente = velocidade - limite

if velocidade > limite:
    print('Você esta a {}Km/h excedeu {}km/h e sua multa sera R${}'.format(velocidade, excedente, multa))
else:
    print('Você esta dentro do limite de velocidade')
    print('DIRIJA COM SEGURANÇA!!')