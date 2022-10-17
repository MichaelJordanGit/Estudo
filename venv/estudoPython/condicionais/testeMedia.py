nome = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 6:
    print('A media do aluno {} é {}'.format(nome, media))
    print('Parabens vc esta aprovado!!')
else:
    print('A media do aluno {} é {}'.format(nome, media))
    print('Infelizmente vc está reprovado!')