"""
Conhecendo o Pickle:

Objeto Python -> Serialização -> Objeto Binário
Objeto Binário -> Desserialização -> Objeto Python

#OBS:   Não é recomendado usar arquivos pickles vindo dos outros. (maliciosos possivelmente)
    -> É PREFERÍVEL LIDAR COM DADOS USADOS EM FORMATO PICKLE

"""

import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} está comendo')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def comunicar(self):
        print(f'{self.nome} says: MIAU')


felix = Gato('Felix','Preto e branco')
ronix = Gato('Ronix', 'Branco')


#SERIALIZANDO
with open('Animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, ronix), arquivo)

#DESSERIALIZANDO
with open('Animais.pickle', 'rb') as arquivo2:
    gato1, gato2 = pickle.load(arquivo2)
    print(f'O gato 1 se chama {gato1.nome}\nO gato 2 se chama {gato2.nome}')
    gato1.comunicar()
    print(f'O tipo dos gatos é {type(gato1)}')
