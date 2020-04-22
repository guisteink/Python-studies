"""
StringIO -> funcao da biblioteca IO, que é utilizada pra manusear arquivos na memória. ler e criar.
"""
from io import StringIO

mensagem = 'Esta é uma mensagem padrão'

arquivo = StringIO(mensagem) # cria uma mensagem em memória com a seguinte mensagem
#o código de cima é equivalente a: arquivo = open('arquivo.txt', 'w')


arquivo.write('\napenas escrevendo algo mais no arquivo')
arquivo.seek(0)
print(arquivo.read())

