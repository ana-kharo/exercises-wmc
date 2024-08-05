# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'vermelho'
        self.modelo = 'Mustang'
        self.velocidade_min = 0
        self.velocidade_max = 250

# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
    def liga(self):
        self.liga = True

    def desliga(self):
        self.liga = False

    def acelera(self):
        self.acelera = True

    def desacelera(self):
        self.acelera = False        

# Crie uma instância da classe carro.
carro_passeio = Carro()
carro_trabalho = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.
carro_passeio.liga()
carro_passeio.acelera()
# Faça o carro "parar" utilizando os métodos da sua classe.

carro_passeio.desacelera()
