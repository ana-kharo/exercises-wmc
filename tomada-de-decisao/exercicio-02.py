# Primeiro irei solicitar a pessoa usuário em que turno ela estuda:
turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

#Depois defo as regras de tomada de decisão para imprimir a  mensagem de acordo com o turno:
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
