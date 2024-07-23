# Primeiro eu crio um dicionário representando os contatos (nome e telefone)
contatos = {
    'Ana' : '98798-9898',
    'Diogo' : '98986-5432',
    'Vitória' : '3232-5656',
    'Franciele' : '9996-7875'
}

# Depois eu solicito qual nome a pessoa usuária deseja buscar/procurar:
nome_procurado = input('Qual nome deseja buscar na agenda: ')

# Em seguida verifico se o nome consta no dicionário usando condicionais para imprimir na tela:
if nome_procurado in contatos:
    telefone = contatos[nome_procurado]
    print(f'O telefone de {nome_procurado} é {telefone}.')
else:
    print(f'O nome {nome_procurado} não foi encontrado na agenda.')
