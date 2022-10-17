nome = str(input('Qual seu nome? '))

if nome == 'Michael' or nome == 'Juiana' or nome == 'Juan':
    print('Você tem um belo nome!!')
    print('Tenha um otimo dia {}'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Jose' or nome == 'João':
    print('{} você tem um nome bem comum '.format(nome))
else:
    print('Tenha um bom dia {}'.format(nome))