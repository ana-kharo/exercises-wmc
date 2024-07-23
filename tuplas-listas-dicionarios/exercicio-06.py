# Primeiro solicito à pessoa usuária que digite seu nome:
nome = input('Favor, digite seu nome: ')

# Em seguida, converto o nome para letras maiúsculas e inverto a ordem
nome_reverso = nome.upper()[::-1]

# Por fim, imprimo o nome de trás para frente
print('Nome de trás para frente:', nome_reverso)
