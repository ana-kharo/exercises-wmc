# Primeiro eu defino o número de alunos:
numero_de_alunos = 5

# Depois crio a lista que irá armazenar as médias:
medias = []

# Em seguida solicito as notas a cada aluno:
for i in range(numero_de_alunos):
    print(f'--- Aluno {i + 1} ---')
    
    # Solicito as 4 notas do aluno
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    nota4 = float(input('Digite a nota 4: '))
    
    # Calculo a média
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    # Adiciona a média à lista
    medias.append(media)

# Aqui, irei contar o número de alunos com média maior ou igual a 7.0
contador = sum(1 for media in medias if media >= 7.0)

# Imprime o número de alunos com média maior ou igual a 7.0
print('Segue o número de aluno(s) com média maior ou igual a 7.0:', contador)
