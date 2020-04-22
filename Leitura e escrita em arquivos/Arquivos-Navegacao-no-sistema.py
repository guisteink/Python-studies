"""
módulo pra fazer o acesso a determinados diretórios do sistema
os -> operating system (módulo que da acesso as funcoes que navegam e dão acesso aos diretórios desejados)

chdir('..') -> funcao que retorna ao diretório anterior
getcwd() -> funcao que retorna o diretório do arquivo
os.name -> indica o sistema operacional: posix (mac/linux) ; nt (windows)
sys.platform -> indica que windows esta se trabalhando
os.listdir() -> lista todos os diretórios do projeto
os.scandir() -> lista mais detalhadamente esses tipos de diretórios

"""
import os
import sys

print('')
#printando o diretório em que o arquivo pys esta
print(os.getcwd())
os.chdir('..')

print(sys.platform)

#mostra todos os diretórios que estao no projeto trabalhado
print(list(os.listdir()))
print('')

print(list(os.scandir())[4].inode()) #numeração do diretório
print(list(os.scandir())[4].is_dir()) #verificação se é um diretório
print(list(os.scandir())[4].is_file()) #verificação se é um arquivo
print(list(os.scandir())[4].is_symlink()) #é um link simbólico?
print(list(os.scandir())[4].name) #acessando o nome de um diretório por exemplo
print(list(os.scandir())[4].path) #caminho do arquivo
print(list(os.scandir())[4].stat()) #meta dados, tamanho, tipo, etc

os.scandir().close()

