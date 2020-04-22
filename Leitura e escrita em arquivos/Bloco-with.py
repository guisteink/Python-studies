"""

O bloco with serve pra criar um contexto de trabalho, onde os recursos utilizados sejam fechados após o bloco with

"""

#forma pythonica otimizada, onde nao precisa-se usar o close, depois do trabalho com o arquivo
with open('text.txt') as arquivo:
    print(arquivo.read())

#print(arquivo.read()) erro pq o bloco ja foi fechado