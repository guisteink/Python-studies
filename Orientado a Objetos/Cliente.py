from OAO import Pessoa as ps

class Cliente(ps.Pessoa):

    # típico construtor com herança em python
    def __init__(self, nome, idade, cpf, renda):
        super().__init__(nome, idade, cpf)
        self.__renda = renda

    @property
    def renda(self):
        return self.__renda

    @renda.setter
    def renda(self, renda):
        self.__renda = renda

    #CompareTo SOBREPOSICAO
    def __cmp__(self, other):
        if self.getRenda() > other.getRenda():
            return 1
        if self.getRenda() == other.getRenda():
            return 0
        else:
            return -1

    #EQUALS SOBREPOSICAO
    def __eq__(self, other):
        if self.getRenda() == other.getRenda():
            return True
        return False



    def toString(self):
        return super().toString() + f'\nRenda:{self.getRenda()}'

