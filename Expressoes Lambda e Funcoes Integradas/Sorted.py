#Sorted eh uma func. de ordenacao e funciona em qualquer array (tupla, dic, set), porem nao altera as listas, ex
#o retorno do sorted eh sempre uma lista
lista = [1,24,12,4,6,7,88,4,2] #lista
lista2 = {1,24,12,4,6,7,88,4,2} #aqui nao pode repetido, set
lista3 = (1,24,12,4,6,7,88,4,2) #tupla

print('Normal:', lista)
print('Ordenada1:',sorted(lista))
print('Ordenada2:',sorted(lista2))
print('Ordenada3:',sorted(lista3))

#Adicionando parametros ao sorted
print('Ordenada decrescente: ',sorted(lista,reverse = True))

#exemplo
twittersUsers = [
    {"USERNAME": "Samuel", "TWEETS": [["Eu amo pizza"], ["Eu nao gosto de refrigerante"],["Eu nao gosto de brocolis"]]},
    {"USERNAME": "Diogo", "TWEETS": [["Eu amo bolo"]]},
    {"USERNAME": "Daniel", "TWEETS": [["Eu amo pao"], ["Eu nao gosto de vinho"]]},
    {"USERNAME": "Leonardo", "TWEETS": [["Eu amo mouse"], ["Eu nao gosto de suco"]]},
    {"USERNAME": "Daniela", "TWEETS": []}
]
print('\n',twittersUsers,'\n')
print('Ordenado por nome:\n',sorted(twittersUsers, key = lambda usuario: usuario["USERNAME"]))
print('Ordenado por num. de tweets:\n',sorted(twittersUsers, key = lambda usuario: len(usuario["TWEETS"]),reverse = True))
