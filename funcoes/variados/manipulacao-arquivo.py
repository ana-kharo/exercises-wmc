def multiplicacao():
    mult = 10*2
    file = 'arquivo.txt'

    #Abertura de arquivo
    # Open [abertura] somente para leitura:
    arquivo_leitura = open(file, 'r') # read

    # Open [abertura] somente para escrita:
    arquivo_escrito = open(file, 'w') # wright

    # Open [abertura] de arquivo binário:
    arquivo_binario = open(file, 'wb' ) # wright binary

    # Open [abertura] para escrita:
    arquivo_escrita = open(file, 'w')
    arquivo_escrita.write(f'O resultado da multiplicação é {mult}')
    arquivo_escrita.close()

    # leitura
    arquivo_leitura = open(file, 'r') 
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close()


multiplicacao()

