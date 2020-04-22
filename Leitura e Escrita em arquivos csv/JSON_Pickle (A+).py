"""

JSON, de JavaScript Object Notation, é um formato compacto, de padrão aberto independente,
de troca de dados simples e rápida entre sistemas.

Pickle -> Serialização e Desserialização de dados (encriptação)

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (devs)



import json


var = json.dumps(['produto', {'PlayStation 4': ('2TB', '220V', 2048)}])

print(type(var))
print(var)
"""

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return (f'Oi eu sou {self.nome}')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def __str__(self):
        return (f'{super().__str__()} e sou {self.cor}')


########################################################################################################################
import jsonpickle

# escrevendo um arquivo python em json, -----------> DJANGO <----------------
def write_object_to_json():

    felix = Gato('Felix','Preto')

    with open('felix.json', 'w') as arq:
        ret = jsonpickle.encode(felix)
        arq.write(ret)

# lendo um arquivo json-py pra object-py, --------------> DJANGO <------------------
def read_json_to_objectPy():

    with open('felix.json','r') as arq:
        conteudo = arq.read()
        ret = jsonpickle.decode(conteudo)
        print(ret)
        print(type(ret))




read_json_to_objectPy()









