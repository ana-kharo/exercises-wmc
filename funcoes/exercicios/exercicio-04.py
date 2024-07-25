# Primeiro irei criar a função que calcula quanto pode ser comprado de cada moeda estrangeira
def calcular_moedas(dinheiro):
    taxas = {
        "Dólar Americano": 5.66,
        "Peso Argentino": 0.06,
        "Dólar Australiano": 3.69,
        "Dólar Canadense": 4.09,
        "Franco Suíço": 6.45,
        "Euro": 6.14,
        "Libra Esterlina": 7.29
    }
    
    # Agora irei calcular e imprimir a quantidade de cada moeda que pode ser comprada
    for moeda, taxa in taxas.items():
        quantidade = dinheiro / taxa
        print(f"Com R${dinheiro:.2f}, você pode comprar {quantidade:.2f} {moeda}(s).")

dinheiro = float(input("Digite quanto dinheiro você possui na carteira: R$"))

# Aqui irei chamar a função
calcular_moedas(dinheiro)
