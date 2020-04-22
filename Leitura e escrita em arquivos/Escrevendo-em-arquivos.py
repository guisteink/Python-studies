"""
arquivo aberto para leitura: se permite apenas leitura
arquivo aberto pra escrita: se permite apenas escrita

Modos de escrita em arquivo:
    'r' -> abre pra leitura, PADRÃO
    'w' -> é um modo que cria, caso o arquivo nao exista, e sobrepõe caso ja exista
    'x' -> abre e cria pra escrita, somente se o arquivo nao existir
    'a' -> abre pra escrita, e escreve no final do arquivo
    '+' -> abre pra modo de atualização, seja escrita ou leitura
"""

##########################################################################
with open('novoarq.txt', 'w') as arquivo:
    arquivo.write("Esse e o novo arquivo de escrita teste")
    arquivo.writelines(" realizado por Guilherme Stein Kuhn")
    arquivo.write("\nPULOU A LINHA\n")

# usando o modo 'x' de escrita em arquivo e aplicando um tramento de erro
try:
    with open('text.txt', 'a') as arquivo2:
        arquivo2.seek(0)
        arquivo2.write('\n->')
        arquivo2.write("somewhere")
except FileExistsError:
    print('Arquivo já existente')

############################################################################
"""
with open('frutas.txt', 'a') as arquivo3:
    while True:
        fruta = input('Escreva uma fruta, ou digite sair:')
        if fruta == 'sair':
            break
        arquivo3.write(fruta.title())
        arquivo3.write('\n')
"""

