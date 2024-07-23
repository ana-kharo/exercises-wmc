# Primeiro irei pedir 3 números para a pessoa usuária:
num1 = float(input('Favor, digite o primeiro número: '))
num2 = float(input('Agora digite o segundo número: '))
num3 = float(input('Por fim, digite o terceiro número: '))

# Agora irei determinar o maior número
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Por fim, imprimir o resultado
print('O maior número é:', maior)
