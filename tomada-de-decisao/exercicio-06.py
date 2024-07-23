# Primeiro irei solicitar login e a senha à pessoa usuária:
login = input('Favor, digite seu login: ')
senha = input('Agora, digite sua senha: ')

# Depois,verifico se o login e a senha estão corretos
if login == 'admin' and senha == 'admin123':
    print('Ok, acesso permitido.')
else:
    print('Erro: login ou senha incorretos.')
