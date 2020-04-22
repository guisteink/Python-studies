"""

Sistema de Arquivos - Manipulação

mkdir() -> cria um diretorio se este nao existir, caso existe, exibe o erro FileExistsError

"""
#import os

#descbrindo se um diretório existe
print(os.path.exists('Bloco-with.py')) #true or false
print(os.path.exists('NAOEXISTE.py')) #true or false

#criando arquivos
open('arquivoNOVO.txt','w').close()
#outra forma
with open('arquivoNOVO2.txt','w') as arquivo:
    pass

#criando diretorios ÚNICOS
os.mkdir("diretorioMKDIR") # se ta dando erro é pq o diretorio ja existe
os.mkdir(r"C:\Users\guilh\PycharmProjects\devpython\DIRETORIOTESTE") #o r na frente da string é pra criar um raw string (NECESSARIO)

#renomear arquivos
os.rename('arquivoNOVO.txt','guilherme.txt') #erro pq ja foi rodado, alterar parametros para parametros validos

#DELETE, o arquivo nao vai pra lixeira, ele é diretamente deletado do sistema, portanto ->CUIDADO<-
os.remove('arquivoNOVO2') #ja rodado, ERRO
#outra forma de remover
os.rmdir('diretorioMKDIR')

#REMOVENDO UMA ARVORE DE DIRETÓRIOS
for arquivo in os.scandir('diretorioMKDIR'): #ja rodei e apagou tudo dentro do diretorioMKDIR
    print(f' - {arquivo.name}')
    if arquivo.is_file():
    os.remove(arquivo.path)



#Trabalhando com arquivos temporarios
import os
import tempfile

#basicamente criei um arquivo temporario, e escrevi algo nele
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretorio temporario{tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'),'w') as arquivo_temp:
        arquivo_temp.write("Escrevendo em um arquivo temporario :D:D")
        arquivo_temp = tempfile.NamedTemporaryFile()
        arquivo_temp.write(b'GUilherme')
        print(arquivo_temp.name)