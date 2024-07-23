# Primeiro irei perguntar a pessoa usuário quanto ela ganha por hora e o numero de horas trabalhadas/mês:
valor_hora = float(input('Favor digitar qual o valor da sua hora: '))
horas_mes = float(input('E qual é o número de suas horas trabalhadas no mês? '))

# Agora irei calcular o valor total do salário no mês:
salario = valor_hora * horas_mes

# Aqui irei imprimir o resultado
print(f'O valor do seu salário no mês será de R$ {salario}')