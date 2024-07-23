# Primeiro eu inicio o loop ou a condição 'enquanto'setando como true:
while True:
    # Depois eu solicito a nota a pessoa usuária:
    nota = float(input('Favor, digite uma nota entre (0 e 10): '))
    
    # Daí verifico se a nota está dentro do intervalo proposto:
    if 0 <= nota <= 10:
        if nota >= 7:
            print('Você foi aprovada(o) \o/')
        else:
            print('Você foi reprovada(o) :( ) ')
        break
else:
    print('Nota inválida! Favor, tentar novamente!')       