def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Escolha a opção que deseja converter:")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    opcao = input("Digite 1 ou 2: ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_fahrenheit(celsius)}°F")
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_celsius(fahrenheit)}°C")
    else:
        print("Opção inválida, , tente novamente.")

menu()
