""" HIGH-PERFORMANCE CONTAINER DATATYPES """

from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import deque

lista_padrao = [1,1,2,2,4,5,2,2,51,51,12,3,114,14,141,31,2]
lista_texto_padrao = 'Guilherme Stein tem 1,80 de altura, 80kgs, estuda comp e tem olhos verdes'

########################################################################################################################
#COUNTER -> Contador de ocorrências
print('\n')
count = Counter(lista_padrao)
print(count) #gera um dicionario que eh do tipo counter, que faz a contagem de ocorrências que cada elemento da lista tem
count2 = Counter(lista_texto_padrao)#conta quantas vezes kd letra aparece
print(count2)

#exemplo: contar as palavras de um texto
texto = lista_texto_padrao.split() #separa cada palavra do texto
print(texto)
count3 = Counter(texto) #conta cada palavra
print(count3)
print(count3.most_common(2)) #conta as 2 palavras mais comuns, ou seja, com mais ocorrências



########################################################################################################################
#DEFAULT DICT -> Um dicionario com certos tratamentos de erros
print('\n')
dicionario = defaultdict()
print(dicionario)



########################################################################################################################
#ORDERED DICT -> Um dicionario que se organiza ao realizar operacoes, insercoes, etc.
print('\n')
ordDic = OrderedDict()
print(ordDic)



########################################################################################################################
#NAMED TUPLE ->Eh uma tupla generica, que se nomeia variaveis
print('\n')
cachorro = namedtuple('cachorro',['idade','raca','cor'])
bob = cachorro(idade=2,raca='labrador',cor='preto')
print(bob)
print(bob[0]) #elemento 1 -> idade
print(bob.raca) #outra forma de acesso




########################################################################################################################
#Deque -> uma lista de alta performance
print('\n')
deq = deque('aprendendo python')
deq.append('123')
deq.appendleft(456)
print(deq)
print(deq.pop())






