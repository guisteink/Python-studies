# FILTER SERVE PRA FILTRAR DADOS DE UMA CERTA COLEÇÃO

# biblioteca pra trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.4, 4.55, -0, 9, 8.8899, 0.54]

# calculando a média dos dados utilizando o mean()
media = statistics.mean(dados)
print('Média:', media)

# a funçao filter() também recebe de parametro uma funçao e um iterável
# a funcao lambda retorna recebe x, e retorna ele se for maior que a media
res = filter(lambda x: x > media, dados)
print('Maiores que a média:', list(res))

# outro exemplo, filtrando paises
paises = ['Brasil', '', 'Argentina', 'EUA', '', 'Venezuela', 'Peru', '', '']
res = filter(None, paises)  # res é um object filter, entao pra ver em lista, se cria uma da seguinte forma
res2 = filter(lambda pais: pais == 'Brasil', paises)
print(list(res))
print(list(res2))

# outro exemplo

twittersUsers = [
    {"USERNAME": "Samuel", "TWEETS": [["Eu amo pizza"], ["Eu nao gosto de refrigerante"]]},
    {"USERNAME": "Diogo", "TWEETS": [["Eu amo bolo"], ["Eu nao gosto de cerveja"]]},
    {"USERNAME": "Daniel", "TWEETS": [["Eu amo pao"], ["Eu nao gosto de vinho"]]},
    {"USERNAME": "Leonardo", "TWEETS": [["Eu amo mouse"], ["Eu nao gosto de suco"]]},
    {"USERNAME": "Daniela", "TWEETS": []}
]

inativos = list(filter(lambda usuario: len(usuario["TWEETS"]) == 0, twittersUsers))
likePao = list(filter(lambda usuario: usuario["TWEETS"] == [["Eu amo pao"], ["Eu nao gosto de vinho"]], twittersUsers))
print(inativos)
print(likePao)

# usando map e filter
titulos = ['flamengo','vasco', 'fluminense', 'botafogo']

meutime = list(map(lambda time: f'Seu time é o {time}', filter(lambda time: len(time)<10 , titulos)))
print(meutime)
