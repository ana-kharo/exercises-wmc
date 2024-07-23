# Primeiro eu solicito 3 numeros para a pessoa usuária:

num1 = int(input('Favor, digite o primeiro número: '))
num2 = int(input('Agora, digite o segundo número: '))
num3 = int(input('Por fim, digite o terceiro número: '))

# Agora eu verifico a ordem dos números
if num1 <= num2 <= num3:
    ordem = [num1, num2, num3]
elif num1 <= num3 <= num2:
    ordem = [num1, num3, num2]
elif num2 <= num1 <= num3:
    ordem = [num2, num1, num3]
elif num2 <= num3 <= num1:
    ordem = [num2, num3, num1]
elif num3 <= num1 <= num2:
    ordem = [num3, num1, num2]
else:
    ordem = [num3, num2, num1]

# Ao final, imprimo os números em ordem crescente
print('Os números na ordem crescente são: ', ordem)