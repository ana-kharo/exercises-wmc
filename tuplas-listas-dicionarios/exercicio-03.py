# Primeiro irei criar o dicionario, simulando um carrinho de compras:
carrinho_compras = {
    'cerveja' : {'preço': 6.50, 'qt': 6},
    'pao de forma' : {'preço': 5.90, 'qt': 2},
    'queijo' : {'preço': 16.50, 'qt': 4},
    'peito de peru': {'preço': 4.90, 'qt': 4},
    'sabão liquído': {'preço': 33.00, 'qt': 1}
}

# Agora irei somar os produtos do carrinho de compras:
total = 0
for produto in carrinho_compras:
    info = carrinho_compras[produto]
    subtotal = info['preço'] * info['qt']
    total += subtotal

# Por fim, imprimo o total do carrinho de compras:
print(f'R${total} é o total do seu carrinho de compras')