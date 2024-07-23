# Primeiro, irei solicitar a quantidade de quilômetros (Km):

km = float(input('Favor, digitar a quantidade de quilômetros (Km): '))

# Em seguida farei a transformação ou conversão para metros, centímetros e milímetros:
metros = km * 1000
centimetros = metros * 100
milimetros = centimetros * 10

# Agora irei exibir o resultado das conversões
print(f'A quantidade de quilômetros passada foi de -> {km}, que equivale a:')
print(f'{metros} metros')
print(f'{centimetros} centímetros')
print(f'e {milimetros} milímetros')


