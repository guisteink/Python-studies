"""

Herança multipla -> é a possibilidade de uma classe herdar atributos/metodos de multiplas classes. Fazendo com que
a classe filha herde todos atributos e metodos de todas as classes superiores

OBS: Pode ser feita por
    - Multiderivaçao direta
    - Multiderivaçao indireta

# Multiderivaçao Direta
class Base01:
    pass

class Base02:
    pass

class Base03:
    pass

class MultiDerivada(Base01,Base02,Base03):
    pass

# Multiderivacao Indireta
class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada2(Base3):
    pass

"""


# exemplo usual

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Oi eu sou {self.nome}, um animal'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando'

    def cumprimentar(self):
        return f'Oi eu sou {self.nome}, um animal aquático'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando'

    def cumprimentar(self):
        return f'Oi eu sou {self.nome}, um animal terrestre'


# OS METODOS SOBRESCRITOS COMO 'cumprimentar', A CLASSE HERDA DO PRIMEIRO PARAMETRO DE HERANÇA, NO EXEMPLO 'Terrestre'
class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome, cor):
        super().__init__(nome)
        self.__cor = cor

    @property
    def cor(self, cor):
        return self.__cor


########################################################################################################################
novopinguim = Pinguim('pingú','branco')

print(novopinguim.cumprimentar())

