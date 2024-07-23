# Primeiro crio o contador de sim, que inicia com 0 e uma lista para armazenar as respostas:
contador_sim = 0
resposta = []

# Defino as perguntas:
perguntas = [
    'Telefonou para a vítima? (sim/não): ',
    'Esteve no local do crime? (sim/não): ',
    'Mora perto da vítima? (sim/não): ',
    'Devia para a vítima? (sim/não): ',
    'Já trabalhou com a vítima (sim/não): '
]

# Aqui irei fazer as perguntas e contar os "sim":
for pergunta in perguntas:
    resposta = input(pergunta)
    while resposta not in ['sim', 'não']:
        print('Resposta inválida! Por favor, responda com "sim" ou "não".')
        resposta = input(pergunta)
    if resposta == 'sim':
        contador_sim += 1

# Agora irei classificar a participação:
if contador_sim == 5:
    classificacao = 'Pessoa assasina'        
elif contador_sim >= 3:
    classificacao = 'Cúmplice'
elif contador_sim == 2:
    classificacao = 'Pessoa suspeita'
else:
    classificacao = 'Inocente'

# Por final, exibo a classificação:
print('Classificação: ', classificacao)


