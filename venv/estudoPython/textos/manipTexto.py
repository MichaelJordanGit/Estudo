nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiuscula é {}' .format(nome.upper())) # transforma o nome em maiusculo upper()
print('Seu nome em minusculo é {}' .format(nome.lower())) # transforma o nome em minusculo lower()
print('Seu nome tem {} letras' .format(len(nome)-nome.count(' '))) # conta letras (-) o espaço
print('Seu primeiro nome tem {} letras' .format(nome.find(' '))) # contagem de caracteres ate o primeiro espaço find()




