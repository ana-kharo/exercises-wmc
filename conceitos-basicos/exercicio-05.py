# Aqui terei que comparar o tempo gasto numa viagem entre avião, carro e ônibus.
# Já temos a velocidade ->  Km/h de cada um:

velocidade_aviao = 600 # Km/h
velocidade_carro = 100 # Km/h
velocidade_onibus = 80 # Km/h

# Vou precisar então solicitar a distância a percorrer ->  quantidade de quilômetros:
distancia = float(input('Favor, digitar quantos quilômetros possui a viagem: '))

# Assim posso calcular o tempo:
tempo_aviao = distancia / velocidade_aviao
tempo_carro = distancia / velocidade_carro
tempo_onibus = distancia / velocidade_onibus

# Por fim, exibir os comparativos:
print(f'Para fins de comparação, uma viagem de {distancia} Km:')
print(f'Você irá gastar de avião um tempo médio de {tempo_aviao} horas')
print(f'Já de carro, irá gastar um tempo médio de {tempo_carro} horas')
print(f'E de ônibus, levará um tempo médio de {tempo_onibus} horas')


