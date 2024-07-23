# Primeiro eu inicio o loop ou a condição 'enquanto'setando como true:
while True:
    # Depois eu solicito a nota a pessoa usuária:
    nota = float(input('Favor, digite uma nota entre 0 e 10: '))
    
    # Daí verifico se a nota está dentro do intervalo proposto:
    if nota >= 0 and nota <= 10:
        print('A sua nota é válida :D ')
        break  # Encerro o loop caso a nota seja válida
    else:
        print('Sua nota é inválida! Favor tente novamente.')
