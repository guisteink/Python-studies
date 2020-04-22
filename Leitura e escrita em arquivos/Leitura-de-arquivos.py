"""
Recomendações ao se trabalhar com arquivo:
    - Abrir o arquivo em questão;
    - Manusear o arquivo de forma desejada;
    - Fechar o arquivo.
________________________________________________________________________________________________________________________

open()-> função para abrir um arquivo, para leitura. Passa-se como parametro o diretório desse arquivo a ser aberto.
Essa função retorna um _io.TextIOWrapper que é com o que se trabalha (parametro obrigatório)

read()-> função para ler o conteúdo de um arquivo, ex: arquivo.read(). retorno é uma string
obs: a funcao read le todo o conteudo do arquivo, e o cursor para no fim.

seek()-> funçao para movimentar o cursor pelo arquivo, ela recebe um parametro que indica onde sera colocado o cursor

readline()-> funcao que le o conteudo do arquivo por linha. retorno é uma string

close()-> funcao que finaliza a conexao entre arquivo com o disco rígido (streaming).

closed()-> funcao booleana que verifica se o arquivo está aberto ou fechado. ex: arquivo.closed()
"""

arquivo = open('text.txt')

str = arquivo.read()
print(arquivo.read())

arquivo.seek(0)

print(arquivo.closed)

print(arquivo.readline())

arquivo.close()