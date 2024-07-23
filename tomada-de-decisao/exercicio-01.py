# Primeiro irei pedir os números para a pessoa usuária

num1 = float(input('Favor, digite um número: '))
num2 = float(input('Agora digite um outro número: '))

# Agora irei colocar a regra de tomada de decisão e imprimir o maior número:
if num1 > num2:
    print(f'O maior entre os números é o: {num1}')
else:
    print(f'O maior entre os números é o: {num2}')