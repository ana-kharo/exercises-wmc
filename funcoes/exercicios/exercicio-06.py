# Primeiro, irei importar a biblioteca random (para gerar números aleatórios)
import random

# Aqui, irei colocar as palavras pré-definidas
palavras = ['misterio', 'empoderamento', 'desenvolvedoras', 'linguagem', 'carreira', 'sucesso']

# Agora criarei a função que vai escolher a palavra aleatoriamente
def escolher_aleatoriamente(palavras):
    return random.choice(palavras)

# Preciso também de uma função que exiba a palavra com as letras adivinhadas e espaço para letras ñ adivinhadas:
def exibir_palavra(palavra_secreta, letras_adivinhadas):
    exibicao = ''
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

# E agora defino a principal função do jogo:
def jogo_forca():
    palavra_secreta = escolher_aleatoriamente(palavras)
    letras_adivinhadas = []
    tentativas_restantes = 6
    adivinhou_palavra = False

# Agora irei imprimir o ínivio do jogo e pedir para adivinhas a palavra, depois exibir se adivinhou ou não:
    print('Boas vindas ao jogo da forca :D')
    print('Se concentre e adivinhe a palavra secreta.')
    print(exibir_palavra(palavra_secreta, letras_adivinhadas))

# Faço também um "enquanto" a pessoa não adivinha, queis são as tentativas restantes:
    while not adivinhou_palavra and tentativas_restantes > 0:
        letra = input('Favor, digite uma letra: ').lower()

        if letra in letras_adivinhadas:
            print('Essa letra, você já adivinhou, vamos tentar outra?')
        elif letra in palavra_secreta:
            letras_adivinhadas.append(letra) 
            print(f'Uhu! Você acertou. A palavra tem a letra {letra} ')  
        else:
            tentativas_restantes -=1
            print(f'Errrrowww! A palavra secreta não tem a letra {letra}')
            print(f'Agora você possui {tentativas_restantes} tentativas restantes.')  

        palavra_atual = exibir_palavra(palavra_secreta, letras_adivinhadas)
        print(palavra_atual)

        if '_' not in palavra_atual:
            adivinhou_palavra = True

    if adivinhou_palavra:
        print('Aeeeee \o/ você acertou a palavra!!!')
    else:
        print(f'Ahhhh :( a forca te pegou, a palavra secreta era...{palavra_secreta}).')

# Por fim, executo o jogo
jogo_forca()                
