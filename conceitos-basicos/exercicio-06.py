# Primeiro irei solicitar a pessoa usuária seu peso e sua altura: 
peso = float(input('Favor, digitar o seu peso em Kg: '))
altura = float(input('E agora a sua altura em metros: '))

# Aqui irei realizar o calculo do imc
imc = peso / (altura * altura)

# Por fim exibir o resultado
print(f'O resultado do seu imc é: {imc:.2f} ')