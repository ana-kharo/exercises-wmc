# Primeiro, irei solicitar a idade da pessoa usuária:
idade = int(input('Favor, digite a usa idade: '))

#Depois criar as regras de tomada de decisão para relacionar o range de idades com a mensagem:
if idade >= 0 and idade <=12:
    print('Você é uma criança.')
elif idade >= 13 and idade <=17:
    print('Você é adolescente')
elif idade >= 18 and idade <=64:
    print('Você é uma pessoa adulta')    
elif idade >= 65:
    print('Você é uma pessoa idosa')
else:
    print('Idade inválida, favor tente novamente')    