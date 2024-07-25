def reverter_numero(numero):
    return int(str(numero)[::-1])

numero_reverso = reverter_numero(127)
print(f'O número 127 revertido é: {numero_reverso}')
