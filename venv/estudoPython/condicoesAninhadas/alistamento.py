from datetime import date
anoNasc = int(input('Digite seu ano de nascimento: '))
dataAtual = date.today().year
idade = dataAtual - anoNasc

print('[ 1 ] Sexo MASCULINO')
print('[ 2 ] Sexo FEMININO')
sexo = int(input('Escolha uma das opções: '))



if sexo == 1:
    print('Você é do sexo Masculino')

elif idade <= 17:
    saldo = 18 - idade
    print('Ainda não esta no periodo de alistamento')
    print('Você esta com  {} anos '.format(idade))
    ano = dataAtual + saldo
    print('Seu ano de alistamento sera {} '.format(ano))
elif idade == 18:
    print('Você esta com {} anos e precisa \33[0;31m URGENTEMENTE\33[m fazer seu alistamento'.format(idade))
elif idade > 18:
    saldo = idade - 18
    ano = dataAtual - saldo
    print('Você tem {} anos de idade '.format(idade))
    print('Seu ano de alistamento foi em {}'.format(ano))
    print('Você \33[0;33m PERDEU \33[m o prazo de alistamento')
    print('Compareça o quanto antes a uma \33[0;33m JUNTA MILITAR \33[m e regularize sua situação')
    print('')
elif sexo == 2:
    print('Você é o sexo Feminino')
    print('Não é obrigatorio prestar serviço militar')
