# Primeiro irei solicitar a pessoa usuário que digite seu ano de nascimento e ano atual:
ano_nascimento = int(input('Favor digitar seu ano de nascimento: '))
ano_atual = int(input('Favor digitar em que ano estamos: '))

#Agora irei calcular a idade atual

idade_atual = ano_atual - ano_nascimento

#Após isso exibo a pessoa usuário sua idade atual
print(f'Atualmente você tem: {idade_atual} anos')