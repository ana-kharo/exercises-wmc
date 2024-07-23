# Primeiro irei inicializar contadores de pares e ímpares
pares = 0
impares = 0

while True:
    # Depois eu solicito um número positivo e dou a opção 0 para encerrar
    numero = int(input('Digite um número positivo (ou 0 para encerrar): '))
    
    # Crio o encerramento loop caso o usuário digite zero
    if numero == 0:
        break
    
    # Verifico se o número é positivo
    if numero > 0:
        # Confiro se o número é par ou ímpar e atualizo os contadores
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print('Número inválido! Favor, digite um número positivo.')

# Imprim então, a quantidade de números pares e ímpares
print('Quantidade de números pares:', pares)
print('Quantidade de números ímpares:', impares)
