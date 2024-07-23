# Primeiro irei pedir a pessoa usuária quantidade de litros de combustível e distância percorrida:
litros_combustivel = float(input('Digite a quantidade de litros de combustível consumidos: '))
distancia = float(input('Agora digite a distância já percorrida:  '))

# Agora irei calcular o consumo médio de km por litro:
consumo_medio = distancia / litros_combustivel

# Por fim irei imprimir o resultado do consumo médio:
print(f'O seu consumo médio é de {consumo_medio:.4f} km por litro' )