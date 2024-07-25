def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)

    except ZeroDivisionError:
        print('Erro: Impossível dividir um valor por zero')

divisao(10,2)   