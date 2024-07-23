# Primeiro irei pedir o numero de horas de exercício por semana para a pessoa usuária
horas_semana = float(input('Favor digitar o número de horas gasto em exercícios na semana: '))

# Agora irei calcular o total de caloria queimadas em um mês, considerando média de 5 calorias por minuto
#Primeiro converto as horas para minutos

minutos_semana = horas_semana * 60

#Pego as semanas do mês (em média)
semanas_mes = 4

#Calculo então o total de minutos de exercicio em um mês

minutos_mes = minutos_semana * semanas_mes

#E por fim, calculo o totoal de calorias queimadas em um mês
calorias_queimadas = minutos_mes * 5


print(f'O seu total de calorias queimadas em um mês é de {calorias_queimadas:.2f} calorias')