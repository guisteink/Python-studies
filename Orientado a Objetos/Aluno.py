from OAO import Pessoa as ps

class Aluno(ps.Pessoa):

    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        return self.__matricula

    #compareTo sobreposicao
    def __cmp__(self, other):
        if self.getMatricula() > other.getMatricula():
            return 1
        if self.getMatricula() == other.getMatricula():
            return 0
        else:
            return -1

    #equals sobreposiçao
    def __eq__(self, other):
        if self.getMatricula() == other.getMatricula():
            return True
        return False

    def toString(self):
        return super().toString() + f'\nMatricula:{self.getMatricula()}'


#####################################################################################################################


